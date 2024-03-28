from client import Client

class Chat:
    def __init__(self):
        self.client = None

    def run(self, api_key=None, model=None, prompt=None, stream=None, json=None, system_prompt=None, max_tokens=None, temperature=None, top_p=None, random_seed=None, safe_prompt=None):
        
        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('base_model')

        conversation_history = []

        if system_prompt:
            conversation_history.append({"role": "system", "content": system_prompt})

        print("Assistant: Hello! How can I assist you today?")
        while True:
            if prompt:
                user_input = prompt.strip()
                print(f"User: {user_input}")
                prompt = None
            else:
                user_input = input("User: ").strip()
                if user_input.lower() in ['exit', 'quit']:
                    print("\nThank you for using the Mistral AI toolkit. Have a great day!")
                    break

                if not user_input:
                    print("Invalid input detected. Please enter a valid message.")
                    continue
            
            if json:
                conversation_history.append({"role": "user", "response_format": {"type": "json_object"}, "content": user_input + ". Only respond in JSON."})
            else:
                conversation_history.append({"role": "user", "content": user_input})

            data = {
                "model": self.model,
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
                response = self.client.stream_post(endpoint, data)
            else:
                response = self.client.post(endpoint, data)
                print(f"Assistant: {response}")
            conversation_history.append({"role": "assistant", "content": response})

class Text:
    def __init__(self):
        self.client = None

    def run(self, api_key=None, model=None, prompt=None, stream=None, json=None, system_prompt=None, max_tokens=None, temperature=None, top_p=None, random_seed=None, safe_prompt=None):
        
        self.client = Client(api_key=api_key)
        self.model = model if model else self.client.config.get('base_model')

        if not prompt:
            print("Error: { Invalid input detected }. Please enter a valid message.")
            exit(1)

        conversation_history = []
        
        if system_prompt:
            conversation_history.append({"role": "system", "content": system_prompt})

        user_input = prompt.strip()
        
        print("Assistant: Hello! How can I assist you today?")
        print(f"User: {user_input}")
        
        if json:
            conversation_history.append({"role": "user", "response_format": {"type": "json_object"}, "content": user_input + ". Only respond in JSON."})
        else:
            conversation_history.append({"role": "user", "content": user_input})

        data = {
            "model": self.model,
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
            response = self.client.stream_post(endpoint, data)
        else:
            response = self.client.post(endpoint, data)
            print(f"Assistant: {response}")
        
        print("\nThank you for using the Mistral AI toolkit. Have a great day!")