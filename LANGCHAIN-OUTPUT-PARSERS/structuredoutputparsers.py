from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
 

load_dotenv()

# define the model

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name='fact_1', description='A factual statement about the topic'),
    ResponseSchema(name='fact_2', description='Another factual statement about the topic'),
    ResponseSchema(name='fact_3', description='A third factual statement about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template= 'Give me three facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()}

)

prompt = template.invoke({'topic': 'black hole'})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)