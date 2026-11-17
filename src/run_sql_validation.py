import sqlite3
from pathlib import Path

database_path = Path("data/ecommerce_analysis.db")
sql_file_path = Path("sql/data_validation.sql")
results_path = Path("reports/sql_validation_results.txt")

results_path.parent.mkdir(parents=True, exist_ok=True)

connection = sqlite3.connect(database_path)
sql_text = sql_file_path.read_text(encoding="utf-8")

# Remove SQL comments and split the file into individual queries.
lines = [
    line for line in sql_text.splitlines()
    if not line.strip().startswith("--")
]
queries = [
    query.strip()
    for query in "\n".join(lines).split(";")
    if query.strip()
]

try:
    with results_path.open("w", encoding="utf-8") as output:
        output.write("SQL VALIDATION RESULTS\n")
        output.write("=" * 50 + "\n\n")

        for number, query in enumerate(queries, start=1):
            cursor = connection.execute(query)
            rows = cursor.fetchall()

            output.write(f"Query {number}:\n")
            output.write(query + "\n")
            output.write(f"Results: {rows}\n\n")

            print(f"Query {number}: {rows}")

    print(f"\nAll {len(queries)} SQL queries executed successfully!")
    print(f"Results saved to: {results_path}")

except sqlite3.Error as error:
    print(f"\nSQL validation failed: {error}")
    print(f"Error occurred while executing query {number}.")
finally:
    connection.close()