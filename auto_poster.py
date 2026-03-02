import os
import tweepy
import praw
import sys

def post_to_x():
    print("Initiating X (Twitter) Deployment...")
    try:
        # Use API v2 for creating tweets
        client = tweepy.Client(
            consumer_key=os.environ.get("X_API_KEY"),
            consumer_secret=os.environ.get("X_API_SECRET"),
            access_token=os.environ.get("X_ACCESS_TOKEN"),
            access_token_secret=os.environ.get("X_ACCESS_SECRET")
        )

        # Thread optimized for developer engagement
        thread_tweets = [
            "Tired of Electron apps eating your RAM just to run a timer? I built a native macOS/Windows desktop app using Python, Django, and PyWebView to track LLM API limits. Zero background CPU drain. Under 10 files. Fully open-source. 🧵👇",
            "The trick? It doesn't actually run a timer. It uses a Target Timestamp Architecture. When you set a timer, Django calculates the future expiration time and saves it to a local MongoDB. You can kill the app completely.",
            "When you reopen it, the native JS engine compares the DB timestamp to your local hardware clock. Result: Perfect accuracy, complete crash-proof persistence, and absolutely zero background battery drain. ⚡️",
            "It’s a perfect boilerplate for anyone wanting to build lightweight desktop GUIs with standard Python web stacks. Looking for devs to fork it and add direct API webhooks or OS notifications. Grab the code here: [Insert GitHub Repo Link]"
        ]

        # Post the first tweet (the hook)
        response = client.create_tweet(text=thread_tweets[0])
        previous_tweet_id = response.data['id']
        print("✅ Tweet 1 (Hook) posted successfully.")

        # Post the rest of the thread as replies
        for i, tweet in enumerate(thread_tweets[1:], start=2):
            response = client.create_tweet(text=tweet, in_reply_to_tweet_id=previous_tweet_id)
            previous_tweet_id = response.data['id']
            print(f"✅ Tweet {i} appended to thread.")
            
    except Exception as e:
        print(f"❌ X Deployment Failed: {e}")

def post_to_reddit():
    print("\nInitiating Reddit Deployment...")
    try:
        reddit = praw.Reddit(
            client_id=os.environ.get("REDDIT_CLIENT_ID"),
            client_secret=os.environ.get("REDDIT_SECRET"),
            user_agent="Antigravity_Launch_Bot_v1.0",
            username=os.environ.get("REDDIT_USERNAME"),
            password=os.environ.get("REDDIT_PASSWORD")
        )

        title = "I built a cross-platform desktop app without Electron (Python/Django + PyWebView) to track LLM limits."
        
        # Read the Hacker News / r/Python text from the previously generated markdown file
        try:
            with open("MARKETING_COPY.md", "r") as file:
                body = file.read()
        except FileNotFoundError:
            print("❌ Error: MARKETING_COPY.md not found. Please ensure the markdown generation step was completed.")
            return

        subreddits = ['Python', 'django', 'SideProject']

        for sub in subreddits:
            try:
                subreddit = reddit.subreddit(sub)
                subreddit.submit(title, selftext=body)
                print(f"✅ Successfully posted to r/{sub}")
            except Exception as e:
                print(f"❌ Failed to post to r/{sub}. Error: {e}")
                
    except Exception as e:
        print(f"❌ Reddit Authentication Failed: {e}")

if __name__ == "__main__":
    print("🚀 Starting Antigravity Auto-Poster Pipeline...\n")
    
    # Pre-flight check for API keys (check for at least one key for each platform)
    required_keys = ['X_API_KEY', 'REDDIT_CLIENT_ID']
    missing_keys = [key for key in required_keys if not os.environ.get(key)]
    
    if missing_keys:
        print(f"⚠️ Warning: Missing core API keys in environment: {missing_keys}")
        print("Please ensure Antigravity has injected the correct environment variables before proceeding.")
        sys.exit(1)

    post_to_x()
    post_to_reddit()
    print("\n🏁 Antigravity Auto-Poster Pipeline Complete.")
