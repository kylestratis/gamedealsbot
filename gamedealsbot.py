import praw, re
# Will have to make non-case sensitive

r = praw.Reddit('PRAW /r/GameDeals scanner')

already_done = []
list_of_games = ["Europa Universalis IV", "Borderlands", 
"Call of Duty", "Oblitus"]
results = []
while True:
    subreddit = r.get_subreddit('gamedeals')
    submissions = subreddit.get_new()
    for submission in submissions:
        for game in list_of_games:
            # This will need to be changed to support regex
            if game in submission.title and not already_done:
                print submission.title
                already_done.append(submission.title)
    #for submission in submissions:
    #    print submission
     #   for game in list_of_games:
    #        if game in submission:
    #            print submission