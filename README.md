# CustomVCs-Discord
Customizable self-hosted bot for custom Voice Channels and logs for your users

Support is very much appreciated!

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M6GR1HT)

## Functionality
When users join a master channel they get a custom voice chat for themselves, you can edit the permissions they get
![Example preview](https://user-images.githubusercontent.com/87445319/214743659-20c3d79a-7561-429f-954a-0bb35669e7b7.gif)

## Setup
1. Clone the repository into your machine with `git clone https://github.com/TataQueen/CustomVCs-Discord`
2. Run `setup.py` to create the database for the bot to work
3. Create a file named `config.py` and place your bot token inside like this:
 ```python
 token = "YOURTOKENHERE"
 ``` 
4. Edit `defaults.py` and change the values for your server, explained inside the file.
5. Run with `python3 main.py`

## Customization
This repository includes a file `defaults.py` which is used for the settings so you don't have to touch the scripts
This contains all settings and you can disable the modules from there

#### Scripts
- `vc.py` - manages the creation of custom voice channels and uses a sqlite3 database (very efficient)
- `vclogs.py` - logs user interaction with voice channels and creation of custom voice channels (`vc.py`)
- `antinsfw.py` - disables NSFW activation on channels and can be logged (`vclogs.py`)

## Future features
- Support for translations
- Multi server support (New repository)
- More advanced logs (name changes, user capacity, ...)
- Helpful commands