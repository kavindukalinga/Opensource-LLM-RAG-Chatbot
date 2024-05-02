# Opensource LLM RAG Chatbot

- Project : An NLP project aimed at crafting a chatbot capable of answering questions sourced from provided documents. It leverages open-source large language models (LLM) and retrieval augmented generation (RAG) techniques for this purpose.
- Author: Kavindu Kalinga
- Tools: `ollama` , `langchain` ,`ipynb`
- Concepts used: `Natural Language Processing(NLP)`, `Large Language Models(LLM)`, `Retrieval Augmented Generation (RAG)`
- Models used: `llama3:latest`, `nomic-embed-text:latest`, `mxbai-embed-large:latest`
- Languages: `python3`
- Packages and APIs: `crewai`,`faiss-cpu`, `langchain`, `chromadb`, `pypdf`, `pytest`

## Content

- [Opensource LLM RAG Chatbot](#opensource-llm-rag-chatbot)
  - [Content](#content)
  - [Ollama](#ollama)
  - [Ollama models](#ollama-models)
  - [Contributors](#contributors)

## Ollama

Download and Install **Ollama** : <https://ollama.com/download>

```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh
```

```bash
# Usage:
  ollama [flags]
  ollama [command]

# Available Commands:
  serve       Start ollama
  create      Create a model from a Modelfile
  show        Show information for a model
  run         Run a model
  pull        Pull a model from a registry
  push        Push a model to a registry
  list        List models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

# Flags:
  -h, --help      help for ollama
  -v, --version   Show version information
```

## Ollama models

```bash
ollama pull llama3:latest
ollama pull mxbai-embed-large
ollama pull nomic-embed-text:latest
ollama list
```

Make sure `Ollama is running` running on `http://127.0.0.1:11434/`.  
Otherwise run:

```bash
ollama serve
```

```bash
#Example Case:
curl -X POST http://localhost:11434/api/generate -d '{
  "model": "llama3",
  "prompt":"Why is the sky blue?"
 }'
```

## Contributors

<p align="left"> <b>Author : Kavindu Kalinga </b>
<a href="https://www.linkedin.com/in/kalingachandrasiri" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="kalingachandrasiri" height="15" width="20" /></a>
<a href="https://twitter.com/yuk_kalinga_c" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="kavindukalinga" height="15" width="20" /></a>
<a href="https://stackoverflow.com/users/16277941/kavindu-kalinga" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/stack-overflow.svg" alt="kavindu-kalinga" height="15" width="20" /></a>
<a href="https://www.facebook.com/kavindu.kalinga" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="kavindu.kalinga" height="15" width="20" /></a>
<a href="https://www.instagram.com/kavindu_kalinga" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="kavindu_kalinga" height="15" width="20" /></a>
<a href="https://discord.gg/CrazzyHawK#8536" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/discord.svg" alt="CrazzyHawK#8536" height="15" width="20" /></a>
</p>

<a href="https://github.com/kavindukalinga/Opensource-LLM-RAG-Chatbot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kavindukalinga/Opensource-LLM-RAG-Chatbot" />
</a>
