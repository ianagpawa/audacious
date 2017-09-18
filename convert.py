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
    for file_name in arr:
        replacement = replaceFileName(file_name)
        newArr.append(replacement)
    playlist.close()
    newPlaylist = open(destination_folder + "/" + filename, 'w+')
    newPlaylist.writelines(newArr)
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

    os.chdir(home_folder)
    playlist_names = os.listdir(home_folder)

    for playlist in playlist_names:
        if get_m3u(playlist):
            convertPlaylist(playlist, destination_folder)
            print "%s has been converted" % playlist

            source = home_folder + "/" + playlist
            dest_cp = destination_copy + "/" + playlist
            shutil.copy2(source, dest_cp)
            print "%s has been copied to Playlists directory\n" % playlist

    print "All playlilsts have been converted!"
    os.chdir(origin)


convertAll()
