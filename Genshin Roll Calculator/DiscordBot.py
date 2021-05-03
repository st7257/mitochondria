import discord
from discord.ext import commands
import asyncio
import pymongo
from pymongo import MongoClient
import random
cluster = MongoClient("mongodb+srv://steven:j7257197@cluster0.gjjwq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster.get_database('Data')
records = db.Profiles

existsList = ["Albedo",
            "Ganyu",
            "Hu Tao",
            "Klee",
            "Tartaglia",
            "Venti",
            "Xiao",
            "Zhongli",
            "Eula",
            "Diluc",
            "Jean",
            "Keqing",
            "Mona",
            "Qiqi",
            "Elegy for the End",
            "Memory of Dust",
            "Primordial Jade Cutter",
            "Song of Broken Pines",
            "Staff of Homa",
            "Summit Shaper",
            "The Unforged",
            "Vortex Vanquisher",
            "Amos' Bow",
            "Aquila Favonia",
            "Lost Prayer to the Sacred Winds",
            "Primordial Jade Winged-Spear",
            "Skyward Atlas",
            "Skyward Blade",
            "Skyward Harp",
            "Skyward Pride",
            "Skyward Spine",
            "Wolf's Gravestone"
]

charBanner = ["Albedo",
              "Ganyu",
              "Hu Tao",
              "Klee",
              "Tartaglia",
              "Venti",
              "Xiao",
              "Zhongli"
              "Eula"
]

stdBanner = ["Diluc",
             "Jean",
             "Keqing",
             "Mona",
             "Qiqi"
]

weaponsBanner = ["Elegy for the End",
                 "Memory of Dust",
                 "Primordial Jade Cutter",
                 "Song of Broken Pines",
                 "Staff of Homa",
                 "Summit Shaper",
                 "The Unforged",
                 "Vortex Vanquisher",             
]

stdweaponsBanner = ["Amos' Bow",
                    "Aquila Favonia",
                    "Lost Prayer to the Sacred Winds",
                    "Primordial Jade Winged-Spear",
                    "Skyward Atlas",
                    "Skyward Blade",
                    "Skyward Harp",
                    "Skyward Pride",
                    "Skyward Spine",
                    "Wolf's Gravestone",
]

dionaLines = {1:"I—I wasn't waiting for you. I just happened to be resting!",
              2:"Morning~ Can you hand me that can of salted loach from the cabinet? Time to destroy the wine industry!",
              3:"Uh, I was saving this can of fish for when I was really hungry. Stop looking at it like that! ...Mmm, okay, I'll let you have a little taste, but nothing more!",
              4:"Without cat vision, will you be okay walking home in the dark? If you need me to escort you... What? Th—There's lights? Pff, well who said anything about escorting you? Go on now.",
              5:"My ears and tail are no prop, they're real. Proof of my Kätzlein bloodline. It's only weird to you cause you've never seen it before. Wh—Why are you looking at me like that? Fine. You can touch my ears for a second, but the tail is off limits!",
              6:"Well, if you ever feel lonely, you can chat with me. I know lots of cool things~ I'm a good... what's that called... chatting partner! Yes! A good chatting partner, come chat with me... lots... ...okay?",
              7:"When it comes to butterflies, I'm the best at pouncing on— err, catching them. Hey, not in a fun way! I catch butterflies to add a nasty taste to my cocktails. I'm not a cat! Meow! *hiss*",
              8:"Diluc... I can't stand him! If there was no Diluc, there would be no Mondstadt wine industry; if there was no Mondstadt wine industry, Daddy wouldn't drink; and if Daddy didn't drink... he would keep me company. Ohhhh...",
              9:"I adore my daddy more than anyone else! He's the greatest! But... Daddy after he drinks, ugh... Argh! I must bring an end to the wine industry of Mondstadt, and soon! No time for chit-chat!",
              10:"Think you can bully me!?",
              11:"Diona special!",
              12:"A cat's eyes can see even the most elusive prey in the dark.",
              13:"A cat's ears can hear even the softest footsteps on the ground.",
              14:"A cat's legs can climb even the tallest tree in all of Teyvat.",
              15:"A cat's nose can smell those people they are familiar with and like... Ahh!? You're mistaken, how could I say something like that... Ohh..."
}

zsDict = {1:(1232,0.128),
          2:(1356,0.1376),
          3:(1489,0.1472),
          4:(1633,0.16),
          5:(1787,0.1669),
          6:(1951,0.1792),
          7:(2126,0.192),
          8:(2311,0.2048),
          9:(2506,0.2176),
          10:(2712,0.2304),
          11:(2927,0.2432),
          12:(3153,0.256),
          13:(3389,0.272),
          14:(3636,0.288),
          15:(3893,0.304)
}

def dbAdd(UID, CHARA, PITY):
    if records.count_documents({"_id":UID}) == 0:
        dataDict = {"_id" : UID, "Pulls":[(CHARA, PITY)]}
        records.insert_one(dataDict)
        print(1)
    else:
        records.update_one({"_id":UID}, {"$push": {"Pulls" : (CHARA, PITY)}})
        print(2)

def dbDelete(UID, CHARA, PITY):
    length = 0
    profile = records.find_one({"_id":UID}, {"Pulls": 1})
    data = profile["Pulls"]
    length = len(data)
    print(profile)
    print(profile["Pulls"])

    for item in data:
        if item == [CHARA, PITY]:
            data.remove(item)
            break

    if len(data) != length:
        print(profile["Pulls"]) 
        post = {"Pulls" : profile["Pulls"]}
        records.update_one({"_id":UID}, {"$set": post})
        return 1
    else:
        return 0



client = commands.Bot(command_prefix = '!', case_Insenitive = True)
@client.event
async def on_ready():
    print('Bot is ready.')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("ERROR: Command does not exist or was called incorrectly.")

@client.command() 
async def bruh(ctx):
    await ctx.send('it really is a bruh moment tho')

@client.command()
async def echo(ctx, *, message=None):
    """
    A simple command that repeats the users input back to them.
    """
    message = message or "Please provide the message to be repeated."
    await ctx.send(message)

@client.command(pass_context=True)
async def inventory(ctx, member: discord.Member=None):
    """
    Shows a player inventory.
    """
    if member is None:
        member = ctx.message.author
        UID = ctx.message.author.id
    
    else:
        UID = member.id
    print(UID)
    profile = records.find_one({"_id":UID}, {"Pulls": 1})
    data = profile["Pulls"]
    print(profile["Pulls"])
    print(len(profile["Pulls"]))
    temp = ''
    
    if profile == None:
        message = "Called inventory is empty."
        await ctx.send(message)
        return
    
    for item in data:
        temp = temp + "-" + item[0] + " " + item[1] + '\n'

    if (len(profile["Pulls"]) != 0):
        await ctx.send(temp)
    else:
        print(2)
        message = "Called inventory is empty."
        await ctx.send(message)

@client.command(pass_context=True)
async def add(ctx, *args):
    """
    Adds to database.
    """
    print(args)

    if args == ():
        await ctx.send("Proper command syntax: !remove [Character/Item] [Pity Counter]")
        return

    item = ""
    for arg in args:
        if arg != args[-1]:
            item = item + " " + arg
    item = item[1:]
    pity = args[-1]
    print(args)
    print([item])


    print(ctx.message.author.id)
    uid = ctx.message.author.id
    if (item in existsList):
        print('exists')
        if (pity.isnumeric() == True) and (int(pity) <= 90) and (int(pity) >= 1):
            print('numerical')
            dbAdd(uid, item, pity)
            await ctx.send("You added " + item + '.')
        else:
            await ctx.send("Invalid pity value provided.")
    else:
        await ctx.send("Character/Item provided was not found in database.")

@add.error
async def add_error_handler(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print(error)
        await ctx.send("Proper command syntax: !add [Character/Item] [Pity Counter]")

@client.command(pass_context=True)
async def remove(ctx, *args):
    """
    Deletes from database.
    """
    if args == ():
        await ctx.send("Proper command syntax: !remove [Character/Item] [Pity Counter]")
        return

    item = ""
    for arg in args:
        if arg != args[-1]:
            item = item + " " + arg
    item = item[1:]
    pity = args[-1]

    print(ctx.message.author.id)
    uid = ctx.message.author.id
    
    if (item in existsList):
        print('exists')
        if (pity.isnumeric() == True) and (int(pity) <= 90) and (int(pity) >= 1):
            if (dbDelete(uid, item, pity) == 1):
                await ctx.send("You removed " + item + '.')
            else:
                await ctx.send("The item you attempted to remove could not be found.")
        else:
            await ctx.send("Invalid pity value provided.")
    else:
        await ctx.send("Character/Item provided wa not found in database.")

@remove.error
async def remove_error_handler(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print(error)
        await ctx.send("Proper command syntax: !remove [Character/Item] [Pity Counter]")

@client.command(pass_context=True)
async def removeall(ctx):
    post = {"Pulls" : []}
    records.update_one({"_id":ctx.message.author.id}, {"$set": post})
    await ctx.send("Your inventory has been cleared.")



@client.command(pass_context=True)
async def zhonglishield(ctx, *, message=None):
    """
    Calculates Shield for Zhongli.
    """
    print(ctx.message.author.id)
    if message == None:
        await ctx.send("Proper command syntax: &zhonglishield [Max HP] [Talent Lvl]")
    message = message.split(' ')

    if (len(message) == 2) and (message[0].isnumeric() == True) and (message[1].isnumeric() == True) and (int(message[1]) <= 15 and int(message[1]) >= 1):
        health = int(message[0])
        lvl = int(message[1])
        baseShield = ((health*zsDict[lvl][1])*1.5)+zsDict[lvl][0]
        out = 'Your base shield health is: '+str(round(baseShield))+'\n\n' + '--For each hit taken by Jade Shield up to 5 hits, Jade Shield will gain an additional 5% health.' + '\n--The DEF stat of the shielded character is taken into account when calculating the damage taken by Jade Shield.'
        await ctx.send(out)
    else:
        await ctx.send("Proper command syntax: &zhonglishield [Max HP] [Talent Lvl]")


@client.command(pass_context=True)
async def diona(ctx, *, message=None):
    print(ctx.message.author.id)
    leo = 277348457533145088
    line = random.randint(1, 15)
    await ctx.send("<@" + str(leo) + ">\n" + dionaLines[line] +"\nhttps://imgur.com/FspFoCY")


@client.command(pass_context=True)
async def test(ctx, arg1, arg2):
    await ctx.send('You sent {} and {}'.format(arg1, arg2))

client.run('ODM3MDgxNjIyODY4MTMxODQw.YInXAw.POBLs6BBxu5JBDuZzH2bOGSuINE')

