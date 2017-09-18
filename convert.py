import os
import subprocess

from secrets import home_folder

# origin = os.getcwd()
#
# playlists_path = origin + "Music/MusicBee/Playlists"
# playlist_names = os.listdir(playlists_path)
#
#
# subprocess.call("mkdir " + "linuxPlaylists", shell=True)
# destination_folder = origin + "/linuxPlaylists"
# os.chdir(playlists_path)

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
        print 'no'
    

    playlist_names = os.listdir(home_folder)

    for playlist in playlist_names:
        pass

    #
    # subprocess.call("mkdir " + "linuxPlaylists", shell=True)
    # destination_folder = origin + "/linuxPlaylists"
    # os.chdir(playlists_path)

    # for playlist in playlist_names:
    #     convertPlaylist(playlist, destination_folder)
    # print "Everything Completed!"
    os.chdir(origin)

#getArrayOfFileNames('80s.m3u', destination_folder)

convertAll()

# os.chdir(origin)
