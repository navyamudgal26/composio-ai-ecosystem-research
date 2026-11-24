
import os
import pandas as pd
import requests

INPUT = "data/apps_100.csv"
OUTPUT = "output/all_apps_source_audit.csv"

def audit_sources():
    df = pd.read_csv(INPUT).fillna("")
    results = []

    for _, row in df.iterrows():
        for kind, column in [
            ("API", "API_Documentation_URL"),
            ("Authentication", "Authentication_Evidence_URL"),
            ("MCP", "MCP_Evidence_URL")
        ]:
            url = str(row.get(column, "")).strip()
            if not url:
                continue

            try:
                response = requests.get(
                    url,
                    timeout=15,
                    headers={"User-Agent": "Mozilla/5.0"}
                )
                results.append({
                    "Application": row["Application"],
                    "Category": row["Category"],
                    "Source_Type": kind,
                    "URL": url,
                    "HTTP_Status": response.status_code,
                    "Accessible": response.status_code < 400,
                    "Verification": "Manual review required"
                })
            except Exception as error:
                results.append({
                    "Application": row["Application"],
                    "Category": row["Category"],
                    "Source_Type": kind,
                    "URL": url,
                    "HTTP_Status": "Error",
                    "Accessible": False,
                    "Verification": str(error)[:200]
                })

    os.makedirs("output", exist_ok=True)
    result = pd.DataFrame(results)
    result.to_csv(OUTPUT, index=False)
    print("Source audit saved:", OUTPUT)
    print("URLs checked:", len(result))
    print("Note: HTTP accessibility is not proof of API or MCP availability.")

if __name__ == "__main__":
    audit_sources()
