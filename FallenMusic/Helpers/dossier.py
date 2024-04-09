# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from FallenMusic import BOT_NAME

PM_START_TEXT = """
ʜᴇʏ {0}, 🥀
๏ ᴛʜɪs ɪs** {1} !

🇹🇷 telegramın en hızlı ve güçlü botu .
"""

START_TEXT = """
**hoş geldiniz** {0}, 🥀
  {1} komutlarım aşağıdan ordan özelliklerime bakabilirsin {2}.

──────────────────
➻ Hakkımda bilgi almak için ya da bir şey sormak istersen bana katılabilirsin [sᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ]({3}).
"""

HELP_TEXT = f"""
<u>❄ **kullanıcılar için mevcut komutlar {BOT_NAME} :**</u>

๏ /oynat : [sarki ismi] şarkıyı başlatır.
๏ /dur : şarkıyı durdurur.
๏ /dewam : şarkıyı dewam eder.
๏ /skip : şarkıyı atlar diğer sıradaki Şarkıyı açar.
๏ /end : sesli sohbeti durdurur.

๏ /ping : info çeker.
๏ /sudolist : yonetici sayisina bakar.

๏ /song : [şarkı ismi] istediğiniz şarkıyı arar bulur.

๏ /search : sᴇᴀʀᴄᴇs ᴛʜᴇ ɢɪᴠᴇɴ ǫᴜᴇʀʏ ᴏɴ ʏᴏᴜᴛᴜʙᴇ ᴀɴᴅ sʜᴏᴡs ʏᴏᴜ ᴛʜᴇ ʀᴇsᴜʟᴛ.
"""

HELP_SUDO = f"""
<u>✨ **yonetici komutları ɪɴ {BOT_NAME} :**</u>

๏ /activevc : sʜᴏᴡs ᴛʜᴇ ʟɪsᴛ ᴏғ ᴄᴜʀʀᴇɴᴛʟʏ ᴀᴄᴛɪᴠᴇ ᴠᴏɪᴄᴇᴄʜᴀᴛs.
๏ /eval or /sh : ʀᴜɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴄᴏᴅᴇ ᴏɴ ᴛʜᴇ ʙᴏᴛ's ᴛᴇʀᴍɪɴᴀʟ.
๏ /speedtest : ʀᴜɴs ᴀ sᴘᴇᴇᴅᴛᴇsᴛ ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.
๏ /sysstats : sʜᴏᴡs ᴛʜᴇ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.

๏ /setname [ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ɴᴀᴍᴇ.
๏ /setbio [ᴛᴇxᴛ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴛᴇxᴛ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ʙɪᴏ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
๏ /setpfp [ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ] : ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴘғᴘ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
๏ /delpfp : ᴅᴇʟᴇᴛᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘғᴘ ᴏғ ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ.
"""

HELP_DEV = f"""
<u>✨ **ᴏᴡɴᴇʀ ᴄᴏᴍᴍᴀɴᴅs ɪɴ {BOT_NAME} :**</u>

๏ /config : ᴛᴏ ɢᴇᴛ ᴀʟʟ ᴄᴏɴꜰɪɢ ᴠᴀʀɪᴀʙʟᴇꜱ ᴏꜰ ʙᴏᴛ.
๏ /broadcast [ᴍᴇssᴀɢᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ] : ʙʀᴏᴀᴅᴄᴀsᴛ ᴛʜᴇ ᴍᴇssᴀɢᴇ ᴛᴏ sᴇʀᴠᴇᴅ ᴄʜᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
๏ /rmdownloads : ᴄʟᴇᴀʀs ᴛʜᴇ ᴄᴀᴄʜᴇ ғɪʟᴇs ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ ᴏɴ ᴛʜᴇ ʙᴏᴛ's sᴇʀᴠᴇʀ.
๏ /leaveall : ᴏʀᴅᴇʀs ᴛʜᴇ ᴀssɪsᴛᴀɴᴛ ᴀᴄᴄᴏᴜɴᴛ ᴛᴏ ʟᴇᴀᴠᴇ ᴀʟʟ ᴄʜᴀᴛs.

๏ /addsudo [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ᴀᴅᴅ ᴛʜᴇ ᴜsᴇʀ ᴛᴏ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.
๏ /rmsudo [ᴜsᴇʀɴᴀᴍᴇ ᴏʀ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴜsᴇʀ] : ʀᴇᴍᴏᴠᴇ ᴛʜᴇ ᴜsᴇʀ ғʀᴏᴍ sᴜᴅᴏ ᴜsᴇʀs ʟɪsᴛ.
"""
