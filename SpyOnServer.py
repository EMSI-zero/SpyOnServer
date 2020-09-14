import discord
from discord.ext import commands
import random


class player:
    
    def __init__(self , member):
        self.member = member
        self.wins = 0
        self.spy = False
        self.suspicions = 0
    
    #adds to players wins for scoreboard
    def wins(self):
        self.wins += 1

    #reinitiates player spy status
    def replay(self):
        self.spy = False

    #sets the player as the spy
    def setSpy(self):
        self.spy = True    



#creates the client
client = commands.Bot(command_prefix='/')

#list of players
players = []

GameStarted = False


#This event makes sure that the bot is online
@client.event
async def on_ready():
    print('Bot is online!')

#Starts the Game
@client.command()
async def GameStart(ctx):
    if(not GameStarted):
        GameStarted = True
        ctx.send('To All Agents! \nATTENTION! \nThere is a Spy among us! Find the culprit and bring him in ASAP!')

    else:
        ctx.send('The search has already begun!')
        

#adds a vote to players Suspicion votes
@client.command()
async def Suspect(member):
    for pp in players:
        if pp.member is member:
            pp.suspicions += 1
    


client.run('NzU0ODc2MDY1MDU4NjUyMjMx.X17HHg.xsW-RpHyTX2FMNAnd-q_-aXQAF8')#recieves the token generated by discord. This token will be regenerated.