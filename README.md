
# RAG Using LlamaParse, GROQ, and Qdrant Vector Stores

### This Streamlit application provides a user-friendly interface for creating effective Retrieval Augmented Generation (RAGs) using LLamaParse for parsing, Qdrant for vector storage, and GROQ for querying. In this tutorial, you'll learn how to leverage these technologies to unlock insights from complex documents and build powerful RAGs.

## Description

#### The application `app.py` utilizes Streamlit as the frontend framework and interacts with the following components:
- **Qdranat Vector Store**: A vector store for storing and querying vectors.
- **LLM Groq Models**: Dynamically loaded Groq models for processing queries.
- **Llama Parse**: A tool for parsing and processing documents.

## Installation

### Prerequisites
- Python 3.9+
- pip

### Installation Steps

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project_directory>
   ```

3. Install dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a Python virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

5. Activate the virtual environment:
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```

6. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variables to the `.env` file:
     ```
     LLAMA_CLOUD_API_KEY=your_llama_cloud_api_key
     QDRANT_URL=your_qdrant_url
     QDRANT_API_KEY=your_qdrant_api_key
     GROQ_API_KEY=your_groq_api_key
     ```

7. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage

1. After running the application, a Streamlit interface will be launched in your default web browser.
2. Select a model from the dropdown list.
3. Enter your search query in the text input field.
4. Click on the "Submit" button to execute the query.
5. View the results displayed below the query input.

## Contributors

- Drona Kaushik Jagad (https://github.com/DJagad)
- This Video Guided me to proceed with different steps for learning this particular project (https://www.youtube.com/watch?v=w7Ap6gZFXl0)

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to customize the descriptions, installation steps, and other sections according to your project's specifics.