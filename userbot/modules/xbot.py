# Copyright (C) 2021 King - Userbot
# Created by Apis
# Jangan hapus credit asu!!!

from random import choice

from userbot import CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
XBOT_STRINGS = [
    "Aku userbot",
    "Jangan main main ya!",
    "Gw gban mampus lu",
    "Gw pake Muk-Userbot",
    "Tidak",
    "Awas aja sampe ngelawan ama gw",
    "Bacot kau",
    "Hilih",
    "Bicit banget lu",
    "muk hanyalah manusia biasa",
    "Hahahaha",
    "Stres",
    "lmao",
    "Goblok!",
    "Apa anjeng!",
    "Idih sokap",
    "Babi",
    "Dasar lu",
    "Grup sepi jan sok keras",
    "Uang hasil link jan sok keras",
    "Hadeh",
    "Ucup udin",
    "Orang gilak",
    "Pasar baru",
    "Koran kabar lama",
    "Batri lama",
    "Tolol sekali",
    "Najis alay",
    "Okey",
    "Asoo",
    "mainin bot teros alay",
    "gua ganteng",
    "Bego amat",
    "Sawadikap tod",
    "Kenapa?",
    "Poci...",
    "mtk",
    "Asu capek:)",
    "Gosok gigi",
    "Gak bisa ngomong r",
    "Upin dan ipin",
    "Python",
    "Ceunah",
]


@register(outgoing=True, pattern="^.xbot$")
async def xbot(xbotpis):
    await xbotpis.edit(choice(XBOT_STRINGS))

CMD_HELP.update(
    {
        "xbot": "**✘ Plugin :** `xbot`\
        \n\n  •  **Perintah :** `.xbot`\
        \n  •  **Function : **Xbot random untuk bersenang senang saja\
    "
    }
)
