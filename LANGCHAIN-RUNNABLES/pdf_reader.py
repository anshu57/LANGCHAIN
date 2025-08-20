from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import HuggingFaceEndpoint

# Load the document
loader = TextLoader("docs.txt")
documents = loader.load()

# split the text into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
docs = text_splitter.split_documents(documents)

# Convert text into embeddings & store in FAISS
vectorstore = FAISS.from_documents(docs, HuggingFaceEmbeddings())

# create a retriever 
retriever = vectorstore.as_retriever()

# Manually Retrieve Relevant documents
query = "What are the key takeaways from the document ?"
retrieved_docs = retriever.get_relevant_documents(query)

# Combine Retrieved Text into a Single Prompt
retrieved_text = "\n".join([doc.page_content for doc in retrieved_docs])


# Initiate llm
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
# Manually pass retrieved text to llm
prompt = f"Based on the following text, answer the question : {query}\n\n{retrieved_text}"
answer = llm(prompt)

print(answer)