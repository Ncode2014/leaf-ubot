# Copyright (C) 2020 KeselekPermen69
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

from hentai import Hentai

from userbot import CMD_HELP
from userbot.events import register
from userbot.modules.anime import post_to_telegraph


@register(outgoing=True, pattern=r"^\.nhentai(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    code = event.pattern_match.group(1)
    await event.edit("`Searching for doujin...`")
    try:
        doujin = Hentai(code)
    except BaseException as n_e:
        if "404" in str(n_e):
            return await event.edit(f"`{code}` is not found!")
        else:
            return await event.edit(f"**Error: **`{n_e}`")
    imgs = ""
    for url in doujin.image_urls:
        imgs += f"<img src='{url}'/>"
    imgs = f"&#8205; {imgs}"
    title = doujin.title()
    graph_link = post_to_telegraph(title, imgs)
    await event.edit(f"[{title}]({graph_link})", link_preview=True)


CMD_HELP.update(
    {"nhentai": ">`.nhentai` <code>" "\nUsage: View NHentai in Telegra.ph\n"}
)
