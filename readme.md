# LLM Data Analyzer

This project provides a Streamlit-based UI for analyzing different types of data (text, images, and spreadsheets) using Language Model (LLM) prompts.

## Setup and Running

### Using Docker Compose (Recommended)

1. Make sure you have Docker and Docker Compose installed on your system.

2. Clone this repository:

   ```
   git clone https://github.com/yourusername/llm-data-analyzer.git
   cd llm-data-analyzer
   ```

3. Build and run the Docker container:

   ```
   docker-compose up --build
   ```

4. Open your web browser and go to `http://localhost:8501` to access the Streamlit UI.

### Manual Setup using venv

1. Make sure you have Python 3.9+ installed on your system.

2. Clone this repository:

   ```
   git clone https://github.com/yourusername/llm-data-analyzer.git
   cd llm-data-analyzer
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

5. Run the Streamlit app:

   ```
   streamlit run app/main.py
   ```

6. Open your web browser and go to `http://localhost:8501` to access the Streamlit UI.

## Usage

1. Upload a file (text, image, or Excel spreadsheet) using the file uploader.
2. Click on either the "Generate Summary" or "List Key Objects" button to analyze the uploaded content.
3. The results will be displayed below the respective buttons.

Note: This is a placeholder implementation. In a real-world scenario, you would need to integrate with an actual LLM API to generate the responses.
