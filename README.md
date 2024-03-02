<p align="center">
    <a href="https://mistral.ai/" title="Go to mistral.ai homepage" target="_blank">
        <img src="https://img.shields.io/badge/MISTRAL%20AI-FF7000?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAAC9CAYAAAAQnvmoAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBJREFUeNrs3cFKVFEcwOH/6FSEBSoRhHcxi1aFIO1s00Tv0C7GR8hdO2cTLe0Vol3vEE4vEEKrNhKkBRalY1bqmJ2ibaT3zuRx/D443NU9zD33/mburE4tkqKYakZJs9M78ezhx8jQRu1GLAfHKj1bM+kwPkzPVv3PcWkI71cnjdse22O3mEZzmC5oxD0F0YBoQDQgGhANIBoQDYgGRAOiAUQDogHRgGhANCAaQDQgGhANiAZEA4gGRAOiAdGAaEA0gGhANCAaEA2IBhANgzcuGjiaGdHAKVevPMN+GtsZXlkvGgdPo53hJ+vU7v3eRLevimJqLh0aZc9/+2htIBe7+Hyr/DVd7kV8GMZovqfxJssvhF8P0EKmX1adAczZigx3UZ6/0602wbrXM/CfBkQDiAZEA6IB0YBoANGAaEA0IBoQDYgGEA2IBkQDogHRAKIB0YBoQDQgGhANIBoQDYgGRAOiAUQDogHRgGhANCAa4F+qb1S7k8Z7C3lo29E6uB+3+j3tq8/rM196Fb4D3cP/GM1uGu8s5BE0osLW5X8zPbFXbQL30OsZiAZEA6IB0QCiAdGAaEA0IBoQDSAaEA2IBkQDogFEA6IB0YBoQDQgGkA0IBoQDYgGRAOIBkQDogHRgGhANIBoQDQgGjixKm9UOzuyG/E6wysbjeW4GvP9nvbBy/HWylZ9ruz5C1c24/r5vfzW60Jaq4m0Zn1298WlpbLnXju7F+3JzeGLJlv7sVF7HJ1+T1sUY80q53cvph/3gwzX62ss154MYr3OlT95LI1Jr2fgPw2IBhANiAZEA6IB0QCiAdGAaEA0IBoQDSAaEA2IBkQDogFEA6IB0YBoQDQgGkA0IBoQDYgGRAOIBkQDogHRgGjgFKq+5+a3ND7l2t4Pd/gk69WyfLaqR7M2GtE9k+mq7/R9xtXVtXY6tMuef3NVC4fWTdGs5PdseT0D0YBoQDQgGhANIBoQDYgGRAOiAUQDogHRgGhANCAaQDQgGhANiAZEA4gGRAOigdyiKYqppmUAvzQgGhANiAZEA4gGRAOiAdGAaOB0+ynAAHOuWl3ZFtplAAAAAElFTkSuQmCC" alt="Mistral AI">
    </a>
</p>

<p align="center">
    <a href=".github/version.json" title="Go to changelog" target="_blank">
        <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=Mistral+AI+Toolkit&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2FRMNCLDYO%2Fmistral-ai-toolkit%2Fmain%2F.github%2Fversion.json" alt="Version">
    </a>
</p>

<p align="center">
    <a href=".github/CHANGELOG.md" title="Go to changelog" target="_blank"><img src="https://img.shields.io/badge/maintained-yes-2ea44f?style=for-the-badge" alt="maintained - yes"></a>
    <a href=".github/CONTRIBUTING.md" title="Go to contributions doc" target="_blank"><img src="https://img.shields.io/badge/contributions-welcome-2ea44f?style=for-the-badge" alt="contributions - welcome"></a>
</p>

<p align="center">
    <a href="/">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/RMNCLDYO/mistral-ai-toolkit/main/.github/mistral-logo-dark.png">
          <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/RMNCLDYO/mistral-ai-toolkit/main/.github/mistral-logo-light.png">
          <img alt="Mistral AI" width="500" src="https://raw.githubusercontent.com/RMNCLDYO/mistral-ai-toolkit/main/.github/mistral-logo-light.png">
        </picture>
    </a>
</p>

## Overview

The Mistral AI Toolkit is designed to simplify the use of Mistrals advanced language models through a user-friendly API wrapper and command-line interface (cli). It enables developers and AI enthusiasts to easily integrate and interact with Mistrals open models, streamlining the development process for AI-powered applications, making it easier for anyone to use these models without restrictions.

## Features

- **Simplified API Access**: Easily access Mistral AI models without detailed knowledge of the underlying API.
- **Command-Line Interface (CLI)**: Execute commands and interact with AI models directly from your terminal.
- **Python Wrapper**: Interact with the full suite of AI models offered by Mistral using just two lines of code.
- **Streaming Support**: Utilize streaming responses for real-time interaction with models (similar to ChatGPT).
- **JSON Mode**: Enable JSON-formatted responses for easier parsing and integration into applications.
- **Configurable Parameters**: Tailor model interactions with parameters like a system prompt, max tokens, temperature, top_p and more for customized outputs.

## Prerequisites

- Python 3.8+
- A Mistral account and API key.

## Dependencies
The following Python packages are required:
- `httpx`: For making asynchronous HTTP requests to the Mistral API.
- `asyncio`: Provides support for running asynchronous tasks.

The following Python packages are optional:
- `python-dotenv`: For managing API keys and other environment variables.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/RMNCLDYO/mistral-ai-toolkit.git
    cd mistral-ai-toolkit
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Getting Started

### Obtaining an API Key

> [!IMPORTANT]  
> In order to generate an API key, you must first add your payment information to your Mistral account. API keys can only be generated when your balance is nonzero.

1. Sign up for an account at [Mistral AI](https://mistral.ai/).
2. Add your payment information to your Mistral account.
3. Navigate to `API Keys` in your account settings or access its directly [here](https://console.mistral.ai/api-keys/).
4. Click `Create new key` to create your API Key.
5. Set a name and add an optional expiration date to the key.
6. Copy your API key and store it somewhere safe.

### Configuration (*Optional*)

> [!WARNING]  
> If you choose not to add your API key to an `.env` file, then you must pass your API key to the wrapper or CLI when running the script.

1. Once you have your API key, you can create a new file named `.env` in the root directory (main folder) of this project, or rename the `example.env` file in the root directory of this project to `.env`.
2. You can then add your API key to the `.env` file as follows:
   ```bash
   MISTRAL_API_KEY=your_api_key_here
   ```
3. If you choose not to use a .env file or pass the API key through the wrapper or cli, you can add the API key directly to your system by running the following command from the terminal:
    ```bash
    export MISTRAL_API_KEY=your_api_key_here
    ```
4. The program will automatically load and use your API key whenever you use the toolkit.

## General Usage

### CLI

Initiate a chat session:
```bash
python cli.py
```

Get usage details and options:
```bash
python cli.py --help
```

### Wrapper

```python
from mistral import Mistral

Mistral().chat()
```

> An executable version of this example can be found [here](./examples/example.py). (*You must move this file to the root folder before running the program.*)

## Advanced Configuration

This section provides a comprehensive overview of each configuration option available through the command-line and wrapper interfaces, including their cli flags, example cli and wrapper usage, parameter limits, and detailed descriptions of each option to guide you in customizing your interactions with the full suite of AI models offered by Mistral.

### CLI Options
| **Option(s)**        	    | **Description**                      	| **Example Usage**                                  	|
|-------------------------	|--------------------------------------	|----------------------------------------------------	|
| `-a`,  `--api_key`       	| Mistral API key for authentication   	| --api_key "api_key_goes_here"                      	|
| `-m`,  `--model`         	| The model you would like to use      	| --model "model_name_goes_here"                     	|
| `-sp`, `--system_prompt` 	| Initial system prompt (instructions) 	| --system_prompt "You are an advanced AI assistant" 	|
| `-t`,  `--temperature`   	| Sampling temperature                 	| --temperature 0.7                                  	|
| `-tp`, `--top_p`         	| Nucleus sampling threshold           	| --top_p 0.9                                        	|
| `-mt`, `--max_tokens`    	| Maximum number of tokens to generate 	| --max_tokens 100                                   	|
| `-rs`, `--random_seed`   	| Random seed for sampling             	| --random_seed 42                                   	|
| `-st`, `--stream`        	| Enable streaming mode for responses  	| --stream                                           	|
| `-js`, `--json`          	| Enable JSON mode for responses       	| --json                                             	|
| `-sf`, `--safe_prompt`   	| Enable safe prompt mode              	| --safe_prompt                                      	|

### Wrapper Options
| **Option(s)**   	| **Description**                      	| **Example Usage**                                	|
|-----------------	|--------------------------------------	|--------------------------------------------------	|
| `api_key`       	| Mistral API key for authentication   	| api_key="api_key_goes_here"                      	|
| `model`         	| The model you would like to use      	| model="model_name_goes_here"                     	|
| `system_prompt` 	| Initial system prompt (instructions) 	| system_prompt="You are an advanced AI assistant" 	|
| `temperature`   	| Sampling temperature                 	| temperature=0.7                                  	|
| `top_p`         	| Nucleus sampling threshold           	| top_p=0.9                                        	|
| `max_tokens`    	| Maximum number of tokens to generate 	| max_tokens=100                                   	|
| `random_seed`   	| Random seed for sampling             	| random_seed=42                                   	|
| `stream`        	| Enable streaming mode for responses  	| stream=True                                      	|
| `json`          	| Enable JSON mode for responses       	| json=True                                        	|
| `safe_prompt`   	| Enable safe prompt mode              	| safe_prompt=True                                 	|

### Usage Details
| **Option(s)**   	| **Type** 	| **Default**            	| **Details**                                                                                                                                                                                                                                                                                                              	|
|-----------------	|----------	|------------------------	|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	|
| `api_key`       	| _str_    	| None                   	| Required for authenticating API requests. Your unique API key can be obtained from your Mistral account.                                                                                                                                                                                                                 	|
| `model`         	| _str_    	| `mistral-large-latest` 	| ID of the model to use.                                                                                                                                                                                                                                                                                                  	|
| `system_prompt` 	| _str_    	| None                   	| The initial system prompt. The system prompt explicitly sets the instructions for the model.                                                                                                                                                                                                                             	|
| `temperature`   	| _int_    	| 0.7                    	| What sampling temperature to use, between 0.0 and 1.0. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. Mistral generally recommends altering this or `top_p` but not both.                                                             	|
| `top_p`         	| _int_    	| 1                      	| Nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. Mistral generally recommends altering this or `temperature` but not both.                                                        	|
| `max_tokens`    	| _int_    	| None                   	| The maximum number of tokens to generate in the completion. The token count of your prompt plus `max_tokens` cannot exceed the model's context length.                                                                                                                                                                   	|
| `random_seed`   	| _int_    	| None                   	| The seed to use for random sampling. If set, different calls will generate deterministic results.                                                                                                                                                                                                                        	|
| `stream`        	| _bool_   	| False                  	| Streams back partial progress. If set, tokens will be sent as data-only server-sent events as they become available, with the stream terminated by a data: [DONE] message. Otherwise, the server will hold the request open until the timeout or until completion, with the response containing the full result as JSON. 	|
| `json`          	| _bool_   	| False                  	| Enables json responses by default.                                                                                                                                                                                                                                                                                       	|
| `safe_prompt`   	| _bool_   	| False                  	| Injects a safety prompt before all conversations.                                                                                                                                                                                                                                                                        	|                                                                 	|

## Advanced Usage

### CLI

Initiate a chat session passing your API key, with streaming mode set, and a custom system prompt:
```bash
python cli.py --api_key "your_api_key" --system_prompt "You are a comedian, you respond to all questions as if they are a funny joke." --stream
```

Get usage details and options:
```bash
python cli.py --help
```

### Wrapper

Initiate a chat session using the Mixtral 8x7B model, with json mode initialized and max_tokens set to 100:
```python
from mistral import Mistral

Mistral().chat(model="open-mixtral-8x7b", json=True, max_tokens=100)
```

## Available Models

| **Model**               	| **Context Length *(max_tokens)*** 	| **Model Type**  	|
|-------------------------	|-----------------------------------	|-----------------	|
| `open-mistral-7b`       	| 32000                             	| Chat Completion 	|
| `open-mixtral-8x7b`     	| 32000                             	| Chat Completion 	|
| `mistral-small-latest`  	| 32000                             	| Chat Completion 	|
| `mistral-medium-latest` 	| 32000                             	| Chat Completion 	|
| `mistral-large-latest`  	| 32000                             	| Chat Completion 	|

## API Rate Limits

| **Model**      	| **Endpoint**            	| **Input**         	| **Output**        	|
|----------------	|-------------------------	|-------------------	|-------------------	|
| Mistral 7B     	| `open-mistral-7b`       	| 0.25$ / 1M tokens 	| 0.25$ / 1M tokens 	|
| Mixtral 8x7B   	| `open-mixtral-8x7b`     	| 0.7$ / 1M tokens  	| 0.7$ / 1M tokens  	|
| Mistral Small  	| `mistral-small-latest`  	| 2$ / 1M tokens    	| 6$ / 1M tokens    	|
| Mistral Medium 	| `mistral-medium-latest` 	| 2.7$ / 1M tokens  	| 8.1$ / 1M tokens  	|
| Mistral Large  	| `mistral-large-latest`  	| 8$ / 1M tokens    	| 24$ / 1M tokens   	|

## Contributing
Contributions are welcome!

Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for detailed guidelines on how to contribute to this project.

## Reporting Issues
Encountered a bug? We'd love to hear about it. Please follow these steps to report any issues:

1. Check if the issue has already been reported.
2. Use the [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md) template to create a detailed report.
3. Submit the report [here](https://github.com/RMNCLDYO/mistral-ai-toolkit/issues).

Your report will help us make the project better for everyone.

## Feature Requests
Got an idea for a new feature? Feel free to suggest it. Here's how:

1. Check if the feature has already been suggested or implemented.
2. Use the [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md) template to create a detailed request.
3. Submit the request [here](https://github.com/RMNCLDYO/mistral-ai-toolkit/issues).

Your suggestions for improvements are always welcome.

## Versioning and Changelog
Stay up-to-date with the latest changes and improvements in each version:

- [CHANGELOG.md](.github/CHANGELOG.md) provides detailed descriptions of each release.

## Security
Your security is important to us. If you discover a security vulnerability, please follow our responsible disclosure guidelines found in [SECURITY.md](.github/SECURITY.md). Please refrain from disclosing any vulnerabilities publicly until said vulnerability has been reported and addressed.

## License
Licensed under the MIT License. See [LICENSE](LICENSE) for details.
