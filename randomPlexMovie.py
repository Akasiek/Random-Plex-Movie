import eel
import sys
import configparser
from eel import browsers
from plexapi.server import PlexServer
from random import randint, choice

# Plex authorization
config = configparser.ConfigParser()
config.read('config/config.ini')

plex = PlexServer(config['auth']['baseurl'], config['auth']['token'])
movies = plex.library.section('Movies')

# Initialising eel library in this directory
eel.init('web')


def close_callback(path, list):
    '''Exiting app when window is closed'''
    print("Window closed... Aborting!")
    sys.exit()


def randomUnwatchedMovie():
    '''Generates a list of unwatched movies. Randomly selects one to be displayed. 
    Pulls movie information and returns movie data for display'''

    global chosen_movie
    chosen_movie = choice(movies.search(unwatched=True))
    chosen_movie_duration_hours = (chosen_movie.duration/(1000*60*60)) % 24
    chosen_movie_duration_minutes = (chosen_movie.duration/(1000*60)) % 60

    writers = [chosen_movie.actors[w].tag for w in range(
        len(chosen_movie.actors))]
    actors = [chosen_movie.writers[a].tag for a in range(
        len(chosen_movie.writers))]
    directors = [chosen_movie.directors[d].tag for d in range(
        len(chosen_movie.directors))]

    return {"title": chosen_movie.title,
            "year": chosen_movie.year,
            "duration_hours": int(chosen_movie_duration_hours),
            "duration_minutes": int(chosen_movie_duration_minutes),
            "directors": directors, "writers": writers, "actors": actors,
            "poster": chosen_movie.posterUrl,
            "background": chosen_movie.artUrl
            }


@ eel.expose
def py_returnMovie():
    '''Sends random movies attributes to JS'''
    return randomUnwatchedMovie()


@ eel.expose
def py_returnClients():
    '''Return list of clients to JS'''
    clients = [client.title for client in plex.clients()]
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
