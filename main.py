import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
import streamlit as st

# Load environment variables from .env file
load_dotenv()

# Get Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Initialize OpenAI provider with Gemini API settings
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
)

# Configure the language model
model = OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=provider)

# Create an greeting agent with instructions, and model
agent = Agent(
    name="Greeting Agent",
    instructions="You are a Greeting Agent, Your task is to greet the user with a friendly message, when someone says hi you've reply back with salam from Ubaid Ali, if someone says bye then say Allah hafiz from Ubaid Ali, when someone asks other than greeting then say Ubaid is here just for greeting, I can't answer anything else, sorry.",
    model=model,
)
agent = Agent(
    name="Pakistan History Agent",
    instructions="Pakistan, founded on August 14, 1947, emerged from British India as a separate Muslim state under the leadership of Muhammad Ali Jinnah. The country has a deep historical legacy, tracing back to the ancient Indus Valley Civilization and later influenced by Maurya, Gupta, Delhi Sultanate, and Mughal empires. Following independence, Pakistan faced political instability, leading to military coups, wars with India (1947, 1965, 1971), and the secession of East Pakistan (now Bangladesh) in 1971. The nation underwent periods of military rule, notably under Ayub Khan, Zia-ul-Haq, and Pervez Musharraf, alongside democratic transitions with leaders like Benazir Bhutto, Nawaz Sharif, and Imran Khan. Pakistan became a nuclear power in 1998 and continues to navigate economic and political challenges, with recent shifts in leadership, including Imran Khan’s removal in 2022 and Shehbaz Sharif’s government in 2024.",
    model=model,
)

# Get user input from the terminal
user_question = input("Please enter your question: ")

# Run the agent with user input and get result
result = Runner.run_sync(agent, user_question)

# Print the result
print(result.final_output)


st.title("SIMPLE LLM AGENT")

write=st.write("Enter you question")