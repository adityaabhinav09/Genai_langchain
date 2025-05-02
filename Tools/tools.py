from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

key = os.getenv('GEMINI_API_KEY')
model = ChatGoogleGenerativeAI(model='gemini-1.5-pro',api_key=key)


result = model.invoke("what is your name?")

print(result.content)
