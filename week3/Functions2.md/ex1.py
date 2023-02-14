movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_high_score(movie):
    return movie('imdb') > 5.5
    print(is_high_score(movies))

def is_movie_above_5point5(movies):
    for movie in movies:
        return movie['imdb'] > 5.5

def get_movies_above_5(movies):
    return [movie for movie in movies if movie['imdb'] > 5.5]

def get_movies_by_category(movies, category_name):
    return [movie for movie in movies if movie['category'] == category_name]

def get_average_imdb_score(movies):
    total=sum([movie['imdb'] for movie in movies])
    return total/len(movies)

def get_average_imdb_score_by_category(movies, category_name):
    score= [movie['imdb'] for movie in movies if movie['category']==category_name]
    return sum(score)/len(score)

print(is_movie_above_5point5(movies))
print(get_movies_by_category(movies,"Thriller"))
print(get_average_imdb_score(movies))
print(get_average_imdb_score_by_category(movies,"Thriller"))
