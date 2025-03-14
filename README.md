# Local OpenAI Agents with Ollama

This repository contains sample implementations of LLM agents using Google Gemma 3 and other models like Qwen2 and GPT-2. The goal is to provide a comprehensive guide and examples for developers interested in leveraging LLM technology.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)


## Introduction
To get started, clone the repository and install the necessary dependencies:

```bash
1) Download - download https://ollama.com/download
2) run "ollama pull gemma3" from your vscode cmd
3) run "ollama pull qwen2:0.5b" from your vscode cmd
4) pip install -U openai-agents chainlit duckduckgo-search python-dotenv httpx
5) Create a .env file in your workspace root and add variables
    OPENAI_API_KEY: ccxxxxxccvv

```

#Running the single-agent-assistant.py Script
The single-agent-assistant.py demonstrates about how to create a Single OpenAI Agent

To run this script, execute it with Python: 
```bash
python .\single-agent-assistant.py
```
![image](https://github.com/user-attachments/assets/81fd2a3a-5f66-41e8-b6df-15b82c86e03f)

#Running the duckduckgo_search_news.py Script - Multi Agents news search
To run this script, execute it with Python: 
```bash
python .\duckduckgo_search_news.py
```

#Running the agent-assistant-ui.py -  Multi Agents news search via UI
To run this script, execute it with Python: 
```bash
chainlit run .\agent-assistant-ui.py
```