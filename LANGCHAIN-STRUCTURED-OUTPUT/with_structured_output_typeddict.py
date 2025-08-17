from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()


model = ChatOpenAI()


#  schema
class Review(TypedDict):

    key_themes: Annotated[list[str], "write down all the key themes discussed in the review "
    "in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The sentiment of the review (e.g., positive, negative, neutral)"]
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]

structured_model = model.with_structured_output(Review)

result = model.invoke("""The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. ALso, the UI looks outdated compared to
other brands. Hoping for a software update to fix this.""")

print(result)