import requests
import json
import subprocess
import pyrogram
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message

from pyrogram import Client, filters
import tgcrypto
from p_bar import progress_bar
from details import api_id, api_hash, bot_token, sudo_groups
from subprocess import getstatusoutput
import helper
import logging
import time
from aiohttp import ClientSession
import asyncio
import aiofiles
from pyrogram.types import User, Message
# import progressor
# from progressor import progress_for_pyrogram
import sys
import re
import os
# import pycurl
# By... heArt🖤
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'http://www.visionias.in/',
    'Sec-Fetch-Dest': 'iframe',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'cross-site',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

# quality dict
visionias_quality_dict = {
    "144": "164000",
    "240": "234000",
    "360": "314000",
    "480": "414000",
    "720": "696000",
}

visionias_url_extract_pattern = r"(https://.*?playlist.m3u8.*?)\""

bot = Client(

    "bot",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token)

# bot = Client(
#    "bot",
#    bot_token=os.environ.get("BOT_TOKEN"),
#    api_id=int(os.environ.get("API_ID")),
#    api_hash=os.environ.get("API_HASH")
# )
# auth_users = [ int(chat) for chat in os.environ.get("AUTH_USERS").split(",") if chat != '']
# sudo_users = auth_users
# sudo_groups = [ int(chat) for chat in os.environ.get("GROUPS").split(",")  if chat != '']


@bot.on_message(filters.command(["start"]) & (filters.chat(sudo_groups)))
async def account_login(bot: Client, m: Message):

    editable = await m.reply_text("**Hellow deAr,** i am here for multipurpose & in **under construction.**\n\n**Developer:** Bʟᴀᴄᴋ⚡Ꭺᴅᴀᴍ️ \n**Language:**🔥Python\n\n**All running commands are:-**\n\n/txt\n/adda_pdf\n/jw\n/Link\n/top\n/cw\n/pw\n\n**BOT IS IN  UNDERCONSTRUCTION.**\n")


@bot.on_message(filters.command(["cancel"]) & (filters.chat(sudo_groups)))
async def cancel(_, m):
    editable = await m.reply_text("Canceling All process Plz wait")
    global cancel
    cancel = True
    await editable.edit("cancled😡")
    return


@bot.on_message(filters.command("restart") & (filters.chat(sudo_groups)))
async def restart_handler(_, m):
    await m.reply_text("Restarted!🙄", True)
    os.execl(sys.executable, sys.executable, *sys.argv)


@bot.on_message(filters.command(["txt"]) & (filters.chat(sudo_groups)))
async def account_login(bot: Client, m: Message):

    editable = await m.reply_text(" **Hello DeAr,** I am Text Downloader Bot.\nI can download videos from text file one by one.\n\n**Developer:** Bʟᴀᴄᴋ⚡Ꭺᴅᴀᴍ️ \n**Language:**🔥Python\n\nNow Send Your **TXT File**\n")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

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
        await m.reply_text("Invalid file input.🥲")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text("**Enter Batch Name**")
                                 ('eg.CDS Viraat 1.0,2024')
                                 ('AFCAT GARUD 1 2024')
                                 ('Mains Batch Course ID')
                                 ('Foundation Batch Course')
    
        
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text
    
    await m.reply_text("**Enter Date 🌹**")
    input4: Message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text

    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    

    editable4 = await m.reply_text("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers=headers) as resp:
                        text = await resp.text()
                        url = re.search(
                            visionias_url_extract_pattern, text).group(1)

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace(
                "#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").strip()

            if raw_text2 == "144":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '256x144' in out:
                    ytf = f"{out['256x144']}"
                elif '320x180' in out:
                    ytf = out['320x180']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data1 in out:
                        ytf = out[data1]
            elif raw_text2 == "180":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '320x180' in out:
                    ytf = out['320x180']
                elif '426x240' in out:
                    ytf = out['426x240']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data2 in out:
                        ytf = out[data2]
            elif raw_text2 == "240":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '426x240' in out:
                    ytf = out['426x240']
                elif '426x234' in out:
                    ytf = out['426x234']
                elif '480x270' in out:
                    ytf = out['480x270']
                elif '480x272' in out:
                    ytf = out['480x272']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data3 in out:
                        ytf = out[data3]
            elif raw_text2 == "360":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '640x360' in out:
                    ytf = out['640x360']
                elif '638x360' in out:
                    ytf = out['638x360']
                elif '636x360' in out:
                    ytf = out['636x360']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '638x358' in out:
                    ytf = out['638x358']
                elif '852x316' in out:
                    ytf = out['852x316']
                elif '850x480' in out:
                    ytf = out['850x480']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['852x470']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data4 in out:
                        ytf = out[data4]
            elif raw_text2 == "480":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '854x480' in out:
                    ytf = out['854x480']
                elif '852x480' in out:
                    ytf = out['852x480']
                elif '854x470' in out:
                    ytf = out['854x470']
                elif '768x432' in out:
                    ytf = out['768x432']
                elif '848x480' in out:
                    ytf = out['848x480']
                elif '850x480' in out:
                    ytf = ['850x480']
                elif '960x540' in out:
                    ytf = out['960x540']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data5 in out:
                        ytf = out[data5]

            elif raw_text2 == "720":

                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                # print(out)
                if '1280x720' in out:
                    ytf = out['1280x720']
                elif '1280x704' in out:
                    ytf = out['1280x704']
                elif '1280x474' in out:
                    ytf = out['1280x474']
                elif '1920x712' in out:
                    ytf = out['1920x712']
                elif '1920x1056' in out:
                    ytf = out['1920x1056']
                elif '854x480' in out:
                    ytf = out['854x480']
                elif '640x360' in out:
                    ytf = out['640x360']
                elif 'unknown' in out:
                    ytf = out["unknown"]
                else:
                    for data6 in out:
                        ytf = out[data6]
            elif "player.vimeo" in url:
                if raw_text2 == '144':
                    ytf = 'http-240p'
                elif raw_text2 == "240":
                    ytf = 'http-240p'
                elif raw_text2 == '360':
                    ytf = 'http-360p'
                elif raw_text2 == '480':
                    ytf = 'http-540p'
                elif raw_text2 == '720':
                    ytf = 'http-720p'
                else:
                    ytf = 'http-360p'
            else:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                for dataS in out:
                    ytf = out[dataS]

            try:
                if "unknown" in out:
                    res = "NA"
                else:
                    res = list(out.keys())[list(out.values()).index(ytf)]

                name = f'{str(count).zfill(3)}) {name1} {res}'
            except Exception:
                res = "NA"

            # if "youtu" in url:
            # if ytf == f"'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]'" or "acecwply" in url:
            if "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mp4 --no-warning "{url}"'
            elif "youtu" in url:
                cmd = f'yt-dlp -i -f "bestvideo[height<={raw_text2}]+bestaudio" --no-keep-video --remux-video mp4 --no-warning "{url}" -o "{name}.%(ext)s"'
            elif "player.vimeo" in url:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'
            elif "m3u8" or "livestream" in url:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'
            elif ytf == "0" or "unknown" in out:
                cmd = f'yt-dlp -f "{ytf}" --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'
            elif ".pdf" in url:
                cmd = "pdf"
            else:
                cmd = f'yt-dlp -f "{ytf}+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mp4 "{url}" -o "{name}.%(ext)s"'

            try:
                Show = f"**Downloading:-**\n\n**Name :-** `{name}\nQuality - {raw_text2}`\n\n**Url :-**\n`{url}`\n\n**With ❤️ From Admins**"
                prog = await m.reply_text(Show)
                cc = f'{str(count).zfill(3)}.  {name1} {res}@Black_Universal.mp4\n\n**Batch:** {raw_text0}\n\n**Date:** {raw_text4}\n\n**Downloaded By** :- Bʟᴀᴄᴋ⚡Ꭺᴅᴀᴍ️'
                cc1 = f'{str(count).zfill(3)}. {name1} {res}@Black_Universal.pdf\n\n**Batch:** {raw_text0}\n\n**Date:** {raw_text4}\n\n**Downloaded By** :- Bʟᴀᴄᴋ⚡Ꭺᴅᴀᴍ️'
#                 if cmd == "pdf" or "drive" in url:
#                     try:
#                         ka=await helper.download(url,name)
#                         await prog.delete (True)
#                         time.sleep(1)
#                         # await helper.send_doc(bot,m,cc,ka,cc1,prog,count,name)
#                         reply = await m.reply_text(f"Uploading - `{name}`\n\n**With ❤️ From Admins.**")
#                         time.sleep(1)
#                         start_time = time.time()
#                         await m.reply_document(ka,caption=cc1)
#                         count+=1
#                         await reply.delete (True)
#                         time.sleep(1)
#                         os.remove(ka)
#                         time.sleep(3)
#                     except FloodWait as e:
#                         await m.reply_text(str(e))
#                         time.sleep(e.x)
#                         continue
                if cmd == "pdf" or ".pdf" in url:
                    try:
                        ka = await helper.aio(url, name)
                        await prog.delete(True)
                        time.sleep(1)
                        reply = await m.reply_text(f"Uploading - ```{name}```\n\n**With ❤️ From Admins.**")
                        time.sleep(1)
                        start_time = time.time()
                        await m.reply_document(ka, caption=f'{str(count).zfill(3)}. {name1} {res}.pdf\n\n**Batch:** {raw_text0}\n\n**Downloaded By** :- Bʟᴀᴄᴋ⚡Ꭺᴅᴀᴍ️')
                        count += 1
                        # time.sleep(1)
                        await reply.delete(True)
                        time.sleep(1)
                        os.remove(ka)
                        time.sleep(3)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(f"**downloading failed **\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n**With ❤️ From Admins**")
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done.")


@bot.on_message(filters.command(["top"]) & (filters.chat(sudo_groups)))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(f"**Hello DeAr,** I am **TopRankers Downloader Bot.**\nI can download videos from text file one by one.\n\n**Developer:** HeArt🖤 \n**Language:**🔥Python\n\nNow Send Your **TXT File.**")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

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
        await m.reply_text("Invalid file input.🥲")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable = await m.reply_text(f"**Copy Paste the App Name of which you want to download videos.**\n\n`vikramjeet`\n\n`sure60`\n\n`theoptimistclasses`")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text0 = input0.text

    editable2 = await m.reply_text("**Enter Batch Name**")
    input5: Message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text

    editable4 = await m.reply_text("Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace("/", "").replace("+", "").replace("#", "").replace(
                "|", "").replace("@", "").replace(":", "").replace("*", "").replace(".", "").strip()
            # await m.reply_text(name +":"+ url)

            # Show = f"**Downloading:-**\n\n**Name :-** ```{name}\nQuality - {raw_text2}```\n\n**Url :-** ```{url}```"
            # prog = await m.reply_text(Show)
            # cc = f'>> **Name :** {name}\n>> **Title :** {raw_text0}\n\n>> **Index :** {count}'

            if raw_text0 in "vikramjeet":

                y = url.replace("/", "%2F")
#                 rout = f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2Flivehttporigin%2F{y[56:-14]}%2Fmaster.m3u8"
                rout = f"https://www.toprankers.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fsignedsec.toprankers.com%2F{y[39:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"
                # print (rout)
                # print(url)
            elif raw_text0 in "sure60":
                y1 = url.replace("/", "%2F")
#                 rout = f"https://onlinetest.sure60.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.sure60.com%2Flivehttporigin%2F{y[49:-14]}%2Fmaster.m3u8"
                rout = f"https://onlinetest.sure60.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.sure60.com%2F{y1[32:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"
            elif raw_text0 in "theoptimistclasses":
                y = url.replace("/", "%2F")
                rout = f"https://live.theoptimistclasses.com/?route=common/ajax&mod=liveclasses&ack=getcustompolicysignedcookiecdn&stream=https%3A%2F%2Fvodcdn.theoptimistclasses.com%2F{y[44:-14]}%2Fmaster.m3u8"
                getstatusoutput(f'curl "{rout}" -c "cookie.txt"')
                cook = "cookie.txt"

            name = f'{str(count).zfill(3)}) {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`\n\n**rout** :- `{rout}`"
            prog = await m.reply_text(Show)
            cc = f'{str(count).zfill(3)}.  {name1} {res}.mp4\n\n**Batch:** {raw_text0}\n\n**Downloaded By: Respected Admins❤️**'

            cmd = f'yt-dlp -o "{name}.mp4" --cookies {cook} "{url}"'
            try:
                download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
                os.system(download_cmd)
                filename = f"{name}.mp4"
                subprocess.run(
                    f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
                await prog.delete(True)
                reply = await m.reply_text(f"Uploading - ```{name}```\n\n**With ❤️ From Admins**")
                try:
                    if thumb == "no":
                        thumbnail = f"{filename}.jpg"
                    else:
                        thumbnail = thumb
                except Exception as e:
                    await m.reply_text(str(e))

                dur = int(helper.duration(filename))

                start_time = time.time()

                await m.reply_video(f"{name}.mp4", supports_streaming=True, height=720, width=1280, caption=cc, duration=dur, thumb=thumbnail, progress=progress_bar, progress_args=(reply, start_time))
                count += 1
                os.remove(f"{name}.mp4")

                os.remove(f"{filename}.jpg")
                os.remove(cook)
                await reply.delete(True)
                time.sleep(1)
            except Exception as e:
                await m.reply_text(f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}`\n\n**rout** :- `{rout}`")
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")


@bot.on_message(filters.command(["adda_pdf"]))
async def adda_pdf(bot: Client, m: Message):
    editable = await m.reply_text(f"**Hi im Pdf Adda pdf dl**\n\n**Developer:** HeArt🖤 \n**Language:**🔥Python\n\nNow send your file to download **ADDA PDFs**\n")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

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
        await m.reply_text("Invalid file input.🥲")
        os.remove(x)
        return

    editable = await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text

    try:
        arg = int(raw_text)
    except:
        arg = 0

    editable2 = await m.reply_text("**Enter Token**")
    input5: Message = await bot.listen(editable.chat.id)
    raw_text5 = input5.text

    if raw_text == '0':
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(arg, len(links)):

            url = links[i][1]
            name1 = links[i][0].replace("\t", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace(
                "@", "").replace(":", "").replace("*", "").replace(".", "").replace("'", "").replace('"', '').strip()
            name = f'{str(count).zfill(3)} {name1}'
            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url}`"
            prog = await m.reply_text(Show)
            cc = f'{str(count).zfill(3)}. {name1}.pdf\n'
            try:
                getstatusoutput(
                    f'curl --http2 -X GET -H "Host:store.adda247.com" -H "user-agent:Mozilla/5.0 (Linux; Android 11; moto g(40) fusion Build/RRI31.Q1-42-51-8; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36" -H "accept:*/*" -H "x-requested-with:com.adda247.app" -H "sec-fetch-site:same-origin" -H "sec-fetch-mode:cors" -H "sec-fetch-dest:empty" -H "referer:https://store.adda247.com/build/pdf.worker.js" -H "accept-encoding:gzip, deflate" -H "accept-language:en-US,en;q=0.9" -H "cookie:cp_token={raw_text5}" "{url}" --output "{name}.pdf"')
                await m.reply_document(f"{name}.pdf", caption=cc)
                count += 1
                await prog.delete(True)
                os.remove(f"{name}.pdf")
                time.sleep(2)
            except Exception as e:
                await m.reply_text(f"{e}\nDownload Failed\n\nName : {name}\n\nLink : {url}")
                continue
    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("Done")

@bot.on_message(filters.command("jw"))

async def account_login(bot: Client, m: Message):

    editable = await m.reply_text("Hello Bruh **I am jw Downloader Bot**. ")

    input: Message = await bot.listen(editable.chat.id)

    x = await input.download()

    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

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

    editable = await m.reply_text(

        f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **0**"

    )

    input1: Message = await bot.listen(editable.chat.id)

    raw_text = input1.text

    try:

        arg = int(raw_text)

    except:

        arg = 0

    editable = await m.reply_text("**Enter Title**")

    input0: Message = await bot.listen(editable.chat.id)

    raw_text0 = input0.text

    await m.reply_text("**Enter resolution**")

    input2: Message = await bot.listen(editable.chat.id)

    raw_text2 = input2.text

    editable4 = await m.reply_text(

        "Now send the **Thumb url**\nEg : ```https://telegra.ph/file/d9e24878bd4aba05049a1.jpg```\n\nor Send **no**"

    )

    input6 = message = await bot.listen(editable.chat.id)

    raw_text6 = input6.text

    thumb = input6.text

    if thumb.startswith("http://") or thumb.startswith("https://"):

        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")

        thumb = "thumb.jpg"

    else:

        thumb == "no"

    if raw_text == '0':

        count = 1

    else:

        count = int(raw_text)

    try:

        for i in range(arg, len(links)):

            url = links[i][1]

            name1 = links[i][0].replace("\t", "").replace(":", "").replace(

                "/",

                "").replace("+", "").replace("#", "").replace("|", "").replace(

                    "@", "").replace("*", "").replace(".", "").strip()

            if "classplusapp" in url:

                headers = {

                    'Host': 'api.classplusapp.com',

                    'x-access-token':'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6OTI5MDk0NTYsIm9yZ0lkIjozNDgzNzksInR5cGUiOjEsIm1vYmlsZSI6IjkxODg3MzU1NDk2MyIsIm5hbWUiOiJBZGFyc2ggQ2hhdWRoYXJ5ICIsImVtYWlsIjpudWxsLCJpc0ludGVybmF0aW9uYWwiOjAsImRlZmF1bHRMYW5ndWFnZSI6ImVuIiwiY291bnRyeUNvZGUiOiJJTiIsImNvdW50cnlJU08iOiI5MSIsInRpbWV6b25lIjoiR01UKzU6MzAiLCJpc0RpeSI6ZmFsc2UsImZpbmdlcnByaW50SWQiOiI4YzUxYzYwMTk1NWUzMTg3NTJjODAwMmMxNTBhZTdlZiIsImlhdCI6MTY4NTY5OTY3MSwiZXhwIjoxNjg2MzA0NDcxfQ.qU6QcWj2f1oBvtFdL54scMXLSa5--1tjSow2sMt6cTvHnKLRmr-MTbEyxW4JnTaS&EIO',

                    'user-agent': 'Mobile-Android',

                    'app-version': '1.4.37.1',

                    'api-version': '18',

                    'device-id': '5d0d17ac8b3c9f51',

                    'device-details':

                    '2848b866799971ca_2848b8667a33216c_SDK-30',

                    'accept-encoding': 'gzip',

                }

                params = (('url', f'{url}'), )

                response = requests.get(

                    'https://api.classplusapp.com/cams/uploader/video/jw-signed-url',

                    headers=headers,

                    params=params)

                a = response.json()['url']

                # print(a)

                #print(a)

                url1 = str(a)

                #print(url1)

            else:

                url1 = url

            name = f'{str(count).zfill(3)}) {name1}'

            Show = f"**Downloading:-**\n\n**Name :-** `{name}`\n\n**Url :-** `{url1}`"

            prog = await m.reply_text(Show)

            cc = f'**Title »** {name1}.mp4\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}\n\n**Downloaded By** :- Bʟᴀᴄᴋ⚡Ꭺᴅᴀᴍ️'

            cc1 = f'**Title »** {name1}.pdf\n**Caption »** {raw_text0}\n**Index »** {str(count).zfill(3)}\n\n**Downloaded By** :- Bʟᴀᴄᴋ⚡Ꭺᴅᴀᴍ️'

            try:

              if "pdf" in url:

                cmd1 = f'yt-dlp -o "{name}.pdf" "{url}"'

                os.system(cmd1)

                if os.path.isfile(f"{name}.mp4"):

                    filename = f"{name}.mp4"

                elif os.path.isfile(f"{name}.mp4"):

                    filename = f"{name}.mp4"

                elif os.path.isfile(f"{name}.pdf"):

                    filename = f"{name}.pdf"

                await m.reply_document(filename, caption=cc)

                os.remove(filename)

                await prog.delete(True)

              else:

                cmd2 = f'yt-dlp "{url1}" -N 45 --external-downloader aria2c --external-downloader-args "-s16 -x16" --no-check-certificate --geo-bypass-country IN -S "res:{raw_text2}" -o "{name}.mp4"'

                os.system(cmd2)

                if os.path.isfile(f"{name}.mp4"):

                    filename = f"{name}.mp4"

                elif os.path.isfile(f"{name}.mp4"):

                    filename = f"{name}.mp4"

                elif os.path.isfile(f"{name}.pdf"):

                    filename = f"{name}.pdf"

#                 filename = f"{name}.mp4"

                subprocess.run(

                    f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"',

                    shell=True)

                await prog.delete(True)

                reply = await m.reply_text(f"Uploading - ```{name}```")

                try:

                    if thumb == "no":

                        thumbnail = f"{filename}.jpg"

                    else:

                        thumbnail = thumb

                except Exception as e:

                    await m.reply_text(str(e))

                dur = int(helper.duration(filename))

                start_time = time.time()

                if "pdf" in url:

                    await m.reply_document(filename, caption=cc)

                else:

                    await m.reply_video(filename,

                                        supports_streaming=True,

                                        height=720,

                                        width=1280,

                                        caption=cc,

                                        duration=dur,

                                        thumb=thumbnail,

                                        progress=progress_bar,

                                        progress_args=(reply, start_time))

                count += 1

                os.remove(filename)

                os.remove(f"{filename}.jpg")

                await reply.delete(True)

                time.sleep(1)

            except Exception as e:

                await m.reply_text(

                    f"**downloading failed ❌**\n{str(e)}\n**Name** - {name}\n**Link** - `{url}` & `{url1}`"

                )

                continue

    except Exception as e:

        await m.reply_text(e)

    await m.reply_text('Done')

        

    



    
@bot.on_message(filters.command(["link"]))
async def upload(bot: Client, m: Message):
    editable = await m.reply_text('Send link in **Name&link** format to download')
    input9: Message = await bot.listen(editable.chat.id)
    raw = input9.text    
    name = raw.split('&')[0]
    url = raw.split('&')[1] or raw
    await m.reply_text("**Enter resolution**")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    
    Show = f"**Downloading:-**\n\n**Name :-** ```{name}\nQuality - {raw_text2}```\n\n**Url :-** ```{url}```"
    prog = await m.reply_text(Show)
    
    cc = f'>> **Name :** {name}'
    
    
    if "youtu" in url:
        if raw_text2 in ["144", "240", "480"]:
            ytf = f'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]'
        elif raw_text2 == "360":
            ytf = "18/134"
        elif raw_text2 == "720":
            ytf = "22/136/18"
        elif raw_text2 =="1080":
            ytf = "137/399"
        else:
            ytf = 18
    else:
        ytf=f"bestvideo[height<={raw_text2}]"

    if "jwplayer" in url:
        if raw_text2 in ["180", "144"]:
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf = f"{out['320x180 ']}/{out['256x144 ']}"
            except Exception as e:
                if e==0:
                    raw_text2=="no"
        elif raw_text2 in ["240", "270"]:
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf = f"{out['480x270 ']}/{out['426x240 ']}"
            except Exception as e:
                if e==0:
                    raw_text2=="no"
        elif raw_text2 == "360":
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf = out['640x360 ']
            except Exception as e:
                if e == 0:
                    raw_text2=="no"
                #cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
        elif raw_text2 == "480":
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf = f"{out['960x540 ']}/{out['852x480 ']}"
            except Exception as e:
                if e==0:
                    raw_text2=="no"
            # cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
        elif raw_text2 == "720":
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf = f"{out['1280x720 ']}"
            except Exception as e:
                if e==0:
                    raw_text2=="no"
            # cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
        elif raw_text2 == "1080":
            try:
                cmd = f'yt-dlp -F "{url}"'
                k = await helper.run(cmd)
                out = helper.vid_info(str(k))
                ytf =f"{out['1920x1080 ']}/{['1920x1056']}"
            except Exception as e:
                if e==0:
                    raw_text2=="no"
        else:
            # cmd = f'yt-dlp -F "{url}"'
            # k = await helper.run(cmd)
            #out = helper.vid_info(str(k))
            # ytf = out['640x360 ']
            #cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
            raw_text2=="no"
#             except Exception as e:
#                 print(e)

    if ytf == f'bestvideo[height<={raw_text2}][ext=mp4]+bestaudio[ext=m4a]':
        cmd = f'yt-dlp -o "{name}.mp4" -f "{ytf}" "{url}"'

    # elif "jwplayer" in url:# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
    #     cmd=f'yt-dlp -o "{name}.mp4" "{url}"'    
    elif "adda247" in url:# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
        cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
    elif "kdcampus" or "streamlock" in url:
        cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
    elif ".pdf" in url: #and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
    elif "drive" in url:
        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
    elif raw_text2 == "no":# and raw_text2 in ["144", "240", "360", "480", "720", "no"]:
        cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
#             elif "unknown" in ytf:
#                 cmd=f'yt-dlp -o "{name}.mp4" "{url}"'
    else:
        cmd = f'yt-dlp -o "{name}.mp4" -f "{ytf}+bestaudio" "{url}"'

    try:
        download_cmd = f"{cmd} -R 25 --fragment-retries 25 --external-downloader aria2c --downloader-args 'aria2c: -x 16 -j 32'"
        os.system(download_cmd)
        filename = f"{name}.mp4"
        subprocess.run(f'ffmpeg -i "{filename}" -ss 00:01:00 -vframes 1 "{filename}.jpg"', shell=True)
        thumbnail = f"{filename}.jpg"
        dur = int(helper.duration(filename))
        await prog.delete (True)
        try:
            await m.reply_video(f"{name}.mp4",caption=cc, supports_streaming=True,height=720,width=1280,thumb=thumbnail,duration=dur)

        except:
            await m.reply_text("There was an error while uploading file as streamable so, now trying to upload as document.")
            await m.reply_document(f"{name}.webm",caption=cc)
        os.remove(f"{name}.mp4")
        os.remove(f"{filename}.jpg")
    except Exception as e:
        await m.reply_text(e)
        await m.reply_text("Done")


    















#   CAREERWILL DOWNLOADER  BOT 













        
         

































bot.run()






    


