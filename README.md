# Local OpenAI Agent with Ollama Sample

This repository provides a sample application demonstrating how to run a local AI agent using [Ollama](https://ollama.com/), an open-source tool for running large language models locally. The project mimics the behavior of an OpenAI-like agent, offering both a web-based chat interface and a simple command-line example.

## Features
- **Single Agent CLI Example**: A standalone script (single-agent-assistant.py) to query the Ollama agent directly from the terminal.
- **Multi Agents CLI Example**: A standalone script (duckduckgo_search_news.py) to query multiple Ollama agent directly from the terminal.
- **Web UI**: A Chainlit-based interface for chatting with the Ollama agent in real-time (agent-assistant-ui.py).
- **Local Execution**: Runs entirely offline, leveraging Ollama’s capabilities.

## Prerequisites
- Python 3.8 or higher
- [Ollama](https://ollama.com/) installed locally
- A compatible language model downloaded via Ollama (e.g., `llama3` or similar)
- pip install -U openai-agents chainlit duckduckgo-search python-dotenv httpx
- Create a .env file in your workspace root and add variables
    OPENAI_API_KEY: ccxxxxxccvv


## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/rajeshmuraleedharan/local-openai-agent-with-ollama-sample.git
   cd local-openai-agent-with-ollama-sample
   ```
2. Set Up a Virtual Environment (optional but recommended)
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install Dependencies
    ```bash
    pip install ollama
    ollama pull llama3
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