from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.muk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Muk`")
    sleep(3)
    await typew.edit("`20 Tahun`")
    sleep(1)
    await typew.edit("`Tinggal Di Tulungagung Jawa timur, Salam Kenal:)`")


@register(outgoing=True, pattern='^.repobot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("👻")
    sleep(2)
    await typew.edit("**🔥Ubot - Fork🔥**\n\n [Muk-Userbot](https://github.com/human-ordinary/Muk-Userbot)\n ")


@register(outgoing=True, pattern='^.ownerbot(?: |$)(.*)')  
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("👻")
    sleep(2)
    await typew.edit("**🔥Owner Bot🔥**\n\n [Muklas](https://t.me/iyainyabre)\n ")


# muk

CMD_HELP.update({
    "owner":
    "•CMD:`.muk`\
    \nPenjelasan: perkenalan ownwer.\
    \n\n•CMD:`.repobot`\
    \nPenjelasan: link github owner.\
    \n\n•CMD:`.ownerbot`\
    \nPenjelasan: telegram ownwer."
})
