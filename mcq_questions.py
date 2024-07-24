import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
st.title("Create MCQ on any topic")

chat_open_ai = ChatOpenAI(model='gpt-3.5-turbo-0125', openai_api_key=api_key)
topic = st.text_input("Enter the topic")
no_of_questions = st.text_input("How many questions you want?")

if st.button("Generate"):
    mcq_prompt = f'''
                Create multiple choice questions in the following format:
                Topic: {topic}
                1: [Question here]
                A) [Option A]
                B) [Option B]
                C) [Option C]
                D) [Option D]
                Correct Answer: [Correct Answer]

                Generate {no_of_questions} questions on the topic of {topic}.
                Questions should be in one line, and options should be listed on separate lines.
                The alignment should be proper heading ,question and option should come seperate lines.
                '''

    response = chat_open_ai.invoke(mcq_prompt)
    print(response.content)
    formatted_response = response.content.replace('A)', '\nA)').replace('B)', '\nB)').replace('C)', '\nC)').replace('D)', '\nD)')
    formatted_response = formatted_response.replace('Correct Answer:', '\nCorrect Answer:')
    st.header(f"MCQs on {topic}")
    st.write(formatted_response)
