import asyncio

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime, bot
from userbot.utils import bash, edit_or_reply, zelda_cmd

hpx_thumb = "https://telegra.ph/file/6443a8f61a0194b065221.mp4"

@zelda_cmd(pattern="hcm (.*)")
async def amireallycuan(cuan):
    user = await bot.get_me()
    reply_message = await cuan.get_reply_message()
    capt = str(cuan.pattern_match.group(1).split(" ", 1)[1])
    link = str(cuan.pattern_match.group(1).split(" ", 2)[0])
    capti = capt.replace(".", " ")
    thumb = hpx_thumb
    output = (
        f"**{capt}**\n\n"
        f"**LINK VIDEO**\n"
        f"{link}\n\n"
        f"-----------------------------------\n"
        f"📍**JOIN :**\n"
        "@HCMutualism\n@VIPLiveRecords"
    )
    if thumb:
        try:
            logo = thumb
            await cuan.delete()
            msg = await bot.send_file(cuan.chat_id, logo, caption=output)
            await asyncio.sleep(300)
        except BaseException:
            await cuan.edit(
                output + "\n\n ***Tidak Ada Thumbnail!"
                "\nHarap balas ke gambar untuk dijadikan thumbnail Content.**"
            )
    else:
        await edit_or_reply(cuan, output)
        
        
CMD_HELP.update(
    {
        "ch_hpx": f"**Plugin : **`Content CH`\
        \n\n  •  **Syntax :** `{cmd}hcm` <Link> <Caption>\
        \n  •  **Function : **Untuk membuat Content Pada Channel.\
    "
    }
)
