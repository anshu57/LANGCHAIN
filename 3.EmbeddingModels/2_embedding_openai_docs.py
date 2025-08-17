from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India.",
    "Beijing is the capital of China.",
    "Tokyo is the capital of Japan."
]

results = embeddings.embed_documents(documents)

print(str(results))