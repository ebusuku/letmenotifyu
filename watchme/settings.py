#!/usr/bin/python3

import os
import configparser
import logging

#DIRECTORY_PATH = os.path.join(os.environ['HOME'], '.letmenotifyu')
DIRECTORY_PATH = "DevLetme"

DATABASE_DIRECTORY = os.path.join(DIRECTORY_PATH, 'database')
MOVIE_DB_PATH = os.path.join(DATABASE_DIRECTORY, 'movie.sqlite')
SERIES_DB_PATH = os.path.join(DATABASE_DIRECTORY, 'series.sqlite')
IMAGE_DIRECTORY = os.path.join(DIRECTORY_PATH, 'images')
MOVIE_IMAGE_DIRECTORY = os.path.join(IMAGE_DIRECTORY, 'movies')
SERIES_IMAGE_DIRECTORY = os.path.join(IMAGE_DIRECTORY,'series')
TORRENT_DIRECTORY = os.path.join(DIRECTORY_PATH, 'torrents')
INCOMPLETE_DIRECTORY = os.path.join(DIRECTORY_PATH, 'incomplete')
COMPLETE_DIRECTORY = os.path.join(DIRECTORY_PATH, 'complete')
LOG_FILE_PATH = os.path.join(DIRECTORY_PATH, 'letmenotifyu.log')
#DATA_FILES_PATH = '/usr/share/letmenotifyu/'

config = configparser.ConfigParser()
                          
def logging_dict(log_level):
    levels = {'Logging.DEBUG': logging.DEBUG,
              'Logging.INFO': logging.INFO}
    return levels[log_level]


def initial():
    os.mkdir(IMAGE_DIRECTORY)
    os.mkdir(TORRENT_DIRECTORY)
    os.mkdir(INCOMPLETE_DIRECTORY)
    os.mkdir(COMPLETE_DIRECTORY)
    os.mkdir(DATABASE_DIRECTORY)
    os.mkdir(MOVIE_IMAGE_DIRECTORY)
    os.mkdir(SERIES_IMAGE_DIRECTORY)
    config['DIRECTORIES'] = {'CompleteDownloads':DIRECTORY_PATH+'/complete/'
    }
    config["LOGGING"] = {'LoggingLevel': "Logging.DEGUG"}
    with open(DIRECTORY_PATH+'/config.ini','w') as cfg_file:
        config.write(cfg_file)
