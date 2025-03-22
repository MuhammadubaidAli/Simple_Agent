Simple LLM Agent

This is a Simple LLM Agent built using Python, Streamlit, and OpenAI's API (Gemini-2.0 Flash). The agent responds to user inputs with either friendly greetings or historical information about Pakistan.
Features

    Greeting Agent:

        Responds with "Salam from Ubaid Ali" when greeted with "hi".

        Replies with "Allah hafiz from Ubaid Ali" when someone says "bye".

        If asked anything else, it responds, "Ubaid is here just for greeting, I can't answer anything else, sorry."

    Pakistan History Agent:

        Provides a brief history of Pakistan when prompted.

Installation & Setup
1. Clone the Repository

git clone <your-repository-url>
cd simple-llm-agent

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Set Up API Keys

Create a .env file in the project directory and add:

GEMINI_API_KEY=your_gemini_api_key_here

5. Run the Application

To run the agent in the terminal:

python main.py

To run the Streamlit interface:

streamlit run main.py

Usage

    The CLI agent asks for user input and returns an appropriate response.

    The Streamlit interface provides a simple UI where users can enter their questions.

Requirements

    Python 3.7+

    Streamlit

    OpenAI API (Gemini)

    python-dotenv for environment variables

Future Improvements

    Enhance the agent's conversational abilities.

    Add support for more topics.

    Deploy as a web-based chatbot.
