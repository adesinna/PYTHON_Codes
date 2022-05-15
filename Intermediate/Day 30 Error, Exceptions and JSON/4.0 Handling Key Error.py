facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
like_list = []

for post in facebook_posts:
    try:  # when you run it first you will see where the error occurs
        total_likes = total_likes + post['Likes']  # where the error occur
    except KeyError:  # what to do
        pass  # tell it to pass that element

print(total_likes)  # sum times it needs to be outside, this acts like the else












