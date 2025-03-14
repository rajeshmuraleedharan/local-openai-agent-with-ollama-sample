# Import necessary libraries and modules
from dotenv import load_dotenv
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
import ssl
import httpx
import certifi

# Load environment variables from a .env file
load_dotenv()

# Optionally set system-wide SSL certificate file (for external HTTPS requests)
os.environ["SSL_CERT_FILE"] = certifi.where()

# Create an unverified SSL context to bypass verification
context = ssl._create_unverified_context()

# Configure an httpx AsyncClient with the unverified SSL context
http_client = httpx.AsyncClient(verify=context)

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Define the model to be used
model = "llama3.2" # Alternative model: qwen2:0.5b

# Initialize the OpenAIChatCompletionsModel with the specified model and API client
model = OpenAIChatCompletionsModel(
    model= model,
    openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1", api_key=api_key, http_client=http_client)
)

# Create an agent with a name and instructions
agent = Agent(name="single-agent-assistant", 
              model=model, 
              instructions="I can help you with anything you need. Just ask me anything!")

# Run the agent synchronously with a sample query and print the result
result = Runner.run_sync(agent, "What is the capital of France?")
print(result.final_output)