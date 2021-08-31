# Coded by Koala
# Recode by @mrismanaziz

import time
from datetime import datetime
from platform import uname
from time import sleep

from userbot import ALIVE_NAME, StartTime
from userbot import CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(outgoing=True, pattern=r"^\.keping$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**『⍟𝐊𝐎𝐍𝐓𝐎𝐋』**")
    await pong.edit("**◆◈𝐊𝐀𝐌𝐏𝐀𝐍𝐆◈◆**")
    await pong.edit("**𝐏𝐄𝐂𝐀𝐇𝐊𝐀𝐍 𝐁𝐈𝐉𝐈 𝐊𝐀𝐔 𝐀𝐒𝐔**")
    await pong.edit("**☬𝐒𝐈𝐀𝐏 𝐊𝐀𝐌𝐏𝐀𝐍𝐆 𝐌𝐄𝐍𝐔𝐌𝐁𝐔𝐊 𝐀𝐒𝐔☬**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**✲ 𝙺𝙾𝙽𝚃𝙾𝙻 𝙼𝙴𝙻𝙴𝙳𝚄𝙶** "
        f"\n ⫸ ᴷᵒⁿᵗᵒˡ `%sms` \n"
        f"**✲ 𝙱𝙸𝙹𝙸 𝙿𝙴𝙻𝙴𝚁** "
        f"\n ⫸ ᴷᵃᵐᵖᵃⁿᵍ『`{ALIVE_NAME}`』 \n" % (duration)
    )


@register(outgoing=True, pattern=r"^\.a(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Haii Salken Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**Assalamualaikum**")


# Owner @Si_Dian


@register(outgoing=True, pattern=r"^\.j(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG GOBLOKK!!!🔥**")


# Owner @Si_Dian


@register(outgoing=True, pattern=r"^\.k(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo KIMAAKK SAYA {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("**LU SEMUA NGENTOT 🔥**")


# Owner @Si_Dian


@register(outgoing=True, pattern=r"^\.ass(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Salam Dulu Biar Sopan**")
    sleep(2)
    await typew.edit("**السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")


# Owner @mixiologist


@register(outgoing=True, pattern=r"^\.waa(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Kalo Orang Salam Itu Dijawab**")
    sleep(2)
    await typew.edit("**وَعَلَيْكُمُ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ**")
 

@register(outgoing=True, pattern='^.orgil(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`ANJING ADA ORANG GILA.....`")
    sleep(1)
    await typew.edit("`ORANG GILAAAAAA!!`")
    sleep(1)
    await typew.edit("`🏃                        🤸`")
    await typew.edit("`🏃                       🤸`")
    await typew.edit("`🏃                      👨‍🦽`")
    await typew.edit("`🏃                     ⛹️`")
    await typew.edit("`🏃   `LARII`          🤾`")
    await typew.edit("`🏃                   🤾`")
    await typew.edit("`🏃                  🤾`")
    await typew.edit("`🏃                 🤾`")
    await typew.edit("`🏃                🤾`")
    await typew.edit("`🏃               🤺`")
    await typew.edit("`🏃              🏊`")
    await typew.edit("`🏃             🏊`")
    await typew.edit("`🏃            🏄`")
    await typew.edit("`🏃           🤾`")
    await typew.edit("`🏃PULUPULU   🧚`")
    await typew.edit("`🏃           ⛹️`")
    await typew.edit("`🏃            ⛹️`")
    await typew.edit("`🏃             🤺`")
    await typew.edit("`🏃              🥴`")
    await typew.edit("`🏃               🏃`")
    await typew.edit("`🏃                🏃`")
    await typew.edit("`🏃                 🤸`")
    await typew.edit("`🏃                  🤸`")
    await typew.edit("`🏃                   🤸`")
    await typew.edit("`🏃                    🤸`")
    await typew.edit("`🏃                     ⛹️`")
    await typew.edit("`🏃  Huh-Huh           🏃`")
    await typew.edit("`🏃                   🤑`")
    await typew.edit("`🏃                  🙈`")
    await typew.edit("`🏃                 ⛹️`")
    await typew.edit("`🏃                🏃`")
    await typew.edit("`🏃               🤴`")
    await typew.edit("`🏃              🐖`")
    await typew.edit("`🏃             🐖`")
    await typew.edit("`🏃            🥴`")
    await typew.edit("`🏃           🥴`")
    await typew.edit("`🏃          🤡`")
    await typew.edit("`🏃         🤭`")
    await typew.edit("`CAPE BANGET ANJING!!!`")
    sleep(1)
    await typew.edit("`🏃       🏃`")
    await typew.edit("`🏃      🤾`")
    await typew.edit("`🏃     🏃`")
    await typew.edit("`🏃    🏃`")
    await typew.edit("`Dahlah Pasrah Aja`")
    sleep(1)
    await typew.edit("`🧎🐖`")
    sleep(2)
    await typew.edit("`-TAMAT-`")


# create by rama


@register(outgoing=True, pattern='^.thanks(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "╔══╦╗────╔╗─╔╗╔╗\n"
                     "╚╗╔╣╚╦═╦═╣╚╗║╚╝╠═╦╦╗\n"
                     "─║║║║║╬║║║╩║╚╗╔╣║║║║\n"
                     "─╚╝╚╩╩╩╩╩╩╩╝─╚╝╚═╩═╝\n"
                     "▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄\n"
                     "●▬▬▬▬ஜ۩۞۩ஜ▬▬▬▬●")


@register(outgoing=True, pattern='^.malam(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╔═╦═╦╗╔═╦══╦═╦══╗\n"
                     "║═╣═╣║║╬║║║║╬╠╗╔╝\n"
                     "╠═║═╣╚╣║║║║║║║║║\n"
                     "╚═╩═╩═╩╩╩╩╩╩╩╝╚╝\n\n"
                     "╔══╦═╦╗╔═╦══╗\n"
                     "║║║║╬║║║╬║║║║\n"
                     "║║║║║║╚╣║║║║║\n"
                     "╚╩╩╩╩╩═╩╩╩╩╩╝")


@register(outgoing=True, pattern='^.rumah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAMBAR RUMAH**\n"
                     "╱◥◣\n"
                     "│∩ │◥███◣ ╱◥███◣\n"
                     "╱◥◣ ◥████◣▓∩▓│∩ ║\n"
                     "│╱◥█◣║∩∩∩ ║◥█▓ ▓█◣\n"
                     "││∩│ ▓ ║∩田│║▓ ▓ ▓∩ ║\n"
                     "๑۩๑๑۩๑๑ ۩๑๑۩๑▓๑۩๑๑۩๑")


@register(outgoing=True, pattern='^.hbd(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("╔╗─╔╗\n"
                     "║║─║║\n"
                     "║╚═╝╠══╦══╦══╦╗─╔╗\n"
                     "║╔═╗║╔╗║╔╗║╔╗║║─║║\n"
                     "║║─║║╔╗║╚╝║╚╝║╚═╝║\n"
                     "╚╝─╚╩╝╚╣╔═╣╔═╩═╗╔╝\n"
                     "───────║║─║║─╔═╝║\n"
                     "───────╚╝─╚╝─╚══╝\n"
                     "╔══╗───╔╗╔╗───╔╗──────╔╗\n"
                     "║╔╗║──╔╝╚╣║───║║──────║║\n"
                     "║╚╝╚╦╦╩╗╔╣╚═╦═╝╠══╦╗─╔╣║\n"
                     "║╔═╗╠╣╔╣║║╔╗║╔╗║╔╗║║─║╠╝\n"
                     "║╚═╝║║║║╚╣║║║╚╝║╔╗║╚═╝╠╗\n"
                     "╚═══╩╩╝╚═╩╝╚╩══╩╝╚╩═╗╔╩╝\n"
                     "──────────────────╔═╝║\n"
                     "──────────────────╚══╝\n")


@register(outgoing=True, pattern='^.wibuu(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Kata Emak`")
    sleep(2)
    await typew.edit("`Kalo Ketemu Wibuu`")
    sleep(3)
    await typew.edit("`Harus Lari Sekenceng Mungkin🏃🏻`")
    sleep(3)
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`ㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await typew.edit("`🧎🏻‍♂️ huhh... akhirnya bisa lolos dari wibu mematikan`")


# create by iky


@register(outgoing=True, pattern='^.piw(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Bapaknya Udin Di Makan Singkong`")
    sleep(2)
    await typew.edit("`Cuma Sendiri ni Senggol Dong`")


# create by iky


@register(outgoing=True, pattern='^.alay(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("eh kamu, iya kamu")
    sleep(1)
    await typew.edit("**ALAY** bnget sih")
    sleep(1)
    await typew.edit("spam bot mulu")
    sleep(1)
    await typew.edit("baru jadi userbot ya?? xixixi")
    sleep(1)
    await typew.edit("pantes **NORAK**")


# @Rzky3016


@register(outgoing=True, pattern='^.sad(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Jangan**")
    sleep(2)
    await typew.edit("**Tinggalkan**")
    sleep(2)
    await typew.edit("**Yang**")
    sleep(1)
    await typew.edit("**Setia**")
    sleep(2)
    await typew.edit("**Demi**")
    sleep(2)
    await typew.edit("**Sesuatu**")
    sleep(2)
    await typew.edit("**Yang**")
    sleep(2)
    await typew.edit("**Menarik**")
    sleep(2)
    await typew.edit("**Jangan Tinggalkan Yang Setia Demi Sesuatu Yang Menarik:)**")


@register(outgoing=True, pattern='^.dahlah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**`Ayo Menyerah`**")
    sleep(2)
    await typew.edit("**`Ngapain Semangat`**")


# @Rzky3016


@register(outgoing=True, pattern='^wkwk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`😂 `")
    await typew.edit("`🤣`")
    await typew.edit("`😂 `") 
    await typew.edit("`🤣 `")
    await typew.edit("`😂`")
    await typew.edit("`🤣`")
    await typew.edit("`😂`")
    await typew.edit(" 🤣`")
    await typew.edit("`😂`")
    await typew.edit(" 🤣`")
    await typew.edit("`😂`")
    await typew.edit(" 🤣`")
    await typew.edit("`😂`")
    await typew.edit(" 🤣`")
    await typew.edit("`😂`")
    await typew.edit("`WKWK`")
# Create by myself @localheart


@register(outgoing=True, pattern="^.fusage(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Getting Information...`")
    sleep(1)
    await typew.edit(
        "**Informasi Dyno ★**:\n\n╭━━━━━━━━━━━━━━━━━━━━╮\n"
        f"-> `Penggunaan Dyno` **{ALIVE_NAME}**:\n"
        f" ❉ **10 Jam - "
        f"51 Menit - 0%**"
        "\n ◐━─━─━─━─━──━─━─━─━─━◐\n"
        "-> `Sisa Dyno Bulan Ini`:\n"
        f" ❉ **9989 Jam - 9948 Menit "
        f"- 99%**\n"
        "╰━━━━━━━━━━━━━━━━━━━━╯"
    )


# @mixiologist

CMD_HELP.update({
    "gabut":
    "•CMD:`.piw`\
    \nPenjelasan: senggol dong.\
    \n\n•CMD:`.wibuu`\
    \nPenjelasan: awas ada wibu :v.\
    \n\n•CMD:`.alay`\
    \nPenjelasan: buat orang yang mainin bot teross\
    \n\n•CMD:`.fusage`\
    \nPenjelasan: dyno palsu.\
    \n\n•CMD:`.orgil`\
    \n\n•CMD:`.thanks`\
    \nPenjelasan: liat sendiri\
    \n\n•CMD:`.malam`\
    \nPenjelasan: liat sendiri\
    \n\n•CMD:`.hbd`\
    \nPenjelasan: liat sendiri\
    \n\n•CMD:`.rumah`\
    \nPenjelasan: liat sendiri\
    \nPenjelasan: ada orang gila.\
    \n\n•CMD:`.is`\
    \nPenjelasan: istigfar dulu.\
    \n\n•CMD:`.lat`\ \nPenjelasan: ingetin sholat."
})
