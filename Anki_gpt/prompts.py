# flake8: noqa
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


## Use a shorter template to reduce the number of tokens in the prompt
template="""
        Regarding the formulation of the card content, you stick to two principles: First, minimum information principle: The material you learn must be formulated in as simple way as it is only possible. 
        Simplicity does not have to imply losing information and skipping the difficult part. Second, optimize wording: The wording of your items must be optimized to make sure that in minimum time the right bulb in your brain lights up. 
        This will reduce error rates, increase specificity, reduce response time, and help your concentration.
        The questions should be concise and clear, and the answers should be accurate and informative.Please generate flashcards in csv format and put semicolon (;) between questions and answers.
       This is an example of how you should generate flashcard :"Q: the question you generate;A:the answer of question
        """


system_message_prompt = SystemMessagePromptTemplate.from_template(template)
human_template = "I am a medical student and I want you to act as a professional flashcard creator, able to create several Anki flashcards from this text: {text}"
human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])


