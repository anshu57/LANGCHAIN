from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
    )

model = ChatHuggingFace(llm=llm)

# 1st prompt -> Detailed Report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=["topic"]        
    )


# 2nd Prompt -> Summary
template2 = PromptTemplate(
    template='Write a 5 line Summary on the folllowing text. /n {text}',
    input_variables=["text"]
)


prompt1 = template1.invoke({'topic': 'blackhole'})
result = model.invoke(prompt1)

prompt2 = template2.invoke({'text':result.content})

result1 = model.invoke(prompt2)
print(result1.content)