import discord
from datetime import date
import datetime
import calendar
import time

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    #command to check status
    if message.content.startswith("$status"):
        await message.channel.send("I'm online!")
        print("I'm online!")

    #command to ping users if the bot isn't actively checking the time
    if message.content.startswith("$ping"):
        #tag members
        await message.channel.send("<@222925120790855683>, <@273980598987522059> <@599696360236646410> <@533811826652348426> Remember to check this week's Luxury Furnisher!")
        
        #post links
        await message.channel.send("https://eso-hub.com/en/luxury-furnisher")
        await message.channel.send("https://lovelynorth.com/luxury-vendor/")

    #command to start checking if event is going on
    if message.content.startswith("$start"):
        await message.channel.send("Starting up!")
        print("Starting up!")
        #list of days while event is running
        eligible_days_list = ["Friday", "Saturday", "Sunday"]

        #always want program running
        while(True):
            #check today's date to see if it is a day while event is running, run code if it is between 5PM-6PM AZ time, check every hour
            if(calendar.day_name[date.today().weekday()] in eligible_days_list and datetime.datetime.today().timetuple()[3] == 17):
                
                #tag members
                await message.channel.send("<@222925120790855683>, <@273980598987522059> <@599696360236646410> <@533811826652348426> Remember to check this week's Luxury Furnisher!")
                
                #post links
                await message.channel.send("https://eso-hub.com/en/luxury-furnisher")
                await message.channel.send("https://lovelynorth.com/luxury-vendor/")
                
                time.sleep(3600)
            
            #check to see if day is monday and it is between 7AM-8AM AZ time, check every hour
            elif(calendar.day_name[date.today().weekday()] == "Monday" and datetime.datetime.today().timetuple()[3] == 7):
                
                #tag members
                await message.channel.send("<@222925120790855683>, <@273980598987522059> <@599696360236646410> <@533811826652348426> Last call to check this week's Luxury Furnisher before it expires!")
                
                #post links 
                await message.channel.send("https://eso-hub.com/en/luxury-furnisher")
                await message.channel.send("https://lovelynorth.com/luxury-vendor/")
                
                time.sleep(3600)
            
            #check every hour
            else:
                time.sleep(3600)

#token
token = "TOKEN"

#run bot
client.run(token)