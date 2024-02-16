import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


# function to get response from llama 2 model
def getLLamaresponse(input_text, no_of_words, blog_style):

    # LLama2 Model
    llm = CTransformers(model=dir_path + '/model/llama-2-7b-chat.ggmlv3.q3_K_S.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})

    # Prompt Template

    template = f"""Write a blog for {blog_style} job profile for a topic {input_text}
                    within {no_of_words} words."""

    prompt = PromptTemplate(
        input_variables=['style', 'text', 'n_words'],
        template=template
    )

    # Generate the response from the LLama 2 model
    response = llm(prompt.format(style=blog_style,
                                 text=input_texts,
                                 n_words=no_of_words))
    print(response)
    return response


st.set_page_config(
    page_title='Blogs Generate',
    layout='centered',
    initial_sidebar_state='collapsed'
)
st.header('Blogs Generator ')

input_texts = st.text_input('Enter your Blog Topic')

# Creating two more columns for additional 2 fileds

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No_of_Words')

with col2:
    blog_style = st.selectbox('Writing the Blog for', ('Researcher', 'Data Science', 'Common People'),
                              index=0
                              )

submit = st.button('Generate')

# Final response"
if submit:
    st.write(getLLamaresponse(input_text=input_texts, no_of_words=no_words, blog_style=blog_style))

