from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-20b",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

loader = TextLoader('/Users/anshugangwar/Desktop/Anshu/LangChain/docs.txt')

docs = loader.load()


print(docs[0].metadata)

prompt = PromptTemplate(
    template= 'Write a summary for the following document - \n {document}',
    input_variables = ['document']
)
parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({'document': docs[0].page_content}))