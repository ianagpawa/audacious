# Audacious
### By Ian Agpawa
##### This repo is for a python script to convert music playlists saved in Windows to Ubuntu use-able playlists.  File paths of song files are updated and new playlists are created.  This works best if all your music is stored in a centralized location (sub-folders are fine).  

### Quick Start
-Clone the repo: `git clone https://github.com/ianagpawa/audacious.git`


### Before Executing The Script
- You will need to create `secrets.py` in the main project directory.  In the `secrets.py` file, you will need to declare the file path to your music directory in Ubuntu.
```
home_folder = {{MUSIC_DIRECTORY}}
```

-Copies of your playlists should be placed in the `Playlists` folder.

#### Executing The Script
While in the project folder, execute the following command:
```
python convert.py
```

You can then open these playlists with your media player program.  Confirmed to work with Audacious.

### What's included
Within the project folder, you will find the following files:

```
audacious/
    ├── Playlists/
    ├── convert.py
    └── README.md
```

## Creator

**Ian Agpawa**


[Github](https://github.com/ianagpawa)

 agpawaji@gmail.com
