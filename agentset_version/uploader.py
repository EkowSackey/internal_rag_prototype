import os
import requests
from agentset import Agentset

client = Agentset(
    namespace_id = os.getenv("NAMESPEACE_ID"), 
    token = os.getenv("AGENTSET_TOKEN")
)

with open("./cleancode.pdf", "rb") as f:
    file = f.read()

upload = client.uploads.create(
    file_name = "cleancode.pdf",
    file_size = len(file),
    content_type = "application/pdf"
)

requests.put(
    upload.data.url,
    data = file,
    headers = {
        "Content-Type": "application/pdf"
    }
)

job = client.ingest_jobs.create(
    payload={
        "type": "MANAGED_FILE",
        "key" : upload.data.key,
        "filename" : "cleancode.pdf"
    }
)

print(f"Upload started: {job.data.id}")