from platform import uname

from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.p(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamualaikum**")


@register(outgoing=True, pattern=r"^\.as(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Assalamualaikum Warahmatullahi Wabarakatuh**")
    
    
@register(outgoing=True, pattern=r"^\.wa(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Wa'alaikumussalam Warahmatullahi Wabarakatuh**")


@register(outgoing=True, pattern="^.P(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Haii Salken Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**Assalamualaikum...**")


@register(outgoing=True, pattern=r"^\.l(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Wa'alaikumussalam**")


@register(outgoing=True, pattern='^M(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**𝐁𝐇𝐀𝐀𝐀𝐊𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒**")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇......")


@register(outgoing=True, pattern='^.M(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAI PERKENALKAN NAMA SAYA GAK TAU LUPA!!**")


@register(outgoing=True, pattern="^.al(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Alhamdulillah..**")


@register(outgoing=True, pattern="^.ma(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐓𝐞𝐫𝐢𝐦𝐚 𝐊𝐚𝐬𝐢𝐡. .")



CMD_HELP.update(
    {
        "salam": "**Plugin : **`salam`\
        \n\n  •  **Syntax :** `.p`\
        \n  •  **Function : **Untuk Mengucap Salam\
        \n\n  •  **Syntax :** `.as`\
        \n  •  **Function : **Assalamualaikum Warahmatullahi Wabarakatuh\
        \n\n  •  **Syntax :** `.wa`\
        \n  •  **Function : **Wa'alaikumussalam Warahmatullahi Wabarakatuh\
        \n\n  •  **Syntax :** `.l`\
        \n  •  **Function : **Untuk Menjawab salam\
        \n\n  •  **Syntax :** `.ass`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `.waa`\
        \n  •  **Function : **Salam Bahas arab\
        \n\n  •  **Syntax :** `.semangat`\
        \n  •  **Function : **Memberikan Semangat.\
        \n\n  •  **Syntax :** `.ast`\
        \n  •  **Function : **Memunculkan tulisan 𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇.......\
        \n\n  •  **Syntax :** `M`\
        \n  •  **Function : **Memunculkan tulisan 𝐁𝐇𝐀𝐀𝐀𝐊𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒𝐒\
        \n\n  •  **Syntax :** `.M`\
        \n  •  **Function : **Memunculkan tulisan HAI PERKENALKAN NAMA SAYA GAK TAU LUPA\
        \n\n  •  **Syntax :** `.ywc`\
        \n  •  **Function : **nMenampilkan Sama sama\
        \n\n  •  **Syntax :** `.sayang`\
        \n  •  **Function : **Kata I Love You.\
        \n\n  •  **Syntax :** `.k`\
        \n  •  **Function : **LU SEMUA NGENTOT 🔥\
        \n\n  •  **Syntax :** `.j`\
        \n  •  **Function : **NIMBRUNG GOBLOKK!!!🔥\
        \n\n  •  **Syntax :** `.al`\
        \n  •  **Function : **Alhamdulillah\
         n\n  •  **Syntax :** `.ma`\
        \n  •  **Function : **𝐓𝐞𝐫𝐢𝐦𝐚 𝐊𝐚𝐬𝐢𝐡. .\
    "
    }
)
