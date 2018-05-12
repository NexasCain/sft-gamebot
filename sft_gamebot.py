#SFT GameBot

#This bot is made for the wonderful peeps of SFT's Discord server. Once this bot
#is given to SFT, I will make requested adjustments to the best of my ability,
#and add more games upon request after they have been fully tested and completed.

#IMPORTANT!!!
#You MUST enter the Bot Token at line 25 inbetween the two quotation marks! ("")

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import logging
import string
import time
import datetime
import os

import json

logging.basicConfig(level=logging.INFO)

#This isn't used since I made all commands use the on_message event. Leave it just in case.
bot = commands.Bot(command_prefix = "-")
bot.remove_command('help')


SFT_Token = os.environ.get('BOT_TOKEN')

TEST_Token = os.environ.get('TEST_BOT_TOKEN')

Bot_Token = TEST_Token

bot_spam_channel_id = "413470467719036940"


#Game reference
check_achievements = False
#Word Guess
wgID = 0
word = 0
scrambled_word = 0
wg_stoper = 0
wg_play = False
#Reaction
reactID = 0
word2 = 0
reaction_stoper = 0
reaction_play = False
#MasterMind
mmID = 0
guessNum = 0
combo = 0
mmplayer = 0
#DiceLuck
dlWinnerID = 0
dlQuitterID = 0
totalplayers = 0
player1name = 0
player2name = 0
player3name = 0
starttestgame = 0
roll1 = 0
roll2 = 0
roll3 = 0
roll4 = 0
roll5 = 0
keepRoll = 0
playersTurn = 0
currentRoll = 0
lastRoll = 0
currentTotal = 0
player1total = 0
player2total = 0
player3total = 0
numbOfDice = 5
diceluckGoal = 300

#TicTacToe
tttID = 0
tttP1 = 0
tttP2 = 0
tttBlank = ":black_medium_square:"
ttt1 = tttBlank
ttt2 = tttBlank
ttt3 = tttBlank
ttt4 = tttBlank
ttt5 = tttBlank
ttt6 = tttBlank
ttt7 = tttBlank
ttt8 = tttBlank
ttt9 = tttBlank
tttWinner = 0
tttStart = 0
tttTimer = 0
tttTime = 0
tttTimerStop = 0
when_to_stop = 0

#Connect4
c4ID = 0
C4_player1 = 0
C4_player2 = 0
C4_start = 0
C4_turn = 0

blankC4 = ":white_square_button:"
redC4 = ":red_circle:"
yellowC4 = ":large_orange_diamond:"
col1 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
col2 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
col3 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
col4 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
col5 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
col6 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
col7 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]



#tableC4="%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n:one::two::three::four::five::six::seven:"%(col1[0],col2[0],col3[0],col4[0],col5[0],col6[0],col7[0],col1[1],col2[1],col3[1],col4[1],col5[1],col6[1],col7[1],col1[2],col2[2],col3[2],col4[2],col5[2],col6[2],col7[2],col1[3],col2[3],col3[3],col4[3],col5[3],col6[3],col7[3],col1[4],col2[4],col3[4],col4[4],col5[4],col6[4],col7[4],col1[5],col2[5],col3[5],col4[5],col5[5],col6[5],col7[5])


#INSANITY
insaneID = 0
insanePlayers = []


#Traitor
traitorID = 0
traitor_embed_que = None
traitor1 = "Open"
traitor2 = "Open"
traitor3 = "Open"
traitor4 = "Open"
traitor5 = "Open"
traitor6 = "Open"
traitor7 = "Open"
traitor8 = "Open"
traitor9 = "Open"
traitorStart = 0
totalTraitorPlayers = 0






tttLayout = """
:one: :two: :three:
:four: :five: :six:
:seven: :eight: :nine:"""

diceluckInstructions = """
DiceLuck is a game where you roll dice, take chances, and gamble your points! First to %s or beyond wins!
When it's your turn, You can either take a chance with the dice the player before you kept (along with the score they earned), or start from scratch.
If the player before you looses their score, you cannot use their dice, and their score is lost!
If you don't score points on a roll, you loose your roll!
If you decide to keep what you have, you keep the points, and the next player can roll off of your recent score!
Good luck!"""%(str(diceluckGoal))
diceluckRules = """

To earn points in DiceLuck, you must roll one or a combination of the following:
1 1 1 = 100 points
2 2 2 = 20 points
3 3 3 = 30 points
4 4 4 = 40 points
5 5 5 = 50 points
6 6 6 = 60 points
5 = 5 points
1 = 10 points

When you roll these, the dice that gave you the points are held, and cannot be rolled.
However, if all five dice are held, you may roll all five dice again to have a chance to enhance your current score.
If you roll and get no points, your turn ends and you've lost all the points you gained on that turn. """





bothelpMessage = """**-BotHelp**
(This command)

**-Info**
(Gives some info about the bot)

**__[Game Commands]__**
**__|WordGuess|__**
**-WordGuess** or **-WG**
(Starts the Word guess game or gives a new word)

**__|Mastermind|__**
**-Mastermind**
(Starts a game of Mastermind)

**-mm <3 digit number>**
(Used to submit a guess to the answer for Mastermind)

**__|TicTacToe|__**
**-ttt**
(Joins you to a game of TicTacToe if one isn't in progress)

**__|Connect4|__**
**-Connect4** or **-C4**
(Joins you to a game of Connect4)

**<Number 1-9>**
(Places your mark on that space)

**__|DiceLuck|__**
**-BotHelp DiceLuck** or **-BotHelp DL**
(Shows all commands for DiceLuck)

**__[Math]__**
**-math <Math Expression>**
(Solves a math expression using Python supported opperations)
(type **-BotHelp Math** for more info)

**__[Misc. Commands]__**
**__-Register__**
(Registers you to the GameBot Statistics)

**__-Profile__**
(Shows your personal stats)

**__-Leaderboard__**
(Shows the leaderboards of different types.)
(Enable Reactions!)

**__-Buy__**
(Allows you to buy with your points!)"""


DiceLuckHelp = """**__DICELUCK Help__**

**-DiceLuck Rules**
(Tells the rules and instructions for DiceLuck)

**-DiceLuck Join**
(Joins you to a game of DiceLuck)

**-DL Goal <number>**
(Use to set a custom goal before the game, default goal is 300)

**-DL Leave**
(Removes you from the DiceLuck game que)

**-DL Start**
(Starts the game)

**-DL Roll**
(Rolls the dice if it's your turn, and rolls off of someone elses if another player's turn just ended)

**-DL No**
(Starts your turn from scratch)

**-DL Score**
(Shows the scores of the current game)

**-DL Reset**
(Resets the DiceLuck game)
(Only those with permission can use this command!)"""

MathHelp = """**__[-Math Help]__**
**|Supported opperations|**
+   (Addition)

-   (Subtraction)

*   (Multiplication)

/   (Division)

()  (Parenthases)

**  (Exponents)"""

Bot_Info = """**__Version 1.5__**
:video_game: I was created by Nexas Cain with the help of a meme (Rab), Plater, and the encouragement from Nexas' best friends. Nexas won't admit this, but he is very greatful for all who helped! :space_invader:"""


insaneInstructions = "Click the corosponding number reaction to move a piece. Red circles can only move right, Blue circles can only move left. Get the Red to the right and Blue to the left to win! Pieces can move over one space or jump over one piece."


words = [("GAMES", "games"),                    ("INSTAGRAM", "Instagram"),             ("HELLO", "hello"),             ("FILE", "file"),
        ("MINECRAFT", "Minecraft"),             ("SNAPCHAT", "Snapchat"),               ("PIZZA", "pizza"),             ("STAMP", "stamp"),
        ("CHEESECAKE", "cheesecake"),           ("FACEBOOK", "Facebook"),               ("DISK","disk"),                ("SWAP", "swap"),
        ("FALLOUT", "fallout"),                 ("METROID", "metroid"),                 ("PAPER", "paper"),             ("WASP", "wasp"),
        ("ENVELOPE", "envelope"),               ("OBSIDIAN", "obsidian"),               ("PHONE", "phone"),             ("ANT", "ant"),
        ("ATOMIC", "atomic"),                   ("PYTHON", "python"),                   ("CHOICE", "choice"),           ("FUN", "fun"),
        ("RADIOACTIVE", "radioactive"),         ("DETECTIVE", "detective"),             ("START", "start"),             ("SUPER", "super"),
        ("GRANDFATHER", "grandfather"),         ("BATMAN", "batman"),                   ("POWER", "power"),             ("CHAIR", "chair"),
        ("MARVEL", "marvel"),                   ("TOASTER", "toaster"),                 ("TIME", "time"),               ("DESK", "desk"),
        ("DOMINO", "domino"),                   ("CHIMICHANGA", "chimichanga"),         ("PRINTER", "printer"),         ("BOOK", "book"),
        ("SPAMBOT", "spambot"),                 ("DRAGON", "dragon"),                   ("NIGHT", "night"),             ("HUNGER", "hunger"),
        ("MECHANICAL", "mechanical"),           ("TREATY", "treaty"),                   ("DAY", "day"),                 ("JAVA", "java"),
        ("HEADPHONES", "headphones"),           ("CHICKEN", "chicken"),                 ("MORNING", "morning"),         ("SCRIPT", "script"),
        ("HANDBAG", "handbag"),                 ("TAFFY", "taffy"),                     ("MOUSE", "mouse"),             ("FAN", "fan"),
        ("MULTIPLICATION", "multiplication"),   ("SLEEP", "sleep"),                     ("ZERO", "zero"),               ("SEVEN", "seven"),
        ("TEST", "test"),                       ("SUGGESTIONS", "suggestions"),         ("ONE", "one"),                 ("EIGHT", "eight"),
        ("GLOVES", "gloves"),                   ("BASKET", "basket"),                   ("TWO", "two"),                 ("NINE", "nine"),
        ("EDUCATED", "educated"),               ("HYDROGEN", "hydrogen"),               ("THREE", "three"),             ("TEN", "ten"),
        ("STRANGER", "stranger"),               ("PLUTONIUM", "plutonium"),             ("FOUR", "four"),               ("SEVENTEEN", "seventeen"),
        ("ARMADA", "armada"),                   ("TELEVISION", "television"),           ("FIVE", "five"),
        ("AWESOME", "awesome"),                 ("SYRUP", "syrup"),                     ("SIX", "six"),
        ("RAINSTORM", "rainstorm"),             ("TOWELIE", "Towelie"),
        ("PANCAKE", "pancake"),                 ("SUPERFUNTIME", "SuperFunTime"),
        ("UNKNOWN", "unknown"),
        ("SCIENTIFIC", "scientific"),
        ("SPARKLING", "sparkling"),
        ("EARTHQUAKE", "earthquake"),
        ("GUARANTEE", "guarantee"),
        ("EXERCISE", "exercise"),
        ("WINE", "wine"),
        ("WACKY", "wacky"),
        ("MAGENTA", "magenta"),
        ("COMMUNICATE", "communicate"),
        ("DEAR", "dear"),
        ("READ", "read"),
        ("READY", "ready"),
        ("CHESS", "chess"),
        ("SYSTEM", "system"),
        ("STRENGTHEN", "strengthen"),
        ("PROGRAM", "program"),
        ("IDIOTIC", "idiotic"),
        ("SUCCEED", "succeed"),
        ("PREPARE", "prepare"),
        ("AMERICA", "America")
        ]





class Main_Commands():
    def __init__(self, bot):
        self.bot = bot



async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name='-BotHelp'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-Mastermind'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-WordGuess'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-TicTacToe'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-DiceLuck'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-Info'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-Math'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-React'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-Connect4'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-Leaderboard'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-Profile'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-Register'))
        await asyncio.sleep(7)
        await bot.change_presence(game=discord.Game(name='-Buy'))
        await asyncio.sleep(7)

async def check_achievements():
    with open('stats.json') as ach:
        lines = json.load(ach)
    await bot.send_message(message.channel, "Test")
    for achieve in lines['achievements']:
        bot.send_message(message.channel, achieve['name'])
        bot.send_message(message.channel, "Checking initiated!")


    #check_achievements = False

@bot.event
async def on_ready():
    print ("Ready to go Sire!")
    print ("I am running on " + bot.user.name)
    await bot.loop.create_task(status_task())


@bot.event
async def on_message(message):

    #async def edit_stats(id,game):


    if message.channel.id == bot_spam_channel_id:

        if message.content.upper().startswith("-SEND_FILES"):
            if message.author.id == "329058795026382849":
                await bot.send_file(message.author,"stats.json")
                await bot.send_file(message.author,"achievements.json")
                

        if message.content.upper().startswith("-PROFILE"):
            with open('stats.json') as stats:
                lines = json.load(stats)
                registered = False
            for player in lines['players']:
                if player['id'] == message.author.id:
                    registered = True
                    profile = "**Game Stats:**\n\n**Wins** \n\n:regional_indicator_w:-Wordguess: %s           :regional_indicator_r:-Reaction: %s\n\n:m:-Mastermind: %s        :game_die:-DiceLuck: %s\n\n:regional_indicator_x:-TicTacToe: %s             :red_circle:-Connect4: %s\n\n:question:-Insanity: %s               :beginner:-Points: %s\n"%(player['wgWins'],player['reactWins'],player['mmWins'],player['dlWins'],player['tttWins'],player['c4Wins'],player['insaneWins'],player['points'])

                    with open('achievements.json') as achie:
                        ach = json.load(achie)
                        earned = ""

                    for a in ach['achievements']:
                        for id in a['players']:
                            if id == message.author.id:
                                earned += "**[**"+a['name']+"**]**\n"

                    if earned == "":
                        earned = "None"

                    achievements_earned = "\n\n**Achievements:**\n\n" + earned

                    em = discord.Embed(title=None, description=profile+achievements_earned, colour=0xBCAD20)
                    em.set_author(name="Profile of " + message.author.name,icon_url=message.author.avatar_url)
                    em.set_image(url=message.author.avatar_url)
                    await bot.send_message(message.channel,content=None, embed=em)

            if registered == False:
                await bot.send_message(message.channel, "Please register with the SFT GameBot by typing ``-Register`!")



        #Joining
        if message.content.upper().startswith("-REGISTER"):
            #stats = open("stats.txt", "r")
            with open('stats.json') as stats:
                lines = json.load(stats)
                registered = False
                #await bot.send_message(message.channel, "Test")
                #await bot.send_message(message.channel, lines)

            #Check if player is registered already
            for player in lines['players']:
                #await bot.send_message(message.channel, "Test")
                if player['id'] == message.author.id:
                    #await bot.send_message(message.channel, "Test")
                    registered = True
                    await bot.send_message(message.channel, "You are already registered!")

            #
            #if player isn't registered, this will register them!
            if registered == False:
                lines['players'] += [{'id': message.author.id, 'name': message.author.name, 'booster': 1, 'points': 0, 'quits': 0, 'wgWins': 0, 'reactWins': 0, 'mmWins': 0, 'dlWins': 0, 'tttWins': 0, 'c4Wins': 0, 'insaneWins': 0}]
                await bot.send_message(message.channel, "You've been registered with the SFT GameBot!")

            with open('stats.json','w') as stats:
                json.dump(lines, stats, indent=4)

            #await bot.send_message(message.channel, "Done")


        if message.content.upper().startswith("-LEADERBOARD"):
            wgLeaderboardStats = []
            reactLeaderboardStats = []
            mmLeaderboardStats = []
            dlLeaderboardStats = []
            tttLeaderboardStats = []
            c4LeaderboardStats = []
            insaneLeaderboardStats = []
            allLeaderboardStats = []
            pointLeaderboardStats = []
            #await bot.send_message(message.channel, "Testing")
            with open('stats.json') as stats:
                lines = json.load(stats)



            for player in lines['players']:

                #Set game leaderboards!
                #Wordguess
                wgLeaderboardStats += [(player['wgWins'],player['name'])]
                #Reaction
                reactLeaderboardStats += [(player['reactWins'],player['name'])]
                #Mastermind
                mmLeaderboardStats += [(player['mmWins'],player['name'])]
                #DiceLuck
                dlLeaderboardStats += [(player['dlWins'],player['name'])]
                #TicTacToe
                tttLeaderboardStats += [(player['tttWins'],player['name'])]
                #Connect4
                c4LeaderboardStats += [(player['c4Wins'],player['name'])]
                #Insanity
                insaneLeaderboardStats += [(player['insaneWins'],player['name'])]
                #ALL
                allLeaderboardStats += [(int(player['wgWins'])+int(player['reactWins'])+int(player['mmWins'])+int(player['dlWins'])+int(player['tttWins'])+int(player['c4Wins'])+int(player['insaneWins'])+int(player['points']),player['name'])]
                #Points
                pointLeaderboardStats += [(player['points'],player['name'])]
                #await bot.send_message(message.channel, allLeaderboardStats)
                #Set up Embed Message
                #Set up Reactions for Embed Message


            #await bot.send_message(message.channel, wgLeaderboardStats)
            #async def getKey(item):
            #    return item[0]
            #sorted(wgLeaderboardStats,key=getKey)
            #wgLeaderboard = sorted(wgLeaderboardStats)
            try:
                wgLeaderboard = sorted(wgLeaderboardStats, key=lambda x: -x[0])
                reactLeaderboard = sorted(reactLeaderboardStats, key=lambda x: -x[0])
                mmLeaderboard = sorted(mmLeaderboardStats, key=lambda x: -x[0])
                dlLeaderboard = sorted(dlLeaderboardStats, key=lambda x: -x[0])
                tttLeaderboard = sorted(tttLeaderboardStats, key=lambda x: -x[0])
                c4Leaderboard = sorted(c4LeaderboardStats, key=lambda x: -x[0])
                insaneLeaderboard = sorted(insaneLeaderboardStats, key=lambda x: -x[0])
                allLeaderboard = sorted(allLeaderboardStats, key=lambda x: -x[0])
                pointLeaderboard = sorted(pointLeaderboardStats, key=lambda x: -x[0])
                #await bot.send_message(message.channel, "Sorted!")
            except:
                await bot.send_message(message.channel, "Failed to sort something.")
            allLBnum = [x[0] for x in allLeaderboard]
            allLBname = [x[1] for x in allLeaderboard]
            wgLBnum = [x[0] for x in wgLeaderboard]
            wgLBname = [x[1] for x in wgLeaderboard]
            mmLBnum = [x[0] for x in mmLeaderboard]
            mmLBname = [x[1] for x in mmLeaderboard]
            reactLBnum = [x[0] for x in reactLeaderboard]
            reactLBname = [x[1] for x in reactLeaderboard]
            dlLBnum = [x[0] for x in dlLeaderboard]
            dlLBname = [x[1] for x in dlLeaderboard]
            tttLBnum = [x[0] for x in tttLeaderboard]
            tttLBname = [x[1] for x in tttLeaderboard]
            c4LBnum = [x[0] for x in c4Leaderboard]
            c4LBname = [x[1] for x in c4Leaderboard]
            insaneLBnum = [x[0] for x in insaneLeaderboard]
            insaneLBname = [x[1] for x in insaneLeaderboard]
            pointLBnum = [x[0] for x in pointLeaderboard]
            pointLBname = [x[1] for x in pointLeaderboard]
            allLB = "**All Games:**\n\n**1:** %s: %s\n\n**2: **%s: %s\n\n**3: **%s: %s\n\n**4: **%s: %s\n\n**5: **%s: %s\n\n**6: **%s: %s\n\n**7: **%s: %s\n\n**8: **%s: %s\n\n**9: **%s: %s\n\n**10: **%s: %s"%(allLBname[0],allLBnum[0],allLBname[1],allLBnum[1],allLBname[2],allLBnum[2],allLBname[3],allLBnum[3],allLBname[4],allLBnum[4],allLBname[5],allLBnum[5],allLBname[6],allLBnum[6],allLBname[7],allLBnum[7],allLBname[8],allLBnum[8],allLBname[9],allLBnum[9])
            wgLB = "**Wordguess:**\n\n**1:** %s: %s\n\n**2: **%s: %s\n\n**3: **%s: %s\n\n**4: **%s: %s\n\n**5: **%s: %s\n\n**6: **%s: %s\n\n**7: **%s: %s\n\n**8: **%s: %s\n\n**9: **%s: %s\n\n**10: **%s: %s"%(wgLBname[0],wgLBnum[0],wgLBname[1],wgLBnum[1],wgLBname[2],wgLBnum[2],wgLBname[3],wgLBnum[3],wgLBname[4],wgLBnum[4],wgLBname[5],wgLBnum[5],wgLBname[6],wgLBnum[6],wgLBname[7],wgLBnum[7],wgLBname[8],wgLBnum[8],wgLBname[9],wgLBnum[9])
            mmLB = "**Mastermind:**\n\n**1:** %s: %s\n\n**2: **%s: %s\n\n**3: **%s: %s\n\n**4: **%s: %s\n\n**5: **%s: %s\n\n**6: **%s: %s\n\n**7: **%s: %s\n\n**8: **%s: %s\n\n**9: **%s: %s\n\n**10: **%s: %s"%(mmLBname[0],mmLBnum[0],mmLBname[1],mmLBnum[1],mmLBname[2],mmLBnum[2],mmLBname[3],mmLBnum[3],mmLBname[4],mmLBnum[4],mmLBname[5],mmLBnum[5],mmLBname[6],mmLBnum[6],mmLBname[7],mmLBnum[7],mmLBname[8],mmLBnum[8],mmLBname[9],mmLBnum[9])
            reactLB = "**Reaction:**\n\n**1:** %s: %s\n\n**2: **%s: %s\n\n**3: **%s: %s\n\n**4: **%s: %s\n\n**5: **%s: %s\n\n**6: **%s: %s\n\n**7: **%s: %s\n\n**8: **%s: %s\n\n**9: **%s: %s\n\n**10: **%s: %s"%(reactLBname[0],reactLBnum[0],reactLBname[1],reactLBnum[1],reactLBname[2],reactLBnum[2],reactLBname[3],reactLBnum[3],reactLBname[4],reactLBnum[4],reactLBname[5],reactLBnum[5],reactLBname[6],reactLBnum[6],reactLBname[7],reactLBnum[7],reactLBname[8],reactLBnum[8],reactLBname[9],reactLBnum[9])
            dlLB = "**DiceLuck:**\n\n**1:** %s: %s\n\n**2: **%s: %s\n\n**3: **%s: %s\n\n**4: **%s: %s\n\n**5: **%s: %s\n\n**6: **%s: %s\n\n**7: **%s: %s\n\n**8: **%s: %s\n\n**9: **%s: %s\n\n**10: **%s: %s"%(dlLBname[0],dlLBnum[0],dlLBname[1],dlLBnum[1],dlLBname[2],dlLBnum[2],dlLBname[3],dlLBnum[3],dlLBname[4],dlLBnum[4],dlLBname[5],dlLBnum[5],dlLBname[6],dlLBnum[6],dlLBname[7],dlLBnum[7],dlLBname[8],dlLBnum[8],dlLBname[9],dlLBnum[9])
            tttLB = "**TicTacToe:**\n\n**1:** %s: %s\n\n**2: **%s: %s\n\n**3: **%s: %s\n\n**4: **%s: %s\n\n**5: **%s: %s\n\n**6: **%s: %s\n\n**7: **%s: %s\n\n**8: **%s: %s\n\n**9: **%s: %s\n\n**10: **%s: %s"%(tttLBname[0],tttLBnum[0],tttLBname[1],tttLBnum[1],tttLBname[2],tttLBnum[2],tttLBname[3],tttLBnum[3],tttLBname[4],tttLBnum[4],tttLBname[5],tttLBnum[5],tttLBname[6],tttLBnum[6],tttLBname[7],tttLBnum[7],tttLBname[8],tttLBnum[8],tttLBname[9],tttLBnum[9])
            c4LB = "**Connect4:**\n\n**1:** %s: %s\n\n**2: **%s: %s\n\n**3: **%s: %s\n\n**4: **%s: %s\n\n**5: **%s: %s\n\n**6: **%s: %s\n\n**7: **%s: %s\n\n**8: **%s: %s\n\n**9: **%s: %s\n\n**10: **%s: %s"%(c4LBname[0],c4LBnum[0],c4LBname[1],c4LBnum[1],c4LBname[2],c4LBnum[2],c4LBname[3],c4LBnum[3],c4LBname[4],c4LBnum[4],c4LBname[5],c4LBnum[5],c4LBname[6],c4LBnum[6],c4LBname[7],c4LBnum[7],c4LBname[8],c4LBnum[8],c4LBname[9],c4LBnum[9])
            insaneLB = "**Insanity:**\n\n**1:** %s: %s\n\n**2: **%s: %s\n\n**3: **%s: %s\n\n**4: **%s: %s\n\n**5: **%s: %s\n\n**6: **%s: %s\n\n**7: **%s: %s\n\n**8: **%s: %s\n\n**9: **%s: %s\n\n**10: **%s: %s"%(insaneLBname[0],insaneLBnum[0],insaneLBname[1],insaneLBnum[1],insaneLBname[2],insaneLBnum[2],insaneLBname[3],insaneLBnum[3],insaneLBname[4],insaneLBnum[4],insaneLBname[5],insaneLBnum[5],insaneLBname[6],insaneLBnum[6],insaneLBname[7],insaneLBnum[7],insaneLBname[8],insaneLBnum[8],insaneLBname[9],insaneLBnum[9])
            pointLB = "**Points:**\n\n**1:** %s: %s\n\n**2: **%s: %s\n\n**3: **%s: %s\n\n**4: **%s: %s\n\n**5: **%s: %s\n\n**6: **%s: %s\n\n**7: **%s: %s\n\n**8: **%s: %s\n\n**9: **%s: %s\n\n**10: **%s: %s"%(pointLBname[0],pointLBnum[0],pointLBname[1],pointLBnum[1],pointLBname[2],pointLBnum[2],pointLBname[3],pointLBnum[3],pointLBname[4],pointLBnum[4],pointLBname[5],pointLBnum[5],pointLBname[6],pointLBnum[6],pointLBname[7],pointLBnum[7],pointLBname[8],pointLBnum[8],pointLBname[9],pointLBnum[9])
            # %s\n\n**2: **%s: %s\n\n**3: **%s: %s\n\n**4: **%s: %s\n\n**5: **%s: %s\n\n**6: **%s: %s\n\n**7: **%s: %s\n\n**8: **%s: %s\n\n**9: **%s: %s\n\n**10: **%s: %s

            em = discord.Embed(title=None, description=allLB, colour=0xBCAD20)
            em.set_author(name="SuperFunTime's Gaming Leaderboard")
            #em.set_footer(text=)
            leaderboard_msg = await bot.send_message(message.channel,content=None, embed=em)
            #Add reactions for leaderboards here!
            await bot.add_reaction(leaderboard_msg,'🎮')
            await bot.add_reaction(leaderboard_msg,'🇼')
            await bot.add_reaction(leaderboard_msg,'🇷')
            await bot.add_reaction(leaderboard_msg,'\N{Circled Latin Capital Letter M}')
            await bot.add_reaction(leaderboard_msg,'🎲')
            await bot.add_reaction(leaderboard_msg,'🇽')
            await bot.add_reaction(leaderboard_msg,'🔴')
            await bot.add_reaction(leaderboard_msg,'❓')
            await bot.add_reaction(leaderboard_msg,'🔰')
            await bot.add_reaction(leaderboard_msg,'❌')
            LB_going = True
            while LB_going == True:
                LB_react = await bot.wait_for_reaction(emoji=None,user=message.author,timeout=60,message=leaderboard_msg)
                if LB_react:
                    if LB_react.reaction.emoji == '❌':
                        await bot.delete_message(leaderboard_msg)
                    elif LB_react.reaction.emoji == '🎮':
                        LB_now = allLB

                    elif LB_react.reaction.emoji == '🇼':
                        LB_now = wgLB

                    elif LB_react.reaction.emoji == '🇷':
                        LB_now = reactLB

                    elif LB_react.reaction.emoji == '\N{Circled Latin Capital Letter M}':
                        LB_now = mmLB

                    elif LB_react.reaction.emoji == '🎲':
                        LB_now = dlLB

                    elif LB_react.reaction.emoji == '🇽':
                        LB_now = tttLB

                    elif LB_react.reaction.emoji == '🔴':
                        LB_now = c4LB

                    elif LB_react.reaction.emoji == '❓':
                        LB_now = insaneLB

                    elif LB_react.reaction.emoji == '🔰':
                        LB_now = pointLB

                    await bot.remove_reaction(message=leaderboard_msg, emoji=LB_react.reaction.emoji, member=message.author)

                    em = discord.Embed(title=None, description=LB_now, colour=0xBCAD20)
                    em.set_author(name="SuperFunTime's Gaming Leaderboard")
                    #leaderboard_msg = await bot.send_message(message.channel,content=None, embed=em)
                    leaderboard_msg = await bot.edit_message(message=leaderboard_msg,new_content=None,embed=em)

                else:
                    await bot.delete_message(leaderboard_msg)



        if message.content.upper().startswith("-BUY"):

            with open('stats.json') as stats:
                s = json.load(stats)

            for player in s['players']:
                if player['id'] == message.author.id:
                    #await bot.send_message(message.channel, player['booster'])

                    page = 1

                    if page == 1:
                        item = "Point Booster :arrow_double_up:"
                        itemID = 'booster'

                        if player['booster'] == 1:
                            booster_price = 250

                        elif player['booster'] == 2:
                            booster_price = 750

                        elif player['booster'] == 3:
                            booster_price = 2250

                        else:
                            booster_price = 100000

                    #await bot.send_message(message.channel, "Test")
                    buy_desc = "**Item:** "+item+"\n\n**:large_orange_diamond: Price:** "+str(booster_price)+" :beginner:\n\n**:small_orange_diamond: Points:** "+str(player['points'])+" :beginner:\n"
                    #await bot.send_message(message.channel, "Test")



                    PageNum = "Page "+str(page)+" of 1"
                    #await bot.send_message(message.channel, "Test")

                    em = discord.Embed(title="-BUY!", description=buy_desc, colour=0xBCAD20)
                    em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                    em.set_footer(text=PageNum)
                    buyMsg = await bot.send_message(message.channel,content=None,embed=em)

                    await bot.add_reaction(buyMsg,'\N{Black Left-Pointing Triangle}')
                    await bot.add_reaction(buyMsg,'\N{Black Right-Pointing Triangle}')
                    await bot.add_reaction(buyMsg,'💳')
                    await bot.add_reaction(buyMsg,'❌')

                    buy_wait = 0
                    while buy_wait == 0:
                        #inPlayerReact = await bot.wait_for_reaction(emoji=None,user=message.author,timeout=60,message=inMsg)
                        buy_react = await bot.wait_for_reaction(emoji=None,user=message.author,timeout=60,message=buyMsg)
                        if buy_react:
                            if buy_react.reaction.emoji == '\N{Black Left-Pointing Triangle}':
                                if page > 1:
                                    page -= 1

                            elif buy_react.reaction.emoji == '\N{Black Right-Pointing Triangle}':
                                if page < 1:
                                    page += 1

                            elif buy_react.reaction.emoji == '💳':
                                if player['points'] >= booster_price:
                                    player['points'] -= booster_price
                                    player['booster'] += 1
                                    with open('stats.json','w') as stats:
                                        json.dump(s,stats,indent=4)
                                #await bot.send_message(message.channel, "Finish this")

                            elif buy_react.reaction.emoji == '❌':
                                await bot.delete_message(buyMsg)
                                buy_wait = 1

                            await bot.remove_reaction(message=buyMsg,emoji=buy_react.reaction.emoji,member=message.author)


                            if page == 1:
                                item = "Point Booster :arrow_double_up:"
                                itemID = 'booster'

                                if player['booster'] == 1:
                                    booster_price = 250

                                elif player['booster'] == 2:
                                    booster_price = 750

                                elif player['booster'] == 3:
                                    booster_price = 2250

                                else:
                                    booster_price = 100000

                            buy_desc = "**Item:** "+item+"\n\n**:large_orange_diamond: Price:** "+str(booster_price)+" :beginner:\n\n**:small_orange_diamond: Points:** "+str(player['points'])+" :beginner:\n"

                            em = discord.Embed(title="BUY!", description=buy_desc, colour=0xBCAD20)
                            em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                            em.set_footer(text=PageNum)
                            buyMsg = await bot.edit_message(message=buyMsg,new_content=None,embed=em)


                        else:
                            await bot.delete_message(buyMsg)
                            buy_wait = 1

            # em = discord.Embed(title="-BUY!", description=buy_desc, colour=0xBCAD20)
            # em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
            # em.set_footer(text=PageNum)
            # buyMsg = await bot.send_message(channel=message.channel,content=None,embed=em)
            #
            #






        #Info
        if message.content.upper().startswith("-INFO") and message.channel.id == bot_spam_channel_id:
            #await bot.send_message(message.channel, "My name is " + bot.user.name)
            #await bot.send_message(message.channel, "I was created by Nexas Cain with the help of a meme (Rab), Plater, and the encouragement from Nexas' best friends. Nexas won't admit this, but he is very greatful for all who helped!")
            global check_achievements

            em = discord.Embed(title=None, description=Bot_Info, colour=0xBCAD20)
            em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
            em.set_footer(text="I'm watching you %s"%(message.author.name))
            em.set_image(url=bot.user.avatar_url)
            await bot.send_message(message.channel,content=None, embed=em)

            #await client.send_file(discord.AppInfo.icon)






        #Math
        if message.content.upper().startswith("-MATH"):
            if message.channel.id == bot_spam_channel_id:
                eq1 = message.content[6:]
                def less_dangerous_eval(equation):
                    if not set(equation).intersection(string.ascii_letters + '{}[]_;\n'):
                        return eval(equation)
                    else:
                        bot.send_message(message.channel, "illegal character")
                        return None

                evaled = less_dangerous_eval(eq1)
                await bot.send_message(message.channel, evaled)





        if message.content.upper().startswith("-TR"):
            global traitor_embed_que
            global traitor1
            global traitor2
            global traitor3
            global traitor4
            global traitor5
            global traitor6
            global traitor7
            global traitor8
            global traitor9
            global traitorStart
            global totalTraitorPlayers
            if message.channel.id == bot_spam_channel_id:

                paramater = message.content.upper()[4:]

                if paramater == "JOIN":
                    if traitorStart != 0:
                        await bot.send_message(message.channel, "**Traitor** is already in progress!")
                    else:

                        if message.author.nick != None:
                            traitorMessager = message.author.nick
                        else:
                            traitorMessager = message.author.name

                        if traitor1 == "Open":
                            traitor1 = traitorMessager
                            totalTraitorPlayers += 1
                        elif traitor2 == "Open":
                            traitor2 = traitorMessager
                            totalTraitorPlayers += 1
                        elif traitor3 == "Open":
                            traitor3 = traitorMessager
                            totalTraitorPlayers += 1
                        elif traitor4 == "Open":
                            traitor4 = traitorMessager
                            totalTraitorPlayers += 1
                        elif traitor5 == "Open":
                            traitor5 = traitorMessager
                            totalTraitorPlayers += 1
                        elif traitor6 == "Open":
                            traitor6 = traitorMessager
                            totalTraitorPlayers += 1
                        elif traitor7 == "Open":
                            traitor7 = traitorMessager
                            totalTraitorPlayers += 1
                        elif traitor8 == "Open":
                            traitor8 = traitorMessager
                            totalTraitorPlayers += 1
                        elif traitor9 == "Open":
                            traitor9 = traitorMessager
                            totalTraitorPlayers += 1
                        else:
                            await bot.send_message(message.channel, "**Traitor** que is full!")



                        if traitor2 == "Open":
                            traitor_que = "The current Traitor queue is:\n1: %s\n2: %s\n3: %s\n4: %s\n5: %s\n6: %s\n7: %s\n8: %s\n9: %s"%(traitor1,traitor2,traitor3,traitor4,traitor5,traitor6,traitor7,traitor8,traitor9)

                            em = discord.Embed(title="Traitor", description=traitor_que, colour=0xBCAD20)
                            em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                            traitor_embed_que = await bot.send_message(message.channel, content=None, embed=em)

                        else:
                            traitor_que = "The current Traitor queue is:\n1: %s\n2: %s\n3: %s\n4: %s\n5: %s\n6: %s\n7: %s\n8: %s\n9: %s"%(traitor1,traitor2,traitor3,traitor4,traitor5,traitor6,traitor7,traitor8,traitor9)

                            em = discord.Embed(title="Traitor", description=traitor_que, colour=0xBCAD20)
                            em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                            await bot.edit_message(traitor_embed_que, new_content=None, embed=em)


                        await bot.delete_message(message)


                elif paramater == "START":
                    if totalTraitorPlayers <= 4:
                        await bot.send_message(message.channel, "Please have at least 5 players before you start!")
                    elif 4 < totalTraitorPlayers < 7:
                        numberOfTraitors = 1
                        traitorStart = 1
                    elif 7 <= totalTraitorPlayers < 9:
                        numberOfTraitors = 2
                        traitorStart = 1
                    elif totalTraitorPlayers == 9:
                        numberOfTraitors = 3
                        traitorStart = 1

                    select_traitors = [traitor1,traitor2,traitor3,traitor4,traitor5,traitor6,traitor7,traitor8,traitor9]

                    loops = 0
                    while loops <= 9:
                        for i in select_traitors:
                            if i == 'Open':
                                await bot.send_message(message.channel, i)
                                select_traitors.remove(i)
                                loops += 1

                                await bot.send_message(message.channel, select_traitors)

                            else:
                                loops = 10


                    else:




                        if numberOfTraitors >= 1:
                            chosen_traitor_1 = random.choice(select_traitors)
                            await bot.send_message(message.channel, "TEST:" + chosen_traitor_1)
                            #if chosen_traitor_1 in select_traitors:
                                #await bot.send_message(message.channel, "Test 2")
                            select_traitors.remove(chosen_traitor_1)

                        #Traitors have been set








        if message.content.upper().startswith("-DICELUCK RULES"):
            if message.channel.id == bot_spam_channel_id:
                await bot.send_message(message.channel, diceluckInstructions)
                await bot.send_message(message.channel, diceluckRules)

        if message.content.upper().startswith("-DICELUCK JOIN") or message.content.upper().startswith("-DL JOIN"):
            global player1name
            global player2name
            global player3name
            global totalplayers
            global starttestgame
            global playersTurn
            global roll1
            global roll2
            global roll3
            global roll4
            global roll5
            global currentTotal
            global player1total
            global player2total
            global player3total
            global numbOfDice
            global diceluckGoal


            pID = message.author.id
            with open('achievements.json') as achievements:
                a = json.load(achievements)

            for achievement in a['achievements']:
                if achievement['name'] == 'Gaming Nub':
                    achievement_won = False
                    for id in achievement['players']:
                        if id == pID:
                            achievement_won = True

                    if achievement_won == False:
                        achievement['players'] += [(pID)]
                        await bot.send_message(message.author, "You just earned the achievement: **Gaming Nub**!")

            with open('achievements.json','w') as achievements:
                json.dump(a,achievements,indent=4)


            if message.channel.id == bot_spam_channel_id:
                if starttestgame == 1:
                    await bot.send_message(message.channel, "Please wait for the current game to finish.")
                elif player1name == 0:
                    if message.author.nick != None:
                        player1name = message.author.nick
                    else:
                        player1name = message.author.name
                    totalplayers += 1
                    await bot.send_message(message.channel, "**" + player1name + "** has joined, and is player one!")
                elif player2name == 0:
                    if message.author.nick != None:
                        player2name = message.author.nick
                    else:
                        player2name = message.author.name
                    totalplayers += 1
                    await bot.send_message(message.channel, "**" + player2name + "** has joined, and is player two!")
                elif player3name == 0:
                    if message.author.nick != None:
                        player3name = message.author.nick
                    else:
                        player3name = message.author.name
                    totalplayers += 1
                    await bot.send_message(message.channel, "**" + player3name + "** has joined, and is player three!")
                else:
                    await bot.send_message(message.channel, "Sorry, but no more players can join at this time.")

                await bot.send_message(message.channel, "You can set a goal between 100 and 1000 with `-DL Goal <number>`, and the current goal is **" + str(diceluckGoal) + "**")

                if totalplayers == 1:
                    await bot.send_message(message.channel, "You need at least one more player to start!")
                if totalplayers == 2:
                    await bot.send_message(message.channel, "If you two are the only players who want to play, type `-DL Start`")
                if totalplayers == 3:
                    await bot.send_message(message.channel, "No more players can join, please type `-DL Start`")

        if message.content.upper().startswith("-DL LEAVE"):
            global dlQuitterID
            dlQuitterID = message.author.id
            if message.channel.id == bot_spam_channel_id:
                if message.author.nick != None:
                    leaver = message.author.nick
                else:
                    leaver = message.author.name
                if leaver == player1name:
                    dlQuitterID = message.author.id
                    check_achievements = True
                    await bot.send_message(message.channel, "**" + leaver + "** has left the game.")

                    with open('stats.json') as stats:
                        lines = json.load(stats)

                    for player in lines['players']:
                        if player['id'] == dlQuitterID:
                            player['quits'] += 1
                            player['points'] -= 10
                            pID = message.author.id
                            with open('achievements.json') as achievements:
                                a = json.load(achievements)

                            for achievement in a['achievements']:
                                if achievement['name'] == 'Certified Quitter':
                                    #await bot.send_message(message.channel, "Testing Ach.")
                                    if player['quits'] >= 30:
                                        achievement_won = False
                                        for id in achievement['players']:
                                            if id == pID:
                                                achievement_won = True

                                        if achievement_won == False:
                                            achievement['players'] += [(pID)]
                                            await bot.send_message(message.author, "You just earned the achievement: **Certified Quitter**!")

                            with open('achievements.json','w') as achievements:
                                json.dump(a,achievements,indent=4)


                    with open('stats.json','w') as stats:
                        json.dump(lines, stats, indent=4)

                    player1name = 0
                    totalplayers -= 1
                    if totalplayers == 1:
                        starttestgame = 0
                        if player2name != 0:
                            await bot.send_message(message.channel, "**" + player2name + "** wins by default. A new game is ready to be played!")
                            player2name = 0
                        elif player3name != 0:
                            await bot.send_message(message.channel, "**" + player3name + "** wins by default. A new game is ready to be played!")
                            player3name = 0

                    else:
                        if player2name != 0:
                            playersTurn = player2name
                            await bot.send_message(message.channel, "**" + player2name + "** may take their turn now.")
                        elif player3name != 0:
                            playersTurn = player3name
                            await bot.send_message(message.channel, "**" + player3name + "** may take their turn now.")

                elif leaver == player2name:
                    dlQuitterID = message.author.id
                    check_achievements = True
                    await bot.send_message(message.channel, "**" + leaver + "** has left the game.")

                    with open('stats.json') as stats:
                        lines = json.load(stats)

                    for player in lines['players']:
                        if player['id'] == dlQuitterID:
                            player['quits'] += 1
                            player['points'] -= 10
                            pID = message.author.id
                            with open('achievements.json') as achievements:
                                a = json.load(achievements)

                            for achievement in a['achievements']:
                                if achievement['name'] == 'Certified Quitter':
                                    #await bot.send_message(message.channel, "Testing Ach.")
                                    if player['quits'] >= 30:
                                        achievement_won = False
                                        for id in achievement['players']:
                                            if id == pID:
                                                achievement_won = True

                                        if achievement_won == False:
                                            achievement['players'] += [(pID)]
                                            await bot.send_message(message.author, "You just earned the achievement: **Certified Quitter**!")

                            with open('achievements.json','w') as achievements:
                                json.dump(a,achievements,indent=4)


                    with open('stats.json','w') as stats:
                        json.dump(lines, stats, indent=4)

                    player2name = 0
                    totalplayers -= 1
                    if totalplayers == 1:
                        starttestgame = 0
                        if player1name != 0:
                            await bot.send_message(message.channel, "**" + player1name + "** wins by default. A new game is ready to be played!")
                            player1name = 0
                        elif player3name != 0:
                            await bot.send_message(message.channel, "**" + player3name + "** wins by default. A new game is ready to be played!")
                            player3name = 0

                    else:
                        if player3name != 0:
                            playersTurn = player3name
                            await bot.send_message(message.channel, "**" + player3name + "** may take their turn now.")
                        elif player1name != 0:
                            playersTurn = player1name
                            await bot.send_message(message.channel, "**" + player1name + "** may take their turn now.")

                elif leaver == player3name:
                    dlQuitterID = message.author.id
                    check_achievements = True
                    await bot.send_message(message.channel, "**" + leaver + "** has left the game.")

                    with open('stats.json') as stats:
                        lines = json.load(stats)

                    for player in lines['players']:
                        if player['id'] == dlQuitterID:
                            player['quits'] += 1
                            player['points'] -= 10
                            pID = message.author.id
                            with open('achievements.json') as achievements:
                                a = json.load(achievements)

                            for achievement in a['achievements']:
                                if achievement['name'] == 'Certified Quitter':
                                    #await bot.send_message(message.channel, "Testing Ach.")
                                    if player['quits'] >= 30:
                                        achievement_won = False
                                        for id in achievement['players']:
                                            if id == pID:
                                                achievement_won = True

                                        if achievement_won == False:
                                            achievement['players'] += [(pID)]
                                            await bot.send_message(message.author, "You just earned the achievement: **Certified Quitter**!")

                            with open('achievements.json','w') as achievements:
                                json.dump(a,achievements,indent=4)


                    with open('stats.json','w') as stats:
                        json.dump(lines, stats, indent=4)

                    player3name = 0
                    totalplayers -= 1
                    if totalplayers == 1:
                        starttestgame = 0
                        if player2name != 0:
                            await bot.send_message(message.channel, "**" + player2name + "** wins by default. A new game is ready to be played!")
                            player2name = 0
                        elif player1name != 0:
                            await bot.send_message(message.channel, "**" + player1name + "** wins by default. A new game is ready to be played!")
                            player1name = 0

                    else:
                        if player1name != 0:
                            playersTurn = player1name
                            await bot.send_message(message.channel, "**" + player1name + "** may take their turn now.")
                        elif player2name != 0:
                            playersTurn = player2name
                            await bot.send_message(message.channel, "**" + player2name + "** may take their turn now.")

                else:
                    await bot.send_message(message.channel, "You are not in this game **" + leaver + "**")

        if message.content.upper().startswith("-DL RESET"):
            if message.channel.id == bot_spam_channel_id:
                resetterRoles = message.author.roles
                for role in resetterRoles:
                    if role.id == "390624920360714240":
                        if message.author.nick != None:
                            resetter = message.author.nick
                        else:
                            resetter = message.author.name
                        await bot.send_message(message.channel, "Authorized. Reseting DiceLuck. . .")
                        player1name = 0
                        player2name = 0
                        player3name = 0
                        starttestgame = 0
                        totalplayers = 0
                        roll1 = 0
                        roll2 = 0
                        roll3 = 0
                        roll4 = 0
                        roll5 = 0
                        keepRole = 0
                        playersTurn = 0
                        keepRoll = 0
                        player1total = 0
                        player2total = 0
                        player3total = 0
                        numbOfDice = 5
                        diceluckGoal = 300
                        await bot.send_message(message.channel, "DiceLuck has been reset **" + resetter + "**!")


        if message.content.upper().startswith("-DL START"):
            if message.channel.id == bot_spam_channel_id:
                if starttestgame == 1:
                    await bot.send_message(message.channel, "A game is already in progress. Please wait for this game to finish before starting a new game.")
                elif totalplayers >= 2:
                    starttestgame = 1
                    await bot.send_message(message.channel, "Welcome to DiceLuck!")
                    await bot.send_message(message.channel, diceluckInstructions + diceluckRules)
                    playersTurn = player1name
                    await bot.send_message(message.channel, "**" + playersTurn + "** may begin. use the command `-DL Roll` to take your turn.")
                else:
                    await bot.send_message(message.channel, "You need at lease two players to play this game!")


        if message.content.upper().startswith("-DL ROLL"):
            if message.channel.id == bot_spam_channel_id:
                if message.author.nick != None:
                    roller = message.author.nick
                else:
                    roller = message.author.name
                if roller == playersTurn:
                    global currentRoll
                    global lastRoll
                    dicesides = [(1,":one:"), (2,":two:"), (3,":three:"), (4,":four:"), (5,":five:"), (6,":six:")]
                    if numbOfDice == 0:
                        numbOfDice == 5
                    if numbOfDice >= 1:
                        roll1 = random.choice(dicesides)
                        if numbOfDice >= 2:
                            roll2 = random.choice(dicesides)
                            if numbOfDice >= 3:
                                roll3 = random.choice(dicesides)
                                if numbOfDice >= 4:
                                    roll4 = random.choice(dicesides)
                                    if numbOfDice == 5:
                                        roll5 = random.choice(dicesides)
                                    else:
                                        roll5 = (0, ":record_button:")
                                else:
                                    roll4 = (0, ":record_button:")
                                    roll5 = (0, ":record_button:")
                            else:
                                roll3 = (0, ":record_button:")
                                roll4 = (0, ":record_button:")
                                roll5 = (0, ":record_button:")
                        else:
                            roll2 = (0, ":record_button:")
                            roll3 = (0, ":record_button:")
                            roll4 = (0, ":record_button:")
                            roll5 = (0, ":record_button:")


                    await bot.send_message(message.channel, roll1[1] + roll2[1] + roll3[1] + roll4[1] + roll5[1])
                    rolledNumbs = [roll1[0],roll2[0],roll3[0],roll4[0],roll5[0]]

                    numbOfZeros = 0
                    numbOfOnes = 0
                    numbOfTwos = 0
                    numbOfThrees = 0
                    numbOfFours = 0
                    numbOfFives = 0
                    numbOfSixs = 0
                    for number in rolledNumbs:
                        if number == 0:
                            numbOfZeros += 1
                        if number == 1:
                            numbOfOnes += 1
                        if number == 2:
                            numbOfTwos += 1
                        if number == 3:
                            numbOfThrees += 1
                        if number == 4:
                            numbOfFours += 1
                        if number == 5:
                            numbOfFives += 1
                        if number == 6:
                            numbOfSixs += 1

                    if numbOfOnes >= 3:
                        currentTotal += 100
                        numbOfOnes -= 3
                        numbOfDice -= 3
                    if numbOfTwos >= 3:
                        currentTotal += 20
                        numbOfTwos -= 3
                        numbOfDice -= 3
                    if numbOfThrees >= 3:
                        currentTotal += 30
                        numbOfThrees -= 3
                        numbOfDice -= 3
                    if numbOfFours >= 3:
                        currentTotal += 40
                        numbOfFours -= 3
                        numbOfDice -= 3
                    if numbOfFives >= 3:
                        currentTotal += 50
                        numbOfFives -= 3
                        numbOfDice -= 3
                    if numbOfSixs >= 3:
                        currentTotal += 60
                        numbOfSixs -= 3
                        numbOfDice -= 3
                    if numbOfOnes == 1:
                        currentTotal += 10
                        numbOfOnes -= 1
                        numbOfDice -= 1
                    if numbOfOnes == 2:
                        currentTotal += 20
                        numbOfOnes -= 2
                        numbOfDice -= 2
                    if numbOfFives == 1:
                        currentTotal += 5
                        numbOfFives -= 1
                        numbOfDice -= 1
                    if numbOfFives == 2:
                        currentTotal += 10
                        numbOfFives -= 2
                        numbOfDice -= 2
                    if numbOfDice == 0:
                        numbOfDice += 5


                    numbOfZeros = 0
                    numbOfOnes = 0
                    numbOfTwos = 0
                    numbOfThrees = 0
                    numbOfFours = 0
                    numbOfFives = 0
                    numbOfSixs = 0

                    if player1total >= diceluckGoal or player2total >= diceluckGoal or player3total >= diceluckGoal:
                        if player1total >= diceluckGoal:
                            dlwinTotal = player1total
                            dlWinner = player1name
                        elif player2total >= diceluckGoal:
                            dlwinTotal = player2total
                            dlWinner = player2name
                        elif player3total >= diceluckGoal:
                            dlwinTotal = player3total
                            dlWinner = player3name
                        await bot.send_message(message.channel, "Congragulations **" + dlWinner + "**! You win with a score of **" + str(dlwinTotal) + "**.")
                        totalplayers = 0
                        player1name = 0
                        player2name = 0
                        player3name = 0
                        starttestgame = 0
                        roll1 = 0
                        roll2 = 0
                        roll3 = 0
                        roll4 = 0
                        roll5 = 0
                        keepRoll = 0
                        playersTurn = 0
                        currentRoll = 0
                        lastRoll = 0
                        currentTotal = 0
                        player1total = 0
                        player2total = 0
                        player3total = 0
                        numbOfDice = 5
                        diceluckGoal = 300

                    elif lastRoll == currentTotal:
                        currentTotal = 0
                        lastRoll = 0
                        numbOfDice = 5
                        if roller == player1name:
                            if player2name != 0:
                                playersTurn = player2name
                            else:
                                playersTurn = player3name

                        elif roller == player2name:
                            if player3name != 0:
                                playersTurn = player3name
                            else:
                                playersTurn = player1name

                        elif roller == player3name:
                            if player1name != 0:
                                playersTurn = player1name
                            else:
                                playersTurn = player2name

                        await bot.send_message(message.channel, "Sorry, you lost this roll! Next up, **" + playersTurn + "**. Use `-DL Roll` to begin your turn!")
                    else:
                        lastRoll = currentTotal
                        if playersTurn == player1name:
                            possibleTotal = player1total + currentTotal
                        elif playersTurn == player2name:
                            possibleTotal = player2total + currentTotal
                        elif playersTurn == player3name:
                            possibleTotal = player3total + currentTotal
                        await bot.send_message(message.channel, "Your score for this turn: **" + str(currentTotal) + "**")
                        await bot.send_message(message.channel, "If you do `-DL Keep`: **" + str(possibleTotal) + "**")
                        await bot.send_message(message.channel, "Dice you can roll on your next turn: **" + str(numbOfDice) + "**")
                        await bot.send_message(message.channel, "Would you like to keep your score, or roll again for more? Use `-DL Keep` or `-DL Roll`")




                else:
                    await bot.send_message(message.channel, "Please wait your turn if you are playing, and if you aren't, don't try to mess with the game in progress or start a new game if one isn't being played.")


        if message.content.upper().startswith("-DL KEEP"):
            keeper_id = message.author.id
            if message.channel.id == bot_spam_channel_id:
                if message.author.nick != None:
                    keeper = message.author.nick
                else:
                    keeper = message.author.name
                if keeper == playersTurn:
                    if playersTurn == player1name or playersTurn == player2name or playersTurn == player3name:
                        if playersTurn == player1name:
                            player1total += currentTotal
                            if player1total >= diceluckGoal or player2total >= diceluckGoal or player3total >= diceluckGoal:
                                if player1total >= diceluckGoal:
                                    dlwinTotal = player1total
                                    dlWinner = player1name
                                if player2total >= diceluckGoal:
                                    dlwinTotal = player2total
                                    dlWinner = player2name
                                if player3total >= diceluckGoal:
                                    dlwinTotal = player3total
                                    dlWinner = player3name



                                with open('stats.json') as stats:
                                    lines = json.load(stats)

                                for player in lines['players']:
                                    if player['id'] == keeper_id:
                                        player['dlWins'] += 1
                                        player['points'] += 20*player['booster']
                                        pID = message.author.id
                                        with open('achievements.json') as achievements:
                                            a = json.load(achievements)

                                        for achievement in a['achievements']:
                                            if achievement['name'] == "Know when to Hold'em":
                                                #await bot.send_message(message.channel, "Testing Ach.")
                                                if player['dlWins'] >= 10:
                                                    achievement_won = False
                                                    for id in achievement['players']:
                                                        if id == pID:
                                                            achievement_won = True

                                                    if achievement_won == False:
                                                        achievement['players'] += [(pID)]
                                                        await bot.send_message(message.author, "You just earned the achievement: **Know when to Hold'em**!")

                                        with open('achievements.json','w') as achievements:
                                            json.dump(a,achievements,indent=4)

                                with open('stats.json','w') as stats:
                                    json.dump(lines, stats, indent=4)


                                dlWinnerID = message.author.id
                                check_achievements = True

                                await bot.send_message(message.channel, "Congragulations **" + dlWinner + "**! You win with a score of **" + str(dlwinTotal) + "**.")
                                totalplayers = 0
                                player1name = 0
                                player2name = 0
                                player3name = 0
                                starttestgame = 0
                                roll1 = 0
                                roll2 = 0
                                roll3 = 0
                                roll4 = 0
                                roll5 = 0
                                keepRoll = 0
                                playersTurn = 0
                                currentRoll = 0
                                lastRoll = 0
                                currentTotal = 0
                                player1total = 0
                                player2total = 0
                                player3total = 0
                                numbOfDice = 5
                                diceluckGoal = 300
                            if player2name != 0:
                                playersTurn = player2name
                            else:
                                playersTurn = player3name
                            await bot.send_message(message.channel, "Your score is now **" + str(player1total) + "**! Next up is **" + playersTurn + "**. Would you like to take a chance with the leftover dice, or start from scratch? Use `-DL Roll` to take a chance, or `-DL No` to start from scratch.")

                        elif playersTurn == player2name:
                            player2total += currentTotal
                            if player1total >= diceluckGoal or player2total >= diceluckGoal or player3total >= diceluckGoal:
                                if player1total >= diceluckGoal:
                                    dlwinTotal = player1total
                                    dlWinner = player1name
                                if player2total >= diceluckGoal:
                                    dlwinTotal = player2total
                                    dlWinner = player2name
                                if player3total >= diceluckGoal:
                                    dlwinTotal = player3total
                                    dlWinner = player3name



                                with open('stats.json') as stats:
                                    lines = json.load(stats)

                                for player in lines['players']:
                                    if player['id'] == keeper_id:
                                        player['dlWins'] += 1
                                        player['points'] += 20*player['booster']
                                        pID = message.author.id
                                        with open('achievements.json') as achievements:
                                            a = json.load(achievements)

                                        for achievement in a['achievements']:
                                            if achievement['name'] == "Know when to Hold'em":
                                                #await bot.send_message(message.channel, "Testing Ach.")
                                                if player['dlWins'] >= 10:
                                                    achievement_won = False
                                                    for id in achievement['players']:
                                                        if id == pID:
                                                            achievement_won = True

                                                    if achievement_won == False:
                                                        achievement['players'] += [(pID)]
                                                        await bot.send_message(message.author, "You just earned the achievement: **Know when to Hold'em**!")

                                        with open('achievements.json','w') as achievements:
                                            json.dump(a,achievements,indent=4)


                                with open('stats.json','w') as stats:
                                    json.dump(lines, stats, indent=4)


                                dlWinnerID = message.author.id
                                check_achievements = True

                                await bot.send_message(message.channel, "Congragulations **" + dlWinner + "**! You win with a score of **" + str(dlwinTotal) + "**.")
                                totalplayers = 0
                                player1name = 0
                                player2name = 0
                                player3name = 0
                                starttestgame = 0
                                roll1 = 0
                                roll2 = 0
                                roll3 = 0
                                roll4 = 0
                                roll5 = 0
                                keepRoll = 0
                                playersTurn = 0
                                currentRoll = 0
                                lastRoll = 0
                                currentTotal = 0
                                player1total = 0
                                player2total = 0
                                player3total = 0
                                numbOfDice = 5
                                diceluckGoal = 300
                            if player3name != 0:
                                playersTurn = player3name
                            else:
                                playersTurn = player1name
                            await bot.send_message(message.channel, "Your score is now **" + str(player2total) + "**! Next up is **" + playersTurn + "**. Would you like to take a chance with the leftover dice, or start from scratch? Use `-DL Roll` to take a chance, or `-DL No` to start from scratch.")

                        elif playersTurn == player3name:
                            player3total += currentTotal
                            if player1total >= diceluckGoal or player2total >= diceluckGoal or player3total >= diceluckGoal:
                                if player1total >= diceluckGoal:
                                    dlwinTotal = player1total
                                    dlWinner = player1name
                                if player2total >= diceluckGoal:
                                    dlwinTotal = player2total
                                    dlWinner = player2name
                                if player3total >= diceluckGoal:
                                    dlwinTotal = player3total
                                    dlWinner = player3name



                                with open('stats.json') as stats:
                                    lines = json.load(stats)

                                for player in lines['players']:
                                    if player['id'] == keeper_id:
                                        player['dlWins'] += 1
                                        player['points'] += 20*player['booster']
                                        pID = message.author.id
                                        with open('achievements.json') as achievements:
                                            a = json.load(achievements)

                                        for achievement in a['achievements']:
                                            if achievement['name'] == "Know when to Hold'em":
                                                #await bot.send_message(message.channel, "Testing Ach.")
                                                if player['dlWins'] >= 10:
                                                    achievement_won = False
                                                    for id in achievement['players']:
                                                        if id == pID:
                                                            achievement_won = True

                                                    if achievement_won == False:
                                                        achievement['players'] += [(pID)]
                                                        await bot.send_message(message.author, "You just earned the achievement: **Know when to Hold'em**!")

                                        with open('achievements.json','w') as achievements:
                                            json.dump(a,achievements,indent=4)


                                with open('stats.json','w') as stats:
                                    json.dump(lines, stats, indent=4)


                                dlWinnerID = message.author.id
                                check_achievements = True

                                await bot.send_message(message.channel, "Congragulations **" + dlWinner + "**! You win with a score of **" + str(dlwinTotal) + "**.")
                                totalplayers = 0
                                player1name = 0
                                player2name = 0
                                player3name = 0
                                starttestgame = 0
                                roll1 = 0
                                roll2 = 0
                                roll3 = 0
                                roll4 = 0
                                roll5 = 0
                                keepRoll = 0
                                playersTurn = 0
                                currentRoll = 0
                                lastRoll = 0
                                currentTotal = 0
                                player1total = 0
                                player2total = 0
                                player3total = 0
                                numbOfDice = 5
                                diceluckGoal = 300
                            if player1name != 0:
                                playersTurn = player1name
                            else:
                                playersTurn = player2name
                            await bot.send_message(message.channel, "Your score is now **" + str(player3total) + "**! Next up is **" + playersTurn + "**. Would you like to take a chance with the leftover dice, or start from scratch? Use `-DL Roll` to take a chance, or `-DL No` to start from scratch.")


                        else:
                            await bot.send_message(message.channel, "Are you even in a game **" + message.author.name + "**?")


                else:
                    await bot.send_message(message.channel, "If it isn't your turn or you aren't in this game, please don't try to interfere.")

        if message.content.upper().startswith("-DL NO"):
            if message.channel.id == bot_spam_channel_id:
                if message.author.nick != None:
                    nextRoller = message.author.nick
                else:
                    nextRoller = message.author.name
                if nextRoller == playersTurn:
                    numbOfDice = 5
                    currentTotal = 0
                    await bot.send_message(message.channel, "Use `-DL Roll` to take your turn now.")
                else:
                    await bot.send_message(message.channel, "If it isn't your turn or you aren't in this game, please don't try to interfere.")

        if message.content.upper().startswith("-DL GOAL"):
            if message.channel.id == bot_spam_channel_id:
                if message.author.nick != None:
                    goaler = message.author.nick
                else:
                    goaler = message.author.name
                dlArgs = message.content.split(" ")
                goalArg = int(dlArgs[2])
                if starttestgame == 0:
                    if goaler == player1name or goaler == player2name or goaler == player3name:
                        if 100 <= goalArg <= 1000:
                            diceluckGoal = goalArg
                            await bot.send_message(message.channel, "The goal for this game has been set to **" + str(diceluckGoal) + "** by **" + goaler + "**!")
                        else:
                            await bot.send_message(message.channel, "Please set a reasonable goal between 100 and 1000")
                    else:
                        await bot.send_message(message.channel, "You are not qued in the game.")
                else:
                    await bot.send_message(message.channel, "The game is already in progress, the goal cannot be changed.")

        if message.content.upper().startswith("-DL SCORE"):
            if message.channel.id == bot_spam_channel_id:
                if starttestgame == 1:
                    if player1name == 0:
                        await bot.send_message(message.channel, "**" + player2name + "** has " + str(player2total) + " points and **" + player3name + "** has " + str(player3total) + " points!")
                    if player2name == 0:
                        await bot.send_message(message.channel, "**" + player1name + "** has " + str(player1total) + " points and **" + player3name + "** has " + str(player3total) + " points!")
                    if player3name == 0:
                        await bot.send_message(message.channel, "**" + player1name + "** has " + str(player1total) + " points and **" + player3name + "** has " + str(player3total) + " points!")
                    else:
                        await bot.send_message(message.channel, "**" + player1name + "** has " + str(player1total) + " points, **" + player2name + "** has " + str(player2total) + " points, and **" + player3name + "** has " + str(player3total) + " points!")
                else:
                    await bot.send_message(message.channel, "There is no game in progress.")


        #MASTERMIND GAME!!!
        if message.content.upper().startswith("-MASTERMIND"):
            global combo
            global mmplayer

            pID = message.author.id
            with open('achievements.json') as achievements:
                a = json.load(achievements)

            for achievement in a['achievements']:
                if achievement['name'] == 'Gaming Nub':
                    achievement_won = False
                    for id in achievement['players']:
                        if id == pID:
                            achievement_won = True

                    if achievement_won == False:
                        achievement['players'] += [(pID)]
                        await bot.send_message(message.author, "You just earned the achievement: **Gaming Nub**!")

            with open('achievements.json','w') as achievements:
                json.dump(a,achievements,indent=4)

            if message.channel.id == bot_spam_channel_id:
                if mmplayer != 0:
                    await bot.send_message(message.channel, "Please wait until the current game is finished")
                else:
                    if message.author.nick != 0:
                        mmplayer = message.author.nick
                    elif message.author.nick == 0:
                        mmplayer = message.author.name
                    numbs = ["1", "2", "3", "4", "5", "6"]
                    n1 = random.choice(numbs)
                    n2 = random.choice(numbs)
                    n3 = random.choice(numbs)
                    combo = n1 + n2 + n3
                    await bot.send_message(message.channel, "Guess the three numbers in the correct order. You have six attempts, and the numbers range from one to six. Good luck!")
                    await bot.send_message(message.channel, "The following symbols indicate whether you have a correct number in the correct position, a correct number in the incorrect position, and/or an incorrect number.")
                    await bot.send_message(message.channel, """:black_large_square: : Incorrect Number
    :white_square_button: : Correct Number, Wrong position
    :white_large_square: : Correct Number, Correct Position""")
                    await bot.send_message(message.channel, "NOTE: The order of the bot's responces to your guesses do not line up to show you which numbers are correct. They only show you if any of them are correct in no specific order!")

        if message.content.upper().startswith("-MM"):
            global mmID
            if message.channel.id == bot_spam_channel_id:
                if message.author.nick != 0:
                    mmMessager = message.author.nick
                elif message.author.nick == 0:
                    mmMessager = message.author.name
                if combo == 0:
                    await bot.send_message(message.channel, "Please start a new game with -MasterMind")
                else:
                    if mmMessager == mmplayer:
                        global guessNum
                        guessNum += 1
                        args = message.content.split(" ")
                        newargs = str(args[1])
                        if newargs == combo:



                            with open('stats.json') as stats:
                                lines = json.load(stats)

                            for player in lines['players']:
                                if player['id'] == message.author.id:
                                    player['mmWins'] += 1
                                    player['points'] += 5*player['booster']
                                    pID = message.author.id
                                    with open('achievements.json') as achievements:
                                        a = json.load(achievements)

                                    for achievement in a['achievements']:
                                        if achievement['name'] == "Hacker!":
                                            #await bot.send_message(message.channel, "Testing Ach.")
                                            if player['mmWins'] >= 25:
                                                achievement_won = False
                                                for id in achievement['players']:
                                                    if id == pID:
                                                        achievement_won = True

                                                if achievement_won == False:
                                                    achievement['players'] += [(pID)]
                                                    await bot.send_message(message.author, "You just earned the achievement: **Hacker!**!")

                                        if achievement['name'] == "First Try!":
                                            if guessNum == 1:
                                                achievement_won = False
                                                for id in achievement['players']:
                                                    if id == pID:
                                                        achievement_won = True
                                                if achievement_won == False:
                                                    achievement['players'] += [(pID)]
                                                    await bot.send_message(message.author, "You just earned the achievement: **First Try!**!")


                                    with open('achievements.json','w') as achievements:
                                        json.dump(a,achievements,indent=4)

                            with open('stats.json','w') as stats:
                                json.dump(lines, stats, indent=4)

                            mmID = message.author.id

                            await bot.send_message(message.channel, ":white_large_square:" * 3)
                            await bot.send_message(message.channel, "You win! The answer was %s"%(combo))
                            if guessNum == 1:
                                resp = "1 guess!"
                            else:
                                resp = "%s guesses!"%(str(guessNum))
                            await bot.send_message(message.channel, "It took you %s"%(resp))
                            guessNum = 0
                            combo = 0
                            mmplayer = 0

                            check_achievements = True

                        sepnum = list(newargs)
                        setnumbs = list(combo)

                            #Calculate the matching numbers AND positions using THIS thing: calcMatches()
                        n1 = setnumbs[0]
                        n2 = setnumbs[1]
                        n3 = setnumbs[2]
                        m1 = sepnum[0]
                        m2 = sepnum[1]
                        m3 = sepnum[2]



                        totalExactMatches = 0
                        totalMatches = 0
                        nonMatches = 0

                            #Check if ANY numbers are equal first

                        if n1 == m1 or n1 == m2 or n1 == m3:
                            if n1 == m1:
                                totalExactMatches += 1
                            else:
                                totalMatches += 1
                        else:
                            nonMatches += 1

                        if n2 == m1 or n2 == m2 or n2 == m3:
                            if n2 == m2:
                                totalExactMatches += 1
                            else:
                                totalMatches += 1
                        else:
                            nonMatches += 1

                        if n3 == m1 or n3 == m2 or n3 == m3:
                            if n3 == m3:
                                totalExactMatches += 1
                            else:
                                totalMatches += 1
                        else:
                            nonMatches += 1


                        await bot.send_message(message.channel, ":white_large_square:" * totalExactMatches + ":white_square_button:" * totalMatches + ":black_large_square:" * nonMatches)


                        await bot.send_message(message.channel, "You have " + str(6 - int(guessNum)) + " guesses left!")
                        if guessNum >= 6:
                            await bot.send_message(message.channel, "Sorry, you're out of guesses! The answer was %s"%(combo))
                            guessNum = 0
                            combo = 0
                            mmplayer = 0




                    else:
                        await bot.send_message(message.channel, "You are not the current player. Please wait until **" + mmplayer + "** finishes his/her game.")

        if message.content.upper().startswith("-BOTHELP"):
            if message.channel.id == bot_spam_channel_id:
                other = message.content.upper()[9:]
                #await bot.send_message(message.channel, other)
                if other == "MATH":
                    BHmessage = MathHelp

                elif other == "DL" or other == "DICELUCK":
                    #await bot.send_message(message.channel, "TEST")
                    BHmessage = DiceLuckHelp
                    #await bot.send_message(message.channel, "TEST")

                else:
                    BHmessage = bothelpMessage
                #await bot.send_message(message.channel, "TEST")
                em = discord.Embed(title="BotHelp", description=BHmessage, colour=0xBCAD20)
                em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
                await bot.send_message(message.author,content=None, embed=em)
                await bot.add_reaction(message, "\N{Eyes}")

                #await bot.send_message(message.channel, """``````""")




        if message.content.upper().startswith("-TTT") or message.content.upper().startswith("-TICTACTOE"):
            global tttP1
            global tttP2
            global tttBlank
            global ttt1
            global ttt2
            global ttt3
            global ttt4
            global ttt5
            global ttt6
            global ttt7
            global ttt8
            global ttt9
            global tttStart
            global tttPTurn
            global tttRow1
            global tttRow2
            global tttRow3
            global tttBoard
            global tttTimer
            global tttTimerStop
            global when_to_stop
            global tttID
            if message.channel.id == bot_spam_channel_id:

                resetTTT = message.content.upper()[5:10]
                if resetTTT == "RESET":
                    tttP1 = 0
                    tttP2 = 0
                    ttt1 = tttBlank
                    ttt2 = tttBlank
                    ttt3 = tttBlank
                    ttt4 = tttBlank
                    ttt5 = tttBlank
                    ttt6 = tttBlank
                    ttt7 = tttBlank
                    ttt8 = tttBlank
                    ttt9 = tttBlank
                    tttWinner = 0
                    tttStart = 0
                    tttTimer = 0
                    when_to_stop = 0
                    tttTimerStop = 0
                    await bot.send_message(message.channel, "The game has been reset!")
                else:
                    #await bot.send_message(message.channel, "0"+resetTTT)
                    if message.author.nick == None:
                        tttJoiner = message.author.name
                    else:
                        tttJoiner = message.author.nick
                    if tttP1 == 0:
                        if tttJoiner != tttP2:
                            tttP1 = tttJoiner
                            tttTimer = 0
                            tttTime = 0
                            tttTimer = 1
                            await bot.send_message(message.channel, "Welcome to TicTacToe **" + tttP1 + "**!")

                            if tttP1 != 0 and tttP2 != 0:
                                tttStart = 1
                                await bot.send_message(message.channel, "Let's begin **" + tttP1 + "** and **" + tttP2 + "**!")
                                tttPlayers = [tttP1,tttP2]
                                tttPTurn = random.choice(tttPlayers)
                                await bot.send_message(message.channel, "**" + tttPTurn + "** may begin! Remember, use the numbers **1-9** to mark a position!" + tttLayout)
                                #SHOW THE BLANK BOARD HERE!!!

                    elif tttP2 == 0:
                        if tttJoiner != tttP1:
                            tttP2 = tttJoiner
                            tttTimer = 0
                            tttTime = 0
                            tttTimerStop = 1
                            when_to_stop = 0
                            await bot.send_message(message.channel, "Welcome to TicTacToe **" + tttP2 + "**!")

                            if tttP1 != 0 and tttP2 != 0:
                                tttStart = 1
                                await bot.send_message(message.channel, "Let's begin **" + tttP1 + "** and **" + tttP2 + "**!")
                                tttPlayers = [tttP1,tttP2]
                                tttPTurn = random.choice(tttPlayers)
                                await bot.send_message(message.channel, "**" + tttPTurn + "** may begin! Remember, use the numbers **1-9** to mark a position!" + tttLayout)
                                #SHOW THE BLANK BOARD HERE!!!

                    else:
                        await bot.send_message(message.channel, "Please wait for the current game to finish.")

                    #if tttTimer == 0:
                    #    tttTimer = 1
                    #    time.time()







        if tttTimer == 1:
            if tttTime == 0:
                #Time = time.sleep(5)



                when_to_stop = 30
                time_left_msg = await bot.send_message(message.channel, "Time left for another player to join: " + str(when_to_stop))

                while when_to_stop > 0:
                    if tttTimerStop == 0:
                        await bot.edit_message(time_left_msg, new_content="Time left for another player to join: " + str(when_to_stop))
                        when_to_stop -= 1
                        await asyncio.sleep(1)
                    else:
                        pass

                if tttTimerStop == 0:
                    tttTimer = 0
                    tttP1 = 0
                    tttP2 = 0
                    tttBlank = "black_medium_square"
                    ttt1 = tttBlank
                    ttt2 = tttBlank
                    ttt3 = tttBlank
                    ttt4 = tttBlank
                    ttt5 = tttBlank
                    ttt6 = tttBlank
                    ttt7 = tttBlank
                    ttt8 = tttBlank
                    ttt9 = tttBlank
                    tttWinner = 0
                    tttStart = 0
                    await bot.edit_message(time_left_msg, "TicTacToe que has timed out!")



        if message.content.upper().startswith("-C4") or message.content.upper().startswith("-CONNECT4"):
            if message.channel.id == bot_spam_channel_id:
                blankC4 = ":white_square_button:"
                redC4 = ":red_circle:"
                yellowC4 = ":large_orange_diamond:"
                global C4_player1
                global C4_player2
                global C4_start
                global C4_turn
                global col1
                global col2
                global col3
                global col4
                global col5
                global col6
                global col7
                global c4ID

                if message.author.nick == None:
                    C4Joiner = message.author.name
                else:
                    C4Joiner = message.author.nick

                if C4_start == 1:
                    await bot.send_message(message.channel, "A game of Connect4 is already in progress!")
                else:
                    if C4_player1 == 0:
                        C4_player1 = C4Joiner
                        await bot.send_message(message.channel, "One more player is needed to start!")
                    elif C4_player2 == 0:
                        if C4Joiner == C4_player1:
                            await bot.send_message(message.channel, "Please allow someone besides yourself to play with you.")
                        else:
                            C4_player2 = C4Joiner
                            C4_start = 1
                            C4_players = [C4_player1,C4_player2]
                            C4_turn = random.choice(C4_players)
                            await bot.send_message(message.channel, "Let's begin, shall we?\n**" + C4_turn + "** may start!")









        #TicTacToe & Connect4
        if message.content.upper().startswith("1") or message.content.upper().startswith("2") or message.content.upper().startswith("3") or message.content.upper().startswith("4") or message.content.upper().startswith("5") or message.content.upper().startswith("6") or message.content.upper().startswith("7") or message.content.upper().startswith("8") or message.content.upper().startswith("9"):
            if message.channel.id == bot_spam_channel_id:
                x1 = ":regional_indicator_x:"
                o1 = ":regional_indicator_o:"
                tttBlank = ":black_medium_square:"

                pID = message.author.id
                with open('achievements.json') as achievements:
                    a = json.load(achievements)

                for achievement in a['achievements']:
                    if achievement['name'] == 'Gaming Nub':
                        achievement_won = False
                        for id in achievement['players']:
                            if id == pID:
                                achievement_won = True

                        if achievement_won == False:
                            achievement['players'] += [(pID)]
                            await bot.send_message(message.author, "You just earned the achievement: **Gaming Nub**!")

                with open('achievements.json','w') as achievements:
                    json.dump(a,achievements,indent=4)

                #Checking if it's TicTacToe
                #IMPORTANT: CONNECT4 IS BELOW!!!


                if tttStart == 1:
                    #await bot.send_message(message.channel, "TEST")
                    if message.author.nick == None:
                        tttmessager = message.author.name
                    else:
                        tttmessager = message.author.nick

                    if tttmessager == tttPTurn:
                        tttNumber = str(message.content[0])
                        #await bot.send_message(message.channel, tttNumber)
                        if tttNumber == "1":
                            if ttt1 == tttBlank:
                                if tttPTurn == tttP1:
                                    ttt1 = x1
                                    tttTurnComplete = 1
                                elif tttPTurn == tttP2:
                                    ttt1 = o1
                                    tttTurnComplete = 1
                            else:
                                await bot.send_message(message.channel, "Please choose an available space")
                        elif tttNumber == "2":
                            if ttt2 == tttBlank:
                                if tttPTurn == tttP1:
                                    ttt2 = x1
                                    tttTurnComplete = 1
                                elif tttPTurn == tttP2:
                                    ttt2 = o1
                                    tttTurnComplete = 1
                            else:
                                await bot.send_message(message.channel, "Please choose an available space")
                        elif tttNumber == "3":
                            if ttt3 == tttBlank:
                                if tttPTurn == tttP1:
                                    ttt3 = x1
                                    tttTurnComplete = 1
                                elif tttPTurn == tttP2:
                                    ttt3 = o1
                                    tttTurnComplete = 1
                            else:
                                await bot.send_message(message.channel, "Please choose an available space")
                        elif tttNumber == "4":
                            if ttt4 == tttBlank:
                                if tttPTurn == tttP1:
                                    ttt4 = x1
                                    tttTurnComplete = 1
                                elif tttPTurn == tttP2:
                                    ttt4 = o1
                                    tttTurnComplete = 1
                            else:
                                await bot.send_message(message.channel, "Please choose an available space")
                        elif tttNumber == "5":
                            if ttt5 == tttBlank:
                                if tttPTurn == tttP1:
                                    ttt5 = x1
                                    tttTurnComplete = 1
                                elif tttPTurn == tttP2:
                                    ttt5 = o1
                                    tttTurnComplete = 1
                            else:
                                await bot.send_message(message.channel, "Please choose an available space")
                        elif tttNumber == "6":
                            if ttt6 == tttBlank:
                                if tttPTurn == tttP1:
                                    ttt6 = x1
                                    tttTurnComplete = 1
                                elif tttPTurn == tttP2:
                                    ttt6 = o1
                                    tttTurnComplete = 1
                            else:
                                await bot.send_message(message.channel, "Please choose an available space")
                        elif tttNumber == "7":
                            if ttt7 == tttBlank:
                                if tttPTurn == tttP1:
                                    ttt7 = x1
                                    tttTurnComplete = 1
                                elif tttPTurn == tttP2:
                                    ttt7 = o1
                                    tttTurnComplete = 1
                            else:
                                await bot.send_message(message.channel, "Please choose an available space")
                        elif tttNumber == "8":
                            if ttt8 == tttBlank:
                                if tttPTurn == tttP1:
                                    ttt8 = x1
                                    tttTurnComplete = 1
                                elif tttPTurn == tttP2:
                                    ttt8 = o1
                                    tttTurnComplete = 1
                            else:
                                await bot.send_message(message.channel, "Please choose an available space")
                        elif tttNumber == "9":
                            if ttt9 == tttBlank:
                                if tttPTurn == tttP1:
                                    ttt9 = x1
                                    tttTurnComplete = 1
                                elif tttPTurn == tttP2:
                                    ttt9 = o1
                                    tttTurnComplete = 1
                            else:
                                await bot.send_message(message.channel, "Please choose an available space")
                        else:
                            await bot.send_message(message.channel, "Didn't work: " + tttNumber + "-" + x1 + o1 + ttt1)


                        if ttt1 == ttt2 == ttt3 == x1 or ttt1 == ttt2 == ttt3 == o1 or ttt4 == ttt5 == ttt6 == x1 or ttt4 == ttt5 == ttt6 == o1 or ttt7 == ttt8 == ttt9 == x1 or ttt7 == ttt8 == ttt9 == o1 or ttt1 == ttt4 == ttt7 == x1 or ttt1 == ttt4 == ttt7 == o1 or ttt2 == ttt5 == ttt8 == x1 or ttt2 == ttt5 == ttt8 == o1 or ttt3 == ttt6 == ttt9 == x1 or ttt3 == ttt6 == ttt9 == o1 or ttt1 == ttt5 == ttt9 == x1 or ttt1 == ttt5 == ttt9 == o1 or ttt3 == ttt5 == ttt7 == x1 or ttt3 == ttt5 == ttt7 == o1:



                            with open('stats.json') as stats:
                                lines = json.load(stats)

                            for player in lines['players']:
                                if player['id'] == message.author.id:
                                    player['tttWins'] += 1
                                    player['points'] += 3*player['booster']


                                    pID = message.author.id
                                    with open('achievements.json') as achievements:
                                        a = json.load(achievements)

                                    for achievement in a['achievements']:
                                        if achievement['name'] == 'First Blood':
                                            achievement_won = False
                                            for id in achievement['players']:
                                                if id == pID:
                                                    achievement_won = True

                                            if achievement_won == False:
                                                achievement['players'] += [(pID)]
                                                await bot.send_message(message.author, "You just earned the achievement: **First Blood**!")

                                    with open('achievements.json','w') as achievements:
                                        json.dump(a,achievements,indent=4)





                            with open('stats.json','w') as stats:
                                json.dump(lines, stats, indent=4)




                            tttWinner = tttPTurn
                        elif ttt1 != tttBlank and ttt2 != tttBlank and ttt3 != tttBlank and ttt4 != tttBlank and ttt5 != tttBlank and ttt6 != tttBlank and ttt7 != tttBlank and ttt8 != tttBlank and ttt9 != tttBlank:
                            tttWinner = "No one"


                        if tttTurnComplete == 1:
                            if tttPTurn == tttP1:
                                tttPTurn = tttP2
                            elif tttPTurn == tttP2:
                                tttPTurn = tttP1
                        tttTurnComplete = 0

                        tttRow1 = ttt1+ttt2+ttt3
                        tttRow2 = ttt4+ttt5+ttt6
                        tttRow3 = ttt7+ttt8+ttt9
                        tttBoard = tttRow1 + """
    """ + tttRow2 + """
    """ + tttRow3

                        em = discord.Embed(title="TicTacToe", description=tttBoard,colour=0xBCAD20)
                        em.set_author(name=message.author.name, icon_url=message.author.avatar_url)
                        await bot.send_message(message.channel, content=None, embed=em)

                        if tttWinner != 0:

                            tttID = message.author.id

                            await bot.send_message(message.channel, "**%s** wins! Another game is ready to be played!"%(tttWinner))
                            tttP1 = 0
                            tttP2 = 0
                            ttt1 = tttBlank
                            ttt2 = tttBlank
                            ttt3 = tttBlank
                            ttt4 = tttBlank
                            ttt5 = tttBlank
                            ttt6 = tttBlank
                            ttt7 = tttBlank
                            ttt8 = tttBlank
                            ttt9 = tttBlank
                            tttWinner = 0
                            tttStart = 0
                            tttTime = 0
                            tttTimer = 0
                            tttTimerStop = 0


                #CONNECT4 STARTS HERE
                if C4_start == 1:
                    if message.author.nick == None:
                        C4player = message.author.name
                    else:
                        C4player = message.author.nick
                    if C4player == C4_turn:

                        blankC4 = ":white_square_button:"
                        redC4 = ":red_circle:"
                        yellowC4 = ":large_orange_diamond:"
                        if C4_turn == C4_player1:
                            coinC4 = redC4
                        elif C4_turn == C4_player2:
                            coinC4 = yellowC4

                        C4number = str(message.content[0])

                        if C4number == "1":
                            if col1[5] != blankC4:
                                if col1[4] != blankC4:
                                    if col1[3] != blankC4:
                                        if col1[2] != blankC4:
                                            if col1[1] != blankC4:
                                                if col1[0] != blankC4:
                                                    await bot.send_message(message.channel, "Please choose an available column")
                                                else:
                                                    col1[0] = coinC4
                                                    if C4_turn == C4_player1:
                                                        C4_turn = C4_player2
                                                    elif C4_turn == C4_player2:
                                                        C4_turn = C4_player1
                                            else:
                                                col1[1] = coinC4
                                                if C4_turn == C4_player1:
                                                    C4_turn = C4_player2
                                                elif C4_turn == C4_player2:
                                                    C4_turn = C4_player1
                                        else:
                                            col1[2] = coinC4
                                            if C4_turn == C4_player1:
                                                C4_turn = C4_player2
                                            elif C4_turn == C4_player2:
                                                C4_turn = C4_player1
                                    else:
                                        col1[3] = coinC4
                                        if C4_turn == C4_player1:
                                            C4_turn = C4_player2
                                        elif C4_turn == C4_player2:
                                            C4_turn = C4_player1
                                else:
                                    col1[4] = coinC4
                                    if C4_turn == C4_player1:
                                        C4_turn = C4_player2
                                    elif C4_turn == C4_player2:
                                        C4_turn = C4_player1
                            else:
                                col1[5] = coinC4
                                if C4_turn == C4_player1:
                                    C4_turn = C4_player2
                                elif C4_turn == C4_player2:
                                    C4_turn = C4_player1

                        elif C4number == "2":
                            if col2[5] != blankC4:
                                if col2[4] != blankC4:
                                    if col2[3] != blankC4:
                                        if col2[2] != blankC4:
                                            if col2[1] != blankC4:
                                                if col2[0] != blankC4:
                                                    await bot.send_message(message.channel, "Please choose an available column")
                                                else:
                                                    col2[0] = coinC4
                                                    if C4_turn == C4_player1:
                                                        C4_turn = C4_player2
                                                    elif C4_turn == C4_player2:
                                                        C4_turn = C4_player1
                                            else:
                                                col2[1] = coinC4
                                                if C4_turn == C4_player1:
                                                    C4_turn = C4_player2
                                                elif C4_turn == C4_player2:
                                                    C4_turn = C4_player1
                                        else:
                                            col2[2] = coinC4
                                            if C4_turn == C4_player1:
                                                C4_turn = C4_player2
                                            elif C4_turn == C4_player2:
                                                C4_turn = C4_player1
                                    else:
                                        col2[3] = coinC4
                                        if C4_turn == C4_player1:
                                            C4_turn = C4_player2
                                        elif C4_turn == C4_player2:
                                            C4_turn = C4_player1
                                else:
                                    col2[4] = coinC4
                                    if C4_turn == C4_player1:
                                        C4_turn = C4_player2
                                    elif C4_turn == C4_player2:
                                        C4_turn = C4_player1
                            else:
                                col2[5] = coinC4
                                if C4_turn == C4_player1:
                                    C4_turn = C4_player2
                                elif C4_turn == C4_player2:
                                    C4_turn = C4_player1

                        elif C4number == "3":
                            if col3[5] != blankC4:
                                if col3[4] != blankC4:
                                    if col3[3] != blankC4:
                                        if col3[2] != blankC4:
                                            if col3[1] != blankC4:
                                                if col3[0] != blankC4:
                                                    await bot.send_message(message.channel, "Please choose an available column")
                                                else:
                                                    col3[0] = coinC4
                                                    if C4_turn == C4_player1:
                                                        C4_turn = C4_player2
                                                    elif C4_turn == C4_player2:
                                                        C4_turn = C4_player1
                                            else:
                                                col3[1] = coinC4
                                                if C4_turn == C4_player1:
                                                    C4_turn = C4_player2
                                                elif C4_turn == C4_player2:
                                                    C4_turn = C4_player1
                                        else:
                                            col3[2] = coinC4
                                            if C4_turn == C4_player1:
                                                C4_turn = C4_player2
                                            elif C4_turn == C4_player2:
                                                C4_turn = C4_player1
                                    else:
                                        col3[3] = coinC4
                                        if C4_turn == C4_player1:
                                            C4_turn = C4_player2
                                        elif C4_turn == C4_player2:
                                            C4_turn = C4_player1
                                else:
                                    col3[4] = coinC4
                                    if C4_turn == C4_player1:
                                        C4_turn = C4_player2
                                    elif C4_turn == C4_player2:
                                        C4_turn = C4_player1
                            else:
                                col3[5] = coinC4
                                if C4_turn == C4_player1:
                                    C4_turn = C4_player2
                                elif C4_turn == C4_player2:
                                    C4_turn = C4_player1

                        elif C4number == "4":
                            if col4[5] != blankC4:
                                if col4[4] != blankC4:
                                    if col4[3] != blankC4:
                                        if col4[2] != blankC4:
                                            if col4[1] != blankC4:
                                                if col4[0] != blankC4:
                                                    await bot.send_message(message.channel, "Please choose an available column")
                                                else:
                                                    col4[0] = coinC4
                                                    if C4_turn == C4_player1:
                                                        C4_turn = C4_player2
                                                    elif C4_turn == C4_player2:
                                                        C4_turn = C4_player1
                                            else:
                                                col4[1] = coinC4
                                                if C4_turn == C4_player1:
                                                    C4_turn = C4_player2
                                                elif C4_turn == C4_player2:
                                                    C4_turn = C4_player1
                                        else:
                                            col4[2] = coinC4
                                            if C4_turn == C4_player1:
                                                C4_turn = C4_player2
                                            elif C4_turn == C4_player2:
                                                C4_turn = C4_player1
                                    else:
                                        col4[3] = coinC4
                                        if C4_turn == C4_player1:
                                            C4_turn = C4_player2
                                        elif C4_turn == C4_player2:
                                            C4_turn = C4_player1
                                else:
                                    col4[4] = coinC4
                                    if C4_turn == C4_player1:
                                        C4_turn = C4_player2
                                    elif C4_turn == C4_player2:
                                        C4_turn = C4_player1
                            else:
                                col4[5] = coinC4
                                if C4_turn == C4_player1:
                                    C4_turn = C4_player2
                                elif C4_turn == C4_player2:
                                    C4_turn = C4_player1

                        elif C4number == "5":
                            if col5[5] != blankC4:
                                if col5[4] != blankC4:
                                    if col5[3] != blankC4:
                                        if col5[2] != blankC4:
                                            if col5[1] != blankC4:
                                                if col5[0] != blankC4:
                                                    await bot.send_message(message.channel, "Please choose an available column")
                                                else:
                                                    col5[0] = coinC4
                                                    if C4_turn == C4_player1:
                                                        C4_turn = C4_player2
                                                    elif C4_turn == C4_player2:
                                                        C4_turn = C4_player1
                                            else:
                                                col5[1] = coinC4
                                                if C4_turn == C4_player1:
                                                    C4_turn = C4_player2
                                                elif C4_turn == C4_player2:
                                                    C4_turn = C4_player1
                                        else:
                                            col5[2] = coinC4
                                            if C4_turn == C4_player1:
                                                C4_turn = C4_player2
                                            elif C4_turn == C4_player2:
                                                C4_turn = C4_player1
                                    else:
                                        col5[3] = coinC4
                                        if C4_turn == C4_player1:
                                            C4_turn = C4_player2
                                        elif C4_turn == C4_player2:
                                            C4_turn = C4_player1
                                else:
                                    col5[4] = coinC4
                                    if C4_turn == C4_player1:
                                        C4_turn = C4_player2
                                    elif C4_turn == C4_player2:
                                        C4_turn = C4_player1
                            else:
                                col5[5] = coinC4
                                if C4_turn == C4_player1:
                                    C4_turn = C4_player2
                                elif C4_turn == C4_player2:
                                    C4_turn = C4_player1

                        elif C4number == "6":
                            if col6[5] != blankC4:
                                if col6[4] != blankC4:
                                    if col6[3] != blankC4:
                                        if col6[2] != blankC4:
                                            if col6[1] != blankC4:
                                                if col6[0] != blankC4:
                                                    await bot.send_message(message.channel, "Please choose an available column")
                                                else:
                                                    col6[0] = coinC4
                                                    if C4_turn == C4_player1:
                                                        C4_turn = C4_player2
                                                    elif C4_turn == C4_player2:
                                                        C4_turn = C4_player1
                                            else:
                                                col6[1] = coinC4
                                                if C4_turn == C4_player1:
                                                    C4_turn = C4_player2
                                                elif C4_turn == C4_player2:
                                                    C4_turn = C4_player1
                                        else:
                                            col6[2] = coinC4
                                            if C4_turn == C4_player1:
                                                C4_turn = C4_player2
                                            elif C4_turn == C4_player2:
                                                C4_turn = C4_player1
                                    else:
                                        col6[3] = coinC4
                                        if C4_turn == C4_player1:
                                            C4_turn = C4_player2
                                        elif C4_turn == C4_player2:
                                            C4_turn = C4_player1
                                else:
                                    col6[4] = coinC4
                                    if C4_turn == C4_player1:
                                        C4_turn = C4_player2
                                    elif C4_turn == C4_player2:
                                        C4_turn = C4_player1
                            else:
                                col6[5] = coinC4
                                if C4_turn == C4_player1:
                                    C4_turn = C4_player2
                                elif C4_turn == C4_player2:
                                    C4_turn = C4_player1

                        elif C4number == "7":
                            if col7[5] != blankC4:
                                if col7[4] != blankC4:
                                    if col7[3] != blankC4:
                                        if col7[2] != blankC4:
                                            if col7[1] != blankC4:
                                                if col7[0] != blankC4:
                                                    await bot.send_message(message.channel, "Please choose an available column")
                                                else:
                                                    col7[0] = coinC4
                                                    if C4_turn == C4_player1:
                                                        C4_turn = C4_player2
                                                    elif C4_turn == C4_player2:
                                                        C4_turn = C4_player1
                                            else:
                                                col7[1] = coinC4
                                                if C4_turn == C4_player1:
                                                    C4_turn = C4_player2
                                                elif C4_turn == C4_player2:
                                                    C4_turn = C4_player1
                                        else:
                                            col7[2] = coinC4
                                            if C4_turn == C4_player1:
                                                C4_turn = C4_player2
                                            elif C4_turn == C4_player2:
                                                C4_turn = C4_player1
                                    else:
                                        col7[3] = coinC4
                                        if C4_turn == C4_player1:
                                            C4_turn = C4_player2
                                        elif C4_turn == C4_player2:
                                            C4_turn = C4_player1
                                else:
                                    col7[4] = coinC4
                                    if C4_turn == C4_player1:
                                        C4_turn = C4_player2
                                    elif C4_turn == C4_player2:
                                        C4_turn = C4_player1
                            else:
                                col7[5] = coinC4
                                if C4_turn == C4_player1:
                                    C4_turn = C4_player2
                                elif C4_turn == C4_player2:
                                    C4_turn = C4_player1




                        tableC4="%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n%s%s%s%s%s%s%s\n:one::two::three::four::five::six::seven:"%(col1[0],col2[0],col3[0],col4[0],col5[0],col6[0],col7[0],col1[1],col2[1],col3[1],col4[1],col5[1],col6[1],col7[1],col1[2],col2[2],col3[2],col4[2],col5[2],col6[2],col7[2],col1[3],col2[3],col3[3],col4[3],col5[3],col6[3],col7[3],col1[4],col2[4],col3[4],col4[4],col5[4],col6[4],col7[4],col1[5],col2[5],col3[5],col4[5],col5[5],col6[5],col7[5])

                        em = discord.Embed(title="Connect4", description=tableC4, colour=0xBCAD20)
                        em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
                        await bot.send_message(message.channel,content=None, embed=em)


                        #Predicting the winner of Connect4
                        winsC4 = [
                        col1[5]==redC4 and col1[4]==redC4 and col1[3]==redC4 and col1[2]==redC4,
                        col1[4]==redC4 and col1[3]==redC4 and col1[2]==redC4 and col1[1]==redC4,
                        col1[3]==redC4 and col1[2]==redC4 and col1[1]==redC4 and col1[0]==redC4,

                        col2[5]==redC4 and col2[4]==redC4 and col2[3]==redC4 and col2[2]==redC4,
                        col2[4]==redC4 and col2[3]==redC4 and col2[2]==redC4 and col2[1]==redC4,
                        col2[3]==redC4 and col2[2]==redC4 and col2[1]==redC4 and col2[0]==redC4,

                        col3[5]==redC4 and col3[4]==redC4 and col3[3]==redC4 and col3[2]==redC4,
                        col3[4]==redC4 and col3[3]==redC4 and col3[2]==redC4 and col3[1]==redC4,
                        col3[3]==redC4 and col3[2]==redC4 and col3[1]==redC4 and col3[0]==redC4,

                        col4[5]==redC4 and col4[4]==redC4 and col4[3]==redC4 and col4[2]==redC4,
                        col4[4]==redC4 and col4[3]==redC4 and col4[2]==redC4 and col4[1]==redC4,
                        col4[3]==redC4 and col4[2]==redC4 and col4[1]==redC4 and col4[0]==redC4,

                        col5[5]==redC4 and col5[4]==redC4 and col5[3]==redC4 and col5[2]==redC4,
                        col5[4]==redC4 and col5[3]==redC4 and col5[2]==redC4 and col5[1]==redC4,
                        col5[3]==redC4 and col5[2]==redC4 and col5[1]==redC4 and col5[0]==redC4,

                        col6[5]==redC4 and col6[4]==redC4 and col6[3]==redC4 and col6[2]==redC4,
                        col6[4]==redC4 and col6[3]==redC4 and col6[2]==redC4 and col6[1]==redC4,
                        col6[3]==redC4 and col6[2]==redC4 and col6[1]==redC4 and col6[0]==redC4,

                        col7[5]==redC4 and col7[4]==redC4 and col7[3]==redC4 and col7[2]==redC4,
                        col7[4]==redC4 and col7[3]==redC4 and col7[2]==redC4 and col7[1]==redC4,
                        col7[3]==redC4 and col7[2]==redC4 and col7[1]==redC4 and col7[0]==redC4,



                        col1[0]==redC4 and col2[0]==redC4 and col3[0]==redC4 and col4[0]==redC4,
                        col2[0]==redC4 and col3[0]==redC4 and col4[0]==redC4 and col5[0]==redC4,
                        col3[0]==redC4 and col4[0]==redC4 and col5[0]==redC4 and col6[0]==redC4,
                        col4[0]==redC4 and col5[0]==redC4 and col6[0]==redC4 and col7[0]==redC4,

                        col1[1]==redC4 and col2[1]==redC4 and col3[1]==redC4 and col4[1]==redC4,
                        col2[1]==redC4 and col3[1]==redC4 and col4[1]==redC4 and col5[1]==redC4,
                        col3[1]==redC4 and col4[1]==redC4 and col5[1]==redC4 and col6[1]==redC4,
                        col4[1]==redC4 and col5[1]==redC4 and col6[1]==redC4 and col7[1]==redC4,

                        col1[2]==redC4 and col2[2]==redC4 and col3[2]==redC4 and col4[2]==redC4,
                        col2[2]==redC4 and col3[2]==redC4 and col4[2]==redC4 and col5[2]==redC4,
                        col3[2]==redC4 and col4[2]==redC4 and col5[2]==redC4 and col6[2]==redC4,
                        col4[2]==redC4 and col5[2]==redC4 and col6[2]==redC4 and col7[2]==redC4,

                        col1[3]==redC4 and col2[3]==redC4 and col3[3]==redC4 and col4[3]==redC4,
                        col2[3]==redC4 and col3[3]==redC4 and col4[3]==redC4 and col5[3]==redC4,
                        col3[3]==redC4 and col4[3]==redC4 and col5[3]==redC4 and col6[3]==redC4,
                        col4[3]==redC4 and col5[3]==redC4 and col6[3]==redC4 and col7[3]==redC4,

                        col1[4]==redC4 and col2[4]==redC4 and col3[4]==redC4 and col4[4]==redC4,
                        col2[4]==redC4 and col3[4]==redC4 and col4[4]==redC4 and col5[4]==redC4,
                        col3[4]==redC4 and col4[4]==redC4 and col5[4]==redC4 and col6[4]==redC4,
                        col4[4]==redC4 and col5[4]==redC4 and col6[4]==redC4 and col7[4]==redC4,

                        col1[5]==redC4 and col2[5]==redC4 and col3[5]==redC4 and col4[5]==redC4,
                        col2[5]==redC4 and col3[5]==redC4 and col4[5]==redC4 and col5[5]==redC4,
                        col3[5]==redC4 and col4[5]==redC4 and col5[5]==redC4 and col6[5]==redC4,
                        col4[5]==redC4 and col5[5]==redC4 and col6[5]==redC4 and col7[5]==redC4,



                        col1[3]==redC4 and col2[2]==redC4 and col3[1]==redC4 and col4[0]==redC4,
                        col1[4]==redC4 and col2[3]==redC4 and col3[2]==redC4 and col4[1]==redC4,
                        col1[5]==redC4 and col2[4]==redC4 and col3[3]==redC4 and col4[2]==redC4,

                        col2[3]==redC4 and col3[2]==redC4 and col4[1]==redC4 and col5[0]==redC4,
                        col2[4]==redC4 and col3[3]==redC4 and col4[2]==redC4 and col5[1]==redC4,
                        col2[5]==redC4 and col3[4]==redC4 and col4[3]==redC4 and col5[2]==redC4,

                        col3[3]==redC4 and col4[2]==redC4 and col5[1]==redC4 and col6[0]==redC4,
                        col3[4]==redC4 and col4[3]==redC4 and col5[2]==redC4 and col6[1]==redC4,
                        col3[5]==redC4 and col4[4]==redC4 and col5[3]==redC4 and col6[2]==redC4,

                        col4[3]==redC4 and col5[2]==redC4 and col6[1]==redC4 and col7[0]==redC4,
                        col4[4]==redC4 and col5[3]==redC4 and col6[2]==redC4 and col7[1]==redC4,
                        col4[5]==redC4 and col5[4]==redC4 and col6[3]==redC4 and col7[2]==redC4,



                        col1[2]==redC4 and col2[3]==redC4 and col3[4]==redC4 and col4[5]==redC4,
                        col1[1]==redC4 and col2[2]==redC4 and col3[3]==redC4 and col4[4]==redC4,
                        col1[0]==redC4 and col2[1]==redC4 and col3[2]==redC4 and col4[3]==redC4,

                        col2[2]==redC4 and col3[3]==redC4 and col4[4]==redC4 and col5[5]==redC4,
                        col2[1]==redC4 and col3[2]==redC4 and col4[3]==redC4 and col5[4]==redC4,
                        col2[0]==redC4 and col3[1]==redC4 and col4[2]==redC4 and col5[3]==redC4,

                        col3[2]==redC4 and col4[3]==redC4 and col5[4]==redC4 and col6[5]==redC4,
                        col3[1]==redC4 and col4[2]==redC4 and col5[3]==redC4 and col6[4]==redC4,
                        col3[0]==redC4 and col4[1]==redC4 and col5[2]==redC4 and col6[3]==redC4,

                        col4[2]==redC4 and col5[3]==redC4 and col6[4]==redC4 and col7[5]==redC4,
                        col4[1]==redC4 and col5[2]==redC4 and col6[3]==redC4 and col7[4]==redC4,
                        col4[0]==redC4 and col5[1]==redC4 and col6[2]==redC4 and col7[3]==redC4,









                        col1[5]==yellowC4 and col1[4]==yellowC4 and col1[3]==yellowC4 and col1[2]==yellowC4,
                        col1[4]==yellowC4 and col1[3]==yellowC4 and col1[2]==yellowC4 and col1[1]==yellowC4,
                        col1[3]==yellowC4 and col1[2]==yellowC4 and col1[1]==yellowC4 and col1[0]==yellowC4,

                        col2[5]==yellowC4 and col2[4]==yellowC4 and col2[3]==yellowC4 and col2[2]==yellowC4,
                        col2[4]==yellowC4 and col2[3]==yellowC4 and col2[2]==yellowC4 and col2[1]==yellowC4,
                        col2[3]==yellowC4 and col2[2]==yellowC4 and col2[1]==yellowC4 and col2[0]==yellowC4,

                        col3[5]==yellowC4 and col3[4]==yellowC4 and col3[3]==yellowC4 and col3[2]==yellowC4,
                        col3[4]==yellowC4 and col3[3]==yellowC4 and col3[2]==yellowC4 and col3[1]==yellowC4,
                        col3[3]==yellowC4 and col3[2]==yellowC4 and col3[1]==yellowC4 and col3[0]==yellowC4,

                        col4[5]==yellowC4 and col4[4]==yellowC4 and col4[3]==yellowC4 and col4[2]==yellowC4,
                        col4[4]==yellowC4 and col4[3]==yellowC4 and col4[2]==yellowC4 and col4[1]==yellowC4,
                        col4[3]==yellowC4 and col4[2]==yellowC4 and col4[1]==yellowC4 and col4[0]==yellowC4,

                        col5[5]==yellowC4 and col5[4]==yellowC4 and col5[3]==yellowC4 and col5[2]==yellowC4,
                        col5[4]==yellowC4 and col5[3]==yellowC4 and col5[2]==yellowC4 and col5[1]==yellowC4,
                        col5[3]==yellowC4 and col5[2]==yellowC4 and col5[1]==yellowC4 and col5[0]==yellowC4,

                        col6[5]==yellowC4 and col6[4]==yellowC4 and col6[3]==yellowC4 and col6[2]==yellowC4,
                        col6[4]==yellowC4 and col6[3]==yellowC4 and col6[2]==yellowC4 and col6[1]==yellowC4,
                        col6[3]==yellowC4 and col6[2]==yellowC4 and col6[1]==yellowC4 and col6[0]==yellowC4,

                        col7[5]==yellowC4 and col7[4]==yellowC4 and col7[3]==yellowC4 and col7[2]==yellowC4,
                        col7[4]==yellowC4 and col7[3]==yellowC4 and col7[2]==yellowC4 and col7[1]==yellowC4,
                        col7[3]==yellowC4 and col7[2]==yellowC4 and col7[1]==yellowC4 and col7[0]==yellowC4,



                        col1[0]==yellowC4 and col2[0]==yellowC4 and col3[0]==yellowC4 and col4[0]==yellowC4,
                        col2[0]==yellowC4 and col3[0]==yellowC4 and col4[0]==yellowC4 and col5[0]==yellowC4,
                        col3[0]==yellowC4 and col4[0]==yellowC4 and col5[0]==yellowC4 and col6[0]==yellowC4,
                        col4[0]==yellowC4 and col5[0]==yellowC4 and col6[0]==yellowC4 and col7[0]==yellowC4,

                        col1[1]==yellowC4 and col2[1]==yellowC4 and col3[1]==yellowC4 and col4[1]==yellowC4,
                        col2[1]==yellowC4 and col3[1]==yellowC4 and col4[1]==yellowC4 and col5[1]==yellowC4,
                        col3[1]==yellowC4 and col4[1]==yellowC4 and col5[1]==yellowC4 and col6[1]==yellowC4,
                        col4[1]==yellowC4 and col5[1]==yellowC4 and col6[1]==yellowC4 and col7[1]==yellowC4,

                        col1[2]==yellowC4 and col2[2]==yellowC4 and col3[2]==yellowC4 and col4[2]==yellowC4,
                        col2[2]==yellowC4 and col3[2]==yellowC4 and col4[2]==yellowC4 and col5[2]==yellowC4,
                        col3[2]==yellowC4 and col4[2]==yellowC4 and col5[2]==yellowC4 and col6[2]==yellowC4,
                        col4[2]==yellowC4 and col5[2]==yellowC4 and col6[2]==yellowC4 and col7[2]==yellowC4,

                        col1[3]==yellowC4 and col2[3]==yellowC4 and col3[3]==yellowC4 and col4[3]==yellowC4,
                        col2[3]==yellowC4 and col3[3]==yellowC4 and col4[3]==yellowC4 and col5[3]==yellowC4,
                        col3[3]==yellowC4 and col4[3]==yellowC4 and col5[3]==yellowC4 and col6[3]==yellowC4,
                        col4[3]==yellowC4 and col5[3]==yellowC4 and col6[3]==yellowC4 and col7[3]==yellowC4,

                        col1[4]==yellowC4 and col2[4]==yellowC4 and col3[4]==yellowC4 and col4[4]==yellowC4,
                        col2[4]==yellowC4 and col3[4]==yellowC4 and col4[4]==yellowC4 and col5[4]==yellowC4,
                        col3[4]==yellowC4 and col4[4]==yellowC4 and col5[4]==yellowC4 and col6[4]==yellowC4,
                        col4[4]==yellowC4 and col5[4]==yellowC4 and col6[4]==yellowC4 and col7[4]==yellowC4,

                        col1[5]==yellowC4 and col2[5]==yellowC4 and col3[5]==yellowC4 and col4[5]==yellowC4,
                        col2[5]==yellowC4 and col3[5]==yellowC4 and col4[5]==yellowC4 and col5[5]==yellowC4,
                        col3[5]==yellowC4 and col4[5]==yellowC4 and col5[5]==yellowC4 and col6[5]==yellowC4,
                        col4[5]==yellowC4 and col5[5]==yellowC4 and col6[5]==yellowC4 and col7[5]==yellowC4,



                        col1[3]==yellowC4 and col2[2]==yellowC4 and col3[1]==yellowC4 and col4[0]==yellowC4,
                        col1[4]==yellowC4 and col2[3]==yellowC4 and col3[2]==yellowC4 and col4[1]==yellowC4,
                        col1[5]==yellowC4 and col2[4]==yellowC4 and col3[3]==yellowC4 and col4[2]==yellowC4,

                        col2[3]==yellowC4 and col3[2]==yellowC4 and col4[1]==yellowC4 and col5[0]==yellowC4,
                        col2[4]==yellowC4 and col3[3]==yellowC4 and col4[2]==yellowC4 and col5[1]==yellowC4,
                        col2[5]==yellowC4 and col3[4]==yellowC4 and col4[3]==yellowC4 and col5[2]==yellowC4,

                        col3[3]==yellowC4 and col4[2]==yellowC4 and col5[1]==yellowC4 and col6[0]==yellowC4,
                        col3[4]==yellowC4 and col4[3]==yellowC4 and col5[2]==yellowC4 and col6[1]==yellowC4,
                        col3[5]==yellowC4 and col4[4]==yellowC4 and col5[3]==yellowC4 and col6[2]==yellowC4,

                        col4[3]==yellowC4 and col5[2]==yellowC4 and col6[1]==yellowC4 and col7[0]==yellowC4,
                        col4[4]==yellowC4 and col5[3]==yellowC4 and col6[2]==yellowC4 and col7[1]==yellowC4,
                        col4[5]==yellowC4 and col5[4]==yellowC4 and col6[3]==yellowC4 and col7[2]==yellowC4,



                        col1[2]==yellowC4 and col2[3]==yellowC4 and col3[4]==yellowC4 and col4[5]==yellowC4,
                        col1[1]==yellowC4 and col2[2]==yellowC4 and col3[3]==yellowC4 and col4[4]==yellowC4,
                        col1[0]==yellowC4 and col2[1]==yellowC4 and col3[2]==yellowC4 and col4[3]==yellowC4,

                        col2[2]==yellowC4 and col3[3]==yellowC4 and col4[4]==yellowC4 and col5[5]==yellowC4,
                        col2[1]==yellowC4 and col3[2]==yellowC4 and col4[3]==yellowC4 and col5[4]==yellowC4,
                        col2[0]==yellowC4 and col3[1]==yellowC4 and col4[2]==yellowC4 and col5[3]==yellowC4,

                        col3[2]==yellowC4 and col4[3]==yellowC4 and col5[4]==yellowC4 and col6[5]==yellowC4,
                        col3[1]==yellowC4 and col4[2]==yellowC4 and col5[3]==yellowC4 and col6[4]==yellowC4,
                        col3[0]==yellowC4 and col4[1]==yellowC4 and col5[2]==yellowC4 and col6[3]==yellowC4,

                        col4[2]==yellowC4 and col5[3]==yellowC4 and col6[4]==yellowC4 and col7[5]==yellowC4,
                        col4[1]==yellowC4 and col5[2]==yellowC4 and col6[3]==yellowC4 and col7[4]==yellowC4,
                        col4[0]==yellowC4 and col5[1]==yellowC4 and col6[2]==yellowC4 and col7[3]==yellowC4
                        ]
                        for w in winsC4:
                            if w:
                                if C4_turn == C4_player1:
                                    C4_turn = C4_player2
                                elif C4_turn == C4_player2:
                                    C4_turn = C4_player1



                                with open('stats.json') as stats:
                                    lines = json.load(stats)

                                for player in lines['players']:
                                    if player['id'] == message.author.id:
                                        player['c4Wins'] += 1
                                        player['points'] += 5*player['booster']

                                with open('stats.json','w') as stats:
                                    json.dump(lines, stats, indent=4)


                                c4ID = message.author.id
                                check_achievements = True


                                await bot.send_message(message.channel, "**" + C4_turn + "** wins!")
                                C4_player1 = 0
                                C4_player2 = 0
                                C4_start = 0
                                C4_turn = 0

                                blankC4 = ":white_square_button:"
                                redC4 = ":red_circle:"
                                yellowC4 = ":large_orange_diamond:"
                                col1 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                                col2 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                                col3 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                                col4 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                                col5 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                                col6 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                                col7 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                                await bot.send_message(message.channel, "Another game of **Connect4** is ready to be played!")




        #WordGuess
        if message.content.upper().startswith("-WORDGUESS") or message.content.upper().startswith("-WG"):
            global word
            global scrambled_word
            global wg_play
            global wg_stoper
            global wgID
            if message.channel.id == bot_spam_channel_id:
                if wg_play == True:
                    await bot.send_message(message.channel, "Have patience...")
                else:
                    wg_play = True
                    while wg_play == True:
                        opt = random.choice(words)

                        word = opt[1]
                        jumble = ""
                        unscram = opt[1]
                        def scrambled(unscram):
                            l = list(unscram)
                            random.shuffle(l)
                            return ''.join(l)

                        scrambled_word = scrambled(unscram)

                        now = datetime.datetime.utcnow()
                        await bot.send_message(message.channel, "Unscramble " + scrambled_word + " to win!")

                        wg_msg = await bot.wait_for_message(timeout=25, channel=message.channel, content=word)


                        #assert react_msg, "Test"

                        if wg_msg:
                            delta = now - wg_msg.timestamp
                            micros = int((round(delta.microseconds,-4))/10000)
                            wg_time = 24 * 60 * 60 - delta.seconds
                            if wg_time > 86000:
                                wg_time = "0"



                            with open('stats.json') as stats:
                                lines = json.load(stats)

                            for player in lines['players']:
                                if player['id'] == wg_msg.author.id:
                                    player['wgWins'] += 1
                                    player['points'] += 1*player['booster']

                            with open('stats.json','w') as stats:
                                json.dump(lines, stats, indent=4)

                            wgID = wg_msg.author.id
                            with open('achievements.json') as achievements:
                                a = json.load(achievements)

                            for achievement in a['achievements']:
                                if achievement['name'] == 'Gaming Nub':
                                    achievement_won = False
                                    for id in achievement['players']:
                                        if id == wgID:
                                            achievement_won = True

                                    if achievement_won == False:
                                        await bot.send_message(message.channel, wg_msg.author.id)
                                        achievement['players'] += [(wg_msg.author.id)]
                                        await bot.send_message(wg_msg.author, "You just earned the achievement: **Gaming Nub**!")

                            with open('achievements.json','w') as achievements:
                                json.dump(a,achievements,indent=4)



                            await bot.send_message(message.channel, "**" + wg_msg.author.name + "** unscrambled the word **" + word + "** in {0}.{1} seconds!".format(wg_time, micros))
                            wg_stoper = 0
                        else:
                            await bot.send_message(message.channel, "Nobody guessed the word in time. The word was " + word + ".")
                            wg_stoper += 1
                            word = 0
                            if wg_stoper == 5:
                                wg_stoper = 0
                                wg_play = False

                        await asyncio.sleep(35)


        if message.content.upper().startswith("-REACTION") or message.content.upper().startswith("-REACT"):
            global word2
            global reaction_stoper
            global reaction_play
            global reactID
            if message.channel.id == bot_spam_channel_id:
                if reaction_play == True:
                    await bot.send_message(message.channel, "Have patience...")
                else:
                    reaction_play = True
                    while reaction_play == True:
                        reactWord = random.choice(words)
                        word2 = reactWord[1]
                        now = datetime.datetime.utcnow()
                        await bot.send_message(message.channel, "Type the word **" + word2 + "** to win!")

                        react_msg = await bot.wait_for_message(timeout=25, channel=message.channel, content=word2)


                        #assert react_msg, "Test"

                        if react_msg:
                            delta = now - react_msg.timestamp
                            micros = int((round(delta.microseconds,-4))/10000)
                            reaction_time = 24 * 60 * 60 - delta.seconds
                            if reaction_time > 86000:
                                reaction_time = "0"



                            with open('stats.json') as stats:
                                lines = json.load(stats)

                            for player in lines['players']:
                                if player['id'] == react_msg.author.id:
                                    player['reactWins'] += 1
                                    player['points'] += 1*player['booster']

                            with open('stats.json','w') as stats:
                                json.dump(lines, stats, indent=4)

                            reactID = react_msg.author.id
                            #try:
                            with open('achievements.json') as achievements:
                                a = json.load(achievements)

                            for achievement in a['achievements']:
                                if achievement['name'] == 'Gaming Nub':
                                    achievement_won = False
                                    for id in achievement['players']:
                                        if id == react_msg.author.id:
                                            achievement_won = True

                                    if achievement_won == False:
                                        await bot.send_message(message.channel, react_msg.author.id)
                                        achievement['players'] += [(react_msg.author.id)]
                                        await bot.send_message(react_msg.author, "You just earned the achievement: **Gaming Nub**!")

                            with open('achievements.json','w') as achievements:
                                json.dump(a,achievements,indent=4)


                            # except:
                            #     await bot.send_message(message.channel, 'Failed to check for achievements')

                            # stats.close()
                            #
                            # stats = open("stats.txt","w")
                            #
                            # stats.close()


                            if micros == 100:
                                reaction_time += 1
                            await bot.send_message(message.channel, "**" + react_msg.author.name + "** won in {0}.{1} seconds!".format(reaction_time, micros))
                            reaction_stoper = 0
                        else:
                            await bot.send_message(message.channel, "Nobody got the word in time.")
                            reaction_stoper += 1
                            if reaction_stoper == 5:
                                reaction_stoper = 0
                                reaction_play = False

                        await asyncio.sleep(35)

                        #if react_msg == None:
                        #    await bot.send_message(message.channel, "No one typed the word in time.")
                        #elif react_msg.content == word2:
                        #    await bot.send_message(message.channel, message.author.name + " won!")






        if message.content.upper().startswith("-INSANE") or message.content.upper().startswith("-INSANITY"):
            global insanePlayers
            global insaneID
            #SET UP PLAYER SPECIFIC GAME
            #insanePlayers = [(id,name,inPos[1,2,3,4,5,6,7,8,9])]
            #spaces: :black_large_square: :red_circle: :large_blue_circle:
            #Red starts left, Blue starts right


            pID = message.author.id
            with open('achievements.json') as achievements:
                a = json.load(achievements)

            for achievement in a['achievements']:
                if achievement['name'] == 'Gaming Nub':
                    achievement_won = False
                    for id in achievement['players']:
                        if id == pID:
                            achievement_won = True

                    if achievement_won == False:
                        achievement['players'] += [(pID)]
                        await bot.send_message(message.author, "You just earned the achievement: **Gaming Nub**!")

            with open('achievements.json','w') as achievements:
                json.dump(a,achievements,indent=4)


            #Check if joining player is already playing
            inCancelJoin = 0
            for player in insanePlayers:
                if message.author.id == player[0]:
                    inCancelJoin = 1

            if inCancelJoin == 0:
                inRed = ":red_circle:"
                inBlue = ":large_blue_circle:"
                inBlank = ":black_large_square:"
                inPlayerID = message.author.id
                if message.author.nick == None:
                    inPlayerName = message.author.name
                else:
                    inPlayerName = message.author.nick
                inPos = [inRed,inRed,inRed,inRed,inBlank,inBlue,inBlue,inBlue,inBlue]
                inPlaying = 1
                insanePlayers += [(inPlayerID,inPlayerName,inPos)]
                #await bot.send_message(message.channel, inPlayerName + " joined successfully!")
                #for player in insanePlayers:
                #    await bot.send_message(message.channel, player[1])

                #Now send the embed message to show the game
                insaneBoard = inPos[0]+inPos[1]+inPos[2]+inPos[3]+inPos[4]+inPos[5]+inPos[6]+inPos[7]+inPos[8]+"\n:one::two::three::four::five::six::seven::eight::nine:"

                em = discord.Embed(title="Insanity!", description=insaneBoard, colour=0xBCAD20)
                em.set_author(name=inPlayerName, icon_url=message.author.avatar_url)
                em.set_footer(text=insaneInstructions)
                inMsg = await bot.send_message(message.channel,content=None, embed=em)

                #add_reaction(message, emoji)
                #await bot.add_reaction(inMsg,'\N{Black Left-Pointing Triangle}')
                await bot.add_reaction(inMsg,'1⃣')
                await bot.add_reaction(inMsg,'2⃣')
                await bot.add_reaction(inMsg,'3⃣')
                await bot.add_reaction(inMsg,'4⃣')
                await bot.add_reaction(inMsg,'5⃣')
                await bot.add_reaction(inMsg,'6⃣')
                await bot.add_reaction(inMsg,'7⃣')
                await bot.add_reaction(inMsg,'8⃣')
                await bot.add_reaction(inMsg,'9⃣')
                await bot.add_reaction(inMsg,'❌')
                #await bot.add_reaction(inMsg,'\N{Black Right-Pointing Triangle}')

                #now wait for reactions from the player
                #wait_for_reaction(emoji=None, *, user=None, timeout=None, message=None, check=None)
                while inPlaying == 1:
                    inPlayerReact = await bot.wait_for_reaction(emoji=None,user=message.author,timeout=60,message=inMsg)
                    if inPlayerReact:
                        #await bot.send_message(message.channel, "Reaction recieved!")
                        if inPlayerReact.reaction.emoji == '1⃣':
                            await bot.remove_reaction(message=inMsg, emoji='1⃣', member=message.author)
                            if inPos[0] == inRed:
                                if inPos[1] == inBlank:
                                    inPos[0] = inBlank
                                    inPos[1] = inRed
                                elif inPos[2] == inBlank:
                                    inPos[0] = inBlank
                                    inPos[2] = inRed

                        elif inPlayerReact.reaction.emoji == '2⃣':
                            await bot.remove_reaction(message=inMsg, emoji='2⃣', member=message.author)
                            if inPos[1] == inRed:
                                if inPos[2] == inBlank:
                                    inPos[1] = inBlank
                                    inPos[2] = inRed
                                elif inPos[3] == inBlank:
                                    inPos[1] = inBlank
                                    inPos[3] = inRed
                            elif inPos[1] == inBlue:
                                if inPos[0] == inBlank:
                                    inPos[1] = inBlank
                                    inPos[0] = inBlue

                        elif inPlayerReact.reaction.emoji == '3⃣':
                            await bot.remove_reaction(message=inMsg, emoji='3⃣', member=message.author)
                            if inPos[2] == inRed:
                                if inPos[3] == inBlank:
                                    inPos[2] = inBlank
                                    inPos[3] = inRed
                                elif inPos[4] == inBlank:
                                    inPos[2] = inBlank
                                    inPos[4] = inRed
                            elif inPos[2] == inBlue:
                                if inPos[1] == inBlank:
                                    inPos[2] = inBlank
                                    inPos[1] = inBlue
                                elif inPos[0] == inBlank:
                                    inPos[2] = inBlank
                                    inPos[0] = inBlue

                        elif inPlayerReact.reaction.emoji == '4⃣':
                            await bot.remove_reaction(message=inMsg, emoji='4⃣', member=message.author)
                            if inPos[3] == inRed:
                                if inPos[4] == inBlank:
                                    inPos[3] = inBlank
                                    inPos[4] = inRed
                                elif inPos[5] == inBlank:
                                    inPos[3] = inBlank
                                    inPos[5] = inRed
                            elif inPos[3] == inBlue:
                                if inPos[2] == inBlank:
                                    inPos[3] = inBlank
                                    inPos[2] = inBlue
                                elif inPos[1] == inBlank:
                                    inPos[3] = inBlank
                                    inPos[1] = inBlue

                        elif inPlayerReact.reaction.emoji == '5⃣':
                            await bot.remove_reaction(message=inMsg, emoji='5⃣', member=message.author)
                            if inPos[4] == inRed:
                                if inPos[5] == inBlank:
                                    inPos[4] = inBlank
                                    inPos[5] = inRed
                                elif inPos[6] == inBlank:
                                    inPos[4] = inBlank
                                    inPos[6] = inRed
                            elif inPos[4] == inBlue:
                                if inPos[3] == inBlank:
                                    inPos[4] = inBlank
                                    inPos[3] = inBlue
                                elif inPos[2] == inBlank:
                                    inPos[4] = inBlank
                                    inPos[2] = inBlue

                        elif inPlayerReact.reaction.emoji == '6⃣':
                            await bot.remove_reaction(message=inMsg, emoji='6⃣', member=message.author)
                            if inPos[5] == inRed:
                                if inPos[6] == inBlank:
                                    inPos[5] = inBlank
                                    inPos[6] = inRed
                                elif inPos[7] == inBlank:
                                    inPos[5] = inBlank
                                    inPos[7] = inRed
                            elif inPos[5] == inBlue:
                                if inPos[4] == inBlank:
                                    inPos[5] = inBlank
                                    inPos[4] = inBlue
                                elif inPos[3] == inBlank:
                                    inPos[5] = inBlank
                                    inPos[3] = inBlue

                        elif inPlayerReact.reaction.emoji == '7⃣':
                            await bot.remove_reaction(message=inMsg, emoji='7⃣', member=message.author)
                            if inPos[6] == inRed:
                                if inPos[7] == inBlank:
                                    inPos[6] = inBlank
                                    inPos[7] = inRed
                                elif inPos[8] == inBlank:
                                    inPos[6] = inBlank
                                    inPos[8] = inRed
                            elif inPos[6] == inBlue:
                                if inPos[5] == inBlank:
                                    inPos[6] = inBlank
                                    inPos[5] = inBlue
                                elif inPos[4] == inBlank:
                                    inPos[6] = inBlank
                                    inPos[4] = inBlue

                        elif inPlayerReact.reaction.emoji == '8⃣':
                            await bot.remove_reaction(message=inMsg, emoji='8⃣', member=message.author)
                            if inPos[7] == inRed:
                                if inPos[8] == inBlank:
                                    inPos[7] = inBlank
                                    inPos[8] = inRed
                            elif inPos[7] == inBlue:
                                if inPos[6] == inBlank:
                                    inPos[7] = inBlank
                                    inPos[6] = inBlue
                                elif inPos[5] == inBlank:
                                    inPos[7] = inBlank
                                    inPos[5] = inBlue

                        elif inPlayerReact.reaction.emoji == '9⃣':
                            await bot.remove_reaction(message=inMsg, emoji='9⃣', member=message.author)
                            if inPos[8] == inBlue:
                                if inPos[7] == inBlank:
                                    inPos[8] = inBlank
                                    inPos[7] = inBlue
                                elif inPos[6] == inBlank:
                                    inPos[8] = inBlank
                                    inPos[6] = inBlue

                        elif inPlayerReact.reaction.emoji == '❌':
                            inPlaying = 0
                            for player in insanePlayers:
                                if player[0] == message.author.id:
                                    insanePlayers.remove(player)
                                    await bot.delete_message(inMsg)

                        insaneBoard = inPos[0]+inPos[1]+inPos[2]+inPos[3]+inPos[4]+inPos[5]+inPos[6]+inPos[7]+inPos[8]+"\n:one::two::three::four::five::six::seven::eight::nine:"

                        em = discord.Embed(title="Insanity!", description=insaneBoard, colour=0xBCAD20)
                        em.set_author(name=inPlayerName, icon_url=message.author.avatar_url)
                        em.set_footer(text=insaneInstructions)
                        inMsg = await bot.edit_message(message=inMsg,new_content=None,embed=em)

                        insaneWin = [inBlue,inBlue,inBlue,inBlue,inBlank,inRed,inRed,inRed,inRed]

                        if inPos == insaneWin:


                            with open('stats.json') as stats:
                                lines = json.load(stats)

                            for player in lines['players']:
                                if player['id'] == inPlayerID:
                                    player['insaneWins'] += 1
                                    player['points'] += 7*player['booster']

                                    pID = message.author.id
                                    with open('achievements.json') as achievements:
                                        a = json.load(achievements)

                                    for achievement in a['achievements']:
                                        if achievement['name'] == 'Sanity is for Boring People':
                                            achievement_won = False
                                            for id in achievement['players']:
                                                if id == pID:
                                                    achievement_won = True

                                            if achievement_won == False:
                                                achievement['players'] += [(pID)]
                                                await bot.send_message(message.author, "You just earned the achievement: **Sanity is for Boring People**!")

                                        if achievement['name'] == 'Do you know the Definition of Insanity?':
                                            #await bot.send_message(message.channel, "Testing Ach.")
                                            if player['insaneWins'] >= 20:
                                                achievement_won = False
                                                for id in achievement['players']:
                                                    if id == pID:
                                                        achievement_won = True

                                                if achievement_won == False:
                                                    achievement['players'] += [(pID)]
                                                    await bot.send_message(message.author, "You just earned the achievement: **Do you know the Definition of Insanity?**!")

                                        if achievement['name'] == "...It's doing the same thing over and over...":
                                            #await bot.send_message(message.channel, "Testing Ach.")
                                            if player['insaneWins'] >= 40:
                                                achievement_won = False
                                                for id in achievement['players']:
                                                    if id == pID:
                                                        achievement_won = True

                                                if achievement_won == False:
                                                    achievement['players'] += [(pID)]
                                                    await bot.send_message(message.author, "You just earned the achievement: **...It's doing the same thing over and over...**!")

                                        if achievement['name'] == "...expecting things to change.":
                                            #await bot.send_message(message.channel, "Testing Ach.")
                                            if player['insaneWins'] >= 80:
                                                achievement_won = False
                                                for id in achievement['players']:
                                                    if id == pID:
                                                        achievement_won = True

                                                if achievement_won == False:
                                                    achievement['players'] += [(pID)]
                                                    await bot.send_message(message.author, "You just earned the achievement: **...expecting things to change.**!")



                                    with open('achievements.json','w') as achievements:
                                        json.dump(a,achievements,indent=4)




                            with open('stats.json','w') as stats:
                                json.dump(lines, stats, indent=4)

                            insaneID = message.author.id
                            check_achievements = True

                            insaneBoard = inPos[0]+inPos[1]+inPos[2]+inPos[3]+inPos[4]+inPos[5]+inPos[6]+inPos[7]+inPos[8]+"\n:one::two::three::four::five::six::seven::eight::nine:\n"+inBlank+":regional_indicator_y::regional_indicator_o::regional_indicator_u:"+inBlank+":regional_indicator_w::regional_indicator_i::regional_indicator_n:"+inBlank

                            em = discord.Embed(title="Insanity!", description=insaneBoard, colour=0xBCAD20)
                            em.set_author(name=inPlayerName, icon_url=message.author.avatar_url)
                            em.set_footer(text=insaneInstructions)
                            inMsg = await bot.edit_message(message=inMsg,new_content=None,embed=em)





                    else:
                        inPlaying = 0
                        for player in insanePlayers:
                            if player[0] == message.author.id:
                                insanePlayers.remove(player)
                                await bot.delete_message(inMsg)






        if message.content.upper().startswith("-RESET"):
            if message.channel.id == bot_spam_channel_id:
                #await bot.send_message(message.channel, message.author.top_role)
                #perms_role = None
                #await bot.send_message(message.channel, perms_role)
                #resetters_toprole = message.author.top_role
                #if perms_role <= resetters_toprole.position:
                #    await bot.send_message(message.channel, "Success")
                #if "Test" in message.author.server.role_hierarchy:
                #    if "Test" <= message.author.top_role:
                #        await bot.send_message(message.channel, role)
                #perms_role = message.author.server.role.name("Test")
                if message.author.top_role.position > 0:

                    threeTTT = message.content.upper()[7:10]
                    twoMMWGDL = message.content.upper()[7:9]
                    tenMM = message.content.upper()[7:17]
                    nineTTTWG = message.content.upper()[7:16]
                    eightDL = message.content.upper()[7:15]
                    other = message.content.upper()[7:]

                    #await bot.send_message(message.channel, reset_game)
                    if tenMM == "MASTERMIND" or twoMMWGDL == "MM" or other == "oof":
                        guessNum = 0
                        combo = 0
                        mmplayer = 0
                        await bot.send_message(message.channel, "Mastermind has been reset!")

                    elif nineTTTWG == "TICTACTOE" or threeTTT == "TTT" or other == ["TICTACTOE","TTT"]:
                        tttP1 = 0
                        tttP2 = 0
                        tttBlank = ":black_medium_square:"
                        ttt1 = tttBlank
                        ttt2 = tttBlank
                        ttt3 = tttBlank
                        ttt4 = tttBlank
                        ttt5 = tttBlank
                        ttt6 = tttBlank
                        ttt7 = tttBlank
                        ttt8 = tttBlank
                        ttt9 = tttBlank
                        tttWinner = 0
                        tttStart = 0
                        tttTimer = 0
                        tttTime = 0
                        tttTimerStop = 0
                        when_to_stop = 0
                        await bot.send_message(message.channel, "TicTacToe has been reset!")

                    elif nineTTTWG == "WORDGUESS" or twoMMWGDL == "WG" or other == "oof":
                        word = 0
                        wg_stoper = 0
                        wg_play = False
                        await bot.send_message(message.channel, "Wordguess has been reset!")

                    elif eightDL == "DICELUCK" or twoMMWGDL == "DL" or other == "oof":
                        totalplayers = 0
                        player1name = 0
                        player2name = 0
                        player3name = 0
                        starttestgame = 0
                        roll1 = 0
                        roll2 = 0
                        roll3 = 0
                        roll4 = 0
                        roll5 = 0
                        keepRoll = 0
                        playersTurn = 0
                        currentRoll = 0
                        lastRoll = 0
                        currentTotal = 0
                        player1total = 0
                        player2total = 0
                        player3total = 0
                        numbOfDice = 5
                        diceluckGoal = 300
                        await bot.send_message(message.channel, "DiceLuck has been reset!")

                    elif threeTTT == "ALL":
                        word = 0
                        guessNum = 0
                        combo = 0
                        mmplayer = 0
                        totalplayers = 0
                        player1name = 0
                        player2name = 0
                        player3name = 0
                        starttestgame = 0
                        roll1 = 0
                        roll2 = 0
                        roll3 = 0
                        roll4 = 0
                        roll5 = 0
                        keepRoll = 0
                        playersTurn = 0
                        currentRoll = 0
                        lastRoll = 0
                        currentTotal = 0
                        player1total = 0
                        player2total = 0
                        player3total = 0
                        numbOfDice = 5
                        diceluckGoal = 300
                        tttP1 = 0
                        tttP2 = 0
                        tttBlank = ":black_medium_square:"
                        ttt1 = tttBlank
                        ttt2 = tttBlank
                        ttt3 = tttBlank
                        ttt4 = tttBlank
                        ttt5 = tttBlank
                        ttt6 = tttBlank
                        ttt7 = tttBlank
                        ttt8 = tttBlank
                        ttt9 = tttBlank
                        tttWinner = 0
                        tttStart = 0
                        tttTimer = 0
                        tttTime = 0
                        tttTimerStop = 0
                        when_to_stop = 0
                        await bot.send_message(message.channel, "Everything has been reset!")

                    elif twoMMWGDL == "C4" or eightDL == "CONNECT4":
                        C4_player1 = 0
                        C4_player2 = 0
                        C4_start = 0
                        C4_turn = 0

                        blankC4 = ":white_square_button:"
                        redC4 = ":red_circle:"
                        yellowC4 = ":large_orange_diamond:"
                        col1 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                        col2 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                        col3 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                        col4 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                        col5 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                        col6 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                        col7 = [blankC4,blankC4,blankC4,blankC4,blankC4,blankC4]
                        await bot.send_message(message.channel, "Connect4 has been reset!")

                    else:
                        await bot.send_message(message.channel, "Please choose a game to reset, or reset all with `-Reset All`")


                else:
                    await bot.send_message(message.channel, "You don't have permission to use this command, silly! Ask for a Mod+ to reset a game.")

        if message.content.upper().startswith("-STATUS"):
            if message.channel.id == bot_spam_channel_id:

                if word == 0:
                    wgStatus = "Not started"
                else:
                    wgStatus = "Current scramble is: " + scrambled_word

                if mmplayer == 0:
                    mmStatus = "Open"
                else:
                    mmStatus = "**" + mmplayer + "** is playing"

                if starttestgame == 0:
                    dlStatus = "Open"
                else:
                    if player1name == 0:
                        dlStatus = "Current players are **" + player2name + "** and **" + player3name + "**"
                    elif player2name == 0:
                        dlStatus = "Current players are **" + player1name + "** and **" + player3name + "**"
                    elif player3name == 0:
                        dlStatus = "Current players are **" + player1name + "** and **" + player2name + "**"
                    else:
                        dlStatus = "Current players are **" + player1name + "**, **" + player2name + "**, and **" + player3name + "**"

                if tttP1 == 0:
                    tttStatus = "Open"
                else:
                    tttStatus = "Current players are **" + tttP1 + "** and **" + tttP2 + "**"

                bot_status = """Game Status:

    Wordguess: %s

    Mastermind: %s

    DiceLuck: %s

    TicTacToe: %s"""%(wgStatus,mmStatus,dlStatus,tttStatus)

                #await bot.send_message(message.channel, "TEST")

                em = discord.Embed(title="Status", description=bot_status, colour=0xBCAD20)
                #await bot.send_message(message.channel, "TEST")
                em.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
                #await bot.send_message(message.channel, "TEST")
                await bot.send_message(message.channel, content=None, embed=em)


        if message.content.upper().startswith("-PING"):
            if message.channel.id == bot_spam_channel_id:
                now = datetime.datetime.utcnow()
                delta = now - message.timestamp
                await bot.send_message(message.channel, ":ping_pong: Pong! `{}ms`".format(int((round(delta.microseconds,-3))/1000)))













    await bot.process_commands(message)




bot.run(Bot_Token)

print("nexascain.exe has started successfully!")
