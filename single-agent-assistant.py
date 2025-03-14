from dotenv import load_dotenv
import os
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI
import ssl
import httpx
import certifi

load_dotenv()

# Optionally set system-wide SSL certificate file (for external HTTPS requests)
os.environ["SSL_CERT_FILE"] = certifi.where()

# Create an unverified SSL context to bypass verification
context = ssl._create_unverified_context()

# Configure an httpx AsyncClient with the unverified SSL context
http_client = httpx.AsyncClient(verify=context)

api_key = os.getenv("OPENAI_API_KEY")
model = "llama3.2" #qwen2:0.5b

model = OpenAIChatCompletionsModel(
    model= model,
    openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1",api_key=api_key,http_client=http_client)
)

agent = Agent(name="single-agent-assistant", 
              model=model, 
              instructions="I can help you with anything you need. Just ask me anything!")

result = Runner.run_sync(agent, "What is the capital of France?")
print(result.final_output)