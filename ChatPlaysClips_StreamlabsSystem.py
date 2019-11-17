# ---------------------------------------
# Import Libraries
# ---------------------------------------
import os
import json
import codecs
import sys
import threading
sys.path.append(os.path.dirname(__file__))
import constants
BridgeApp = os.path.join(os.path.dirname(__file__), "bridge\\SLOBSRC.exe")
from clips import Clip

# ---------------------------------------
# Script Information
# ---------------------------------------
ScriptName = "ChatPlaysClips"
Website = "https://www.twitch.tv/meisterboom"
Description = "Allows viewers to play certain clips and videos with a chat command."
Creator = "MeisterBoom"
Version = "0.1.0"

# ---------------------------------------
# Globals
# ---------------------------------------
work_dir = None
settings_file = None
settings = {}
clipcollection = list()
clip_playing = False
ui_config_file = None
global_cooldown_key = "!CPC_GLOBAL"
global_cooldown_setting = 0
user_cooldown_key = "!CPC_USER"
user_cooldown_setting = 0

# ---------------------------------------
# Helper Functions
# ---------------------------------------


def Logger(response):
    if response:
        Parent.Log(ScriptName, response)
    return


def SetSourceVisibility(source, visibility, scene=None):
    """ Set the visibility of a source optionally in a targeted scene. """
    if scene:
        Logger(os.popen("{0} visibility_source_scene \"{1}\" \"{2}\" {3}".format(BridgeApp, source, scene, visibility)).read())
    else:
        Logger(os.popen("{0} visibility_source_active \"{1}\" {2}".format(BridgeApp, source, visibility)).read())
    return


# ---------------------------------------
# Init
# ---------------------------------------
def Init():
    global work_dir
    global ui_config_file
    work_dir = os.path.dirname(__file__)
    ui_config_file = os.path.join(work_dir, "UI_Config.json")
    if __init_settings():
        if __load_clips_from_directory():
            __overwrite_ui_config()
        else:
            __reset_ui_settings()
    else:
        __reset_ui_settings()
    return


def __init_settings():
    """ Initializes settings file. Returns true on success, else first time startup. """
    try:
        global settings_file
        global settings
        global global_cooldown_setting
        global user_cooldown_setting
        settings_file = os.path.join(work_dir, "settings.json")
        if os.path.exists(settings_file):
            with codecs.open(settings_file, encoding='utf-8-sig') as set_file:
                settings = json.load(set_file, encoding='utf-8-sig')
            if "global_cooldown" in settings:
                if settings["global_cooldown"] > 0:
                    global_cooldown_setting = settings["global_cooldown"]
            if "user_cooldown" in settings:
                if settings["user_cooldown"] > 0:
                    user_cooldown_setting = settings["user_cooldown"]
            return True
        return False
    except Exception, e:
        Logger("__init_settings_file: " + str(e))
        return False


def __load_clips_from_directory():
    """ Loads the clips from the directory parsed in the settings file. Returns True on success"""
    try:
        if os.path.exists(settings["directory"]):
            for f in os.listdir(settings["directory"]):
                if f.endswith(".mp4"):
                    clipcollection.append(Clip(settings["directory"], f, settings))
            return True
        Logger("__load_clips_from_directory: Path {} does not exist!".format(settings["directory"]))
        return False
    except Exception, e:
        Logger("__load_clips_from_directory: " + str(e))
        return False


def __overwrite_ui_config():
    """ Overwrites the UI_Config to display all the clips loaded."""
    try:
        global ui_config_file
        if len(clipcollection) > 0:
            ui_string = constants.default_ui_config
            ui_string += ",\n  "
            for clip in clipcollection:
                ui_string += clip.ui_settings()
                ui_string += ",\n  "
            ui_string = ui_string[:ui_string.rfind(',')]
            ui_string += "\n}"
            file_writer = open(ui_config_file, "w")
            file_writer.write(ui_string)
        else:
            __reset_ui_settings()
    except Exception, e:
        Logger("__overwrite_ui_config: " + str(e))


def __reset_ui_settings():
    """ Resets the UI_Config."""
    try:
        global ui_config_file
        ui_string = constants.default_ui_config
        ui_string += "\n}"
        file_writer = open(ui_config_file, "w")
        file_writer.write(ui_string)
    except Exception, e:
        Logger("__reset_ui_settings: " + str(e))

#---------------------------------------
# Execute
#---------------------------------------

def Execute(data):
    if "enabled" in settings and settings["enabled"] and data.IsChatMessage() and not clip_playing:
        command = data.GetParam(0).lower()
        if str(command).startswith("!"):
            for clip in clipcollection:
                if clip.command == str(command):
                    if clip.active:
                        userId = data.User
                        username = data.UserName
                        if __cost_check(clip, userId, username):
                            if __user_cooldown_check(userId, username):
                                if __global_cooldown_check(username):
                                    if __clip_cooldown_check(clip, username):
                                        __play_clip(clip, userId)
                        break
    return


def __cost_check(clip, userId, username):
    if clip.cost is not None and clip.cost > 0:
        userpoints = Parent.GetPoints(userId)
        if userpoints >= clip.cost:
            return True
        else:
            if "user_cost_message" in settings:
                message = str(settings["user_cost_message"])
                if message != "" and len(message) > 0:
                    message = message.replace("$user", username)
                    message = message.replace("$d", str(clip.cost - userpoints))
                    message = message.replace("$curr", Parent.GetCurrencyName())
                    Parent.SendStreamMessage(message)
            return False
    else:
        return True


def __global_cooldown_check(username):
    if global_cooldown_setting <= 0:
        return True
    else:
        if Parent.IsOnCooldown(ScriptName, global_cooldown_key):
            if "global_cooldown_message" in settings:
                message = str(settings["global_cooldown_message"])
                if message != "" and len(message) > 0:
                    message = message.replace("$user", username)
                    cdi = Parent.GetCooldownDuration(ScriptName, global_cooldown_key)
                    message = message.replace("$s", str(cdi))
                    Parent.SendStreamMessage(message)
            return False
        else:
            return True


def __user_cooldown_check(userId, username):
    if user_cooldown_setting <= 0:
        return True
    else:
        if Parent.IsOnUserCooldown(ScriptName, user_cooldown_key, userId):
            if "user_cooldown_message" in settings:
                message = str(settings["user_cooldown_message"])
                if message != "" and len(message) > 0:
                    message = message.replace("$user", username)
                    cdi = Parent.GetUserCooldownDuration(ScriptName, user_cooldown_key, userId)
                    message = message.replace("$s", str(cdi))
                    Parent.SendStreamMessage(message)
            return False
        else:
            return True


def __clip_cooldown_check(clip, username):
    if clip.cooldown <= 0:
        return True
    else:
        if Parent.IsOnCooldown(ScriptName, clip.command):
            if "specific_cooldown_message" in settings:
                message = str(settings["specific_cooldown_message"])
                if message != "" and len(message) > 0:
                    message = message.replace("$user", username)
                    cdi = Parent.GetCooldownDuration(ScriptName, clip.command)
                    message = message.replace("$s", str(cdi))
                    message = message.replace("$c", clip.command)
                    Parent.SendStreamMessage(message)
            return False
        else:
            return True


def __play_clip(clip, userId):
    global clip_playing
    clip_playing = True

    if global_cooldown_setting > 0:
        Parent.AddCooldown(ScriptName, global_cooldown_key, global_cooldown_setting)
    if user_cooldown_setting > 0:
        Parent.AddUserCooldown(ScriptName, user_cooldown_key, userId, user_cooldown_setting)
    if clip.cooldown > 0:
        Parent.AddCooldown(ScriptName, clip.command, clip.cooldown)
    __show_clip(clip)
    if clip.duration > 0:
        t = threading.Timer(clip.duration, lambda: __hide_clip(clip))
        t.start()
    return


def __show_clip(clip):
    clip.playing = True
    threading.Thread(target=SetSourceVisibility, args=(clip.source, "on", clip.scene)).start()
    return


def __hide_clip(clip):
    global clip_playing
    clip.playing = False
    clip_playing = False
    threading.Thread(target=SetSourceVisibility, args=(clip.source, "off", clip.scene)).start()
    return


# ---------------------------------------
# Tick
# ---------------------------------------
def Tick():
    return
