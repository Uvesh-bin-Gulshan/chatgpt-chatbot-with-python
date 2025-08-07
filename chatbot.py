from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key=os.getenv("CHAT_BOT_KEY")
if not api_key:
    raise ValueError("API key not found.Please set the OpenAI API key in the .env file.")

#Initialize the OpenAI client with your API key
client=OpenAI(api_key=api_key)
def chat_with_gpt():
    print("Say hi to your GPT-4 chatbot!(type 'quit' to exit)")
    while True:
        user_input=input("You:")
        if user_input.lower()=="quit":
            print("Exiting to chat. Goodbye!")
            break