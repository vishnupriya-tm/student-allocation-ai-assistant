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
You are an expert PostgreSQL SQL generator.

Your job is to convert natural language questions into PostgreSQL SELECT queries.

IMPORTANT RULES:

1. Use ONLY this table:

{table_name}

2. Use ONLY these columns:

{", ".join(columns)}

3. Never invent tables.

4. Never invent columns.

5. Return ONLY raw SQL.

6. Generate ONLY SELECT statements.

7. If aggregation is required:
   - Use SUM() only on numeric columns.
   - Use AVG() only on numeric columns.
   - Use COUNT() for counting.

8. For questions like:
   - "Who are my top customers?"
   - "Top performing customers"
   - "Best customers"

   Use:

   SELECT *
   FROM {table_name}
   ORDER BY revenue DESC
   LIMIT 10

9. For questions like:
   - "Which city contributes the highest revenue?"

   Use:

   SELECT city,
          SUM(revenue) AS total_revenue
   FROM {table_name}
   GROUP BY city
   ORDER BY total_revenue DESC
   LIMIT 1


Question:

{question}

SQL:
"""

    response = model.generate_content(prompt)

    sql = response.text.strip()

    sql = sql.replace("```sql", "")
    sql = sql.replace("```", "")
    sql = sql.strip()

    return sql