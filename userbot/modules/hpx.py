import asyncio

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime, bot
from userbot.utils import bash, edit_or_reply, zelda_cmd

hpx_thumb = "https://telegra.ph/file/6c06e1d0a0183d0f4da06.jpg"

@zelda_cmd(pattern="hpx (.*)")
async def amireallycuan(cuan):
    user = await bot.get_me()
    reply_message = await cuan.get_reply_message()
    capt = str(cuan.pattern_match.group(1).split(" ", 1)[1])
    link = str(cuan.pattern_match.group(1).split(" ", 2)[0])
    capti = capt.replace(".", " ")
    thumb = hpx_thumb
    output = (
        f"✰ {capt}\n\n"
        f"**LINK NOBAR** 🎞🔞\n"
        f"{link}\n\n"
        f"-----------------------------------\n"
        f"📍**LIHAT LEBIH BANYAK :**\n"
        "@asupanhypersex - @hyperseexx"
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
        "content_hpx": f"**Plugin : **`Content CH`\
        \n\n  •  **Syntax :** `{cmd}hpx` <Link> <Caption>\
        \n  •  **Function : **Untuk membuat Content Pada Channel.\
    "
    }
)
