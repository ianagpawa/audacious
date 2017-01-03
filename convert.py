import os

cur_path = os.getcwd()
playlists_path = cur_path + "/Playlists"

playlist_names = os.listdir(playlists_path)

os.chdir(playlists_path)

#
# f = open('80s.m3u', 'r')
#
# arr = f.readlines()
#
# print arr
#
# f.close()

def replaceFileName(file_name):
    slashes = file_name.replace("\\", "/")
    replaced = slashes.replace("D:", "/media/onyx/Daedra")
    return replaced

def getArrayOfFileNames(filename):
    playlist = open(filename, 'r')
    arr = playlist.readlines()
    for file_name in arr:
        replacement = replaceFileName(file_name)
        print replacement
    playlist.close()

getArrayOfFileNames(playlist_names[0])


os.chdir(cur_path)
