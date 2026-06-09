from db import search_documents


results = search_documents(
    "What is FastAPI?"
)

print(results["documents"][0])