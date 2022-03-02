import asyncio

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, StartTime, bot
from userbot.utils import bash, edit_or_reply, zelda_cmd

@zelda_cmd(pattern="content (.*)")
async def amireallycuan(cuan):
    user = await bot.get_me()
    reply_message = await cuan.get_reply_message()
    capt = str(cuan.pattern_match.group(1).split(" ", 1)[1])
    link = str(cuan.pattern_match.group(1).split(" ", 2)[0])
    capti = capt.replace(".", " ")
    thumb = reply_message.media
    output = (
        f"{capt}\n\n"
        f"⬇️ **KLIK UNTUK MENONTON** ⬇️\n"
        f"{link}\n\n"
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
        "content": f"**Plugin : **`Content CH`\
        \n\n  •  **Syntax :** `{cmd}content` <Link> <Caption>\
        \n  •  **Function : **Untuk membuat Content Pada Channel.\
        \n\n  •  **NOTE :** Balas/Reply ke gambar untuk di jadikan Thumbnail Content.\
    "
    }
)