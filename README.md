# AI Email Assistant Agent

An AI-powered email assistant that drafts and automatically saves professional emails based on user instructions. The application is built using [Streamlit](https://streamlit.io/), [Pydantic AI](https://ai.pydantic.dev/), and [Groq](https://groq.com/) (using the `llama-3.3-70b-versatile` model).

**Live App:** [agentic-email-assistant](https://agentic-email-assistant-a.streamlit.app/)

## Features
- **Interactive Web UI**: Streamlit interface to input instructions and view results.
- **AI Agent Orchestration**: Uses Pydantic AI to generate emails and decide when to call saving tools.
- **Local File Saving**: Automatically saves generated emails to the local `saved_emails/` folder.
- **Ordered Outputs**: Outputs the file location first, followed by the complete email content.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Chusmalatha/agentic-email-assistant.git
cd email-agent
```

### 2. Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables
Create a file named `.env` in the root directory and add your Groq API key:
```env
GROQ_API_KEY=your_actual_groq_api_key_here
```

## Running the Application
To start the Streamlit web interface, run:
```bash
streamlit run app.py
```
This will open the application in your default web browser (typically at `http://localhost:8501`).

## Project Structure
- `app.py`: The main Streamlit web application.
- `agent.py`: Agent definition, system prompts, and tool registration using Pydantic AI.
- `tools.py`: Helper functions for local file operations (saving emails).
- `saved_emails/`: Directory where generated emails are saved.
- `.env`: Environment variables configuration (ignored in git).
