<p align="center"><a href="https://t.me/NOINOI_BOT"><img src="https://telegra.ph/file/c15feb04daa395f5f5b89.jpg"></a></p>
<p align="center">
    <br><b>Video Stream is an Advanced Telegram Bot that's allow you to play Video & Music on Telegram Group Video Chat</b><br>
</p>

## ✨ Features
- Music & Video stream support
- MultiChat support
- Playlist & Queue support
- Skip, Pause, Resume, Stop feature
- Music & Video downloader feature
- Inline Search support
- YouTube direct search support
- YouTube/Local/Live/m3u8 stream support
- Inline Search support
- Control With Button support
- Volume Control
- Userbot Auto Join
- Broadcast & Global Ban
- Shell Executor (eval & sh)
- SpeedTest Runner
- Direct Updater

## 🛠 Commands:
| Command | Description |
| ------ | ------ |
| `/play (query)` | play music from youtube |
| `/vplay (query)` | play video from youtube |
| `/vstream (live link)` | play video live streaming video |
| `/pause` | pause the streaming (admin only) |
| `/resume` | resume the streaming (admin only) |
| `/skip` | switch to next stream (admin only) |
| `/stop` | end the streaming (admin only) |
| `/vmute` | for mute the userbot on voice chat |
| `/vunmute` | for unmute the userbot on voice chat |
| `/volume 1/200` | adjust the volume of userbot (userbot must be admin) |
| `/playlist` | show you all the current stream list |
| `/song (query)` | download music from youtube |
| `/video (query)` | download video from youtube |
| `/userbotjoin` | invite the userbot to join group (admin only) |
| `/userbotleave` | instruct userbot to leave the group (admin only) |
| `/leaveall` | order the userbot to leave from all group (sudo only) |
| `/update` | update your bot directly without leaving telegram (sudo only) |
| `/restart` | restart your bot directly without leaving telegram (sudo only) |
| `/speedtest` | run server speedtest that you use to run your bot |
| `/broadcast` | brodcast message to all group that in bot database |
| `/gban & /ungban` | use this to gban someone and ungban them |

## Generate Session Name 🔻

[![GenerateString](https://img.shields.io/badge/repl.it-generateString-yellowgreen)](https://replit.com/@levinalab/StringSession#main.py)

## Heroku Deployment 💜

<h3 align="center">Click The button below for deploy your bot to Heroku, Note: Set the app country to Europe (it will help to make the bot stable).</h3>
<p align="center"><a href="https://heroku.com/deploy"><img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" target="_blank"/></a></p>

## VPS Deployment 📡
Get the best Quality of streaming performance by hosting it on VPS, here's the step's:

```sh
sudo apt update && apt upgrade -y
sudo apt install git curl python3-pip ffmpeg -y
pip3 install -U pip
curl -sL https://deb.nodesource.com/setup_16.x | bash -
sudo apt-get install -y nodejs
npm i -g npm
git clone https://github.com/levina-lab/video-stream # clone the repo.
cd video-stream
pip3 install -U -r requirements.txt
cp example.env .env # use vim to edit ENVs
vim .env # fill up the ENVs (Steps: press i to enter in insert mode then edit the file. Press Esc to exit the editing mode then type :wq! and press Enter key to save the file).
python3 main.py # run the bot.

# continue the host with screen or anything else, thanks for reading.
```

# Credits 💖

- [Baziibro](https://github.com/levina-lab) ``Dev``
- [heyaaman](https://github.com/Zxce3) ``Supporter``
- [Levina](https://github.com/levina-lab) ``Bacecode``
- [Laky's](https://github.com/Laky-64) for [``py-tgcalls``](https://github.com/pytgcalls/pytgcalls)
- [Dan](https://github.com/delivrance) for [``Pyrogram``](https://github.com/pyrogram)

### Support & Updates 🎑
<a href="https://t.me/CFC_BOT_SUPPORT"><img src="https://img.shields.io/badge/Join-Group%20Support-blue.svg?style=for-the-badge&logo=Telegram"></a> <a href="https://t.me/BAZIGARXD"><img src="https://img.shields.io/badge/Join-Updates%20Channel-blue.svg?style=for-the-badge&logo=Telegram"></a>
