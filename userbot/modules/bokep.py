import asyncio

from userbot import CMD_HELP, StartTime, bot
from userbot.utils import bash, edit_or_reply, zelda_cmd

@zelda_cmd(pattern="sxs (.*)")
async def amireallysxs(sxs):
    user = await bot.get_me()
    capt = str(sxs.pattern_match.group(1).split(" ", 2)[0])
    link = str(sxs.pattern_match.group(1).split(" ", 2)[1])
    capti = capt.replace(".", " ")
    thumb = "https://telegra.ph/file/ddb9147429cae2ae6135e.jpg"
    await sxs.edit("__Please Wait.__")
    await sxs.edit("__Please Wait..__")
    await sxs.edit("__Please Wait.__")
    await sxs.edit("__Please Wait..__")
    await sxs.edit("__Creating Content...__")
    await sxs.edit("__Creating Content..__")
    await sxs.edit("__Creating Content...__")
    await sxs.edit("⚡")
    await asyncio.sleep(2)
    output = (
        f"**{capti}**\n\n"
        f"⬇️ KLIK UNTUK MENONTON ⬇️\n"
        f"{link}\n\n"
        f"📍Support Join : @LustsketchID\n"
        f"📍Free VIP : @VIPLiveRecords\n"
    )
    if thumb:
        try:
            logo = thumb
            await sxs.delete()
            msg = await bot.send_file(sxs.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            # await msg.delete()
        except BaseException:
            await sxs.edit(
                output + "\n\n ***Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo**"
            )
            # await asyncio.sleep(100)
            # await sxs.delete()
    else:
        await edit_or_reply(sxs, output)
        
        
@zelda_cmd(pattern="lsid (.*)")
async def amireallylsid(lsid):
    user = await bot.get_me()
    capt = str(lsid.pattern_match.group(1).split(" ", 2)[0])
    link = str(lsid.pattern_match.group(1).split(" ", 2)[1])
    capti = capt.replace(".", " ")
    thumb = "https://telegra.ph/file/22eda4c6851fd81b3b46a.jpg"
    await lsid.edit("__Please Wait.__")
    await lsid.edit("__Please Wait..__")
    await lsid.edit("__Please Wait.__")
    await lsid.edit("__Please Wait..__")
    await lsid.edit("__Creating Content...__")
    await lsid.edit("__Creating Content..__")
    await lsid.edit("__Creating Content...__")
    await lsid.edit("⚡")
    await asyncio.sleep(2)
    output = (
        f"**{capti}**\n\n"
        f"⬇️ Your Link\n"
        f"{link}\n\n"
        f"📍Support Join : @SexualSins58\n"
        f"📍Free VIP : @VIPLiveRecords\n"
    )
    if thumb:
        try:
            logo = thumb
            await lsid.delete()
            msg = await bot.send_file(lsid.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            # await msg.delete()
        except BaseException:
            await lsid.edit(
                output + "\n\n ***Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo**"
            )
            # await asyncio.sleep(100)
            # await lsid.delete()
    else:
        await edit_or_reply(lsid, output)
        
        
CMD_HELP.update(
    {
        "ch_asupan": f"**Plugin : **`asupan`\
        \n\n**KHUSUS UNTUK OWNER BOT. BELUM TERSEDIA UNTUK USER**\
    "
    }
)
