from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.is(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`astagfirullahaladzim 1x`")
    sleep(2)
    await typew.edit("`astagfirullahaladzim 2x`")
    sleep(2)
    await typew.edit("`astagfirullahaladzim 3x`")
    sleep(1)
    await typew.edit("`Istighfar dulu kawan:)`")


# Create by myself @localheart


@register(outgoing=True, pattern='^.istighfar(?: |$)(.*)')  
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("Heh Kamu Gaboleh Begitu...")
    sleep(2)
    await typew.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")


# kenUserbot


@register(outgoing=True, pattern='^.lat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Sholat woii`")
    sleep(2)
    await typew.edit("`Maaf cuma mengingatkan bagi yg muslim 🙏`")
    sleep(2)
    await typew.edit("`Sholatlah`")
    sleep(2)
    await typew.edit("`Sebelum disholatkan`")
    sleep(3)
    await typew.edit("`Oke selamat menjalankan ibadah:)`")


# Create by myself @localheart


@register(outgoing=True, pattern='^.wah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Wahh, War nya keren bang`")
    sleep(2)
    await typew.edit("`Tapi, Yang gua liat, kok Kaya lawakan`")
    sleep(2)
    await typew.edit("`Oh iya, Kan lo badut 🤡`")
    sleep(2)
    await typew.edit("`Kosa kata pas ngelawak, Jangan di pake war bang`")
    sleep(2)
    await typew.edit("`Kesannya lo ngasih kita hiburan.`")
    sleep(2)
    await typew.edit("`Kasian badut🤡, Ga di hargain pengunjung, Eh lampiaskan nya ke Tele, Wkwkwk`")
    sleep(3)
    await typew.edit("`Dah sana cabut, Makasih hiburannya, Udah bikin Gua tawa ngakak`")


# Create by myself @localheart


@register(outgoing=True, pattern=r"^\.sayang(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**Cuma Mau Bilang**")
    sleep(3)
    await typew.edit("**Aku Sayang Kamu**")
    sleep(1)
    await typew.edit("**I LOVE YOU 💞**")


# Create by myself @localheart


@register(outgoing=True, pattern=r"^\.semangat(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**Apapun Yang Terjadi**")
    sleep(3)
    await typew.edit("**Tetaplah Bernapas**")
    sleep(1)
    await typew.edit("**Dan Selalu Bersyukur**")


# Create by myself @localheart


@register(outgoing=True, pattern=r"^\.ywc(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Sama sama kawan**")


# Create by myself @localheart


@register(outgoing=True, pattern=r"^\.v(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Selamat datang**")
    sleep(2)
    await typew.edit("**Maaf ya yang keculik**")
    sleep(2)
    await typew.edit("**semoga betah, salken ya 🙂**")


# Create by myself @localheart
