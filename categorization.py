import numpy as np
import openai
from pydantic import BaseModel

with open("api_key.txt", "r") as file:
    key = file.read()

client = openai.OpenAI(api_key=key)

class outputStructure(BaseModel):
    requestCategory: int


def categorizeQuery(goal):
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"You are an AI assistant in a virtual reality environment. You are able to perform action oriented requests, general inquiries, and task oriented requests."
                            f"In action oriented requests, you simply perform an action, for example you may be requested to move forward then turn left. Simply walking around a single objet is also an action task because there is a walk around action."
                            f"In analysis requests, you will be asked to analyze an environment, for example you may be asked what is in front of me or what is the biggest object in this room."
                            f"In task oriented requests you will be asked to perform an action with a specific goal, for example, walk over to the yellow bus."
                            f"Your goal is currently: {goal}. Which type of task is this. Respond with 0 if action oriented, 1 if general inquiry, and 2 if task oriented."
                },
            ]
        }
    ]

    response = client.beta.chat.completions.parse(
        model="gpt-4o",
        messages=messages,
        response_format=outputStructure,
        max_completion_tokens=100
        )

    return response.choices[0].message.parsed.requestCategory