import os
import time

import logging
from slackclient import SlackClient
from duckduckpy import query
import wolframalpha

class Robot:

    def __init__(self, name='robot'):
        self.name = name
        self.slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))
        self.bot_id = self.get_bot_id()
        self.wa_client = wolframalpha.Client(os.environ.get('WA_TOKEN'))
        self.bot_start_time = time.time()
        self.read_delay = 0.2
        self.version = '0.2.3 (alpha)'
        self.COMMANDS_MAP = self.build_commands_map()
