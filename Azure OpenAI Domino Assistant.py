from openai import OpenAI

API_KEY = ""

BASE_URL = ""


MODEL_NAME = "gpt-4.1"


client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "user",
            "content": "What is the current status of my Domino server?"
        }
    ]
)

print(response.choices[0].message.content)