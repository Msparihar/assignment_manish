import streamlit as st
from utils import load_data
from llm_handler import handle_input
from prompts import SUMMARY_PROMPT, KEY_OBJECTS_PROMPT

def main():
    st.title("LLM Data Analyzer")

    uploaded_file = st.file_uploader("Choose a file", type=["txt", "jpg", "png", "xlsx", "pdf"])
    
    if uploaded_file is not None:
        if st.button("Generate Summaries and Key Objects"):
            with st.spinner("Parsing input..."):
                parsed_data, parsed_data_json = load_data(uploaded_file)
            
            with st.spinner("Generating summaries..."):
                if uploaded_file.type.startswith("image/"):
                    # For images, pass the image file directly
                    summary = handle_input(SUMMARY_PROMPT, None, image=uploaded_file)
                    key_objects = handle_input(KEY_OBJECTS_PROMPT, None, image=uploaded_file)
                else:
                    # For other file types, pass the parsed data
                    summary = handle_input(SUMMARY_PROMPT, parsed_data)
                    key_objects = handle_input(KEY_OBJECTS_PROMPT, parsed_data)

            st.subheader("Summary")
            st.markdown(summary)

            st.subheader("Key Objects")
            st.markdown(key_objects)

            with st.expander("View Prompts and Parsed Data"):
                st.subheader("Summary Prompt")
                st.code(SUMMARY_PROMPT)
                
                st.subheader("Key Objects Prompt")
                st.code(KEY_OBJECTS_PROMPT)
                
                if not uploaded_file.type.startswith("image/"):
                    st.subheader("Parsed Data")
                    st.json(parsed_data_json)

if __name__ == "__main__":
    main()