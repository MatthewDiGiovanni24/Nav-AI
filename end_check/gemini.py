from google import genai
from google.genai import types
from pydantic import BaseModel
import os

key_path = os.path.join(os.path.dirname(__file__), "gemini_key.txt")
with open(key_path, "r") as file:
    key = file.read()

client = genai.Client(api_key=key)

class end(BaseModel):
    accomplished: bool

def gemini_vote(goal, path, s):
    with open(path, 'rb') as f:
        image_bytes = f.read()

    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=[
        types.Part.from_bytes(
        data=image_bytes,
        mime_type='image/jpeg',
        ),
        f"Your goal was: {goal}"
        "This was a task oriented goal where an AI had to perform actions to achieve it"
        "For example, if you were told to walk up to an object, are you reasonably close to the object?"
        "I also will give you a list of numbers. For each action, the number is smaller than 1 if the user gets closer to the target object and larger than one if the user gets further."
        "The smaller the number the closer the user got and the larger the further. Each number is relative to the last position.  If the number is 1 the user did not move."
        "You can use this to tell if the user has been getting closer or cannot get any closer in order to better inform you decision. However, mostly use the image to decide."
        f"Here is the list: {s}"
        "Have you accomplished the goal based on this image of what you are seeing?",
    ],
    config={
        "response_schema": end,
    },
    )

    return response.text