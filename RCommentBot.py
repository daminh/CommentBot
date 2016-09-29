import praw
import time

#set variable r to object praw
r = praw.Reddit(user_agent = "Comment bot using Reddit API")
 #Before reddit started using Oauth              
r.login()

words_to_match = ['insane']
cache = []

def bot_on():
    print("Going to the subreddit")
    #any subreddit you want
    subreddit = r.get_subreddit("test")
    print("Browsing through comments")
    #comment object holding up to 50 comments
    comments = subreddit.get_comments(limit=50)
    #go through each comment
    for comment in comments:
        print("Match found! Comment ID: " + comment.id)
        comment_text = comment_text.body
        isMatch = any(string in comment_text for string in words_to_match)
        comment.reply('Try different words such as: crazy, riduculous, amazing, spectactular')
        print("Reply successful")
        cache.append(comment.id)
        print("")

while True:
    bot_on()
    #every 10 sec bot turns on
    time.sleep(10)