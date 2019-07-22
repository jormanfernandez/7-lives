## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("7 Lives")


## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = False


## The version of the game.

define config.version = "1.1.02"


## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _("""

    The summer collapses in the winter, the leaves of the trees go from the ground to its stem, the rain falls towards the heavens and the sun rises in the west. 

    Days of reversal, indecisive and fragile time converging at its beginning and ending point, but, who observes this convergence? Who is the witness of the everything and nothing?

    In his attempt to change the course of time, a man will give everything to restore the distorted reality that has been created over his life by taking it to the most unthinkable human limit.


_________________________________________


    {b}Original Story{/b} by 

        - {a=https://steamcommunity.com/profiles/76561198034338939}Jorman Fernandez{/a}

_________________________________________

    {b}Art{/b}:

        • Characters: 
            {a=http://tokudaya.net/}Tokudaya{/a}
        
        • Backgrounds:

            {a=https://pixabay.com/users/jplenio-7645255/}jplenio{/a}
            {a=https://pixabay.com/users/erikawittlieb-427626/}ErikaWittlieb{/a}
            {a=https://pixabay.com/users/keresi72-16512/}keresi72{/a}
            {a=https://pixabay.com/users/Pexels-2286921/}Pexels{/a}
            {a=https://pixabay.com/users/mschiffm-896030/}mschiffm{/a}
            {a=https://pixabay.com/users/paulbr75-2938186/}paulbr75{/a}
            {a=https://pixabay.com/users/elizabethaferry-383597/}elizabethaferry{/a}
            {a=https://pixabay.com/users/RyanMcGuire-123690/}RyanMcGuire{/a}
            {a=https://pixabay.com/users/tama66-1032521/}Tama66{/a}
            {a=https://pixabay.com/users/JamesDeMers-3416/}JamesDeMers{/a}
            {a=https://pixabay.com/users/werner22brigitte-5337/}werner22brigitte{/a}
            {a=https://www.pexels.com/@milly-eaton-374605}Milly Eaton{/a}
            {a=https://www.pexels.com/@wendelinjacober}Wendelin Jacober{/a}
            {a=https://www.pexels.com/@binyaminmellish}Alturas Homes{/a}
            {a=https://unsplash.com/@eric_sharp}Eric Sharp{/a}
            {a=https://unsplash.com/@olenka_kotyk}Olenka Kotyk{/a}
            {a=https://unsplash.com/@rotaalternativa}Rota Alternativa{/a}
            {a=https://burst.shopify.com/@ndekhors}Nicole De Khors{/a}

        • Public presentation:

            Matias Mancuello

        - I did some stuff as well. {i}The crappy ones{/i}...

_________________________________________

   {b}Music{/b}:

        {a=https://www.darrencurtismusic.com}Darren Curtis{/a}
        {a=https://www.youtube.com/channel/UCNcPLuK8kshHtwI7Uw73aDg}Royalty Free Anime Music{/a}
        {a=https://www.youtube.com/channel/UCqsGQVl-_k5qGE-PwGKO5DA}Mattia Cupelli{/a}

_________________________________________

   {b}Kickstarter{/b}:

        Thanks to all of those who donated to this project. Without you, this would have not become true. Special thanks to:
            {a=https://steamcommunity.com/profiles/76561198083358585/}Esteban Chan{/a} - "The only place where dreams can become unattainable is in your mind"
            {a=https://www.kickstarter.com/profile/461056959}James Cleak{/a} - "At times, we may hurt each other and we may even part, but that is not the end. We'll always be together."
            {a=https://steamcommunity.com/profiles/76561198051326903}ilikepies{/a}
            {a=https://www.kickstarter.com/profile/1608812043}Mictlantecuhtli{/a}
            {a=https://www.kickstarter.com/profile/1629303241}Erinyes Fisher{/a}
            {a=https://www.kickstarter.com/profile/142787005}Sarah1281{/a}
            {a=https://steamcommunity.com/profiles/76561198028415882}DarkCsarX{/a} - "Life is limited, live it to the fullest and without regrets".

_________________________________________

   Also, thanks to {a=https://steamcommunity.com/profiles/76561198078685126/}DrLein{/a} for all the support that you gave me. You are awesome, buddy. And the rest of the people in {a=https://steamcommunity.com/groups/traderslatino}Traders Latino{/a} as well...
_________________________________________""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define config.rollback_enabled = False
define config.main_menu_music = "sounds/music/main.mp3"
define config.history_length = 500
define config.default_text_cps = 20
define config.end_game_transition = Fade(2.0, 0.1, 2.0)

define build.name = "7Lives"
define build.directory_name = "7lives"

## textbox an other sutff ######################################################
define gui.text_color = "#1e1e1e"
define gui.text_size = 24
define gui.name_text_size = 33
define gui.textbox_height = 181
define gui.choice_button_text_idle_color = '#343434'
define gui.choice_button_text_hover_color = '#575757'
define gui.accent_color = '#000060'
define gui.idle_color = '#343434'
define gui.idle_small_color = '#404040'
define gui.hover_color = '#575757'
define gui.selected_color = '#555555'
define gui.insensitive_color = '#454545'
define gui.interface_text_color = '#343434'
define gui.muted_color = '#6080d0'
define gui.hover_muted_color = '#8080f0'
define gui.slider_size = 64
define gui.slider_tile = False
define gui.slider_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)
define gui.namebox_width = 300
define gui.name_ypos = -22
define gui.namebox_borders = Borders(7, 3, 7, 3)
define gui.namebox_tile = True
define gui.history_name_xpos = 0.5
define gui.history_text_xpos = 0.5
define gui.history_name_ypos = 0
define gui.history_text_ypos = 60
define gui.history_name_width = 225
define gui.history_text_width = 1110
define gui.history_name_xalign = 0.5 
define gui.history_text_xalign = 0.5


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

# define config.main_menu_music = "main-menu-theme.ogg"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "7Vidas-1550352914"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/window_icon.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
