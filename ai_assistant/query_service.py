from django.db import connection


FORBIDDEN_WORDS = [
    "drop",
    "delete",
    "update",
    "insert",
    "alter",
    "truncate"
]


def validate_sql(sql):

    sql_lower = sql.lower()

    for word in FORBIDDEN_WORDS:

        if word in sql_lower:
            return False

    return True


def execute_sql(sql):

    with connection.cursor() as cursor:

        cursor.execute(sql)

        columns = [
            col[0]
            for col in cursor.description
        ]

        rows = cursor.fetchall()

    results = []

    for row in rows:

        results.append(
            dict(
                zip(
                    columns,
                    row
                )
            )
        )

    return results