# CustomVCs-Discord
Customizable self-hosted bot for custom VoiceChannels for your users and logging

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

## Future features
- Support for translations