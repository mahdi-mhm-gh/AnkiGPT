import streamlit as st


def faq():
    st.markdown(
        """
# FAQ
## How does AnkiGPT work?
Upload a file (txt, docx or pdf) and write the subject you want flashcards for. 
AnkiGPT will generate a csv file of Q/A flashcards based on your document and subject.
"The CSV file containing information related to your subject can be located 
in the AnkiGPT directory under the name of the subject."

## What should I do if I face with this error:"IndexError: list index out of range"?
Please press the submit button again. This is the first version of AnkiGPT and I will try to fix this bug😊

## Is my data safe?
Yes, your data is safe. AnkiGPT does not store your documents or
questions. All uploaded data is deleted after you close the browser tab.

## Why does it take so long to index my document?
If you are using a free OpenAI API key, it will take a while to index
your document. This is because the free API key has strict [rate limits](https://platform.openai.com/docs/guides/rate-limits/overview).
To speed up the indexing process, you can use a paid API key.



## Are the answers 100% accurate?
No, the answers are not 100% accurate. AnkiGPT uses chatGPT to generate
answers. chatGPT is a powerful language model, but it sometimes makes mistakes 
and is prone to hallucinations.

"""
    )
