# ReCode by @mrismanaziz
# FROM ZELDA USERBOT <https://github.com/nmiabdfhmy/Zelda-Ubot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, bot
from userbot.events import zelda_cmd
from userbot.utils import edit_delete, edit_or_reply


@bot.on(zelda_cmd(outgoing=True, pattern=r"q ?(.*)"))
async def quotess(qotli):
    if qotli.fwd_from:
        return
    if not qotli.reply_to_msg_id:
        return await qotli.edit("**Mohon Balas Ke Pesan**")
    reply_message = await qotli.get_reply_message()
    if not reply_message.text:
        return await qotli.edit("**Mohon Balas Ke Pesan**")
    chat = "@QuotLyBot"
    if reply_message.sender.bot:
        return await qotli.edit("**Mohon Balas Ke Pesan**")
    await qotli.edit("**Sedang Memproses Sticker, Mohon Menunggu**")
    try:
        async with bot.conversation(chat) as conv:
            try:
                response = conv.wait_event(
                    events.NewMessage(
                        incoming=True,
                        from_users=1031952739))
                msg = await bot.forward_messages(chat, reply_message)
                response = await response
                """ - don't spam notif - """
                await bot.send_read_acknowledge(conv.chat_id)
            except YouBlockedUserError:
                return await qotli.reply("**Harap Jangan Blockir @QuotLyBot Buka Blokir Lalu Coba Lagi**")
            if response.text.startswith("Hi!"):
                await qotli.reply("**Silahkan Unblock @QuotLyBot dan coba lagi!!**")
            else:
                await qotli.delete()
                await bot.forward_messages(qotli.chat_id, response.message)
                await bot.send_read_acknowledge(qotli.chat_id)
                """ - cleanup chat after completed - """
                await qotli.client.delete_messages(conv.chat_id, [msg.id, response.id])                      
    except TimeoutError:
        await qotli.edit()


@bot.on(zelda_cmd(outgoing=True, pattern=r"qq ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await edit_delete(event, "**Mohon Balas ke Pesan**")
        return
    reply_message = await event.get_reply_message()
    warna = event.pattern_match.group(1)
    chat = "@QuotLyBot"
    await edit_or_reply(event, "`Processing...`")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1031952739)
            )
            first = await conv.send_message(f"/qcolor {warna}")
            ok = await conv.get_response()
            await asyncio.sleep(2)
            second = await bot.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("**Silahkan Unblock @QuotLyBot dan coba lagi!!**")
            return
        if response.text.startswith("Hi!"):
            await edit_or_reply(
                event, "**Mohon Menonaktifkan Pengaturan Privasi Forward Anda**"
            )
        else:
            await event.delete()
            await bot.forward_messages(event.chat_id, response.message)
    await bot.delete_messages(conv.chat_id, [first.id, ok.id, second.id, response.id])


CMD_HELP.update(
    {
        "quotly": f"**Plugin : **`quotly`\
        \n\n  •  **Syntax :** `{cmd}qq` <warna>\
        \n  •  **Function : **Membuat pesan mu menjadi sticker bisa custom warna background.\
    "
    }
)
