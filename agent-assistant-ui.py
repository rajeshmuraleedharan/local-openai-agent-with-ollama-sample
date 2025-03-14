# Import necessary libraries and modules
import chainlit as cl
from duckduckgo_search_news import run_news_workflow

@cl.on_message
async def main(message: cl.Message):
    """
    Main function to handle incoming messages and fetch news articles.
    """
    topic = message.content

    # Inform the user that the search for news has started
    await cl.Message(
        content=f"Searching for news about '{topic}'...",
        author="news-agent"
    ).send()
    
    try:
        # Run the news workflow to fetch news articles for the given topic
        news_content = await run_news_workflow(message.content)

        # Send the fetched news content back to the user
        await cl.Message(
            content=news_content,
            author="news-agent"
        ).send()
    except Exception as e:
        # Handle any errors that occur during the news fetching process
        await cl.Message(
            content=f"Error fetching news: {str(e)}",
            author="news-agent"
        ).send()

@cl.on_chat_start
async def start():
    """
    Function to handle the start of a chat session.
    """
    await cl.Message(
        content="Hello! I'm a news agent. I can help you find the latest news articles on a given topic. Try asking me for news on a topic you are interested in.",
        author="news-agent"
    ).send()