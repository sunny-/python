import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('ml-1m/users.dat', sep='::', header=None,names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ml-1m/ratings.dat', sep='::', header=None,names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('ml-1m/movies.dat', sep='::', header=None,names=mnames)

data = pd.merge(pd.merge(ratings, users), movies)

data[:6]
data.ix[0]

mean_ratings = data.pivot_table(values = 'rating', index='title', columns='gender', aggfunc='mean')

mean_ratings[:5]

ratings_by_title = data.groupby('title').size()

ratings_by_title[:10]

active_titles = ratings_by_title.index[ratings_by_title >= 250]

active_titles

mean_ratings = mean_ratings.ix[active_titles]

mean_ratings

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

sorted_by_diff = mean_ratings.sort_index(by='diff')

sorted_by_diff[:15]

rating_std_by_title = data.groupby('title')['rating'].std()

rating_std_by_title = rating_std_by_title.ix[active_titles]

rating_std_by_title.order(ascending=False)[:10]


