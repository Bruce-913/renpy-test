# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define k = Character("KSI")

define l = Character("Lunchly Larry")

define s = Character("Skibidi Choir")

image studio  = "studio.png"

image bg room = "bg room.png"

image lunchly larry = "lunchly larry.png"

image skibidi-toilet = "skibidi-toilet.png"

image KSI = "KSI.png"
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show lunchly larry at left
    with move

    # These display lines of dialogue.

    l "Hi I'm lunchly larry"

    l "Something crazy is happening in our city!"
    # should display skibidi toilet sprite and hide the lunchly larry sprite
    hide lunchly larry
    show skibidi-toilet at left

    # should show skibidi choir dialogue
    s "KSI's new song is affecting our people!"

    s "By the way my name is Skibidi Toilet."

    hide skibidi-toilet
    show KSI at left


    k "And I'm KSI and I'm about to get ready to bring you down a rabbithole of brainrot"
    k "Specifically a little brinrot I created as an experiment"

    menu: 
        "Now I'll give you two options from here:"

        "Hear my story out of how I ruined this world":
            jump story_beginning

        "Never hear about my story":
            jump no_story

label story_beginning:

    scene studio


    k "it all started with this studio"


label no_story:

    show KSI at left
    k "This is the end for you"

return
    # This ends the game.

    
