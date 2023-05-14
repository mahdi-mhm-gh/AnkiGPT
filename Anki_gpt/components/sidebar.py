import streamlit as st

from components.faq import faq


def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "2. Upload a pdf, docx, or txt file📄\n"
            "3. Enter the subject you want to make flashcards for🧾\n"
        )
        api_key_input = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
            value=st.session_state.get("OPENAI_API_KEY", ""),
        )

        if api_key_input:
            set_openai_api_key(api_key_input)

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "💥AnkiGPT allows you to make flashcards for Anki app. "
            "Just upload your document and enter the subject you want "
            "and boom💥. You recieve a csv file that is ready to import Anki app"
        )
        st.markdown(
            "This tool is a work in progress. "
            "You can contribute to the project on [GitHub](https://github.com/mahdi-mhm-gh/AnkiGPT) "  # noqa: E501
            "with your feedback and suggestions💡"
        )
        st.markdown("Made by [Mahdi_Mohammadian](https://www.linkedin.com/in/mahdi-mohammadian-50058b201/)")
        st.markdown("---")

        faq()
