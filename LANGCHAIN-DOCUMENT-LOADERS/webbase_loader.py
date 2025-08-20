from langchain_community.document_loaders import WebBaseLoader
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

url = 'https://www.apple.com/in/shop/buy-mac/macbook-air'
loader = WebBaseLoader(url)

docs = loader.load()

prompt = PromptTemplate(
    template='Answer the following questions \n {question} from the following text - \n {text}',
    input_variables = ['question','text']
)
parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'question':'What is the price of this product', 'text':docs[0].page_content})

print(result)
