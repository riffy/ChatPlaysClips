# ChatPlaysClips

A script for Streamlabs OBS Chatbot that allows viewer to play certain clips. 
Basically its an extended version of OCGineers SLOBS Remote script (see below) using Cooldowns, Costs etc.

The script will load all clips available in a certain directory (**.mp4 files right now only**) so you can make certain settings clip-specific.

## Upcoming Features
* Read the clip duration from file and set as initial setting when loading directory
* Reload script automatically after settings have been changed
* Support more file extensions (mkv, flv, etc.)
* Check if SLOBSRC + Script is used and use the settings from OCGineers script to guarantee compatibility

## Getting Started

1. Download this repository as a .ZIP archive, or go to Releases and download the .ZIP file from there.
2. Import the script to your SLOBS Chatbot program.
3. Change the script general settings.
4. Click **Save Settings**, click ***Reload Scripts*** and click on the script **again**
5. Adjust clip settings and repeat step 4
6. It should work now

### General Settings

![General_Settings](https://user-images.githubusercontent.com/13089522/69006929-d8e52000-0936-11ea-8339-5f5486e64955.PNG)

| Setting  | Description |
| ------------- | ------------- |
| `SLOBS Scene`  | The scene name that contains the clips to play. If left empty, the active scene will be used.  |
| `Clip Directory`  | Path to the directory that contains all clips. Clips will be loaded from this directory.  |
| `User Cost Message`  | The message to be played, when a user has insufficient points to play clip.  |
| `Global Clip Cooldown`  | The time that needs to pass before the next clip can be played (globally). Use this to prevent spamming.  |
| `Global Clip Cooldown Message`  | Any entry will send out a message, if global cooldown is applied. $user , $s . Cost before User Cooldown before Global Cooldown before Clip cooldown!  |
| `User Clip Cooldown`  | The time that needs to pass before a user can play the next clip (globally).  |
| `User Clip Cooldown Message`  | Any entry will send out a message, if user cooldown is applied. $user , $s . Cost before User Cooldown before Global Cooldown before Clip cooldown!  |
| `Specific / Clip Cooldown Message`  | Any entry will send out a message, if clip cooldown is applied. $user , $c , $s . Cost before User Cooldown before Global Cooldown before Clip cooldown!  |

**DON'T FORGET TO SAVE SETTINGS AND RELOAD SCRIPT / VIEW**

### Clip Settings

![clip_settings](https://user-images.githubusercontent.com/13089522/69007016-74c35b80-0938-11ea-9121-11bee96d3557.PNG)

| Setting  | Description |
| ------------- | ------------- |
| `Active`  | Enables / Disables the clip.  |
| `SLOBS Source Name`  | Sourcename in Streamlabs OBS for the clip.  |
| `Duration`  | The time that displays / shows the source in seconds.  |
| `Currency Cost`  | Currency cost to play the Clip. 0 disables cost check.  |
| `Cooldown`  | Cooldown in seconds until this clip can be played again in seconds.  |
| `Command`  | Command to trigger the play of the clip.  |


**DON'T FORGET TO SAVE SETTINGS AND RELOAD SCRIPT / VIEW**

## Contributing

If you want to contribute, open a Pull Request or write an issue.


## Credits & Acknowledgments

* [OCGineer](https://www.ocgineer.com/sl/chatbot/slobsremote.html) - For providing the SLOBS Remote Control. ***Kudos!***
* [Bare7a](https://github.com/Bare7a) - For giving inspiration and helping with the first steps 
