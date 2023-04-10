import json

from pip._vendor import requests
from minehub.service.MessageService import MessageService
from minehub.service.question.QuestionService import QuestionService
from minehub.service.users.UserService import UserService
from minehub.utils.Constants import Constants
from minehub.utils.Utils import Utils


#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 05/03/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the server service
#


class ServerService():

    @classmethod
    def get(cls):
        return {
            'online_players':
                json.loads(requests.get('https://mcapi.us/server/status?port=25565&ip=fightclubmc.net').text)[
                    'players']['now'],
            # 'online_discord_users': cls.getOnlineDiscordUsers(),
            'messages': len(MessageService.getAllMessages()),
            'questions': len(QuestionService.getAllQuestions()),
            'registered_users': len(UserService.getAllUsers())
        }

    @classmethod
    def getOnlineDiscordUsers(cls):
        users = json.loads(requests.get('https://discordapp.com/api/guilds/1048940424804450334/widget.json').text)['members']
        counter = 0
        for user in users:
            if user['status'] == "online":
                counter += 1
        return counter

    @classmethod
    def maintenance(cls):
        resourceConfig = json.load(open('resources/config.json'))
        return Utils.createSuccessResponse(True, True if resourceConfig['maintenance'] == "true" else False)

    @classmethod
    def setMaintenance(cls, status):
        resourceConfig = json.load(open('resources/config.json'))
        resourceConfig['maintenance'] = status
        with open("resources/config.json", "w") as outfile:
            json.dump(resourceConfig, outfile)
        return Utils.createSuccessResponse(True, Constants.CREATED)
