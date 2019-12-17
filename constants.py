default_ui_config = """{
  "output_file": "settings.json",
  "enabled": {
    "group": "General Settings",
    "type": "checkbox",
    "value": true,
    "label": "Enable this script",
    "tooltip": "Enable / Disable the script."
  },
  "scene_name": {
    "group": "General Settings",
    "type": "textbox",
    "value": "Scene Name",
    "label": "SLOBS Scene",
    "tooltip": "Name of the scene that contains the media sources."
  },
  "directory": {
    "group": "General Settings",
    "type": "textbox",
    "value": "",
    "label": "Clip Directory",
    "tooltip": "Paste in the directory where the clips are located."
  },
  "user_cost_message": {
    "group": "General Settings",
    "type": "textbox",
    "value": "Sorry $user , you miss $d $curr to play this clip.",
    "label": "User Cost Message",
    "tooltip": "Any entry will send out a message, if user doesn't have enough points. $user , $d , $curr . Cost before User Cooldown before Global Cooldown before Clip cooldown!"
  },
  "global_cooldown": {
    "group": "General Settings",
    "type": "numberbox",
    "label": "Global Clip Cooldown (seconds)",
    "tooltip": "The time that needs to pass before the next clip can be played (globally).",
    "value": 120
  },
  "global_cooldown_message": {
    "group": "General Settings",
    "type": "textbox",
    "value": "Sorry $user , clips are still on cooldown for another $s seconds.",
    "label": "Global Cooldown Message",
    "tooltip": "Any entry will send out a message, if global cooldown is applied. $user , $s . Cost before User Cooldown before Global Cooldown before Clip cooldown!"
  },
  "user_cooldown": {
    "group": "General Settings",
    "type": "numberbox",
    "label": "Global User Clip Cooldown (seconds)",
    "tooltip": "The time that needs to pass before a user can play the next clip (globally).",
    "value": 120
  },
  "user_cooldown_message": {
    "group": "General Settings",
    "type": "textbox",
    "value": "Sorry $user , you are still on cooldown for another $s seconds.",
    "label": "User Cooldown Message",
    "tooltip": "Any entry will send out a message, if user cooldown is applied. $user , $s . Cost before User Cooldown before Global Cooldown before Clip cooldown!"
  },
  "specific_cooldown_message": {
    "group": "General Settings",
    "type": "textbox",
    "value": "Sorry $user , the clip $c is still on cooldown for another $s seconds.",
    "label": "Specific Cooldown Message",
    "tooltip": "Any entry will send out a message, if clip cooldown is applied. $user , $c , $s . Cost before User Cooldown before Global Cooldown before Clip cooldown!"
  }"""

default_clip_config = """"clip_{}_active": {
    "group": "{}",
    "type": "checkbox",
    "value": {},
    "label": "Active",
    "tooltip": "Enables / Disables the clip."
  },
  "clip_{}_source": {
    "group": "{}",
    "type": "textbox",
    "value": "{}",
    "label": "SLOBS Source Name",
    "tooltip": "Sourcename in Streamlabs OBS for the clip."
  },
  "clip_{}_duration": {
    "group": "{}",
    "type": "numberbox",
    "label": "Duration (seconds)",
    "tooltip": "The time that displays / shows the source in seconds. 0 will show source and not hide it.",
    "value": {}
  },
  "clip_{}_cost": {
    "group": "{}",
    "type": "numberbox",
    "label": "Currency Cost",
    "tooltip": "Currency cost to play the Clip. 0 disables cost check",
    "value": {}
  },
  "clip_{}_cooldown": {
    "group": "{}",
    "type": "numberbox",
    "label": "Cooldown",
    "tooltip": "Cooldown in seconds until this clip can be played again in seconds. 0 will have no clip cooldown effect",
    "value": {}
  }"""

media_extensions = [".mp4", ".ts", ".mov", ".flv", ".mkv", ".avi", ".mp3", ".ogg", ".aac", ".wav", ".gif", ".webm"]