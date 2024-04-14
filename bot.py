import discord
from dotenv import load_dotenv
import os
import csv
from discord.ext import commands

#-------------------------------------------------------DISCORD BOT-------------------------------------------------------
# load_dotenv is a function that loads the key-value pairs from a .env file into the environment variables of the 
# running script
load_dotenv()
# os.getenv is a function that retrieves the value of the environment variable named 'DISCORD_TOKEN'
TOKEN = os.getenv('DISCORD_TOKEN')

# intents is a class that represents the different types of events that the bot can track
intents = discord.Intents.default()
#all these intents are set to True so that the bot can track these events
intents.messages = True  # Assuming you want the bot to track messages
intents.members = True  # This is needed to track when members join
intents.presences = True  # If you need the Presence Intent
bot = commands.Bot(command_prefix='!', intents=intents)


# The event decorator is used to register an event. The on_ready event is called when the bot has successfully connected
@bot.event
#async is a keyword that is used to define a function as a coroutine
#This function is basically an event handler that is called when the bot is ready to start receiving events
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    
@bot.command(name='food_list', help='Sends the food list to the channel')
async def send_food_list(ctx):
    csv_file_path = r'C:\Users\User\Desktop\WebScrape\scraped_menu.csv'
    
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader) #Skip the header row if there is one
        food_list = [row for row in reader] # This assumes each row is a separate food item
    
    food_message = 'Here is the food list for this week!:\n'
    for food in food_list:
        food_message += "- {}\n".format(', '.join(food))
        
    await ctx.send(food_message)
    
            
@send_food_list.error
async def food_list_error(ctx, error):
    await ctx.send('There was an error sending the food list')
    
# The event decorator is used to register an event. The on_message event is called when the bot receives a message
bot.run(TOKEN)

