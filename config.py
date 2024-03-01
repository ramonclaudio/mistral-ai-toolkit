import os

def load_required_env_variables(var_name: str):
    value = os.getenv(var_name)
    if value is None:
        try:
            from dotenv import load_dotenv
            load_dotenv()
            value = os.getenv(var_name)
            if value is None or value == "" or value == " ":
                print(f"{var_name} environment variable is not defined. Please define it in a .env file or directly in your environment. You can also pass it as an argument to the function.")
                exit(1)
        except ImportError:
            print(f"dotenv package is not installed. Please install with 'pip install python-dotenv' or define environment variables directly.")
        except Exception as e:
            print(f"Error loading environment variables: {e}")
    return value

def load_config():
    api_key = load_required_env_variables('MISTRAL_API_KEY')
    base_url = os.getenv('MISTRAL_BASE_URL', 'https://api.mistral.ai')
    chat_endpoint = os.getenv('MISTRAL_CHAT_ENDPOINT', 'chat/completions')
    version = os.getenv('MISTRAL_VERSION', 'v1')
    timeout = int(os.getenv('MISTRAL_TIMEOUT', 20))
    
    return {
        'api_key': api_key,
        'base_url': base_url,
        'chat_endpoint': chat_endpoint,
        'version': version,
        'timeout': timeout
    }