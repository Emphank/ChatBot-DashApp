# Web-based Chatbot Application using Plotly Dash
Users can interact with a chatbot powered by a ChatGPT. 

## Requirements
Python = 3.11.2

## Installation

1. Clone and navigate to the project directory
   ```bash
   git clone https://github.com/chrisshaheen1/CAI.git
   cd CAI
   ```
2. Create and activate the virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\Activate.bat (Windows)
   source venv/bin/activate (Unix/MacOS)
   ```
3. Install packages
   ```bash
   pip install -r requirements.txt
   ```
4. Copy `.env.example` file and rename it `.env`
5. In `.env` file, set your openai api key for `OPENAI_API_KEY`
   ```bash
   OPENAI_API_KEY=<your openai api key>
   ```
4. Run the project
   ```bash
   python index.py
   ```
5. Open **http://127.0.0.1:8050** in your browser.
