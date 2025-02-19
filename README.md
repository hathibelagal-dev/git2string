# repo-to-prompt
repo-to-prompt is a powerful tool that can quickly convert an entire Git repository to a prompt that can be fed to any large language model (LLM).

It will automatically ignore all binary files. Additionally, it will respect your **.gitignore**.

## Usage

```
repo-to-prompt <repo root directory>
```

By default, the prompt will be generated in a file called **llm_prompt.txt**.

You can specify a different filename as follows:

```
repo-to-prompt <repo root directory> --output-file <filename>
```

## Additional Features

- Can count tokens for most OpenAI models
