import google.generativeai as genai

from django.conf import settings


genai.configure(
    api_key=settings.GEMINI_API_KEY
)


model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_sql(
    table_name,
    columns,
    question
):

    prompt = f"""
You are a PostgreSQL expert.

Table Name:
{table_name}

Columns:
{columns}

Convert the user's question into a PostgreSQL query.

Rules:
1. Return SQL only
2. Only generate SELECT queries
3. No explanations
4. No markdown

Question:
{question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text.strip()