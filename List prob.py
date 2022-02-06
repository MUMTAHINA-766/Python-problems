#List of movies that i love

from shutil import move
from unicodedata import name

"""
fav_movie = []

while True:
    print('Movie no ' +str(len(fav_movie)+1)+ ' or press Enter to stop adding to the list.')
    movie = input()

    if movie == '':
        break
    fav_movie = fav_movie + [movie]

if len(fav_movie) != 0:
    print('The lists are ')
    for i in range(len(fav_movie)):
        print(fav_movie[i])

"""

#in and not in keywords
"""
dresses = ['scarf','scart','salwar','shari','blouse','kamiz']

print('What dress you want to wear? ')
name = input()

if name not in dresses:
    print('Its not in your list')
else:
    print(name+ ' is in your list')
"""

#assuming multiple values at once

fruits = ['apple','orange','cherry','mango']
a,b,c,d = fruits
print(a,b,c,d)

