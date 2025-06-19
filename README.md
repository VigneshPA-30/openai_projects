# LangChain Projects Collection

This repository contains a collection of projects demonstrating various capabilities of LangChain with OpenAI integration. Each project showcases different aspects of AI-powered applications.

## Project Structure

The workspace contains four main projects:

### 1. Test API (project1-test_api)
A project that demonstrates the use of LangChain's sequential chains to:
- Generate code based on user requirements
- Automatically create tests for the generated code
- Supports multiple programming languages
- Uses OpenAI's API for code generation

### 2. Chatbot (project2-chatbot)
An interactive chatbot implementation that features:
- Persistent conversation memory using file storage
- ChatGPT integration via LangChain
- Interactive command-line interface
- Message history stored in JSON format

### 3. Embeddings Project (project3-embeddings)
A text similarity search system that:
- Processes and splits text documents
- Creates embeddings using OpenAI
- Uses Chroma for vector storage
- Implements similarity search functionality
- Includes custom text splitting configuration

### 4. AI Agents (project4-agents)
An advanced implementation of AI agents that:
- Integrates with SQLite database
- Provides database querying capabilities
- Includes report generation functionality
- Uses OpenAI Functions for agent execution
- Implements conversation memory
- Custom handlers for chat model interactions

## Setup and Installation

1. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Linux/Mac
# or
.\env\Scripts\activate  # On Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Each project can be run independently from its respective directory:

### Test API
```bash
cd project1-test_api
python main.py --task "your task" --language "programming language"
```

### Chatbot
```bash
cd project2-chatbot
python main.py
```

### Embeddings
```bash
cd project3-embeddings
python main.py
```

### Agents
```bash
cd project4-agents
python main.py
```

## Requirements

- Python 3.12+
- OpenAI API key
- Required packages listed in requirements.txt

## License

This project is for educational purposes as part of a Udemy course on ChatGPT and LangChain integration.

## Note

Make sure to handle your API keys securely and never commit them to version control.