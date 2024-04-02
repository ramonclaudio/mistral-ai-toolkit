<p align="center">
    <a href="https://mistral.ai/" title="Go to mistral.ai">
        <img src="https://img.shields.io/badge/MISTRAL%20AI-FF7000?style=for-the-badge&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAM0AAAC9CAYAAAAQnvmoAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyBJREFUeNrs3cFKVFEcwOH/6FSEBSoRhHcxi1aFIO1s00Tv0C7GR8hdO2cTLe0Vol3vEE4vEEKrNhKkBRalY1bqmJ2ibaT3zuRx/D443NU9zD33/mburE4tkqKYakZJs9M78ezhx8jQRu1GLAfHKj1bM+kwPkzPVv3PcWkI71cnjdse22O3mEZzmC5oxD0F0YBoQDQgGhANIBoQDYgGRAOiAUQDogHRgGhANCAaQDQgGhANiAZEA4gGRAOiAdGAaEA0gGhANCAaEA2IBhANgzcuGjiaGdHAKVevPMN+GtsZXlkvGgdPo53hJ+vU7v3eRLevimJqLh0aZc9/+2htIBe7+Hyr/DVd7kV8GMZovqfxJssvhF8P0EKmX1adAczZigx3UZ6/0602wbrXM/CfBkQDiAZEA6IB0YBoANGAaEA0IBoQDYgGEA2IBkQDogHRAKIB0YBoQDQgGhANIBoQDYgGRAOiAUQDogHRgGhANCAa4F+qb1S7k8Z7C3lo29E6uB+3+j3tq8/rM196Fb4D3cP/GM1uGu8s5BE0osLW5X8zPbFXbQL30OsZiAZEA6IB0QCiAdGAaEA0IBoQDSAaEA2IBkQDogFEA6IB0YBoQDQgGkA0IBoQDYgGRAOIBkQDogHRgGhANIBoQDQgGjixKm9UOzuyG/E6wysbjeW4GvP9nvbBy/HWylZ9ruz5C1c24/r5vfzW60Jaq4m0Zn1298WlpbLnXju7F+3JzeGLJlv7sVF7HJ1+T1sUY80q53cvph/3gwzX62ss154MYr3OlT95LI1Jr2fgPw2IBhANiAZEA6IB0QCiAdGAaEA0IBoQDSAaEA2IBkQDogFEA6IB0YBoQDQgGkA0IBoQDYgGRAOIBkQDogHRgGjgFKq+5+a3ND7l2t4Pd/gk69WyfLaqR7M2GtE9k+mq7/R9xtXVtXY6tMuef3NVC4fWTdGs5PdseT0D0YBoQDQgGhANIBoQDYgGRAOiAUQDogHRgGhANCAaQDQgGhANiAZEA4gGRAOigdyiKYqppmUAvzQgGhANiAZEA4gGRAOiAdGAaOB0+ynAAHOuWl3ZFtplAAAAAElFTkSuQmCC" alt="Mistral AI">
    </a>
</p>

<p align="center">
    <a href=".github/CHANGELOG.md" title="Go to Changelog">
        <img src="https://img.shields.io/badge/dynamic/json?style=for-the-badge&label=Mistral+AI+Toolkit&query=version&url=https%3A%2F%2Fraw.githubusercontent.com%2FRMNCLDYO%2Fmistral-ai-toolkit%2Fmain%2F.github%2Fversion.json" alt="Version">
    </a>
</p>

<p align="center">
    <a href=".github/CHANGELOG.md" title="Go to changelog"><img src="https://img.shields.io/badge/maintained-yes-2ea44f?style=for-the-badge" alt="maintained - yes"></a>
    <a href=".github/CONTRIBUTING.md" title="Go to contributions doc"><img src="https://img.shields.io/badge/contributions-welcome-2ea44f?style=for-the-badge" alt="contributions - welcome"></a>
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
The Mistral AI Toolkit makes it easy to use Mistral's open models `Mistral-7b` and `Mixtral-8x7b` along with their flagship suite of models `Mistral (tiny, small, medium & large)` for creating chatbots and generating contextually relevant text based on prompts. It's designed for everyone, from beginners to experienced developers, allowing quick addition of AI features to projects with simple commands. While it offers simplicity and lightweight integration, it doesn't compromise on power; experienced developers can access the full suite of advanced options available via the API, ensuring robust customization and control. This toolkit is perfect for those looking to efficiently tap into advanced AI without getting bogged down in technical details, yet it still provides the depth needed for complex project requirements.

## Key Features
- **Chat Functionality**: Engage in interactive conversations with Mistral's suite of open and advanced conversational models.
- **Text Generation**: Produce creative and contextually relevant text based on prompts.
- **Command-Line Interface (CLI)**: Access the full suite of functionalities directly from the command line.
- **Python Wrapper**: Simplify interaction with Mistral's open models in only 2 lines of code.
- **Streamed Responses**: Receive responses as they are generated for real-time interaction.
- **JSON Mode**: Enable JSON-formatted responses for easier parsing and integration into applications.
- **Flexible Configuration**: Customize the token limits, system prompt, random seed, temperature and more.
- **Minimal Dependencies**: Built to be efficient and lightweight, requiring only the `requests` package for operation.

## Prerequisites
- `Python 3.x`
- An API key from Mistral AI

## Dependencies
The following Python packages are required:
- `requests`: For making HTTP requests to Mistral's API.

The following Python packages are optional:
- `python-dotenv`: For managing API keys and other environment variables.

## Installation
To use the Mistral AI Toolkit, clone the repository to your local machine and install the required Python packages.

Clone the repository:
```bash
git clone https://github.com/RMNCLDYO/mistral-ai-toolkit.git
```

Navigate to the repositories folder:
```bash
cd mistral-ai-toolkit
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Configuration
1. Obtain an API key from [Mistral AI](https://mistral.ai/).
2. You have three options for managing your API key:
   <details>
   <summary>Click here to view the API key configuration options</summary>
   
   - **Setting it as an environment variable on your device (recommended for everyday use)**
       - Navigate to your terminal.
       - Add your API key like so:
         ```shell
         export MISTRAL_API_KEY=your_api_key
         ```
       This method allows the API key to be loaded automatically when using the wrapper or CLI.
     
   - **Using an .env file (recommended for development):**
       - Install python-dotenv if you haven't already: `pip install python-dotenv`.
       - Create a .env file in the project's root directory.
       - Add your API key to the .env file like so:
         ```makefile
         MISTRAL_API_KEY=your_api_key
         ```
       This method allows the API key to be loaded automatically when using the wrapper or CLI, assuming you have python-dotenv installed and set up correctly.
     
   - **Direct Input:**
       - If you prefer not to use a `.env` file, you can directly pass your API key as an argument to the CLI or the wrapper functions.
         
         ***CLI***
         ```shell
         --api_key your_api_key
         ```
         ***Wrapper***
         ```shell
         api_key="your_api_key"
         ```
       This method requires manually inputting your API key each time you initiate an API call, ensuring flexibility for different deployment environments.
   </details>

## Usage
The Mistral AI Toolkit can be used in two different modes: `Chat` and `Text`. Each mode is designed for specific types of interactions with Mistral's open models.

## Chat Mode
Chat mode is intended for chatting with an AI model (similar to a chatbot) or building conversational applications.

#### Example Usage

***CLI***
```bash
python cli.py --chat
```

***Wrapper***
```python
from mistral import Chat

Chat().run()
```

> An executable version of this example can be found [here](./examples/example_chat.py). (*You must move this file to the root folder before running the program.*)

## Text Mode
Text mode is suitable for generating text content based on a provided prompt.

#### Example Usage

***CLI***
```bash
python cli.py --text --prompt "Which one is heavier a pound of iron or a kilogram of feathers?"
```

***Wrapper***
```python
from mistral import Text

Text().run(prompt="Which one is heavier a pound of iron or a kilogram of feathers?")
```

> An executable version of this example can be found [here](./examples/example_text.py). (*You must move this file to the root folder before running the program.*)

## Advanced Configuration

### CLI and Wrapper Options
| **Description**              | **CLI Flags**            | **CLI Usage**                                      | **Wrapper Usage**                                |
|------------------------------|--------------------------|----------------------------------------------------|--------------------------------------------------|
| Enable chat mode             | `-c`,  `--chat`          | --chat                                             | *See mode usage above.*                          |
| Enable text mode             | `-t`,  `--text`          | --text                                             | *See mode usage above.*                          |
| API key for authentication   | `-a`,  `--api_key`       | --api_key "your_api_key"                           | api_key="your_api_key"                           |
| Model name                   | `-m`,  `--model`         | --model "mistral-large-latest"                     | model="mistral-large-latest"                     |
| User prompt                  | `-p`,  `--prompt`        | --prompt "Hello, how are you today?"               | prompt="Hello, how are you today?"               |
| Enable streaming mode        | `-s`,  `--stream`        | --stream                                           | stream=True                                      |
| Enable json mode             | `-js`, `--json`          | --json                                             | json=True                                        |
| System prompt (instructions) | `-sp`, `--system_prompt` | --system_prompt "You are an advanced AI assistant" | system_prompt="You are an advanced AI assistant" |
| Maximum tokens to generate   | `-mt`, `--max_tokens`    | --max_tokens 1024                                  | max_tokens=1024                                  |
| Sampling temperature         | `-tm`, `--temperature`   | --temperature 0.7                                  | temperature=0.7                                  |
| Nucleus sampling threshold   | `-tp`, `--top_p`         | --top_p 0.9                                        | top_p=0.9                                        |
| Random seed for sampling     | `-rs`, `--random_seed`   | --random_seed 42                                   | random_seed=42                                   |
| Enable safe prompt mode      | `-sf`, `--safe_prompt`   | --safe_prompt                                      | safe_prompt=True                                 |

## Available Models

| **Model**               | **Max Tokens*** |
|-------------------------|-----------------|
| `open-mistral-7b`       | 32000           |
| `open-mixtral-8x7b`     | 32000           |
| `mistral-small-latest`  | 32000           |
| `mistral-medium-latest` | 32000           |
| `mistral-large-latest`  | 32000           |

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
