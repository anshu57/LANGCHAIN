from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

document = [
    "Delhi is the capital of India.",
    "Beijing is the capital of China.",
    "Tokyo is the capital of Japan."
]

vectors = embedding.embed_documents(document)

print(str(vectors))
