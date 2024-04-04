import urllib
import json
import requests
import discord
from discord.ext import commands
import datetime
import io
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_choice, create_option
from discord_slash import SlashCommand, SlashContext
 
from urllib import parse, request
from PIL import Image, ImageDraw, ImageFont, ImageFile
import time


with open("configuracion.json") as f: #Creamos un archivo de configuracion para el bot
    config = json.load(f)

bot = commands.Bot(command_prefix='!', description="ayuda bot") #Prefijo para el comando !trono
bot.remove_command("help") # Borra el comando por defecto !help




####
#Programado Por Jose89fcb
#Twitter: twitter.com/jose89fcb
####
slash = SlashCommand(bot, sync_commands=True)
@slash.slash(
    name="trono_pastel", description="Keko habbo Hotel",
    options=[
                create_option(
                  name="keko",
                  description="Escribe el keko",
                  option_type=3,
                  required=True
                ),create_option(
                  name="hotel",
                  description="Elige él hotel",
                  option_type=3,
                  required=True,
                  choices=[
                      create_choice(
                          name="ES - Hotel España",
                          value="es"
                      ),
                      create_choice(
                          name="BR - Hotel Brasil",
                          value="com.br"
                      ),
                      create_choice(
                          name="COM - Hotel Estados unidos",
                          value="com"
                      ),
                      create_choice(
                          name="DE - Hotel Aleman",
                          value="de"
                      ),
                      create_choice(
                          name="FR - Hotel Frances",
                          value="fr"
                      ),
                      create_choice(
                          name="FI - Hotel Finalandia",
                          value="fi"
                      ),
                      create_choice(
                          name="IT - Hotel Italiano",
                          value="it"
                      ),
                      create_choice(
                          name="TR - Hotel Turquia",
                          value="com.tr"
                      ),
                      create_choice(
                          name="NL - Hotel Holandés",
                          value="nl"
                      )
                  ]
                
               
                  
                )
             ])


async def _trono_monster(ctx:SlashContext, keko:str, hotel:str):
    await ctx.defer()
   
    
    response = requests.get(f"https://www.habbo.{hotel}/api/public/users?name={keko}")
   
    
    habbo = response.json()['figureString']
   

   
    

    
    
   
    
    url = "https://www.habbo.com/habbo-imaging/avatarimage?size=l&figure="+ habbo +"&action=sit&action=sit&direction=4&head_direction=4&gesture=std&size=m"
    img1 = Image.open(io.BytesIO(requests.get(url).content))
    img1 = img1.resize((64,110), Image.ANTIALIAS)#tamaño del keko
    
    


    
    


    

   

    

    
    
    



    img2 = img1.copy()
    
    
    almo = Image.open(r"imagenes/silla-parte-trono-pastel.png").convert("RGBA") #imagen de la trozo
    img1 = almo.resize((80,200), Image.ANTIALIAS)#tamaño de la silla

 



    
    

    
    


    img1.paste(img2,(10,30), mask = img2) #Posicion del keko 1
   
    ###
    

   

    img2 = img1.copy()
    pata = Image.open(r"imagenes/pata-parte-trono-pastel.png").convert("RGBA") #imagen de la pata
    img1 = pata.resize((80,200), Image.ANTIALIAS)#tamaño de la pata

    img1.paste(img2,(0,0), mask = img2) #Posicion del keko
    img1.paste(pata,(0,0), mask = pata) #Posicion del trozo de silla
    

    




    

    
    
    
   
    
   
       


      
    
       
      

      
    
       
            
        
        
        
       
        
    with io.BytesIO() as image_binary:
        img1.save(image_binary, 'PNG')
        image_binary.seek(0)
       
        
        await ctx.send(file=discord.File(fp=image_binary, filename=f'keko_{keko}.png'))

        
         
        
        
        
        


@bot.event
async def on_ready():
    print("BOT listo!")
    
bot.run(config["tokendiscord"])   
