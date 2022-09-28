import openai

from gpt import GPT
from gpt import Example

openai.api_key = ""

gpt = GPT(engine="davinci", temperature=0.5, max_tokens=100)

# File_object = open("text.txt","r")

# prompt = File_object.read()
prompt = ""

output = gpt.submit_request(prompt)
print(output.choices[0].text)