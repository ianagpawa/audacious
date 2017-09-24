import os
import subprocess
import shutil

from secrets import home_folder


def replaceFileName(file_name):
    slashes = file_name.replace("\\", "/")
    replaced = slashes.replace("D:", home_folder)
    return replaced


def convertPlaylist(filename, destination_folder):
    playlist = open(filename, 'r+')
    arr = playlist.readlines()
    newArr = []
    newPlaylist = open(destination_folder + "/" + filename, 'w+')
    # newPlaylist = open(destination_folder, 'w+')
    for song_path in arr:
        replacement = replaceFileName(song_path)
        newPlaylist.writelines(replacement)
    playlist.close()
    newPlaylist.close()

def get_m3u(filename):
    extensions = filename[-3:]
    return extensions == 'm3u'


def convertAll():
    origin = os.getcwd()

    if not os.path.isdir("linuxPlaylists"):
        subprocess.call("mkdir " + "linuxPlaylists", shell=True)

    if not os.path.isdir("Playlists"):
        subprocess.call("mkdir " + "Playlists", shell=True)

    destination_folder = origin + "/linuxPlaylists"
    destination_copy = origin + "/Playlists"


    playlist_folder = home_folder + '/Music/MusicBee/Playlists'

    os.chdir(playlist_folder)

    playlist_names = os.listdir(playlist_folder)

    for playlist in playlist_names:
        if get_m3u(playlist):
            convertPlaylist(playlist, destination_folder)
            print "%s has been converted" % playlist

            source = playlist_folder + "/" + playlist
            dest_cp = destination_copy + "/" + playlist
            shutil.copy2(source, dest_cp)
            print "%s has been copied to Playlists directory\n" % playlist

    print "All playlilsts have been converted!"
    os.chdir(origin)

convertAll()

# test_playlist = "Playlists/80s.m3u"
# destination_test = '80s.m3u'
#
# convertPlaylist(test_playlist, destination_test)
