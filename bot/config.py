#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", "7713526")
    API_HASH = config("API_HASH", "6f87b351ddf6c8c56999f8ba5b19cc7c")
    BOT_TOKEN = config("BOT_TOKEN", "5729180937:AAFtuwuwXYxu2EAe-5oT1haxigXZ5tE13c8")
    DEV = 1664850827
    OWNER = config("OWNER","1853178421")
    ffmpegcode = ["-preset faster -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By Compbot' -pix_fmt yuv420p -crf 30 -c:a libopus -b:a 32k -c:s copy -map 0 -ac 2 -ab 32k -vbr 2 -level 3.1 -threads 1"]
    THUMBNAIL = config("THUMBNAIL", default="https://graph.org/file/b115581cc78cfa93390d2.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
