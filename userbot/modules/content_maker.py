import asyncio

from userbot import CMD_HELP, StartTime, bot
from userbot.utils import bash, edit_or_reply, zelda_cmd

@zelda_cmd(pattern="cm (.*)")
async def amireallycontent(content):
    user = await bot.get_me()
    capt = str(content.pattern_match.group(1).split(" ", 2)[0])
    link = str(content.pattern_match.group(1).split(" ", 2)[1])
    capti = capt.replace(".", " ")
    thumb = "https://telegra.ph/file/412f0f8da4a86a6fa75ff.jpg"
    await asyncio.sleep(2)
    output = (
        f"**{capti}**\n\n"
        f"⬇️ KLIK UNTUK MENONTON ⬇️\n"
        f"{link}"
    )
    if thumb:
        try:
            logo = thumb
            await content.delete()
            msg = await bot.send_file(content.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            # await msg.delete()
        except BaseException:
            await content.edit(
                output + "\n\n ***Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo**"
            )
            # await asyncio.sleep(100)
            # await content.delete()
    else:
        await edit_or_reply(content, output)
        
        
CMD_HELP.update(
    {
        "content": f"**Plugin : **`asupan`\
        \n\n**KHUSUS UNTUK OWNER BOT. BELUM TERSEDIA UNTUK USER**\
    "
    }
)
