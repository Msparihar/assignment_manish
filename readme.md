# LLM Data Analyzer

This project provides a Streamlit-based UI for analyzing different types of data (text, images, spreadsheets, and PDFs) using Language Model (LLM) prompts.

![LLM Data Analyzer](./images/Screenshot%202024-08-25%20025241.png)

## Setup and Running

### Using Docker Compose (Recommended)

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone this repository:

   ```
   git clone https://github.com/yourusername/assignment_manish.git
   cd assignment_manish
   ```

3. Create a `.env` file in the project root and add your Unstructured API key and OpenAI API key:

   ```
   UNSTRUCTURED_API_KEY=your_unstructured_api_key_here
   UNSTRUCTURED_API_URL=https://api.unstructured.io/general/v0/general
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Build and run the Docker container:

   ```
   docker-compose up --build
   ```

5. Open your web browser and go to `http://localhost:8501` to access the Streamlit UI.

### Manual Setup using venv

1. Make sure you have Python 3.9+ installed on your system.

2. Clone this repository:

   ```
   git clone https://github.com/yourusername/assignment_manish.git
   cd assignment_manish
   ```

3. Create and activate a virtual environment:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

5. Create a `.env` file in the project root and add your Unstructured API key and OpenAI API key:

   ```
   UNSTRUCTURED_API_KEY=your_unstructured_api_key_here
   UNSTRUCTURED_API_URL=https://api.unstructured.io/general/v0/general
   OPENAI_API_KEY=your_openai_api_key_here
   ```

6. Run the Streamlit app:

   ```
   streamlit run app/main.py
   ```

7. Open your web browser and go to `http://localhost:8501` to access the Streamlit UI.

## Usage

1. Upload a file (text, image, Excel spreadsheet, or PDF) using the file uploader.
2. Click on either the "Generate Summary" button to analyze the uploaded content.
3. The results will be displayed below the respective buttons.

Note: This implementation uses the Unstructured API for parsing Excel and PDF files, and the OpenAI API for language model processing. Make sure you have valid API keys for both services to use all features.
