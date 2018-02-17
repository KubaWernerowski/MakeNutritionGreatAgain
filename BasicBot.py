# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them, because they can break the bot.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform
from botTest import *
from foodInfo import *
from var_holder import *
from API_CALL import *
# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Basic Bot by Saamoz", command_prefix="!", pm_help = False)
state = var_holder()
food_api = APICall()
# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
# Do not mess with it because the bot can break, if you wish to do so, please consult me or someone trusted.
@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
    print('--------')
    print('Use this link to invite {}:'.format(client.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
    print('--------')
    print('Support Discord Server: https://discord.gg/FNNNgqb')
    print('Github Link: https://github.com/Habchy/BasicBot')
    print('--------')
    return await client.change_presence(game=discord.Game(name='PLAYING STATUS HERE'))

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.event
async def on_message(message):
    food_input = message.content
    if not state.awake:
        if message.content == "Wake up myBot":
            state.awake = True
        return
    elif message.content == "Sleep, myBot":
        state.awake = False
        await client.send_message(message.channel, "Going to sleep now...")
        return
    elif message.author == client.user:
        return

    ### if codes reaches this point we are making a call to the nutrionix API
    output = bot_response(message)
    if type(output) == str:
        await client.send_message(message.channel, "Sorry we could not find your requested food item.")
        return
    visuals = output["visual"]
    texts = output["text"]
    if len(visuals) == 0:
        for i in range(len(texts)):
            await client.send_message(message.channel, texts[i])
    elif len(visuals) != len(texts):
        await client.send_message(message.channel, visuals[0])
    else:
        for i in range(len(texts)):
            await client.send_message(message.channel, texts[i])
            await client.send_file(message.channel, visuals[i])
        delete_image_files()

def delete_image_files():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    get_dir = os.listdir(dir_path)

    for item in get_dir:
        if item.endswith(".png"):
            os.remove(os.path.join(dir_path, item))
#send_file(destination, fp, *, filename=None, content=None, tts=False)

client.run('NDE0MTg5NzU1MDE5MDM0NjM0.DWjwcw.UAsR3UFQS4e-7dviBeF0-gGCklQ')

# Basic Bot was created by Saamoz
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub! [Repo Link: https://github.com/Habchy/BasicBot]

# The help command is currently set to be not be Direct Messaged.
# If you would like to change that, change "pm_help = False" to "pm_help = True" on line 9.
