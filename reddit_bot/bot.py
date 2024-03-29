import praw
import config

def login():
    returner= praw.Reddit(username=config.username, password=config.password, client_id=config.client_id, client_secret=config.client_secret, user_agent="my test")
    return returner

def run(r):
    for comment in r.subreddit("Test_Posts").comments(limit=25):
        if "test" in comment.body:
            comment.reply("Hello! I am a bot!")

while True:
    r=login()
    run(r)
