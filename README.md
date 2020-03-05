# tsuserverCC

A Python-based server for Attorney Online, forked from [AttorneyOnline/tsuserver3](https://github.com/AttorneyOnline/tsuserver3)

Requires Python 3.6+ and PyYAML.

### Changes/additions from tsuserver3
* Fully-functional party system with Main Game features inbuilt,
* Testimony recording/playback system,
* Greatly extended support for custom content,
* More options for area management, including:
  - On-the-fly area renaming, creation, and destruction,
  - Password locks,
  - Ability to connect areas via 'exits,'
  - and playercount hiding.
* Serverside notepads,
* Additional moderation features,
* and a category-based music shuffle system.

## How to use

* Install the latest version of Python. **Python 2 will not work**, as tsuserver3 depends on async/await, which can only be found on Python 3.5 and newer.
  - If your system supports it, it is recommended that you use a separate virtual environment, such as [Anaconda](https://www.continuum.io/downloads) for Windows, or [virtualenv](https://virtualenv.pypa.io/en/stable/) for everyone else (it runs itself using Python).
* Open Command Prompt or your terminal, and change to the directory where you downloaded tsuserver3 to. You can do this in two ways:
  - Go up one folder above the tsuserver3 folder, Shift + right click the tsuserver3 folder, and click `Open command window here`. This is the easiest method.
  - Copy the path of the tsuserver3 folder, open the terminal, and type in `cd "[paste here]"`, excluding the brackes, but including the quotation marks if the path contains spaces.
* To install PyYAML and dependencies, type in the following:
  ```bash
  python -m pip install --user -r requirements.txt
  ```
  If you are using Windows and have both Python 2 and 3 installed, you may do the following:
  ```batch
  py -3 -m pip install --user -r requirements.txt
  ```
  This operation should not require administrator privileges, unless you decide to remove the `--user` option.
* Rename `config_sample` to `config` and edit the values to your liking. Be sure to check your YAML file for syntax errors. *Use spaces only; do not use tabs.*
* Run by either double-clicking `start_server.py` or typing in `python start_server.py`, or `py -3 start_server.py` if you use both Python 2 and 3. It is normal to not see any output once you start the server.
  - To stop the server, press Ctrl+C multiple times.

## 

## Commands

### User Commands

* **help**
    - Links to this readme
* **g** "message" 
    - Sends a serverwide message
* **toggleglobal** 
    - Toggles global on and off
* **need** "message" 
    - Sends a serverwide advert
* **toggleadverts** 
    - Toggles adverts on and off
* **area** "area ID" "password"
    - Displays all areas when blank, swaps to area with ID
    - Specify a password to join a password locked area. (If the password matches. Obviously.)
* **getarea** 
    - Shows the current characters in your area
* **getareas** 
    - Shows all characters in all areas
* **mods**
    - Same as **getareas**, but only shows moderators
* **doc** "url" 
    - Gives the doc url if blank, updates the doc url
* **cleardoc** 
    - Clears the doc url
* **status** "status" 
    - Shows current areas status if blank, updates the status
    - Statuses: 'idle', 'rp', 'casing', 'looking-for-players'/'lfp', 'recess', 'gaming'
* **customstatus** "status"
    - Same as /status, but uses user-defined status. Will use the same color as 'idle' as defined by client theme.
* **pm** "target" "Message" 
    - PMs the target. Targets client ID.
* **pmmute**
    - Disables all incoming PMs
* **charselect** 
    - Puts you back to char select screen
* **reload** 
    - Reloads your character ini
* **switch** "character" 
    - Quick switch to a character
* **randomchar** 
    - Randomly chooses a character
* **pos** "position" 
    - Changes your position in the court
    - Positions: 'def', 'pro', 'hld', 'hlp', 'jud', 'wit'
* **bg** "background" 
    - Changes the current background
* **custombg** "background"
    - Changes the current background to a defined bg located in `backgrounds/custom`.
* **currentbg**
    - Gives user the name of the area's current background.
* **roll** "max" 
    - Rolls a 1D6 if blank
* **coinflip**
    - Flips a coin
* **currentmusic** / **music**
    - Displays the current music
* **playrandom**
    - Plays a random track from the server music list.
* **shuffle** "category"
    - Plays a random track, then plays another random track afterwards, etc.
    - Will only play from a single category if one is specified.
    - Shuffle will continue in original area if client switches areas, but will eventually stop once the client disconnects.
* **eviswap** <id1> <id2>
    - Swaps <id1> and <id2> evidence.
* **addcustom** "link"
    - Allows user to set a link for the custom character they are currently using.
* **customlist**
    - Shows a list of links and the respective custom.
* **removecustom**
    - Removes the link for user's custom from the list.
* **clearcustomlist**
    - Clears the custom list.
* **notepad** "note"
    - Adds note to user's notepad, or displays the current notepad if no note is given.
    - Only persists as long as user's client is connected to server.
* **clearnotepad**
    - Clears user's notepad.
* **connectlist**
    - Shows all 'exits' for the current area.
* **autopass**
    - Toggles autopass. When enabled, an OOC broadcast will sound when the user switches areas.
    - This broadcast is visible in the area the user leaves and the area they join and details which area the user is going to or coming from, respectively.
* **musiclist**
    - View the area's current music list.
* **follow** "id"
    - Follow another user. If that user changes areas, the follower will also change areas.
    - Can be used with no arguments to check who the user is following.
    - Works with **autopass**.
* **unfollow**
    - Stop following.
* **followers**
    - Check who is following you. Will also show your followers' followers.
* **followable** "new"
    - Toggle whether users can follow you.
    - Use with argument "new" to disallow new followers without losing current followers.
* **time**
    - Show the current time and date according to the server's time.
* **timer** "start/stop/continue"
    - A stopwatch. Use without arguments to check current timer without stopping it.
    - "start" will start a new timer, "stop" will stop the timer, and "continue" will start the timer where it was last stopped.
* **create** "name"
    - Create a new area with specified name.
    - Area will be appended after Area 25 or any other custom area.
    - Requires permission from staff.
* **serverpoll** "yay/nay"
    - View or vote on the current server poll.
* **digitalroot** "number"
    - Calculate the digital root of a given number.
* **knock** "area ID"
    - Broadcast a message in the selected area that the user is knocking on their door.
* **cm**
    - Makes you a CM of the current area.
### Party Commands
* **party**
    - Shows the user's current party.
    - If the user is not in a party, shows all parties on the server.
    - If the user is the leader of their party, shows party members' roles.
* **parties**
    - Shows all parties on the server.
* **createparty** "name"
    - Creates a party and makes user the leader.
    - Created party will be private/locked by default.
* **partyinvite** "id"
    - Invites a user to your party. Party must be locked.
* **joinparty** "party ID"
    - Join a party. Party must either be public or the user must be invited.
* **leaveparty**
    - Leave the current party.
* **p** "message"
    - Same as **g**, but only visible to other members of your party.
* **partynote** "note"
    - Add a note to the party notepad.
    - Show the party notepad instead if no arguments are given.
* **mgvote** "subject"
    - Vote on a subject. If user has extra 'voting power,' they may vote more than once.
    - If used by party leader, show current vote tally.
#### Party Leader-only Commands
* **unlockparty**
    - Makes current party public.
* **lockparty**
    - Makes current party private.
* **clearpartynote**
    - Clear the party notepad.
* **partykick** "id"
    - Kick the specified user from your party.
* **destroyparty**
    - Destroys the current party.
* **mgroles** "opt. custom roles" 
    - If there enough members in your party, randomly assign party members, excluding the leader, Main Game roles.
    - For custom roles, syntax is as above. e.g. `/mgroles Imitator Wildcard Scapegoat`
* **clearroles**
    - Clears all party members' roles, and resets their 'voting power'.
* **startmgvote** "subjects"
    - Start a party vote on subjects provided, e.g. `/startmgvote Sara Sou Keiji`. Resets everyone's 'voting power'. 
* **revealmgvote**
    - Post the tally in current area's OOC and restore 'voting power'.
* **mgvp** "id" "+/-"
    - Check a party member's 'voting power' or increase/decrease it.
    - Default voting power is 0 (one vote) except for the Sacrifice role, which is 1 (two votes).
### CM Commands
* **lock** "password"
    - Locks your area, preventing anyone outside of the invite list from joining.
    - Optionally, specify a password to be used with **area**.
* **unlock**
    - Unlocks your area.
* **iclock**
    - If area is unlocked, make area spectatable and disallow everyone but CMs from speaking IC.
    - If area is locked, disallow everyone from speaking without making area spectatable.
* **areakick** "ID/*" [area]
    - Kicks target and all of their multi-accs from your area to area 0 or specified [area] and removes them from invite-list should the area be locked.
    - Use "*" to kick everyone who isn't a CM or you.
* **invite** "ID"
    - Adds target to the invite list of your area.
* **uninvite** "ID"
    - Removes target from invite list of your area.
* **forcepos** "position" [target]
    - Forcibly change [target]'s position. Leave blank to affect everyone in area.
    - Positions: 'def', 'pro', 'hld', 'hlp', 'jud', 'wit'
* **connect** "area ID"
    - Sets an 'exit' for the current area. Clients can only leave the area through said 'exits'.
* **disconnect** "area ID"
    - Removes an 'exit' from the current area.
* **clearconnect**
    - Clears all 'exits' for the current area.
* **play** "song file name incl. extension" "length in seconds"
    - Plays a song from `music/custom`.
    - Optionally, specify the length in seconds for the song to loop server-side.
* **addmlist** "song file name incl. extension" "length in seconds"
    - Adds tracks to the area music list that can be played with **playl**. Tracks must be located in `music/custom`.
* **clearmusiclist**
    - Clear the current area's music list.
* **playl** "track number"
    - Plays the specified track from the area's music list. Will loop server-side according to the length provided by **addmlist**.
* **hidecount**
    - Hides the playercount for the current area.
    - Note: player count is only hidden from clients outside the area.
* **rename** "new name"
    - Rename the current area. Will only be visible/joinable to clients after a relog.
    - New name will be announced globally in OOC.
* **destroy**
    - Destroy the current area.
    - Requires area to have been created with **create**.
    - Requires permission from staff.
* **shouts**
    - Toggle shouts in the current area.
* **hide** "id"
    - Hide the specified client from /getarea and the server playercount.
    - Use `*` instead of an ID to hide all players in the area.
* **unhide** "id"
    - Unhide the specified client.
    - Use `*` instead of an ID to unhide all players in the area.
    - This can be used by non-CMs with no arguments to unhide themselves.
#### Testimony Recording
* A new feature in tsuserverCC - you can now record testimonies and play them back with automatic formatting!
* You can now record your testimonies by putting in IC `//[Your Testimony Title]`. Formatting works just as normal, and this will automatically do the WT woosh.
* While recording, you can add new statements by putting in IC `+[Your Statement]`. These will show up as if you're just normally testifying for the first time. 
    - If you're paired and want your partner to have a statement, have the pair add the statement instead. (Make sure they are also a CM.)
* Once you're done recording your testimony, just do `/end`. After this, you can do `///` in IC to make the title appear again, this time with a CE woosh.
* After all that, anyone in the area can say `>` in IC to move to the next statement or `<` for the previous statement. All the statements will be automatically displayed in green.
* If you want to clear the testimony, use /cleartestimony in OOC.
### Mod Commands
* **login** "Password"
    - Grants the Guard checkbox, then checks if password is correct. If so, logs user in as a moderator.
* **gm** "Message" 
    - Sends a serverwide message with mod tag
* **lm** "Message" 
    - Sends an area OOC message with mod tag
* **judgelog** 
    - Displays the last judge actions in the current area
* **announce** "Message" 
    - Sends a serverwide announcement
* **charselect** "ID"
    - Kicks a player back to the character select screen. If no ID was entered then target yourself.
* **kick** "IPID" 
    - Kicks the targets with this IPID.
* **ban** "IPID" "length"
    - Bans the specified IPID for the specified length of time. If no time is specified, ban will default to six hours.
    - All arguments must be wrapped in double quotes.
    - Length syntax is as follows: `"[num] [seconds/minutes/hours/days/weeks] | perma"`.
* **banhdid** "IPID" "length"
    - "Old-style" HDID ban. This will ban both the specified IPID and the associated HDID.
    - All arguments must be wrapped in double quotes.
    - Length syntax is the same as ||ban||.
* **unban** "ban ID" 
    - Unbans the specified ban ID.
* **mute** "Target" 
    - Mutes the target from all IC actions, targets IPID.
* **unmute** "Target","all" 
    - Unmutes the target, "all" will unmute all muted clients
* **oocmute** "Target" 
    - Mutes the target from all OOC actions via ID.
* **oocunmute** "Target" 
    - Unmutes the target.
* **bans**
    - Returns the five most recent bans.
* **baninfo** "ban id" "['ban_id'|'ipid'|'hdid']"
    - Returns requested information about the specified Ban ID from the database.
* **permit** "id"
    - Toggles granting specified client special permissions.
* **setserverpoll** "poll"
    - Set the current server poll, and announce it globally.
* **setserverpoll** "poll"
    - Clear the current server poll, and announce it globally.
* **bglock** 
    - Toggles the background lock in the current area
* **disemvowel** "Target"
    - Removes the vowels from everything said by the target
* **undisemvowel** "Target"
    - Lifts the disemvowel curse from the target
* **blockdj** "target"
    - Mutes the target from changing music. 
* **unblockdj** "target"
    - Undo previous command.
* **blockwtce** "target"
    - Blocks the target from using Witness Testimony/Cross Examination signs.
* **unblockwtce** "target"
    - Undo previous command.
* **evidencemod** <MOD>
    - Changes evidence_mod in this area. Possible values: FFA, CM, HiddenCM, Mods
        * **FFA**
            - Everyone can add, edit and remove evidence.
        * **Mods**
            - Only moderators can add, edit or remove evidence.
        * **CM**
            - Only CM (case-maker, look at /cm for more info) or moderators can add, edit or remove evidence.
        * **HiddenCM**
            - Same as CM, but every evidence has a preset "owner's position" which can be set by a CM or moderator, such that only one side/position of the court may see the evidence. After presenting the evidence, the position of the evidence changes to "all." Possible positions include def (defense), pro (prosecutor), wit (witness), jud (judge), pos (hidden from everyone), and all (everyone can see the evidence).
* **allowiniswap**
    - Toggle allow_iniswap var in this area. 
    - Even if iniswap at all is forbidden you can configure all-time allowed iniswaps in *iniswaps.yaml*
* **unmod**
    - Revokes moderator credentials from the user.

## License

This server is licensed under the AGPLv3 license. In short, if you use a modified version of tsuserverCC, you *must* distribute its source licensed under the AGPLv3 as well, and notify your users where the modified source may be found. The main difference between the AGPL and the GPL is that for the AGPL, network use counts as distribution. If you do not accept these terms, you should use [serverD](https://github.com/Attorney-Online-Engineering-Task-Force/serverD), which uses GPL rather than AGPL.

See the [LICENSE](LICENSE.md) file for more information.