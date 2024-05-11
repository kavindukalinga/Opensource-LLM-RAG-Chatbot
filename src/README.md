# Chat-bot App

```bash
pip install -r requirements.txt
```

```bash
/bin/python3 "/home/kkalinga/Documents/ISA intern/rag-search/Opensource-LLM-RAG-Chatbot/src/populate_database.py"
# Number of existing documents in DB: 65
# ✅ No new documents to add
```

```bash
/bin/python3 "/home/kkalinga/Documents/ISA intern/rag-search/Opensource-LLM-RAG-Chatbot/src/query_data.py" "What is Grafana?"
# Response: Based on the provided context, I'd say that Grafana is a popular open-source platform for building beautiful and interactive dashboards to visualize and explore data from multiple sources.
# Sources: []
```

```bash
docker run -p 5000:5000 -v ./Data/:/Data/ -v ./chroma/huggingface:/chroma/huggingface --name conbot co
nfluencebot

docker run -p 5000:5000 -v "/home/kkalinga/Documents/ISA intern/rag-search/Opensource-LLM-RAG-Chatbot/Data":/Data/ --name conbot confluencebot

docker run -p 5000:5000 -v "/home/kkalinga/Documents/ISA intern/rag-search/Opensource-LLM-RAG-Chatbot/Data":/Data/ -v "/home/kkalinga/Documents/ISA intern/rag-search/Opensource-LLM-RAG-Chatbot/src/mydockerdata":/chroma --name conbot confluencebot
```
