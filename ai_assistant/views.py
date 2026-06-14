from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Dataset
from .serializers import DatasetSerializer
from .services import create_table_and_insert_data

from .gemini_service import generate_sql
from .query_service import validate_sql, execute_sql
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import AllowAny
from django.db import connection

from rest_framework import status



class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return

class DatasetUploadView(generics.CreateAPIView):

    queryset = Dataset.objects.all()

    serializer_class = DatasetSerializer

    def perform_create(self, serializer):

        dataset = serializer.save()

        create_table_and_insert_data(dataset)

@method_decorator(csrf_exempt, name='dispatch')
class DatasetQueryView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        try:

            table_name = request.data.get("table_name")

            question = request.data.get("question")

            if not table_name or not question:

                return Response(
                    {
                        "error": "table_name and question are required"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            dataset = Dataset.objects.filter(
                table_name=table_name
            ).first()

            if not dataset:

                return Response(
                    {
                        "error": "Dataset not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )

            # Fetch columns from PostgreSQL

            with connection.cursor() as cursor:

                cursor.execute(
                    """
                    SELECT column_name
                    FROM information_schema.columns
                    WHERE table_name = %s
                    ORDER BY ordinal_position
                    """,
                    [table_name]
                )

                columns = [

                    row[0]

                    for row in cursor.fetchall()

                    if row[0] != "id"

                ]

            # Gemini generates SQL

            sql = generate_sql(
                table_name,
                columns,
                question
            )

            # Validate SQL

            if not validate_sql(sql):

                return Response(
                    {
                        "error": "Unsafe SQL generated",

                        "sql": sql
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            # Execute SQL

            results = execute_sql(sql)

            return Response(
                {

                    "question": question,

                    "sql": sql,

                    "results": results

                }
            )

        except Exception as e:

            return Response(
                {
                    "error": str(e)
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
# views.py

from rest_framework.views import APIView
from rest_framework.response import Response

class DatasetListView(APIView):

    def get(self, request):

        datasets = Dataset.objects.values(
            "name",
            "table_name"
        )

        return Response(datasets)
    
from django.shortcuts import render


def chat_page(request):

    return render(
        request,
        "ai_assistant/chat.html"
    )