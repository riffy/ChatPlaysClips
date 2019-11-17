class Clip(object):
    def __init__(self, path, f, settings):
        self.path = path
        self.file = f
        self.playing = False
        self.active = True
        self.active_key = "clip_{}_active".format(self.filename())
        self.source = "{}".format(self.filename())
        self.source_key = "clip_{}_source".format(self.filename())
        self.cooldown = 0
        self.cooldown_key = "clip_{}_cooldown".format(self.filename())
        self.cost = 0
        self.cost_key = "clip_{}_cost".format(self.filename())
        self.duration = 0
        self.duration_key = "clip_{}_duration".format(self.filename())
        self.command = "!"
        self.command_key = "clip_{}_command".format(self.filename())
        self.scene = None
        self.scene_key = "scene_name"
        self.__apply_settings(settings)


    def __apply_settings(self, settings):
        if self.active_key in settings:
            self.active = settings[self.active_key]
        if self.source_key in settings:
            self.source = settings[self.source_key]
        if self.cooldown_key in settings:
            self.cooldown = settings[self.cooldown_key]
        if self.cost_key in settings:
            self.cost = settings[self.cost_key]
        if self.duration_key in settings:
            self.duration = settings[self.duration_key]
        if self.command_key in settings:
            self.command = settings[self.command_key]
        if self.scene_key in settings:
            if len(settings[self.scene_key]) > 0:
                self.scene = settings[self.scene_key]
            else:
                self.scene = None
        else:
            self.scene = None


    def fullpath(self):
        return self.path + "\\" + self.file


    def filename(self, extension=False):
        if extension:
            return self.file
        return self.file[:self.file.rfind(".")]


    def ui_settings(self):
        return self._ui_active() + ",\n  " + self._ui_source() + ",\n  " + self._ui_duration() + ",\n  " + \
               self._ui_cost() + ",\n  " + self._ui_cooldown() + ",\n  " + self._ui_command()


    def _ui_active(self):
        re = """"clip_{}_active": """.format(self.filename()) + "{\n" + """    "group": "{}",
    "type": "checkbox",
    "value": {},
    "label": "Active",
    "tooltip": "Enables / Disables the clip." """.format(self.filename(True), str(self.active).lower()) + "\n  }"
        return re


    def _ui_source(self):
        re = """"clip_{}_source": """.format(self.filename()) + "{\n" + """    "group": "{}",
    "type": "textbox",
    "value": "{}",
    "label": "SLOBS Source Name",
    "tooltip": "Sourcename in Streamlabs OBS for the clip." """.format(self.filename(True), self.source) + "\n  }"
        return re


    def _ui_duration(self):
        re = """"clip_{}_duration": """.format(self.filename()) + "{\n" + """    "group": "{}",
    "type": "numberbox",
    "value": {},
    "label": "Duration (seconds)",
    "tooltip": "The time that displays / shows the source in seconds." """.format(self.filename(True), self.duration) + \
             "\n  }"
        return re


    def _ui_cost(self):
        re = """"clip_{}_cost": """.format(self.filename()) + "{\n" + """    "group": "{}",
    "type": "numberbox",
    "value": {},
    "label": "Currency Cost",
    "tooltip": "Currency cost to play the Clip. 0 disables cost check." """.format(self.filename(True), self.cost) + \
             "\n  }"
        return re


    def _ui_cooldown(self):
        re = """"clip_{}_cooldown": """.format(self.filename()) + "{\n" + """    "group": "{}",
    "type": "numberbox",
    "value": {},
    "label": "Cooldown",
    "tooltip": "Cooldown in seconds until this clip can be played again in seconds." """.format(self.filename(True), self.cooldown) + \
             "\n  }"
        return re


    def _ui_command(self):
        re = """"clip_{}_command": """.format(self.filename()) + "{\n" + """    "group": "{}",
    "type": "textbox",
    "value": "{}",
    "label": "Command",
    "tooltip": "Command to trigger the play of the clip." """.format(self.filename(True), self.command) + \
            "\n  }"
        return re
