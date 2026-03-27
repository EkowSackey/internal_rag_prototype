import os
import requests
from agentset import Agentset

client = Agentset(
    namespace_id = os.getenv("NAMESPEACE_ID"), 
    token = os.getenv("AGENTSET_TOKEN")
)

print(f"Upload started: {job.data.id}")

results = client.search.execute(
    query="what are the rules for functions?",
    top_k=5
    )

for result in results.data:
    print(result.text)