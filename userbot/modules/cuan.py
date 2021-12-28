import asyncio

from userbot import CMD_HELP, StartTime, bot
from userbot.utils import bash, edit_or_reply, zelda_cmd

@zelda_cmd(pattern="cuan (.*)")
async def amireallycuan(cuan):
    user = await bot.get_me()
    reply_message = await cuan.get_reply_message()
    capt = str(cuan.pattern_match.group(1).split(" ", 2)[0])
    link = str(cuan.pattern_match.group(1).split(" ", 2)[1])
    capti = capt.replace(".", " ")
    thumb = reply_message.media
    output = (
        f"{capti}\n\n"
        f"⬇️ **KLIK UNTUK MENONTON** ⬇️\n"
        f"{link}\n\n"
        f"📍**Support Join :** \n•@LustsketchID\n•@SexualSins58\n"
        f"📍Free VVIP : @VIPLiveRecords\n"
    )
    if thumb:
        try:
            logo = thumb
            await cuan.delete()
            msg = await bot.send_file(cuan.chat_id, logo, caption=output)
            await asyncio.sleep(300)
        except BaseException:
            await cuan.edit(
                output + "\n\n ***Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo**"
            )
    else:
        await edit_or_reply(cuan, output)
        
        
CMD_HELP.update(
    {
        "ch_cuan": f"**cuan : **`asupan`\
        \n\n**KHUSUS UNTUK OWNER BOT. BELUM TERSEDIA UNTUK USER**\
    "
    }
)