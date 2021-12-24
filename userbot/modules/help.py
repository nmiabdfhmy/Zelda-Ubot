# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot help command """

from userbot import CHANNEL
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, ICON_HELP, bot
from userbot.utils import edit_delete, edit_or_reply, zelda_cmd

modules = CMD_HELP

HELP_TEXT = """⭐ **MODULES PART 1**
• `admin` • `pin` • `undelete` • `gmute` • `zombies` • `adzan` • `aeshtetic` • `afk` • `amongus` • `android` • `animals` • `animasi` • `anime` • `anti_spambot` • `antiflood` • `watch` • `randompp` • `glitch` • `grab` • `bannedall`

⭐ **MODULES PART 2**
• `rnupload` • `appmisc` • `arts` • `ascii` • `asupan` • `blacklist` • `ping` • `speedtest` • `broadcast` • `vcplugin` • `carbon` • `chat` • `invite` • `kickme` • `link` • `regexninja` • `scraper` • `chatbot` • `clone` • `convert`

⭐ **MODULES PART 3**
• `core` • `covid` • `membuat` • `custom` • `deepfry` • `direct` • `emojigames` • `json` • `eval` • `exec` • `term` • `fakeaction` • `fakegban` • `fban` • `figlet` • `file` • `filter` • `rgif` • `fun` • `funmemes`

⭐ **MODULES PART 4**
• `games` • `gcast` • `gucast` • `id` • `getmusic` • `gcommit` • `github` • `gkick` • `gban` • `gps` • `hash` • `base64` • `hazmat` • `helper` • `hentai` • `heroku` • `database` • `imgmeme` • `justfun` • `secretchat`

⭐ **MODULES PART 5**
• `kamuii` • `lastfm` • `locks` • `log` • `logo` • `lyrics` • `memes` • `scam` • `memify` • `mentions` • `send` • `random` • `sleep` • `repo` • `readme` • `restart` • `shutdown` • `raw` • `repeat` • `nekos`

⭐ **MODULES PART 6**
• `nhentai` • `notes` • `nsfw` • `war` • `view` • `open` • `dm` • `sendbot` • `tmsg` • `getlink` • `unbanall` • `limit` • `paste` • `pdf` • `phreaker` • `pic` • `pmbot` • `pmpermit` • `profil` • `punten`

⭐ **MODULES PART 7**
• `purge` • `quotly` • `rastick` • `reverse` • `salam` • `sangmata` • `download` • `tts` • `translate` • `removebg` • `ocr` • `google` • `wiki` • `barcode` • `image_search` • `ytdl` • `screenshot` • `currency` • `ud` • `sed`

⭐ **MODULES PART 8**
• `shazam` • `shortlink` • `sosmed` • `spam` • `ssvideo` • `stats` • `deteksi` • `stickers` • `sticker_v2` • `sudo` • `system` • `alive` • `tagger` • `tag` • `telegraph` • `tiktok` • `timedate` • `tiny` • `torrent` • `transform`

⭐ **MODULES PART 8**
• `update` • `getid` • `vcg` • `waifu` • `wallpaper` • `weather` • `webupload` • `welcome` • `whois` • `wordcloud` • `xiaomi` • `zipfile`
"""


@zelda_cmd(pattern="help(?: |$)(.*)")
async def help(event):
    """For help command"""
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await edit_or_reply(event, str(CMD_HELP[args]))
        else:
            await edit_delete(event, f"`{args}` **Bukan Nama Modul yang Valid.**")
    else:
        user = await bot.get_me()
        string = ""
        for i in CMD_HELP:
            string += "`" + str(i)
            string += f"`\t\t\t{ICON_HELP}\t\t\t"
        await edit_or_reply(
            event,
            f"**Daftar Perintah Untuk [ZELDA USERBOT](https://github.com/nmiabdfhmy/Zelda-Ubot) :**\n\n"
            f"**Jumlah : ** `{len(modules)}` Modules\n"
            f"**Owner : ** [Lord Zelda](https://t.me/UnrealZlda)\n\n"
            f"{HELP_TEXT}"
            f"\n\nJoin and Support @{CHANNEL}",
        )
        await event.reply(
            f"\n**Contoh Ketik** `{cmd}help ping` **Untuk Melihat Informasi Module**"
        )
