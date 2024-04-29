# LLAMA_3_CHATBOT

This project utilizes the llama3 LLM to read questions from the `data/questions.txt` file, ask users for answers, and validate those answers. If an answer is invalid, it repeatedly asks the question until a valid response is provided. Once all questions are answered, it comprehends the information and functions as a chat model to provide that information. If the information is not available, it prompts that it doesn't have the answer.

## Prerequisites

Before you begin, ensure you have the following installed:

- Mac OS
- Python 3
- pip3 (Python package installer)
- Ollama with llam3 model downloaded and running on local machine

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/parikshit-coditas/llama3_QnA_chatmodel.git
    ```

2. **Run the setup script:**

    First, make the setup script executable:

    ```bash
    chmod +x setup.sh
    ```

    Then, execute the setup script:

    ```bash
    ./setup.sh
    ```

    This script will:
    - Create a virtual environment named `venv`.
    - Activate the virtual environment.
    - Install project dependencies from `requirements.txt`.

3. Run `llama3Chatbot.py` to execute code.

    Run following command in terminal. Make sure ollama with llama3 is running
     ```bash
     ollama run llama3
     ```

    To execute code just run

    ```bash
    python3 llama3Chatbot.py
    ```