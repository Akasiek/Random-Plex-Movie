# Random Plex Movie
Python App which chooses random movie from your Plex Library. Also you can send watch request to Plex Client with chosen movie.

[![GitHub](https://img.shields.io/github/license/Akasiek/random-plex-movie?style=flat-square)](https://github.com/Akasiek/random-plex-movie/blob/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/PlexAPI?label=PlexAPI&style=flat-square)](https://pypi.org/project/PlexAPI/4.5.2/)
[![PyPI](https://img.shields.io/pypi/v/Eel?label=Eel&style=flat-square)](https://pypi.org/project/Eel/)

![alt text](https://i.imgur.com/CKplHDk.jpg "Example")

# Needed stuff

- Python 3
- Pip and this libraries:

    - PlexAPI (v4.5)
    - Eel (v0.14)

    Windows 
    ```
        pip install plexapi
        pip install eel
    ```

    MacOS and Linux
    ```
        pip3 install plexapi
        pip3 install eel
    ```

- Google Chrome (You can access the app by any other browser on `localhost:4000`. But Chrome uses app module and it works out of the box)

# Installation

1. Clone repo with this command:

    `git clone https://github.com/Akasiek/random-saved-album.git`

2. Add your Plex credentials to the beginning of randomPlexMovie.py file. 

    ![alt text](https://i.imgur.com/r2z2ihq.jpg "Second step of the installation")

3. Run Python file with this command

    Windows (CMD)

    `py randomPlexMovie.py`

    MacOS and Linux

    `python3 randomPlexMovie.py`

    This will start local web server on port 4000 and open Chrome App. If the port is colliding with something, you can change it in this line:

    ![alt text](https://i.imgur.com/ABLhaJh.jpg "Third step of the installation")

    After closing the app window, the program will stop running. You can change it by deleting argument "close_callback" in this line:

    ![alt text](https://i.imgur.com/kcaZZgR.jpg "Third step of the installation")

***

## Plans for the future

- Login page for Plex credentials




