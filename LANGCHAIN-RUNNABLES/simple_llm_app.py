from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)
model = ChatHuggingFace(llm=llm)

# create a Prompt Template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest a catchy blog title about {topic}"
)

# Define the input
topic = input('Enter a topic')

# Format the prompt manually using PromptTemplate
formatted_prompt = prompt.format(topic=topic)

# calling llm directly
blog_title = model.predict(formatted_prompt)

# Print the output
print("Generated Blog title:", blog_title)