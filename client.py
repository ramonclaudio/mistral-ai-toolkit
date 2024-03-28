import json
import requests
from loading import Loading
from config import load_config

print("------------------------------------------------------------------\n")
print("                        Mistral AI Toolkit                        \n")     
print("               API Wrapper & Command-line Interface               \n")   
print("                       [v1.1.0] by @rmncldyo                      \n")  
print("------------------------------------------------------------------\n")

class Client:
    def __init__(self, api_key=None):
        self.config = load_config(api_key=api_key)
        self.api_key = api_key if api_key else self.config.get('api_key')
        self.version = self.config.get('version')
        self.base_url = self.config.get('base_url')
        self.base_model = self.config.get('base_model')
        self.chat_endpoint = self.config.get('chat_endpoint')
        self.timeout = self.config.get('timeout')
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

    def post(self, endpoint, data):
        loading = Loading()
        url = f"{self.base_url}/{self.version}/{endpoint}"
        try:
            loading.start()
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()["choices"][0]["message"]["content"].replace("\\n", "\n")
        except Exception as e:
            print(f"HTTP Error: {e}")
            raise
        finally:
            loading.stop()

    def stream_post(self, endpoint, data):
        loading = Loading()
        url = f"{self.base_url}/{self.version}/{endpoint}"
        full_response = []
        try:
            loading.start()
            response = requests.post(url, json=data, headers=self.headers, stream=True)
            response.raise_for_status()
            loading.stop()
            response_content = ""
            print("Assistant: ", end="", flush=True)
            for line in response.iter_lines():
                if line:
                    try:
                        line = str(line.strip())
                        if 'data: ' in line:
                            json_data = line.split('data: ')[1][:-1]
                            data_dict = json.loads(json_data)
                            print(data_dict["choices"][0]["delta"]["content"].replace("\\n", "\n"), end="", flush=True)
                            response_content += data_dict["choices"][0]["delta"]["content"].replace("\\n", "\n")
                    except json.JSONDecodeError:
                        pass
            full_response.append(response_content)
            print()
            return full_response[0]
        except Exception as e:
            loading.stop()
            print(f"Stream HTTP Error: {e}")
            raise
        finally:
            loading.stop()