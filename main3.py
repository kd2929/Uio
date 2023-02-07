import requests
import json
import subprocess
from pyrogram.types.messages_and_media import message
import helper
from pyromod import listen
from pyrogram.types import Message
import tgcrypto
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from p_bar import progress_bar
import subprocess
from subprocess import getstatusoutput
import logging
import os
import sys
import re
from pyrogram import Client as bot
DEF_FORMAT = "480"
from dotenv import load_dotenv
load_dotenv()
os.makedirs("./downloads", exist_ok=True)
bot = Client(
    "bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)
async def exec(cmd):
  proc = await asyncio.create_subprocess_exec(*cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
  stdout, stderr = await proc.communicate()
  print(stdout.decode())
  return proc.returncode,stderr.decode()
  
  
  
  
@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
 editable = await m.reply_text("**Hi BOSS I'm Alive**")

@bot.on_message(filters.command(["txt"]))
async def account_login(bot: Client, m: Message):
    global cancel
    cancel = False
    editable = await m.reply_text("**Send Text file containing Urls**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/"

    try:    
        with open(x, "r") as f:
            content = f.read()
        content = content.split("\n")
        links = []
        for i in content:
            links.append(i.split(":", 1))
        os.remove(x)
        # print(len(links))
    except:
        await m.reply_text("Invalid file input.")
        os.remove(x)
        return
    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    try:
        arg = int(raw_text)
    except:
        arg = 0
    editable = await editable.edit("**Enter Batch Name**")
    input01: Message = await bot.listen(editable.chat.id)
    mm = input01.text    
    editable = await editable.edit("**Downloaded By**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    await editable.edit("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    vid_format = input2.text

    editable = await editable.edit("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/cef3ef6ee69126c23bfe3.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"
    if raw_text =='0':
        count =1
    else:       
        count = int(raw_text)
    for i in range(arg, len(links)):
      try:
        url = links[i][1]
        name = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@","").replace("*","").replace(".","").strip()
      except IndexError:
        pass
      command_to_exec = [
              "yt-dlp",
              "--no-warnings",
              "--socket-timeout",
              "30",
              "-R",
              "25",
              url,
              "--fragment-retries",
              "25",
              "--external-downloader",
              "aria2c",
              "--downloader-args",
              "aria2c: -x 16 -j 32"
          ]
      if "youtu" in url:
          ytf = f"b[height<={vid_format}][ext=mp4]/bv[height<={vid_format}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
          command_to_exec.extend(["-f",ytf,"-o",name+".%(ext)s", ])
      elif ".m3u8" in url:
        ytf = f"b[height<={vid_format}]/bv[height<={vid_format}]+ba"  
        command_to_exec.extend(["-f",ytf,"-o",name+".%(ext)s", ])
      elif ".pdf" in url:
          command_to_exec.extend(['yt-dlp','-o',f'{name}.pdf',url])
      else:
        ytf = f"{ytf}/b[height<={vid_format}]/bv[height<={vid_format}]+ba/b/bv+ba"
      ytf = f"{ytf}/b[height<={DEF_FORMAT}]/bv[height<={DEF_FORMAT}]+ba/b/bv+ba"  
      command_to_exec.extend(["-f",ytf,"-o",name+".%(ext)s"])
      Show = f"**Downloading**: __{name}__\n"
      await exec(command_to_exec)
      prog = await m.reply_text(Show)
      if ".pdf" in url:
          cc2 = f'{str(count).zfill(2)}. {name}\n\n**Batch »** {mm}\n**Dowloaded By »** {raw_text0}'
          await bot.send_document(document = name+".pdf",caption=cc2)
          os.remove(f"{name}")
          count+=1
      try:
        if thumb == "no":
            thumbnail = f"{name}.jpg"
        else:
            thumbnail = "thumb.jpg"
      except Exception as e:
        await m.reply_text(str(e))
        continue
      else:
        start_time = time.time()
        cc = f'{str(count).zfill(2)}. {name} - {vid_format}p\n\n**Batch »** {mm}\n**Dowloaded By »** {raw_text0}'
        try:
          duration, width, height = get_video_attributes(path)
        except:
            duration = width = height = 0
            pass
        try:
          await bot.send_video(
              m.chat.id,
              video=name+".mp4",
              caption=cc,
              duration=duration,
              width=width,
              height=height,
              file_name=name,
              supports_streaming=True)
          count+=1    
          await prog.delete (True)
          os.remove(name+".mp4")
        except:pass  
          

@bot.on_message(filters.command(["cancel"]))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled😡")
    return
@bot.on_message(filters.command("restart"))
async def restart_handler(_, m):
    await m.reply_text("Restarted!🙄", True)
    os.execl(sys.executable, sys.executable, *sys.argv)
   












 
bot.run()    
