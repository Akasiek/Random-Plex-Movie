import eel
from eel import browsers
from plexapi.myplex import MyPlexAccount
from random import randint
import sys

# Plex authorization
account = MyPlexAccount('PLEX_E-MAIL', 'PLEX_PASSWORD')
plex = account.resource('PLEX_SERVER_NAME').connect()
movies = plex.library.section('Movies')

# Initialising eel library in this directory
eel.init('web')


def close_callback(path, list):
    '''Exiting app when window is closed'''
    print("Window closed... Aborting!")
    sys.exit()


def randomUnwatchedMovie():
    '''Gets number of unwatched movies in library, assigns random number to each unwatched
    movie. Pulls movie information and returns movie data for display'''
    number_of_unwatched = len(movies.search(unwatched=True))
    random_number_in_range = randint(0, number_of_unwatched-1)

    global chosen_movie
    chosen_movie = movies.search(unwatched=True)[random_number_in_range]
    chosen_movie_duration_hours = (chosen_movie.duration/(1000*60*60)) % 24
    chosen_movie_duration_minutes = (chosen_movie.duration/(1000*60)) % 60

    writers = [chosen_movie.actors[w].tag for w in range(
        len(chosen_movie.actors))]
    actors = [chosen_movie.writers[a].tag for a in range(
        len(chosen_movie.writers))]
    directors = [chosen_movie.directors[d].tag for d in range(
        len(chosen_movie.directors))]

    return {"title": chosen_movie.title, "year": chosen_movie.year,
            "duration_hours": int(chosen_movie_duration_hours),
            "duration_minutes": int(chosen_movie_duration_minutes), "directors": directors,
            "writers": writers, "actors": actors, "poster": chosen_movie.posterUrl,
            "background": chosen_movie.artUrl
            }


@ eel.expose
def py_returnMovie():
    '''Sends random movies attributes to JS'''
    return randomUnwatchedMovie()


@ eel.expose
def py_returnClients():
    '''Return list of clients to JS'''
    clients = []
    for client in plex.clients():
        clients.append(client.title)
    return clients


@ eel.expose
def py_playMovie(client):
    '''Play movie if button was clicked and client was selected'''
    plex.client(client).playMedia(chosen_movie)


# Starting web server for app. Opening app window.
eel.start('index.html',
          browser='Chrome',
          port=randint(49152, 65535),
          close_callback=close_callback,
          size=(1440, 860)
          )
