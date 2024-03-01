import argparse
from mistral import Mistral

def main():
    class CustomFormatter(argparse.ArgumentDefaultsHelpFormatter,
                      argparse.RawDescriptionHelpFormatter):
        pass
    parser = argparse.ArgumentParser(
        description="""
    ------------------------------------------------------------------
                            Mistral AI Toolkit                          
                   API Wrapper & Command-line Interface               
                          [v1.0.0] by @rmncldyo                      
    ------------------------------------------------------------------

    Mistral AI toolit is an API wrapper and command-line interface for Mistral AI's suit of large language models.

    | Option(s)            | Description                          | Example Usage                                      |
    |----------------------|--------------------------------------|----------------------------------------------------|
    | -a,  --api_key       | Mistral API key for authentication   | --api_key "api_key_goes_here"                      |
    | -m,  --model         | The model you would like to use      | --model "model_name_goes_here"                     |
    | -sp, --system_prompt | Initial system prompt (instructions) | --system_prompt "You are an advanced AI assistant" |
    | -t,  --temperature   | Sampling temperature                 | --temperature 0.7                                  |
    | -tp, --top_p         | Nucleus sampling threshold           | --top_p 0.9                                        |
    | -mt, --max_tokens    | Maximum number of tokens to generate | --max_tokens 100                                   |
    | -rs, --random_seed   | Random seed for sampling             | --random_seed 42                                   |
    | -st, --stream        | Enable streaming mode for responses  | --stream                                           |
    | -js, --json          | Enable JSON mode for responses       | --json                                             |
    | -sf, --safe_prompt   | Enable safe prompt mode              | --safe_prompt                                      |
    """,
        formatter_class=CustomFormatter,
        epilog="For detailed usage information, visit our ReadMe here: github.com/RMNCLDYO/mistral-ai-toolkit"
    )
    parser.add_argument('-a', '--api_key', type=str, help='Mistral API key for authentication', metavar='')
    parser.add_argument('-m', '--model', type=str, default='mistral-large-latest', help='The model you would like to use', metavar='')
    parser.add_argument('-sp', '--system_prompt', type=str, help='Initial system prompt (instructions)', metavar='')
    parser.add_argument('-t', '--temperature', type=float, help='Sampling temperature', metavar='')
    parser.add_argument('-tp', '--top_p', type=float, help='Nucleus sampling threshold', metavar='')
    parser.add_argument('-mt', '--max_tokens', type=int, help='Maximum number of tokens to generate', metavar='')
    parser.add_argument('-rs', '--random_seed', type=int, help='Random seed for sampling', metavar='')
    parser.add_argument('-st', '--stream', action='store_true', help='Enable streaming mode for responses')
    parser.add_argument('-js', '--json', action='store_true', help='Enable JSON mode for responses')
    parser.add_argument('-sf', '--safe_prompt', action='store_true', help='Enable safe prompt mode')

    args = parser.parse_args()

    client = Mistral()
    client.chat(api_key=args.api_key, model=args.model, system_prompt=args.system_prompt, temperature=args.temperature, top_p=args.top_p, max_tokens=args.max_tokens, random_seed=args.random_seed, stream=args.stream, json=args.json, safe_prompt=args.safe_prompt)

if __name__ == "__main__":
    main()