import os

def load_required_env_variables(var_name: str):
    value = os.getenv(var_name)
    if value is None:
        try:
            from dotenv import load_dotenv
            load_dotenv()
            value = os.getenv(var_name)
            if value is None or value.strip() == "":
                print(f"Error: {var_name} environment variable is not defined. Please define it in a .env file or directly in your environment. You can also pass it as an argument to the function or export it as an environment variable.")
                exit(1)
        except ImportError:
            print("Error: dotenv package is not installed. Please install it with 'pip install python-dotenv' or define the environment variables directly.")
            exit(1)
        except Exception as e:
            print(f"Error loading environment variables: {e}")
            exit(1)
    return value

def load_config(api_key=None):
    if not api_key:
        api_key = load_required_env_variables('MISTRAL_API_KEY')
    
    return {
        'api_key': api_key,
        'base_url': os.getenv('MISTRAL_BASE_URL', 'https://api.mistral.ai'),
        'base_model': os.getenv('MISTRAL_BASE_MODEL', 'mistral-large-latest'),
        'chat_endpoint': os.getenv('MISTRAL_CHAT_ENDPOINT', 'chat/completions'),
        'version': os.getenv('MISTRAL_VERSION', 'v1'),
        'timeout': int(os.getenv('MISTRAL_TIMEOUT', 20))
    }