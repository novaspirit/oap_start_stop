# OpenAuto Pro Raspberry Pi Start Up And Shut Down Script

[![Discord](https://img.shields.io/discord/316245914987528193?logo=discord)](https://discord.com/invite/v8dAnFV) [![Youtube](https://img.shields.io/badge/YouTube-FF0000?style=flat-square&logo=youtube&logoColor=white)](https://www.youtube.com/channel/UCrjKdwxaQMSV_NDywgKXVmw) [![Twitter URL](https://img.shields.io/twitter/follow/novaspirittech?style=flat-square&logo=twitter)](https://twitter.com/novaspirittech)

YouTube Video [Use For Reference](https://youtu.be/ko-udLtaPk8)

![](/startshutdown_bb.jpg)


## startup script
Load the `tart_script.ino` to your esp01 

## shutdown script
type in terminal
`sudo crontab -e`

add this to the end of crontab

`@reboot /usr/bin/python3 /home/pi/listen_for_shutdown.py >/dev/null 2>&1`
