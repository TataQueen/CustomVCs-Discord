# - Main settings (IMPORTANT!!!)
masterChannel = 1067853653643370580 #Channel ID for the channel creator (Must be a voice chat, cant leave blank).
categoryID = 1067251018150182932 #Category ID for the customized channels.
userLimit = 0 #User limit for voice channels (0-99), set 0 for unlimited.


# - Static channels (prevent channels from being deleted)
staticChannels = [masterChannel, 1067249196488458260] #You should put here the IDs of VoiceChats that you don't want the bot to delete.


# - Default name for new channels
def customNameChannel(name):
  nameChannel = f"Canal de {name}" #This is the format for new channel names use {name} for placing the users name
  return nameChannel

# - Permissions (this only affects the channel creator)
connect = True
deafen_members = True
manage_channels = True
move_members = True
mute_members = True
priority_speaker = True
speak = True
stream = True
view_channel = True


