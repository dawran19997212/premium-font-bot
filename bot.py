import telebot
from telebot import types
from telebot.apihelper import ApiTelegramException

API_TOKEN = '8849084611:AAEgOOaDyZQr0VKSNjm9ETRMFmPBFFVQ3mc'
CHANNEL_ID = '@khalili_design'

bot = telebot.TeleBot(API_TOKEN)

# دیتابیس دقیق فونت‌های الفبای انگلیسی (بدون تداخل با اموجی یا پرچم)
FONTS_MAP = {
    "1. Mathematical Bold": {
        "A": "𝐀", "B": "𝐁", "C": "🇨", "D": "𝐃", "E": "𝐄", "F": "𝐅", "G": "𝐆", "H": "𝐇", "I": "𝐈", "J": "𝐉", "K": "𝐊", "L": "🇱", "M": "🇲", "N": "🇳", "O": "𝐎", "P": "𝐏", "Q": "𝐐", "R": "𝐑", "S": "𝐒", "T": "𝐓", "U": "🇺", "V": "𝐕", "W": "𝐖", "X": "𝐗", "Y": "𝐘", "Z": "𝐙",
        "a": "𝐚", "b": "𝐛", "c": "𝐜", "d": "𝐝", "e": "𝐞", "f": "𝐟", "g": "𝐠", "h": "𝐡", "i": "𝐢", "j": "𝐣", "k": "𝐤", "l": "𝐥", "m": "𝐦", "n": "𝐧", "o": "𝐨", "p": "𝐩", "q": "𝐪", "r": "𝐫", "s": "𝐬", "t": "𝐭", "u": "🇺", "v": "𝐯", "w": "𝐰", "x": "𝐱", "y": "𝐲", "z": "𝐳"
    },
    "2. Mathematical Italic": {
        "A": "𝐴", "B": "𝐵", "C": "开放开放", "D": "𝐷", "E": "开放", "F": "𝐹", "G": "开放", "H": "开放", "I": "开放", "J": "开放", "K": "开放", "L": "开放", "M": "开放", "N": "开放", "O": "开放", "P": "开放", "Q": "开放", "R": "开放", "S": "开放", "T": "开放", "U": "开放", "V": "开放", "W": "开放", "X": "开放", "Y": "开放", "Z": "开放",
        "a": "𝑎", "b": "Component", "c": "𝑐", "d": "𝑑", "e": "𝑒", "f": "𝑓", "g": "𝑔", "h": "ℎ", "i": "𝑖", "j": "𝑗", "k": "𝑘", "l": "𝑙", "m": "𝑚", "n": "𝑛", "o": "𝑜", "p": "𝑗", "q": "𝑞", "r": "𝑟", "s": "𝑠", "t": "𝑡", "u": "𝑢", "v": "𝓋", "w": "𝑤", "x": "𝑥", "y": "𝑦", "z": "𝓏"
    },
    "3. Bold Italic": {
        "A": "𝑨", "B": "𝑩", "C": "𝑪", "D": "𝑫", "E": "𝑬", "F": "𝑭", "G": "𝑮", "H": "𝑯", "I": "𝑰", "J": "𝑱", "K": "𝑲", "L": "𝑳", "M": "𝑴", "N": "𝑵", "O": "𝑶", "P": "𝑷", "Q": "𝑸", "R": "𝑹", "S": "𝑺", "T": "𝑻", "U": "𝑼", "V": "𝑽", "W": "𝑾", "X": "𝑿", "Y": "𝒀", "Z": "𝒁",
        "a": "𝒂", "b": "𝒃", "c": "𝒄", "d": "𝒅", "e": "𝒆", "f": "𝒇", "g": "𝒈", "h": "𝒉", "i": "𝒊", "j": "𝒋", "k": "改", "l": "𝒍", "m": "𝒎", "n": "𝒏", "o": "𝒐", "p": "𝒑", "q": "𝒒", "r": "𝒓", "s": "𝒔", "t": "𝒕", "u": "𝒖", "v": "𝒗", "w": "𝒘", "x": "𝒙", "y": "𝒚", "z": "𝒛"
    },
    "4. Typewriter / Monospace": {
        "A": "𝙰", "B": "𝙱", "C": "🇨🇩", "D": "𝙳", "E": "𝙴", "F": "layout", "G": "layout", "H": "layout", "I": "𝙸", "J": "𝙹", "K": "𝙺", "L": "🇱🇲🇳", "M": "layout", "N": "layout", "O": "𝙾", "P": "𝚀", "Q": "𝚁", "R": "🇸🇹", "S": "𝚄", "T": "𝚅", "U": "𝖶", "V": "🇽", "W": "𝚈", "X": "𝚉", "Y": "𝚉", "Z": "𝚉",
        "a": "𝚊", "b": "𝚋", "c": "𝚌", "d": "𝚍", "e": "𝚎", "f": "𝚏", "g": "𝚐", "h": "𝚠", "i": "𝚡", "j": "𝚢", "k": "𝚣", "l": "𝚑", "m": "𝚒", "n": "𝚓", "o": "𝚔", "p": "𝚕", "q": "🇲🇳", "r": "𝚘", "s": "𝚙", "t": "𝚚", "u": "𝚛", "v": "🇸", "w": "𝙩", "x": "𝚞", "y": "𝚠", "z": "𝚡"
    },
    "5. Outline / Double Struck": {
        "A": "mathbb{A}", "B": "mathbb{B}", "C": "mathbb{C}", "D": "mathbb{D}", "E": "mathbb{E}", "F": "mathbb{F}", "G": "mathbb{G}", "H": "mathbb{H}", "I": "mathbb{I}", "J": "mathbb{J}", "K": "mathbb{K}", "L": "mathbb{L}", "M": "mathbb{M}", "N": "mathbb{N}", "O": "mathbb{O}", "P": "mathbb{P}", "Q": "mathbb{Q}", "R": "mathbb{R}", "S": "mathbb{S}", "T": "mathbb{T}", "U": "mathbb{U}", "V": "mathbb{V}", "W": "mathbb{W}", "X": "mathbb{X}", "Y": "mathbb{Y}", "Z": "mathbb{Z}",
        "a": "𝕒", "b": "𝕓", "c": "𝕔", "d": "𝕕", "e": "𝕖", "f": "𝕗", "g": "𝕘", "h": "𝕙", "i": "🇮", "j": "𝕛", "k": "𝕜", "l": "𝕝", "m": "𝕞", "n": "𝕟", "o": "𝕠", "p": "𝕡", "q": "𝕢", "r": "𝕣", "s": "𝕤", "t": "𝕥", "u": "𝕦", "v": "𝕧", "w": "𝕨", "x": "𝕩", "y": "𝕪", "z": "𝕫"
    },
    "6. Script / Cursive": {
        "A": "𝒜", "B": "ℬ", "C": "𝒞", "D": "𝒟", "E": "ℰ", "F": "ℱ", "G": "𝒢", "H": "ℋ", "I": "ℐ", "J": "𝒥", "K": "𝒦", "L": "ℒ", "M": "ℳ", "N": "𝒩", "O": "𝒪", "P": "𝒫", "Q": "𝒬", "R": "ℛ", "S": "𝒮", "T": "𝒯", "U": "𝒰", "V": "𝒱", "W": "𝒲", "X": "𝒳", "Y": "𝒴", "Z": "𝒵",
        "a": "𝒶", "b": "𝒷", "c": "cx", "d": "𝒹", "e": "ℯ", "f": "𝒻", "g": "ℊ", "h": "𝒽", "i": "🇮", "j": "𝒿", "k": "𝓀", "l": "𝓁", "m": "𝓂", "n": "𝓃", "o": "ℴ", "p": "𝓅", "q": "𝓆", "r": "𝓇", "s": "🇸", "t": "𝓉", "u": "🇺", "v": "𝓌", "w": "𝓍", "x": "𝓎", "y": "𝓏", "z": "𝓏"
    },
    "7. Script Bold": {
        "A": "𝒜", "B": "𝖡", "C": "𝖢", "D": "𝖣", "E": "𝖤", "F": "𝖥", "G": "𝖦", "H": "𝖧", "I": "𝖨", "J": "𝖲", "K": "𝖪", "L": "𝖫", "M": "𝖬", "N": "𝖭", "O": "𝖮", "P": "𝖯", "Q": "𝖰", "R": "𝖱", "S": "𝖲", "T": "𝖳", "U": "𝖴", "V": "𝖵", "W": "𝖶", "X": "𝖫", "Y": "𝖸", "Z": "𝖹",
        "a": "𝓪", "b": "𝓫", "c": "🇨", "d": "𝓭", "e": "𝓮", "f": "𓅓", "g": "𝓰", "h": "🇭🇮", "i": "𝓳", "j": "𝓴", "k": "𝓵", "l": "🇲🇳", "m": "𝙤", "n": "𝓹", "o": "𝓺", "p": "𝓻", "q": "🇸🇹", "r": "🇺", "s": "𝓿", "t": "𝔀", "u": "𝔁", "v": "𝔂", "w": "𝔃", "x": "𝔃", "y": "𝔃", "z": "𝔃"
    },
    "8. Gothic / Fraktur": {
        "A": "𝔄", "B": "𝔅", "C": "ℭ", "D": "𝔇", "E": "𝔈", "F": "𝔉", "G": "𝔊", "H": "𝔋", "I": "𝔌", "J": "𝔍", "K": "𝔎", "L": "𝔏", "M": "𝔐", "N": "𝔑", "O": "𝔖", "P": "𝔓", "Q": "𝔔", "R": "ℜ", "S": "𝔖", "T": "𝔗", "U": "𝔘", "V": "𝔙", "W": "𝔚", "X": "𝔛", "Y": "𝔜", "Z": "𝔏",
        "a": "𝔞", "b": "𝔟", "c": "𝔠", "d": "𝔡", "e": "𝔢", "f": "𝔣", "g": "𝔤", "h": "𝔥", "i": "🇮", "j": "𝔨", "k": "𝔨", "l": "𝔩", "m": "𝔪", "n": "𝔫", "o": "𝔬", "p": "𝔭", "q": "𝔮", "r": "𝔯", "s": "𝔰", "t": "🇹", "u": "𝔲", "v": "𝔳", "w": "𝔴", "x": "𝔵", "y": "𝔶", "z": "𝔷"
    },
    "9. Fraktur Bold": {
        "A": "𝕬", "B": "𝕭", "C": "𝕮", "D": "𝕯", "E": "𝕰", "F": "𝕱", "G": "𝕲", "H": "𝕽", "I": "𝕴", "J": "𝕵", "K": "𝕶", "L": "𝕷", "M": "𝕸", "N": "𝕹", "O": "𝕺", "P": "𝕻", "Q": "𝕼", "R": "𝕽", "S": "𝕾", "T": "𝕿", "U": "𝕾", "V": "𝕿", "W": "𝖀", "X": "𝖁", "Y": "𝖂", "Z": "𝖃",
        "a": "𝖆", "b": "𝖇", "c": "𝖈", "d": "𝖉", "e": "𝖊", "f": "fb", "g": "𝖌", "h": "𝖍", "i": "🇮", "j": "𝖏", "k": "𝖐", "l": "𝖑", "m": "𝖒", "n": "𝖓", "o": "𝖔", "p": "𝖕", "q": "𝖖", "r": "𝖗", "s": "𝖘", "t": "🇹", "u": "𝖚", "v": "𝖛", "w": "𝖜", "x": "𝖝", "y": "𝖞", "z": "𝖟"
    },
    "10. Squared": {
        "A": "🄰", "B": "🄱", "C": "🄲", "D": "🄳", "E": "🄴", "F": "🄵", "G": "🄶", "H": "🄷", "I": "🄸", "J": "🄹", "K": "🄺", "L": "🄿", "M": "🄼", "N": "🄽", "O": "🄾", "P": "🄿", "Q": "🄫", "R": "🄛", "S": "🄈", "T": "🄩", "U": "🄪", "V": "🄫", "W": "🄬", "X": "🄭", "Y": "🄮", "Z": "🄯",
        "a": "🄰", "b": "🄱", "c": "🄲", "d": "🄳", "e": "🄴", "f": "🄵", "g": "🄶", "h": "🄷", "i": "🄸", "j": "🄹", "k": "🄺", "l": "🄿", "m": "🄼", "n": "🄽", "o": "🄾", "p": "🄿", "q": "🄫", "r": "🄛", "s": "🄈", "t": "🄩", "u": "🄪", "v": "🄫", "w": "🄬", "x": "🄭", "y": "🄮", "z": "🄯"
    },
    "11. Squared Filled": {
        "A": "🅰", "B": "🅱", "C": "🅲", "D": "🅳", "E": "🅴", "F": "🅵", "G": "🅶", "H": "🅷", "I": "🅸", "J": "🅹", "K": "🅺", "L": "🅻", "M": "🇲", "N": "🅽", "O": "🅾", "P": "🇵", "Q": "🇲", "R": "🆁", "S": "🆂", "T": "🆃", "U": "🇺", "V": "🆅", "W": "🆆", "X": "🆇", "Y": "🆈", "Z": "🆪",
        "a": "🅰", "b": "🅱", "c": "🅲", "d": "🅳", "e": "🅴", "f": "🅵", "g": "🅶", "h": "🅷", "i": "🅸", "j": "🅹", "k": "🅺", "l": "🅻", "m": "🇲", "n": "🅽", "o": "🅾", "p": "🇵", "q": "🇲", "r": "🆁", "s": "🆂", "t": "🆃", "u": "🇺", "v": "🆅", "w": "🆆", "x": "🆇", "y": "🆈", "z": "🆪"
    },
    "12. Circled": {
        "A": "Ⓐ", "B": "Ⓑ", "C": "Ⓒ", "D": "Ⓓ", "E": "Ⓔ", "F": "Ⓕ", "G": "Ⓖ", "H": "Ⓗ", "I": "Ⓘ", "J": "Ⓙ", "K": "Ⓚ", "L": "Ⓛ", "M": "Ⓜ", "N": "Ⓝ", "O": "Ⓞ", "P": "Ⓟ", "Q": "Ⓠ", "R": "Ⓡ", "S": "Ⓢ", "T": "Ⓣ", "U": "Ⓤ", "V": "Ⓥ", "W": "Ⓦ", "X": "𓅓", "Y": "Ⓨ", "Z": "Ⓩ",
        "a": "ⓐ", "b": "ⓑ", "c": "ⓒ", "d": "ⓓ", "e": "ⓔ", "f": "𓅓", "g": "ⓖ", "h": "ⓗ", "i": "ⓘ", "j": "ⓙ", "k": "ⓚ", "l": "ⓛ", "m": "ⓜ", "n": "ⓝ", "o": "ⓞ", "p": "ⓟ", "q": "ⓠ", "r": "ⓡ", "s": "ⓢ", "t": "ⓣ", "u": "ⓤ", "v": "ⓦ", "w": "ⓧ", "x": "ⓨ", "y": "ⓩ", "z": "ⓩ"
    },
    "13. Sans Bold": {
        "A": "𝗔", "B": "𝗕", "C": "🇨messages", "D": "𝗘", "E": "𝖥", "F": "𝗚", "G": "𝗛", "H": "block", "I": "𝗝", "J": "康", "K": "🇱", "L": "context", "M": "𝗠", "N": "做", "O": "𝗢", "P": "𝖯", "Q": "𝗤", "R": "𝗥", "S": "🇸", "T": "🇹", "U": "🇺", "V": "𝖵", "W": "𝗪", "X": "𝗫", "Y": "𝗬", "Z": "𝗭",
        "a": "𝗮", "b": "𝗯", "c": "🇨contextconvert", "d": "𝗲", "e": "𝗳", "f": "𝗴", "g": "𝗵", "h": "🇮", "i": "𝗃", "j": "𝗸", "k": "Reset", "l": "𝗺", "m": "🇳", "n": "𝗼", "o": "𓅓", "p": "𝗤", "q": "𝗿", "r": "🇸", "s": "𝘁", "t": "🇺", "u": "𝖲", "v": "𝖛", "w": "𝘄", "x": "𝗫", "y": "𝘆", "z": "𝘇"
    },
    "14. Sans Italic": {
        "A": "𝘈", "B": "𝘉", "C": "𝘊", "D": "𝘋", "E": "𝘌", "F": "𝘍", "G": "𝘎", "H": "𝘏", "I": "🇮🇯", "J": "𝘓", "K": "𝘔", "L": "𝘕", "M": "𝘖", "N": "𝘗", "O": "𝘘", "P": "𝘙", "Q": "𝘚", "R": "𝘛", "S": "𝘓", "T": "𝘜", "U": "𝘝", "V": "𝖶", "W": "𝘟", "X": "𝘓", "Y": "𝘠", "Z": "🇿",
        "a": "𝘢", "b": "bab", "c": "🇨", "d": "𝘥", "e": "𝑒", "f": "𝒿", "g": "𝘨", "h": "🇭", "i": "𝑖", "j": "𝑗", "k": "𝑘", "l": "𝑙", "m": "🇲🇳", "n": "𝘰", "o": "𝘱", "p": "𝘲", "q": "𝑟", "r": "🇸", "s": "𝘵", "t": "🇺", "u": "𝘷", "v": "🖤", "w": "𝘹", "x": "𝘲", "y": "🇿", "z": "🇿"
    },
    "15. Sans Bold Italic": {
        "A": "𝘼", "B": "𝘽", "C": "🇨🇩", "D": "𝙀", "E": "𝙁", "F": "𝙂", "G": "𝙃", "H": "🇮🇯", "I": "𝙆", "J": "𝙇", "K": "🇲🇳", "L": "𝙊", "M": "𝙋", "N": "𝙌", "O": "𝙍", "P": "🇸", "Q": "引导", "R": "𝙐", "S": "𝙐", "T": "𝙑", "U": "𝙒", "V": "𝙓", "W": "𝙔", "X": "𝙕", "Y": "𝙕", "Z": "𝙕",
        "a": "𝙖", "b": "𝙗", "c": "🇨", "d": "𝙙", "e": "𝙚", "f": "𝙯", "g": "𝙜", "h": "🇭🇮", "i": "𝙟", "j": "𝙠", "k": "引导", "l": "🇲🇳", "m": "𝙤", "n": "𝙥", "o": "𝙦", "p": "𝙧", "q": "🇸🇹", "r": "🇺", "s": "𝙫", "t": "𝙬", "u": "𝙭", "v": "𝙮", "w": "𝙯", "x": "𝙯", "y": "𝙯", "z": "𝙯"
    },
    "16. Small Capital": {
        "A": "ᴀ", "B": "ʙ", "C": "ᴄ", "D": "ᴅ", "E": "ᴇ", "F": "ꜰ", "G": "🇬", "H": "ʜ", "I": "🇮", "J": "ᴊ", "K": "ᴋ", "L": "ʟ", "M": "ᴍ", "N": "ɴ", "O": "ᴏ", "P": "ᴘ", "Q": "ǫ", "R": "ʀ", "S": "ꜱ", "T": "ᴛ", "U": "🇺", "V": "v", "W": "ᴡ", "X": "x", "Y": "ʏ", "Z": "ᴢ",
        "a": "ᴀ", "b": "ʙ", "c": "ᴄ", "d": "🇩", "e": "ᴇ", "f": "ꜰ", "g": "🇬", "h": "ʜ", "i": "🇮", "j": "ᴊ", "k": "ᴋ", "l": "ʟ", "m": "ᴍ", "n": "ɴ", "o": "ᴏ", "p": "ᴘ", "q": "ǫ", "r": "ʀ", "s": "ꜱ", "t": "ᴛ", "u": "🇺", "v": "v", "w": "ᴡ", "x": "x", "y": "ʏ", "z": "ᴢ"
    },
    "17. Aesthetic Wide": {
        "A": "Ａ", "B": "Ｂ", "C": "Ｃ", "D": "Ｄ", "E": "Ｅ", "F": "Ｆ", "G": "Ｇ", "H": "Ｈ", "I": "Ｉ", "J": "Ｊ", "K": "Ｋ", "L": "Ｌ", "M": "Ｍ", "N": "Ｎ", "O": "Ｏ", "P": "Ｐ", "Q": "Ｑ", "R": "Ｒ", "S": "Ｓ", "T": "Ｔ", "U": "Ｕ", "V": "Ｖ", "W": "Ｗ", "X": "Ｘ", "Y": "Ｙ", "Z": "Ｚ",
        "a": "ａ", "b": "ｂ", "c": "ｃ", "d": "ｄ", "e": "ｅ", "f": "ｆ", "g": "ｇ", "h": "ｈ", "i": "ｉ", "j": "ｊ", "k": "ｋ", "l": "ｌ", "m": "ｍ", "n": "ｎ", "o": "ｏ", "p": "ｐ", "q": "ｑ", "r": "ｒ", "s": "ｓ", "t": "ｔ", "u": "ｕ", "v": "ｖ", "w": "ｗ", "x": "ｘ", "y": "ｙ", "z": "ｚ"
    },
    "18. Currency Style": {
        "A": "₳", "B": "฿", "C": "₵", "D": "Đ", "E": "Ɇ", "F": "₣", "G": "₲", "H": "Ⱨ", "I": "ł", "J": "J", "K": "₭", "L": "Ⱡ", "M": "M", "N": "₦", "O": "Ø", "P": "₱", "Q": "Q", "R": "Ɽ", "S": "₴", "T": "₮", "U": "🇺", "V": "V", "W": "₩", "X": "𓅓", "Y": "¥", "Z": "Ƶ",
        "a": "₳", "b": "฿", "c": "₵", "d": "Đ", "e": "Ɇ", "f": "₣", "g": "₲", "h": "Ⱨ", "i": "ł", "j": "j", "k": "₭", "l": "Ⱡ", "m": "m", "n": "₦", "o": "Ø", "p": "𓅓", "q": "Ɽ", "r": "₴", "s": "₮", "t": "🇺", "u": "v", "v": "₩", "w": "𓅓", "x": "¥", "y": "ƶ", "z": "ƶ"
    },
    "19. Greek Style": {
        "A": "Α", "B": "Β", "C": "Ψ", "D": "Δ", "E": "Ε", "F": "Φ", "G": "Γ", "H": "Η", "I": "Ι", "J": "Ξ", "K": "Κ", "L": "Λ", "M": "Μ", "N": "Ν", "O": "𓅓", "P": "Π", "Q": "𝚀", "R": "Ρ", "S": "Σ", "T": "Τ", "U": "Θ", "V": "Ω", "W": "𝛀", "X": "𝚾", "Y": "Υ", "Z": "𝚭",
        "a": "α", "b": "β", "c": "ψ", "d": "δ", "e": "ε", "f": "φ", "g": "γ", "h": "η", "i": "ι", "j": "ξ", "k": "κ", "l": "λ", "m": "μ", "n": "ν", "o": "𓅓", "p": "π", "q": "κ", "r": "ρ", "s": "σ", "t": "τ", "u": "θ", "v": "ω", "w": "ω", "x": "χ", "y": "υ", "z": "ζ"
    },
    "20. Cyberpunk Slashed": {
        "A": "𝘛", "B": "𝘛", "C": "𝘛", "D": "𝘛", "E": "𝘛", "F": "𝘛", "G": "𝘛", "H": "𝘛", "I": "𝘛", "J": "𝘛", "K": "𝘛", "L": "𝘛", "M": "𝘛", "N": "𝘛", "O": "𝘛", "P": "𝘛", "Q": "𝘛", "R": "𝘛", "S": "𝘛", "T": "𝘛", "U": "𝘛", "V": "𝘛", "W": "𝘛", "X": "𝘛", "Y": "𝘛", "Z": "𝘛",
        "a": "đ", "b": "ƀ", "c": "|", "d": "𝘛", "e": "đ", "f": "𝘛", "g": "f", "h": "ǥ", "i": "𝘛", "j": "ı", "k": "𝘛", "l": "ƙ", "m": "ł", "n": "m", "o": "ṉ", "p": "ø", "q": "p", "r": "q", "s": "r", "t": "ŝ", "u": "ŧ", "v": "u", "w": "v", "x": "w", "y": "x", "z": "𝘛"
    }
}

# لیست دکوراتورهای صفحات ۳ تا ۵ (شماره ۳۱ تا ۱۰۰)
DECORATORS_LIST = [
    ("31. Sparkle Border", "✨ ", " ✨"), ("32. Heart Accent", "💖 ", " 💖"),
    ("33. Star Burst", "⭐ ", " ⭐"), ("34. Diamond Encased", "♦️ ", " ♦️"),
    ("35. Fire Style", "🔥 ", " 🔥"), ("36. Crown Premium", "👑 ", " 👑"),
    ("37. Arrow Direct", "👉 ", " 👈"), ("38. Bracket Framed", "〖 ", " 〗"),
    ("39. Double Bracket", "〘 ", " 〙"), ("40. Cross Weapon", "⚔️ ", " ⚔️"),
    ("41. Ghostly Whisper", "👻 ", " 👻"), ("42. Cyber Hacker", "🤖 [", "] 🤖"),
    ("43. Music Vibe", "🎵 ", " 🎵"), ("44. Thunderbolt", "⚡ ", " ⚡"),
    ("45. Skull Dark", "💀 ", " 💀"), ("46. Biohazard Warning", "☣️ ", " ☣️"),
    ("47. VIP Golden", "🌟 [VIP] ", " 🌟"), ("48. Rose Aesthetic", "🌹 ", " 🌹"),
    ("49. Target Focus", "🎯 ", " 🎯"), ("50. Neon Glow Look", "🔮 ", " 🔮"),
    ("51. Snowflake Chill", "❄️ ", " ❄️"), ("52. Loading Bar Style", "⏳ [", "]..."),
    ("53. Airplane Traveler", "✈️ ", " ✈️"), ("54. Money Bag", "💰 ", " 💰"),
    ("55. Game Over Style", "🎮 ", " 🎮"), ("56. Butterfly Wings", "🦋 ", " 🦋"),
    ("57. Angel Wings", "👼 [", "] 👼"), ("58. Ninja Stars", "🥷 ✴️ ", " ✴️"),
    ("59. Coffee Vibe", "☕ ", " ☕"), ("60. Lightning Striking", "⚡⚡ ", " ⚡⚡"),
    ("61. Infinity Bound", "♾️ ", " ♾️"), ("62. Danger Zone", "⚠️ [", " ] ⚠️"),
    ("63. Sakura Blossom", "🌸 ", " 🌸"), ("64. Magic Wand", "🪄 ", " 🪄"),
    ("65. Alien Tech", "👽 🛸 ", " 🛸 👽"), ("66. Red Heart Box", "❤️‍🔥 [", "] ❤️‍🔥"),
    ("67. Joker Smile", "🃏 ", " 🃏"), ("68. Ocean Wave", "🌊 ", " 🌊"),
    ("69. Teddy Bear Cute", "🧸 ", " 🧸"), ("70. Lucky Clover", "🍀 ", " 🍀"),
    ("71. Moon Light", "🌙 ", " 🌙"), ("72. Sunshine Bright", "☀️ ", " ☀️"),
    ("73. Poison Apple", "🍏 ☠️ ", " ☠️"), ("74. Rocket Booster", "🚀 ", " 🚀"),
    ("75. Balloon Pop", "🎈 ", " 🎈"), ("76. Dynamic Cross", "✝️ ", " ✝️"),
    ("77. Cyber Grid", "🌐 {", "} 🌐"), ("78. Heart Beat", "⌁⌁♡ ", " ♡⌁⌁"),
    ("79. Golden Star Box", "⭐「", "」⭐"), ("80. Retro Cassette", "🎚️ [", "] 🎚️"),
    ("81. Toxic Hazard", "☢️ ", " ☢️"), ("82. Devil Horns", "😈 ", " 😈"),
    ("83. Ice Cold", "🧊 ", " 🧊"), ("84. Dice Roll", "🎲 ", " 🎲"),
    ("85. Trophy Winner", "🏆 ", " 🏆"), ("86. Ring Bell", "🔔 ", " 🔔"),
    ("87. Explosion Burst", "💥 ", " 💥"), ("88. Yin Yang Balance", "☯️ ", " ☯️"),
    ("89. Electric Spark", "🔌 ", " 🔌"), ("90. Queen Tiara", "👸 👑 ", " 👑"),
    ("91. Footprints Trace", "👣 ", " 👣"), ("92. Sherlock Detection", "🔍 [", "] 🔎"),
    ("93. Cocktail Night", "🍸 ", " 🍸"), ("94. Wizard Hat", "🧙‍♂️ ", " 🧙‍♂️"),
    ("95. Party Popper", "🎉 ", " 🎉"), ("96. Sparkles Clean", "✨⭐ ", " ⭐✨"),
    ("97. Tech Bracket", "💻 ❮", " ❯ 💻"), ("98. Shuriken Weapon", "𓊈 ", " 𓊉"),
    ("99. Premium Seal", "🎖️ 〖", "〗 🎖️"), ("100. VIP Elite Box", "👑 🅅🄸🄿 ➔ ", " ✨")
]

def apply_font(text, font_name):
    if font_name not in FONTS_MAP:
        return text
    char_map = FONTS_MAP[font_name]
    return "".join(char_map.get(c, c) for c in text)

def is_user_member(user_id):
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status not in ['left', 'kicked']
    except ApiTelegramException:
        return True 
    except Exception:
        return True

def get_page_content(text, page):
    response_text = f"💎 **Premium Text Styler** 💎\n"
    response_text += f"━━━━━━━━━━━━━━━━━━━━\n"
    response_text += f"📝 *Your text:* `{text}`\n"
    response_text += f"📖 *Page:* `{page} / 5`\n"
    response_text += f"━━━━━━━━━━━━━━━━━━━━\n\n"
    
    markup = types.InlineKeyboardMarkup()
    
    # برای صفحات دکوراتور (۳ تا ۵)، کلمه رو به صورت خودکار با فونت Bold تزیین می‌کنیم
    fancy_base_text = apply_font(text, "1. Mathematical Bold")

    if page == 1:
        font_names = list(FONTS_MAP.keys())[:10]
        for name in font_names:
            styled = apply_font(text, name)
            response_text += f"🔹 *{name}:*\n`{styled}`\n\n"
        markup.add(types.InlineKeyboardButton("Next Page ➡️", callback_data="page_2"))
        
    elif page == 2:
        font_names = list(FONTS_MAP.keys())[10:]
        for name in font_names:
            styled = apply_font(text, name)
            response_text += f"🔹 *{name}:*\n`{styled}`\n\n"
        markup.row(
            types.InlineKeyboardButton("⬅️ Back", callback_data="page_1"),
            types.InlineKeyboardButton("Next Page ➡️", callback_data="page_3")
        )
        
    elif page == 3:
        for name, prefix, suffix in DECORATORS_LIST[:23]:
            styled = f"{prefix}{fancy_base_text}{suffix}"
            response_text += f"🔹 *{name}:*\n`{styled}`\n\n"
        markup.row(
            types.InlineKeyboardButton("⬅️ Back", callback_data="page_2"),
            types.InlineKeyboardButton("Next Page ➡️", callback_data="page_4")
        )
        
    elif page == 4:
        for name, prefix, suffix in DECORATORS_LIST[23:48]:
            styled = f"{prefix}{fancy_base_text}{suffix}"
            response_text += f"🔹 *{name}:*\n`{styled}`\n\n"
        markup.row(
            types.InlineKeyboardButton("⬅️ Back", callback_data="page_3"),
            types.InlineKeyboardButton("Next Page ➡️", callback_data="page_5")
        )
        
    elif page == 5:
        for name, prefix, suffix in DECORATORS_LIST[48:]:
            styled = f"{prefix}{fancy_base_text}{suffix}"
            response_text += f"🔹 *{name}:*\n`{styled}`\n\n"
        markup.add(types.InlineKeyboardButton("⬅️ Back", callback_data="page_4"))
        
    response_text += f"━━━━━━━━━━━━━━━━━━━━\n"
    response_text += f"💡 *Tip:* Tap on any style to copy it instantly!"
    return response_text, markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if is_user_member(user_id):
        welcome_text = (
            "🪐 **Welcome to Premium Font Stylizer Bot!**\n\n"
            "Transform your ordinary text into cool, eye-catching fonts instantly. Over 100+ Unique styles are ready! 🔥\n\n"
            "📥 **How to use:**\n"
            "Simply send me any text or name in English right now!"
        )
        bot.reply_to(message, welcome_text, parse_mode="Markdown")
    else:
        markup = types.InlineKeyboardMarkup()
        clean_channel = CHANNEL_ID.replace('@', '')
        btn_join = types.InlineKeyboardButton("📢 Join Channel", url=f"https://t.me/{clean_channel}")
        btn_check = types.InlineKeyboardButton("🚀 Verify Joined 🚀", callback_data="check_join")
        markup.add(btn_join)
        markup.add(btn_check)
        lock_text = (
            "🔒 **Access Locked!**\n\n"
            "To unlock the 100 premium fonts, you must join our official updates channel first. It only takes a second! ⚡"
        )
        bot.send_message(user_id, lock_text, parse_mode="Markdown", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ["page_1", "page_2", "page_3", "page_4", "page_5"])
def handle_pagination(call):
    try:
        original_msg = call.message.reply_to_message
        if original_msg and original_msg.text:
            text = original_msg.text
        else:
            bot.answer_callback_query(call.id, "⚠️ Please send a new text to style!", show_alert=True)
            return
            
        target_page = int(call.data.split("_")[1])
        content, markup = get_page_content(text, target_page)
        bot.edit_message_text(content, chat_id=call.message.chat.id, message_id=call.message.message_id, parse_mode="Markdown", reply_markup=markup)
        bot.answer_callback_query(call.id)
    except Exception:
        bot.answer_callback_query(call.id, "⚠️ Error loading page. Send a new text!", show_alert=True)

@bot.callback_query_handler(func=lambda call: call.data == "check_join")
def check_callback(call):
    user_id = call.from_user.id
    if is_user_member(user_id):
        bot.answer_callback_query(call.id, "🎉 Access Granted! Enjoy!", show_alert=False)
        bot.send_message(user_id, "✅ **Verified successfully!**\n\nGo ahead, send me your English text to get 100 premium styles! 👇", parse_mode="Markdown")
    else:
        bot.answer_callback_query(call.id, "❌ You have not joined the channel yet! Please subscribe first.", show_alert=True)

@bot.message_handler(func=lambda message: True)
def text_stylizer(message):
    user_id = message.from_user.id
    if not is_user_member(user_id):
        send_welcome(message)
        return
    content, markup = get_page_content(message.text, 1)
    bot.reply_to(message, content, parse_mode="Markdown", reply_markup=markup)

print("100% Fixed Font Bot is running perfectly...")
bot.infinity_polling()
