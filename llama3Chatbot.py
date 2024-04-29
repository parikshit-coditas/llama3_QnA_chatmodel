from langchain_community.llms import Ollama
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.memory import ChatMemoryBuffer

llm=Ollama(base_url='http://localhost:11434', model='llama3')

with open('data/questions.txt', 'r') as file:
    questions = file.readlines()

with open('chat_document/answers.txt', 'w') as file:
    for question in questions:
        question_number = question.split('.')[0]
        while True:
            answer = input(question.strip() + '\nAns: ')
            response = llm.invoke("If answer to give question is valid and not empty then just say single word valid and if not then invalid, make judgment of answer based on following questions with it's answer \n "+f"{question.strip()}\nAns: {answer}\n")
            if 'Invalid' in response: 
               print("Please provide a valid answer.")
            else:
                break
        file.write(f"{question.strip()}\nAns: {answer}\n")


data = SimpleDirectoryReader(input_dir="./chat_document/").load_data()
index = VectorStoreIndex.from_documents(data)

memory = ChatMemoryBuffer.from_defaults(token_limit=400)

chat_engine = index.as_chat_engine(
    chat_mode="context",
    memory=memory,
    system_prompt=(
        """
        Hello! I'm here to help gather information based on a document  provide. Please upload the document containing the information you'd like me to inquire about. Once you've uploaded it, I'll start asking questions to gather the necessary details.
        After each question, please provide a clear and accurate response. If the answer is invalid or not satisfactory, please let me know, and I'll ask again. Once all questions are answered, I'll confirm the information and be able to answer questions related to the gathered data.
        Let's get started! Please upload the document.
        """
    ),
)

while True:
    query = input('Please enter your query (or type "exit" to quit): ')
    if query.lower() == 'exit':
        break
    
    response = chat_engine.chat(query)
    print(response)