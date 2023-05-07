# __   _____   _ __  _   _ 
# \ \ / / __| | '_ \| | | |
#  \ V / (__ _| |_) | |_| |
#   \_/ \___(_) .__/ \__, |
#             |_|    |___/ 

enableVCpy = True # Enable vc.py if installed

# - Main settings ( Important!! )
masterChannel = 0 #Channel ID for the channel creator (Must be a voice chat, cant leave blank).
categoryID = 0 #Category ID for the customized channels.
userLimit = 0 #User limit for voice channels (0-99), set 0 for unlimited.



# - Static channels (prevent certain channels from being deleted)
staticChannels = [masterChannel, 1067249196488458260] #You should put here the IDs of VoiceChats that you don't want the bot to delete.


# - Default name for new channels
def customNameChannel(name):
  nameChannel = f"Canal de {name}" #This is the format for new channel names use {name} for placing the users name
  return nameChannel

# - Permissions (this only affects the channel creator, called user on the definitions)
connect = True # Can the user connect? (I would recommend leaving it true...)
deafen_members = True # Can the user deafen members on their channel? (Server-wide, future versions will undeafen the user after leaving)
manage_channels = True # Can the user can modify the name, user limit, description, voice settings and deleting the channel? (If they delete the channel by themselves it might not save)
move_members = True # Can the user kick members and move them between the channels they have this permission in?
mute_members = True # Can the user mute other members on their channel? (Server-wide, future versions will unmute the user after leaving)
priority_speaker = True # Can the user be a priority speaker? (This lowers the volume for the rest of users when using a keybind)
speak = True # Can the user speak in their own channel? (I would recommend leaving it true...)
stream = True # Can the user share their screen/games?
view_channel = True # Can the user view the channel? (I would recommend leaving it true...)


#              __                               
# __   _____  / /  ___   __ _ ___   _ __  _   _ 
# \ \ / / __|/ /  / _ \ / _` / __| | '_ \| | | |
#  \ V / (__/ /__| (_) | (_| \__ \_| |_) | |_| |
#   \_/ \___\____/\___/ \__, |___(_) .__/ \__, |
#                       |___/      |_|    |___/ 

enableVCLogpy = True # Enable vcLogs.py if installed

# Main settings ( Important!! )
customVCLog = True # Set this to false if you don't have vc.py
logsChannel = 1068495141490409572 # This is where all voice chat logs get saved
sameChannelUpdates = True # Should updates like self-mute/deafen appear in the logs channel ( Takes lots of space and not very useful ) 


#              _   _     __      __                      
#   __ _ _ __ | |_(_) /\ \ \___ / _|_      ___ __  _   _ 
#  / _` | '_ \| __| |/  \/ / __| |_\ \ /\ / / '_ \| | | |
# | (_| | | | | |_| / /\  /\__ \  _|\ V  V /| |_) | |_| |
#  \__,_|_| |_|\__|_\_\ \/ |___/_|   \_/\_(_) .__/ \__, |
#                                           |_|    |___/ 

enableantiNSFWpy = True # Enable antinsfw.py if installed 
logNSFWpy = True # Logs record of those who try to enable NSFW in a VC located on the custom vc category (requires vclogs.py)






# Credits to:

# - TAAG: ASCII art made with https://patorjk.com/software/taag/#p=display&f=Ogre&t=Example