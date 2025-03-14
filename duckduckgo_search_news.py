# Import necessary libraries and modules
from duckduckgo_search import DDGS
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool
from datetime import datetime
from dotenv import load_dotenv
import os
import asyncio

# Load environment variables from a .env file
load_dotenv()

# Get the current date in YYYY-MM-DD format
current_date = datetime.now().strftime("%Y-%m-%d")

# Retrieve the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Define the model to be used
model_name = "llama3.2" 

# Initialize the OpenAIChatCompletionsModel with the specified model and API client
model = OpenAIChatCompletionsModel(
    model=model_name,
    openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1", api_key=api_key)
)

@function_tool
def get_news_articles(topic):
    """
    Function to get news articles for a given topic using DuckDuckGo search.
    """
    try:
        with DDGS() as ddgs:
            # Search for news using DuckDuckGo
            results = ddgs.news(f"{topic} {current_date}", max_results=5)
            if results:
                # Format the results into a readable string
                formatted_results = "\n\n".join(
                    [f"Title: {result['title']}\nURL: {result['url']}\nDescription: {result['body']}" for result in results]
                )
                print(formatted_results)
                return formatted_results
            else:
                return f"No news found for {topic} on {current_date}."
    except Exception as e:
        return f"Error fetching news: {str(e)}"

# Create an agent for fetching news articles
news_agent = Agent(
    name="news-agent",
    model=model,
    tools=[get_news_articles],
    instructions="You provide the latest news articles for a given topic using DuckDuckGo search."
)

# Create an agent for editing news articles
editor_agent = Agent(
    name="editor-agent",
    model=model,
    instructions="Rewrite and give me as news article ready for publishing. Each news story in a separate section."
)

async def run_news_workflow(topic):
    """
    Asynchronous function to run the news workflow for a given topic.
    """
    # Fetch raw news articles using the news agent
    news_response = await asyncio.get_event_loop().run_in_executor(
        None, lambda: Runner.run_sync(news_agent, f"Get me the news about {topic} on {current_date}")
    )

    raw_news = news_response.final_output
    
    # Edit the fetched news articles using the editor agent
    edited_news_response = await asyncio.get_event_loop().run_in_executor(
        None, lambda: Runner.run_sync(editor_agent, raw_news)
    )
    edited_news = edited_news_response.final_output
    
    print("Final news article:")
    print(edited_news)
    
    return edited_news

# Example of running the news workflow for a given topic
if __name__ == "__main__":
    # Run the news workflow for the topic "AI"
    run_news_workflow("AI")