import chainlit as cl
from duckduckgo_search_news import run_news_workflow

@cl.on_message
async def main(message: cl.Message):
    topic = message.content

    
    await cl.Message(
        content=f"Searching for news about '{topic}'...",
        author="news-agent"
        ).send()
    
    try:
        news_content = await run_news_workflow(message.content)

        await cl.Message(
            content=news_content,
            author="news-agent"
        ).send()
    except Exception as e:
        await cl.Message(
            content=f"Error fetching news: {str(e)}",
            author="news-agent"
        ).send()

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Hello! I'm a news agent. I can help you find the latest news articles on a given topic. Try asking me for news on a topic you are interested in.",
        author="news-agent"
    ).send()