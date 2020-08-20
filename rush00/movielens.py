import requests
import pandas as pd
from itertools import chain
from bs4 import BeautifulSoup


class Ratings:
    def __init__(self, ratings_path, movies_path):
        ratings = pd.read_csv(ratings_path, parse_dates=['timestamp'])
        movies = pd.read_csv(movies_path)
        movies['title'] = movies['title'].replace(r' ?\(\d+\)', '', regex=True)
        self.df = ratings.join(movies, on='movieId')
        self.df.drop(['movieId', 'genres'], axis=1, inplace=True)

    def year_counts(self):
        year = self.df['timestamp'].dt.year
        return year.value_counts().sort_index()

    def rating_counts(self):
        return self.df['rating'].value_counts().sort_index()

    def most_rated(self, n=10):
        return self.df.value_counts('title')[:n]

    def best_ratings(self, n=10, metric='average'):
        if metric == 'average':
            ratings = self.df.groupby('title').mean()['rating']
        elif metric == 'median':
            ratings = self.df.groupby('title').median()['rating']
        else:
            raise ValueError('Metric must be either average or median')
        return ratings.round(2).sort_values(ascending=False)[:n]

    def most_controversial(self, n=10):
        ratings = self.df.groupby('title').std()['rating']
        return ratings.round(2).sort_values(ascending=False)[:n]

    def users_by_rating_counts(self):
        return self.df['userId'].value_counts().sort_index()

    def users_by_ratings(self, metric='average'):
        if metric == 'average':
            ratings = self.df.groupby('userId').mean()['rating']
        elif metric == 'median':
            ratings = self.df.groupby('userId').median()['rating']
        else:
            raise ValueError('Metric must be either average or median')
        return ratings.round(2)

    def users_highest_variance(self, n=10):
        ratings = self.df.groupby('userId').std()['rating']
        return ratings.round(2).sort_values(ascending=False)[:n]


class Tags:
    def __init__(self, path):
        self.tags = pd.read_csv(path, parse_dates=['timestamp'])['tag']
        self.unique = self.tags.drop_duplicates()

    def word_count(self, n=10):
        counts = self.unique.apply(lambda x: len(x.split())).rename('count')
        df = pd.concat([self.unique, counts], axis=1).set_index('tag')
        return df.value_counts()[:n]

    def char_count(self, n=10):
        counts = self.unique.apply(lambda x: len(x).rename('count'))
        df = pd.concat([self.unique, counts], axis=1).set_index('tag')
        return df.value_counts()[:n]

    def longest(self, n=10):
        by_words = set(self.word_count(n).index.values)
        by_chars = set(self.char_count(n).index.values)
        return sorted(list(by_words & by_chars))

    def most_popular(self, n=10):
        return self.tags.value_counts()[:n]

    def find_tags(self, word):
        return sorted(list(self.unique.filter(like=word).index.values))


class Movies:
    def __init__(self, path):
        df = pd.read_csv(path)
        title = df['title'].str.extract(r'(?P<title>.*) (?P<year>\(\d+\))')
        title['year'] = pd.to_numeric(title['year'])
        self.df = pd.concat([title, df['genres']], axis=1).set_index('title')

    def release_year_counts(self):
        return self.df['year'].value_counts().sort_index()

    def genre_counts(self):
        genres = chain(*[x.split('|') for x in self.df['genres'].tolist()])
        return pd.Series(genres).value_counts().sort_index()

    def most_num_genres(self, n=10):
        n_genres = self.df['genres'].apply(lambda x: len(x.split('|')))
        return n_genres.sort_values(ascending=False)[:n]


class Links:
    def __init__(self, links_path, movies_path):
        links = pd.read_csv(links_path, index_col='movieId')
        movies = pd.read_csv(movies_path, index_col='movieId')
        movies['title'] = movies['title'].replace(r' ?\(\d+\)', '', regex=True)
        self.df = pd.concat([movies, links], axis=1).set_index('title')
        self.df.drop('genres', axis=1, inplace=True)

    def get_imdb(self, movies, fields):
        data = {'movieId': [se]}

    def top_directors(self, n):
        pass

    def most_expensive(self, n):
        pass

    def most_profitable(self, n):
        pass

    def longest(self, n):
        pass

    def top_cost_per_minute(self, n):
        pass
