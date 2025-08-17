from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Literal, Optional
from pydantic import BaseModel, Field

load_dotenv()


model = ChatOpenAI()


#  schema
class Review(BaseModel):

    key_themes: list[str] = Field(description="write down all the key themes discussed in the review "
    "in a list")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg", "neu"] = Field(description="The sentiment of the review (e.g., positive, negative, neutral)")
    pros: Optional[list[str]] = Field(default=None, description="Write down all the pros inside a list")
    cons: Optional[list[str]] = Field(default=None, description="Write down all the cons inside a list")
    name: Optional[str] = Field(default=None, description="The name of the reviewer")


structured_model = model.with_structured_output(Review)

result = model.invoke("""The hardware is great, but the software feels bloated. There are
too many pre-installed apps that I can't remove. ALso, the UI looks outdated compared to
other brands. Hoping for a software update to fix this.""")

print(result)