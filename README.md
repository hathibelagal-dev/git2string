# repo-to-prompt
repo-to-prompt, or R2P, is a powerful tool that can quickly convert an entire Git repository to a prompt that can be fed to any large language model (LLM).

It will automatically ignore all binary files. Additionally, it will respect your **.gitignore**.

## Usage

If you're already in a git repo:
```
r2p -repo .
```

Alternatively, you can pass a git URL to the tool:
```
r2p -repo <repo url>
```

The prompt will be generated in a file called **r2p_output.txt**.

## Output formats

A simple .txt file would be sufficient for most use cases. But the tool also supports the following output formats:

- Markdown
- JSON

## Additional Features

- Can count tokens for most OpenAI models
