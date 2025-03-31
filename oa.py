import os
from openai import OpenAI
from dotenv import load_dotenv
import json
from reddit_search import search_reddit
load_dotenv()

def response_to_user(user_input, context):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
    
    response = client.chat.completions.create(
        model=os.getenv('OPENAI_MODEL'),
        messages=[
            {
                "role": "system", "content": 
                "You have all the context of the user input and you should answer the user in a friendly manner"
            },
            {"role": "assistant", "content": f"{context}"},
            {"role": "user", "content": f"{user_input}"}
        ]
    )

    content = response.choices[0].message.content
    print("🔴")
    print(f"model response: {content}")
    return content

def get_reddit_query(user_input):
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    response = client.chat.completions.create(
        model=os.getenv('OPENAI_MODEL'),
        messages=[
            {
                "role": "system", "content": 
                "you should make up a query from the user input respective to redit and send it in a json file to the user, and please provide just this nothing else in the response."
            },
            {"role": "user", "content": f"{user_input}"}
        ]
    )

    # Extract the content from the response
    content = response.choices[0].message.content
    print(f"initial response: {content}")

    if '```json' in content:
        json_start = content.find('```json\n') + 8
        json_end = content.find('\n```')
        json_str = content[json_start:json_end]
    else:
        # If no backticks, try to parse the entire content as JSON
        json_str = content.strip()
        
        # If the content starts with a newline, remove it
        if json_str.startswith('\n'):
            json_str = json_str[1:]

    # Parse the JSON
    parsed_data = json.loads(json_str)
    print(f"parsed data: {parsed_data}")

    # Return either query or model_response
    query = parsed_data['query']
    context = search_reddit(query)
    print("🔵")
    response_to_user(user_input, context)

dd = get_reddit_query("what is happening with mark zuckerberg")



