from openai import OpenAI
import json
from dotenv import load_dotenv
import os

load_dotenv()

class Chat:
    def __init__(self,messages):
        self.messages = messages
        self.client = OpenAI(api_key=os.environ.get("KEY",""))
    
    def send_message(self, message:str) -> dict:
        new_message = {"role": "user", "content": message}
        self.messages.append(new_message)
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            response_format={ "type": "json_object" },

            messages=self.messages
        )
        self.messages.append({'role':'system','content':response.choices[0].message.content})
        return json.loads(response.choices[0].message.content)