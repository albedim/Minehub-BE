
#
# @author: Alberto Di Maio, albedim <dimaio.albe@gmail.com>
# Created on: 08/02/23
# Created at: 14:35
# Version: 1.0.0
# Description: This is the class for the constants
#

class Constants():

    NOT_FOUND: str = "This resource was not found"
    NOT_ENOUGH_PERMISSIONS: str = "Not enough permissions"
    CREATED: str = "Created"
    UP_TO_DATE: str = "Up To date"
    NOT_UP_TO_DATE: str = "Not Up To date"
    FULL_SLOTS = "You can't add more"
    ALREADY_CREATED = "This resource was already created"
    INVALID_REQUEST: str = "Invalid request"

    FRONTEND_URL = ''
    DEFAULT_IMAGE = 'default.png'

    EMAIL = 'fightclubmcserver@gmail.com'
    PASSWORD = 'xuqttkjvixdatmzj'
    WELCOME_EMAIL: str = "Hey {name}! \n Benvenuto nella nostra piattaforma"
    PASSWORD_FORGOTTEN_EMAIL: str = "Hey! \n Ecco il link per recuperare la tua password: " + FRONTEND_URL + "/create_password?token={token}"

    PAGE_NOT_FOUND = 'This page was not found. See our documentation'
    PAGE_METHOD_NOT_ALLOWED = 'Method not allowed. See our documentation'
    PAGE_UNKNOWN_ERROR = 'Unknown error'
    QUESTION_STATUS = {'JUST_CREATED': 'just_created', 'READING': 'reading', 'ACCEPTED': 'accepted', 'REJECTED': 'rejected'}
