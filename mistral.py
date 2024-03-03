import asyncio
from client import Client

class Mistral:
    def __init__(self):
        self.client = None

    def chat(self, api_key=None, model="mistral-large-latest", json=None, system_prompt=None, temperature=None, top_p=None, max_tokens=None, stream=None, safe_prompt=None, random_seed=None):
        
        self.client = Client(api_key=api_key)

        async def conversation():
            conversation_history = []
            if system_prompt:
                conversation_history.append({"role": "system", "content": system_prompt})

            print("Assistant: Hello! How can I assist you today?")
            while True:
                user_input = input("User: ")
                if user_input.lower() in ['exit', 'quit']:
                    print("\nThank you for using the Mistral AI toolkit. Have a great day!")
                    break
                
                if json:
                    conversation_history.append({"role": "user", "response_format": {"type": "json_object"}, "content": user_input + ". Only respond in JSON."})
                else:
                    conversation_history.append({"role": "user", "content": user_input})

                data = {
                    "model": model,
                    "messages": conversation_history,
                    "temperature": temperature,
                    "top_p": top_p,
                    "max_tokens": max_tokens,
                    "stream": stream,
                    "safe_prompt": safe_prompt,
                    "random_seed": random_seed
                }
                data = {k: v for k, v in data.items() if v is not None}
                endpoint = self.client.config.get('chat_endpoint')

                if stream:
                    response = await self.client.stream_post(endpoint, data)
                else:
                    response = await self.client.post(endpoint, data)
                    print(f"Assistant: {response}")
                conversation_history.append({"role": "assistant", "content": response})

        try:
            asyncio.run(conversation())
        except RuntimeError as e:
            if str(e) == 'This conversation loop is already running':
                print("Event conversation loop is already running. Skipping asyncio.run() to avoid conflict.")
            else:
                raise
