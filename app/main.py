import streamlit as st
from utils import load_data
from llm_handler import handle_input
from prompts import SUMMARY_SYSTEM_PROMPT, KEY_OBJECTS_SYSTEM_PROMPT, SUMMARY_USER_PROMPT, KEY_OBJECTS_USER_PROMPT

@st.cache_data
def cache_file_data(file):
    """Cache the parsed data and JSON for a given file."""
    parsed_data, parsed_data_json = load_data(file)
    return parsed_data, parsed_data_json

def main():
    """Main function to run the LLM Data Analyzer Streamlit app."""
    st.set_page_config(page_title="LLM Data Analyzer", page_icon="🔍", layout="wide")
    
    st.title("🔍 LLM Data Analyzer")
    st.markdown("---")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Upload Your File")
        uploaded_file = st.file_uploader("Choose a file", type=["txt", "jpg", "png", "xlsx", "pdf"])
    
    with col2:
        st.subheader("ℹ️ Supported File Types")
        st.markdown("""
        - Text (.txt)
        - Images (.jpg, .png)
        - Excel (.xlsx)
        - PDF (.pdf)
        """)
    
    if uploaded_file is not None:
        st.success(f"File uploaded: {uploaded_file.name}")
        
        if st.button("Generate Summaries and Key Objects", key="generate_button"):
            with st.spinner("🔍 Analyzing your data..."):
                if uploaded_file.type.startswith("image/"):
                    parsed_data, parsed_data_json = "", {}
                else:
                    parsed_data, parsed_data_json = cache_file_data(uploaded_file)
                
                if uploaded_file.type.startswith("image/"):
                    summary = handle_input(SUMMARY_SYSTEM_PROMPT, SUMMARY_USER_PROMPT, image=uploaded_file)
                    key_objects = handle_input(KEY_OBJECTS_SYSTEM_PROMPT, KEY_OBJECTS_USER_PROMPT, image=uploaded_file)
                else:
                    summary = handle_input(SUMMARY_SYSTEM_PROMPT, SUMMARY_USER_PROMPT, parsed_data)
                    key_objects = handle_input(KEY_OBJECTS_SYSTEM_PROMPT, KEY_OBJECTS_USER_PROMPT, parsed_data)

            st.markdown("---")
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("📝 Summary")
                st.info(summary)

            with col2:
                st.subheader("🔑 Key Objects")
                st.info(key_objects)

            st.markdown("---")
            with st.expander("🔍 View Prompts and Parsed Data"):
                tab1, tab2, tab3, tab4 = st.tabs(["Summary System Prompt", "Summary User Prompt", "Key Objects System Prompt", "Key Objects User Prompt"])
                
                with tab1:
                    st.code(SUMMARY_SYSTEM_PROMPT)
                
                with tab2:
                    st.code(SUMMARY_USER_PROMPT)
                
                with tab3:
                    st.code(KEY_OBJECTS_SYSTEM_PROMPT)
                
                with tab4:
                    st.code(KEY_OBJECTS_USER_PROMPT)

            st.markdown("---")
            with st.expander("📊 View Parsed Data"):
                st.info("Parsed data would be displayed here.")

if __name__ == "__main__":
    main()