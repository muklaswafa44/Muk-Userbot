# copy for Ram-UBOT
# 


from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.gjm(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Gadulu,janmaksa!!")


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Mangga..")


@register(outgoing=True, pattern='^.pu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Punten..")


@register(outgoing=True, pattern='^.gjl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Gajelas anj")


@register(outgoing=True, pattern='^.an(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Sange mulu , tobat yuk!")
    
    
@register(outgoing=True, pattern='^.w(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Welcome kak, salken ya 🙂**")


@register(outgoing=True, pattern='^.O(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JANGAN MAEN BOT MULU, ALAY LU NJIRR,KESANNYA NORAK, WKWKWK!!**")
    
    
@register(outgoing=True, pattern='^.yb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Yabenarrrrrrr...**")


@register(outgoing=True, pattern='^.st(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**STRESSS 😭😭...**")


@register(outgoing=True, pattern='^.ng(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NGAKAKK ASW 🤣🤣😭...**")


@register(outgoing=True, pattern='^.gls(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK, LO SANGEAN!!!**")


@register(outgoing=True, pattern='^.bsl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BAU SAWI LO..!!**")


@register(outgoing=True, pattern='^.hai(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Hai, Jodohku😚😚..**")


@register(outgoing=True, pattern='^.hey(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Hey, Member Alay..😂**")


@register(outgoing=True, pattern='^.loh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GC SEPI KAYA GINI, BUBARIN AJA PLIS!!🤣**")


@register(outgoing=True, pattern='^.kuat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**gak boleh lemah semangat dong, dulu katanya mau jadi ultraman**")


@register(outgoing=True, pattern='^sad1(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**lihatlah cantik, kau telah mematahkan hati lelaki incaran semua orang**")


@register(outgoing=True, pattern='^x(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**INI GRUB APA KUBURAN SEPI BANGET ASTAGFIRULLAH!!**")


CMD_HELP.update({
    "salam2":
    ".gjm\
\nUsage:\
\n\n.w\
\nUsage:\
\n\n.gjl\
\nUsage:\
\n\n.yb\
\nUsage:\
\n\n.st\
\nUsage:\
\n\n.kuat\
\nUsage:\
\n\n.sad1\
\nUsage:\
\n\n.g\
\nUsage:\
\n\n.pu\
\nUsage:
"
    }
)


CMD_HELP.update({
    "salam3":
    ".O\
\nUsage:\
\n\n.bsl\
\nUsage:\
\n\n.hai\
\nUsage:\
\n\n.ng\
\nUsage:\
\n\n.an\
\nUsage:\
\n\n.gls\
\nUsage:\
\n\n.hey\
\nUsage:\
\n\n.loh\
\nUsage:
   "
    }
)
