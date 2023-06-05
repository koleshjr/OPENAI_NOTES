import os
import openai
import tiktoken
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ['OPENAI_API_KEY']

def get_completion(prompt, model= "gpt-3.5-turbo"):
    messages = [{"role":"user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages ,
        temperature = 0,
    )
    return response.choices[0].message["content"]



# response = get_completion("take the word l-o-l-l-i-p-o-p and reverse it?")
# print(response)

def get_completion_from_messages(messages, model= "gpt-3.5-turbo",max_tokens = 4000, temperature = 0.6):
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages ,
        temperature = 0,
        max_tokens= max_tokens
    )
    return response.choices[0].message["content"]

messages = [
    {
        'role':'system','content': 'You are an assistant who is a better version of steve jobs'
    },
    {
        'role':'user','content': 'pitch a startup that helps in inventory management via a virtual asssistant bot'
    }
]

# response = get_completion_from_messages(messages, temperature = 0.5)
# print(response)

def get_completion_and_token_count(messages, 
                                   model="gpt-3.5-turbo", 
                                   temperature=0, 
                                   max_tokens=500):
    
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, 
        max_tokens=max_tokens,
    )
    
    content = response.choices[0].message["content"]
    token_dict = {
        'prompt_tokens': response['usage']['prompt_tokens'],
        'completion_tokens': response['usage']['completion_tokens'],
        'total_tokens': response['usage']['total_tokens'],
    }

    return content, token_dict

# response, token_dict = get_completion_and_token_count(messages, temperature = 0.5)
# print(response)
# print(token_dict)