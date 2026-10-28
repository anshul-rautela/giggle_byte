<p align="center">
  <img src="assets/banner.svg" alt="GiggleByte banner" width="100%">
</p>

# GiggleByte CLI Chatbot

![Python](https://img.shields.io/badge/Python-3-3776AB?logo=python&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-local-000000)
![Llama 3.1](https://img.shields.io/badge/Model-Llama%203.1-blue)
![OpenAI SDK](https://img.shields.io/badge/OpenAI-SDK-412991?logo=openai&logoColor=white)

GiggleByte is a command-line chatbot with a stand-up comedian personality. It is built with Python and the OpenAI SDK, and runs on a local Llama 3.1 model through Ollama with real-time streaming responses.

## Features

- **Stand-up comedian persona:** Answers include puns, humorous analogies, and a lighthearted tone.
- **Conversational memory:** Context is preserved across turns, so conversations flow naturally.
- **Streaming responses:** Replies appear in the terminal in real time as the model generates them.
- **Fully local and private:** Everything runs on your machine through Ollama. No data leaves your device and no API key is required.

## Prerequisites

- Python 3
- [Ollama](https://ollama.com/) installed and running locally
- The Llama 3.1 model pulled in Ollama

To download and start the model:

```bash
ollama run llama3.1
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/giggle_byte.git
cd giggle_byte
```

2. Create and activate a virtual environment (recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install openai
```

## Usage

Make sure Ollama is running, then start the chatbot:

```bash
python3 giggle_byte.py
```

Type your questions at the prompt and GiggleByte will respond in character. Type `exit` to quit.

## Tech Stack

- Python
- OpenAI SDK (used as a client for Ollama's OpenAI-compatible API)
- Ollama
- Llama 3.1
