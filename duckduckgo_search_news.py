from duckduckgo_search import DDGS
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, function_tool
from datetime import datetime
from dotenv import load_dotenv
import os
import asyncio

load_dotenv()

current_date = datetime.now().strftime("%Y-%m-%d")
api_key = os.getenv("OPENAI_API_KEY")
model_name = "llama3.2"  # Adjust as needed

model = OpenAIChatCompletionsModel(
    model=model_name,
    openai_client=AsyncOpenAI(base_url="http://localhost:11434/v1", api_key=api_key)
)

@function_tool
def get_news_articles(topic):
    try:
        with DDGS() as ddgs:
            # Search for news using DuckDuckGo
            results = ddgs.news(f"{topic} {current_date}", max_results=5)
            if results:
                formatted_results = "\n\n".join(
                    [f"Title: {result['title']}\nURL: {result['url']}\nDescription: {result['body']}" for result in results]
                )
                print(formatted_results)
                return formatted_results
            else:
                return f"No news found for {topic} on {current_date}."
    except Exception as e:
        return f"Error fetching news: {str(e)}"

news_agent = Agent(
    name="news-agent",
    model=model,
    tools=[get_news_articles],
    instructions="You provide the latest news articles for a given topic using DuckDuckGo search."
)

editor_agent = Agent(
    name="editor-agent",
    model=model,
    instructions="Rewrite and give me as news article ready for publishing. Each news story in a separate section."
)

async def run_news_workflow(topic):
    news_response = await asyncio.get_event_loop().run_in_executor(
        None, lambda: Runner.run_sync(news_agent, f"Get me the news about {topic} on {current_date}")
    )

    raw_news = news_response.final_output
    
    edited_news_response = await asyncio.get_event_loop().run_in_executor(
        None, lambda: Runner.run_sync(editor_agent, raw_news)
    )
    edited_news = edited_news_response.final_output
    
    print("Final news article:")
    print(edited_news)
    
    return edited_news

# Example of running the news workflow for a given topic
if __name__ == "__main__":
  run_news_workflow("AI")