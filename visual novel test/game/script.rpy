# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lunchly Larry")

define s = Character("Skibidi Choir")

image bg room = "bg room.png"

image lunchly larry = "lunchly larry.png"

image skibidi-toilet = "skibidi-toilet.png"
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

    l "Idk this is just a test tbh lets see if the code works properly without errors and stuff like that."
    # should display skibidi toilet sprite and hide the lunchly larry sprite
    hide lunchly larry
    show skibidi-toilet at left

    # should show skibidi choir dialogue
    s "This is also a test to make sure skibidi choir and skibidi toilet sprite and dialogue show up properly without error."

    # This ends the game.

    return
