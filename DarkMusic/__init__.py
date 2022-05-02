#
# Copyright (C) 2022 by TEAM-DARK-MUSIC@Github, < https://github.com/TEAM-DARK-MUSIC >.
#
# This file is part of < https://github.com/TEAM-DARK-MUSIC/DarkMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TEAM-DARK-MUSIC/DarkMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from DarkMusic.core.bot import DarkBot
from DarkMusic.core.dir import dirr
from DarkMusic.core.git import git
from DarkMusic.core.userbot import Userbot
from DarkMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = DarkBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
