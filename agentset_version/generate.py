import os
import requests
from agentset import Agentset

client = Agentset(
    namespace_id = os.getenv("NAMESPEACE_ID"), 
    token = os.getenv("AGENTSET_TOKEN")
)


from openai import OpenAI as OpenAIClient

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set. Please check your environment or .env file.")

openai = OpenAIClient()
results = client.search.execute(
    query="what are the rules for functions?",
    top_k=5
    )

context = "\n\n".join([result.text for result in results.data])


response = openai.responses.create(
    model = "gpt-4o",
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What are the rules for functions?"}
    ]
)

print(response.output_text)
