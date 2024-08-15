# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Professor. Emmy", color="#c8ffc8")

define p = Character("[player_name]", color="#f4c8ff")

define ib = Character("Indian boy", color="#c8caff")

define ig = Character("Indian girl", color="#c8caff")

define kb = Character("Korean boy", color="#c8caff")

define kg = Character("Korean Girl", color="#c8caff")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    
    e "Hi. Welcome to Miyeonsi."

    e "This game is a love simulation game for Korea and India."

    e "Before I start the game, I want to know about you."
    
    e "What is your name?"


    python:
        player_name = renpy.input("What is your name?", length=32)
        player_name = player_name.strip()

    # if not player_name:
    #     player_name = "Pat Smith"

    p "My name is [player_name]!"

    e "Hi, [player_name]."
    
    e "Which country are you from?"

    menu:     
        
        "I'm from..."   

        "Korea":

            jump Korean_gender_select

        "India":

            jump Indian_gender_select

    
label Korean_gender_select:

    e "What is your gender?"

    menu:

        "I'm a..."

        "boy":

            jump Korean_boy_ver

        "girl":

            jump Korean_girl_ver

label Korean_boy_ver:

    e "Thank you for letting me know. Then let's get started!"
    
    e "I hope you succeed in your relationship."

    return

label Korean_girl_ver:

    e "Thank you for letting me know. Then let's get started!"
    
    e "I hope you succeed in your relationship."

    jump Ch1_S1_T0_KG
    

label Indian_gender_select:

    e "What is your gender?"

    menu:

        "I'm a..."

        "boy":

            jump Indian_boy_ver

        "girl":

            jump Indian_girl_ver

label Indian_boy_ver:

    e "Thank you for letting me know. Then let's get started!"
    
    e "I hope you succeed in your relationship."

    return

label Indian_girl_ver:

    e "Thank you for letting me know. Then let's get started!"
    
    e "I hope you succeed in your relationship."

    return


### Chaper 1 ###

label Ch1_S1_T0_KG:

    #ex

    scene friend
    
    "We arrive at the cafeteria, and today's menu is bibimbap. We each grab a bowl and sit down."

    p "This must be your first time at the cafeteria, right? This is SNU's cafeteria!"
    
    p "This is bibimbap, a Korean dish where you mix rice with various vegetables and gochujang (Korean chili paste)!"
    
    ib "Oh!! It looks delicious!! I've never had bibimbap before!"
    
    p "Let me mix it for you!"
    
    "I put all my effort into mixing it."

    "But I get so into it that I accidentally bump into someone's arm, causing the spoon to fling a grain of rice onto their face."

    "Q1. What would you do?"

    menu:

        "What would you do?"

        "Quickly dash to grab a tissue.":

            jump Ch1_S2_T1_KG

        "Apologize to [player_name] in embarrassment.":

            jump Ch1_S2_T2_KG

        "Apologize to [player_name] in embarrasApologize to the person you bumped into first.":

            jump Ch1_S2_T3_KG

label Ch1_S2_T1_KG:

    "{b}Good Ending{/b}."

    jump Ch2_S1_T0_KG

label Ch1_S2_T2_KG:

    "{b}Moderate Ending{/b}."

    return

label Ch1_S2_T3_KG:

    "{b}Bad Ending{/b}."

    return



### Chaper 2 ###

label Ch2_S1_T0_KG:

    "{b}Good Ending{/b}."

    return