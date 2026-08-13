import os
import argparse
from dotenv import load_dotenv
from prompts import system_prompt
import prompts
import json
from call_function import available_functions

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if api_key is None:
    raise RuntimeError


from openai import OpenAI



def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    # Now we can access `args.user_prompt`

    print("Hello from llmagent!")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

    messages = [
        {"role": "system", "content": prompts.system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]


    response = client.chat.completions.create(model = "openrouter/free",messages = messages, temperature=0,tools=available_functions)
    
    if response.choices[0].message.tool_calls:
        for tool_call in response.choices[0].message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")
    else:
            print (response.choices[0].message.content)
    
    if response.usage is None:
        raise RuntimeError ("Failed API call") 

    if args.verbose == True:
        print(f"User prompt: {args.user_prompt}\nPrompt tokens: {response.usage.prompt_tokens}\nResponse tokens: {response.usage.completion_tokens}")

if __name__ == "__main__":
    main()
