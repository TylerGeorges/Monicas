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
        
    def build_commands_map(self):
        return {
            '!help': {
                'function': 'command_help',
                'example': '!help',
                'description': 'Displays a list of valid commands'
            },
            '!wiki': {
                'function': 'command_wiki',
                'example': '!wiki <search phrase>',
                'description': 'returns a single search result from wiki (via DuckDuckGo)'
            },
            '<@{}>'.format(self.bot_id): {
                'function': 'command_robot',
                'example': '@{} <question>'.format(self.name),
                'description': 'chat with {}'.format(self.name)
            },
            '!demo': {
                'function': 'command_demo',
                'example': '!demo <question>',
                'description': 'play with the current command in demo mode'
            },
            '!uptime': {
                'function': 'command_uptime',
                'example': '!uptime',
                'description': 'Show <@{}>\'s uptime'.format(self.name)
            },
            '!version': {
                'function': 'command_version',
                'example': '!version',
                'description': 'Show <@{}>\'s version'.format(self.name)
            }
        }
