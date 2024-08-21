# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Professor. Oh", color="#c8ffc8")

define p = Character("[player_name]", color="#f4c8ff")

define ib = Character("Prem", color="#c8caff")

define ig = Character("Priyanka", color="#c8caff")

define kb = Character("Seonjae", color="#c8caff")

define kg = Character("Sol", color="#c8caff")

define f1 = Character("Inhyeok", color="#59ff56")

define gd = Character("Guide", color="#ff6464")

define m = Character("mom", color="#c8caff")

define m1 = Character("merchant A", color="#50ff70")

define m2 = Character("merchant B", color="#e6ffb8")


define affection = 0


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show e start
    
    show screen show_affection

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

    e "Are you a boy or a girl?"

    menu:

        "I'm a..."

        "boy":

            jump Korean_boy_ver

        "girl":

            jump Korean_girl_ver

label Korean_boy_ver:

    e "Thank you for letting me know. Then let's get started!"
    
    e "I hope you succeed in your relationship."

    jump Ch1_S1_T0_KB

label Korean_girl_ver:

    e "Thank you for letting me know. Then let's get started!"
    
    e "I hope you succeed in your relationship."

    jump Ch1_S1_T0_KG
    

label Indian_gender_select:

    e "Are you a boy or a girl?"

    menu:

        "I'm a..."

        "boy":

            jump Indian_boy_ver

        "girl":

            jump Indian_girl_ver

label Indian_boy_ver:

    e "Thank you for letting me know. Then let's get started!"
    
    e "I hope you succeed in your relationship."

    jump Ch1_S1_T0_IB

label Indian_girl_ver:

    e "Thank you for letting me know. Then let's get started!"
    
    e "I hope you succeed in your relationship."

    jump Ch1_S1_T0_IG



### IG ver. ###

label Ch1_S1_T0_IG:

    scene bg building_220:
        zoom 1.2

    "Today was my first day as an exchange student in Korea. The wind felt particularly refreshing that day."

    p "Hmm... I have no idea where anything is since it's my first time here. Let's head to the lounge in Building 220 and think things over."

    "I headed towards the lounge in Building 220 and opened the door."

## need to change the lounge pic
    scene bg lounge_220:
        zoom 4.5
    with dissolve
    
    f1 "Oh? A new face. Are you an exchange student by any chance?"
    show ig cafeteria at left
    p "Yeah, I just arrived as an exchange student from Christ University. My name is [player_name]."
    hide ig cafeteria
    show f1 start at right
    f1 "Nice to meet you! If you have any questions, feel free to ask!"
    hide f1 start
    "Just then, someone suddenly grabbed my shoulder."
    
    show kb cafeteria at right

    kb "Hey! What were you guys talking about?"
    hide kb cafeteria 
    show ig cafeteria at left
    p "Uh?"
    hide ig cafeteria
    show kb cafeteria at right
    kb "Uh? Who... are you?"

    "That was how we first met. He was quite flustered, and his cheeks turned a bit red with embarrassment. Haha."

    kb "Oh!! I'm so sorry!!"
    hide kb cafeteria 
    show f1 start at right
    f1 "Haha, introduce yourself. He's an exchange student who just joined the College of Liberal Studies today."
    hide f1 start
    show ig cafeteria at left
    p "Hi, I'm [player_name]. I'm an exchange student from Christ University in India, now studying at SNU's College of Liberal Studies."
    hide ig cafeteria 
    show kb cafeteria at right
    kb "Oh, nice to meet you!! I'm [kb]. I heard an SNU student went to India, and now we have an exchange student here, too!"

    kb "Anyway, if you need help with anything, feel free to ask! Oh, wait, I don't have your number yet! What's your number?"
    hide kb cafeteria 
    show ig cafeteria at left
    p "My number is ~~!"
    hide ig cafeteria 
    show kb cafeteria at right
    kb "Great, thanks!"

    "(Growling sound)"

    kb "(Quickly changing the subject) Uh, did you have lunch yet? Haha"
    hide kb cafeteria 
    show f1 start at right
    f1 "Haha, we were just about to grab something. Let's go together!"
    hide f1 start
    show ig cafeteria at left
    p "Sounds good!"
    hide ig cafeteria 
    "We headed to the cafeteria together..."
    scene bg snu_cafeteria:
        zoom 1.4
    with dissolve
    show f1 start at right
    f1 "Oh, shoot! I forgot I had an assignment due! You two go ahead and eat! I'll see you later!"
    hide f1 start
    "Being left awkwardly alone... Well, let's go eat."

    jump Ch1_S2_T0_IG

label Ch1_S2_T0_IG:

    ## Cafeteria

    "We arrive at the cafeteria, and today's menu is bibimbap. We each grab a bowl and sit down."
    show kb cafeteria at left
    kb "This must be your first time at the cafeteria, right? This is SNU's cafeteria!"
    
    kb "This is bibimbap, a Korean dish where you mix rice with various vegetables and gochujang (Korean chili paste)!"
    hide kb cafeteria 
    show ig cafeteria at right
    p "Oh!! It looks delicious!! I've never had bibimbap before!"
    hide ig cafeteria
    show kb cafeteria at left
    kb "Let me mix it for you!"

    "I put all my effort into mixing it."

    "But I get so into it that I accidentally bump into someone's arm, causing the spoon to fling a grain of rice onto their face."

    "What would you do?"

    "(Tutorial) This game requires you to make choices at key moments! Depending on your choices, the relationship level can increase or decrease. The final ending will be different based on your decisions, so choose carefully!"

    menu:

        "What would you do?"

        "1. Remove the grain of rice stuck on [kb]'s face with your hand.":
            
            $ affection += 5
            jump Ch1_S3_T1_IG
            

        "2. Hand [kb] a handkerchief.":
            
            $ affection += 2
            jump Ch1_S3_T2_IG
            

        "3. Glare at the person next to you.":

            $ affection -= 5
            jump Ch1_S3_T3_IG

    #show screen show_affection

label Ch1_S3_T1_IG:

    jump Ch1_S4_T0_IG

label Ch1_S3_T2_IG:

    jump Ch1_S4_T0_IG

label Ch1_S3_T3_IG:

    jump Ch1_S4_T0_IG

label Ch1_S4_T0_IG:
    show ig cafeteria at right
    p "Haha, it's okay. I have a handkerchief. You got some rice on your face."

    p "This bibimbap is really good! The flavors are mild, and it goes well with the gochujang!"
    hide ig cafeteria
    show kb cafeteria at left 
    kb "Really? I'm glad you like it, haha. By the way, are you busy these days? Have you explored Seoul much?"
    hide kb cafeteria 
    show ig cafeteria at right
    p "Huh? No, I haven't really had the chance to see much outside the campus... Do you have time tomorrow? Maybe you could show me around Seoul?"
    hide ig cafeteria 
    show kb cafeteria at left
    kb "Yeah, I'm free tomorrow! Let's meet up after class! I'll text you!"
    hide kb cafeteria 
    show ig cafeteria at right
    p "Sounds good. See you tomorrow then!"
    hide ig cafeteria 
    jump Ch2_S1_T0_IG


label Ch2_S1_T0_IG:

    "_Chatting app_"
    show kb pyjamas
    kb "[player_name], have you ever been to Seol-ip?"
    hide kb pyjamas
    show ig pyjamas
    p "Seol-ip..? You mean Seoul National University Station, right? I've never been there!"
    hide ig pyjamas
    show kb pyjamas
    kb "Then do you want to go with me? I'll show you around."
    hide kb pyjamas
    show ig pyjamas 
    p "Okay, good!"
    hide ig pyjamas
    scene bg seolip:
        zoom 1.2

    "The next day. We met in Seol-ip."

    show kb date at right
    kb "Ta-da! Students from our school usually come here to hang out."
    hide kb date
    show ig date at left
    p "Wow, there are a lot of people."
    hide ig date
    show kb date at right
    kb "Um... Since we just had lunch, how about going to a cafe I know and having some dessert?"
    hide kb date
    show ig date at left
    p "Okay."
    hide ig date 
    show kb date at right
    kb "I'll buy you some for your first time at Seol-ip."
    hide kb date
    show ig date at left
    p "Oh really?? Thank you. I'll eat well~"
    hide ig date 
    show kb date at right 
    kb "Huh? It's a karaoke! I wanted to go to a karaoke, haha."
    hide kb date
    show ig date at left
    p "Really? Then let's go in now."
    hide ig date 
    scene bg karaoke:
        zoom 2.8
    with dissolve
    show kb date at left 
    kb "You can pay for the time you want, and select the song you want to sing with the remote control. Here, the mic."
    hide kb date
    show ig date at right
    p "Thank you. You're so kind. I'll sing first!"
    hide ig date 
    show kb date at left
    "I am confident in my singing skills, so I sing my favorite song with great enthusiasm."
    "I look to the side while singing and see the other person staring at me."
    "I was a little nervous about the other person until the song ended."
    hide kb date
    show ig date at right
    p "Wow, you sing really well!"
    hide ig date
    show kb date at left 
    kb "Haha, no. Now sing too."
    hide kb date
    "The other person chose a duet song that is famous for being romantic."
    "Blah blah~"

    "Which of the following actions should I choose?"

    menu:

        "Which of the following actions should I choose?"

        "1. Sing along to the duet song.":
            ## $ affection level increases.
            
            $ affection += 5
            jump Ch2_S2_T1_IG

        "2. Stay still.":
            ## $ affection level decreases.
            $ affection -= 5
            jump Ch2_S2_T2_IG
            

        "3. Pick up a tambourine and dance like crazy.":
            ## $ affection level increases slightly.
            $ affection += 2
            jump Ch2_S2_T3_IG

label Ch2_S2_T1_IG:

    jump Ch2_S3_T0_IG

label Ch2_S2_T2_IG:

    jump Ch2_S3_T0_IG

label Ch2_S2_T3_IG:

    jump Ch2_S3_T0_IG

label Ch2_S3_T0_IG:
    show kb at left 
    kb "Phew, I had fun. Where should we go now... Is there a place you want to go?"
    hide kb date
    show ig date at right
    p "Um... Actually, I wanted to see the palaces of Korea."
    hide ig date
    show kb date at left
    kb "Really? Then do you want to go to Gyeongbokgung Palace together?"
    hide kb date
    show ig date at right
    p "Okay, fine."
    hide ig date
    scene bg gyunbok:
        zoom 2.8
    with dissolve

    "We two take a bus and arrive at Gyeongbokgung Palace."

    "There are many people walking around the palace wearing hanbok."
    show ig date at left
    p "What are those clothes?"
    hide ig date
    show kb date at right
    kb "That's a traditional Korean costume called hanbok. Hanbok is a costume that our people have worn since ancient times, "
    hide kb date
    show ig date at left 
    kb "and it has changed over time based on the basics of a skirt, jeogori, and pants. "
    hide ig date
    show kb date at right
    kb "Today's hanbok follows the style that was popular during the Joseon Dynasty, "
    
    kb "and modernized hanbok, which is designed to be worn in everyday life, is also popular. "
    
    kb "You can rent a hanbok nearby. Shall we try it on together?"
    hide kb date
    show ig date at left
    p "Okay, let's do that!"
    hide ig date
    "The two change into hanbok."
    show kb hanbok at right
    kb "Now let's take a look around Gyeongbokgung Palace."
    hide kb hanbok
    gd "Gyeongbokgung Palace is the first palace built when Joseon was founded and Hanyang (present-day Seoul) became the capital. "
    
    gd "It was used for banquets and receptions by the king and his subjects, as well as for receiving envoys, "
 
    gd "by building a large pond and a grand pavilion. "
 
    gd "Although many buildings were destroyed during the war and colonial period, "
 
    gd "restoration work has been steadily carried out to this day. "

    gd "It is a symbolic palace of the Joseon Dynasty that still maintains its original location since its founding."

    "The two leisurely stroll through Geunjeongjeon and Gyeonghoeru, enjoying the tranquil atmosphere of Gyeongbokgung Palace."
    show kb hanbok at right
    kb "I think we've seen all the palaces. How was it?"
    hide kb hanbok
    show ig hanbok at left
    p "It was really beautiful! The color arrangement and elaborate design were really impressive. "
    "It was touching to be able to experience Korean history and tradition in person while wearing hanbok. "
    "It felt like a harmony of tradition and modernity, considering that there is a palace like this in the middle of Seoul."
    hide ig hanbok
    show kb hanbok at right
    kb "I'm glad it was a good experience haha. Next, I'll introduce you to the famous traditional market in this area."
    hide kb hanbok
    show ig hanbok at left
    p "Right!"
    
    p "Oh, it's cold."

    scene bg gyunbok_raining:
        zoom 1.8

    hide ig hanbok
    show kb hanbok at left
    kb "Huh? It's raining."

    "(Shooting, swoosh, the sound of rain falling)"

    kb "Do you have an umbrella? I only have one for myself…"
    hide kb hanbok
    show ig hanbok at right
    p "No. It seems like Korea gets a lot of rain showers."
    hide ig hanbok
    show kb hanbok at left
    kb "Let's go under the eaves and wait for it to stop."
    hide kb hanbok
    "The two moved under the skirts to take shelter from the rain for a while, but the rain showed no sign of stopping."
    show kb hanbok at left
    kb "Hmm, the rain won't stop. We have to get to the market on time, but..."
    hide kb hanbok
    

    menu:

        "How should I respond to an unexpected downpour?"

        "1. Go to a nearby convenience store and buy an umbrella each.":
            ## Slightly decrease in favorability
            $ affection += 3
            jump Ch2_S4_T1_IG
            

        "2. Share an umbrella and run to the market.":
            ## $ affection level goes up significantly
            $ affection += 5
            jump Ch2_S4_T2_IG

        "3. Suggest that we both just go while getting rained on.":
            ## $ affection level goes down significantly
            $ affection += 3
            jump Ch2_S4_T3_IG

label Ch2_S4_T1_IG:
    
    jump Ch2_S5_T0_IG

label Ch2_S4_T2_IG:

    jump Ch2_S5_T0_IG

label Ch2_S4_T3_IG:

    jump Ch2_S5_T0_IG

label Ch2_S5_T0_IG:
    scene bg kmarket:
        zoom 1.7

    "After many twists and turns, the two arrive at Gwangjang Market."
    show kb hanbok at right
    kb "Okay, this is Gwangjang Market."
    hide kb hanbok
    show ig hanbok at left
    p "It's bigger and more crowded than I thought."
    hide ig hanbok 
    show kb hanbok at right 
    kb "That's right. Gwangjang Market is the largest and oldest traditional market in Korea. "
    "There are various food alleys in Gwangjang Market, hanbok stores where you can buy daily necessities, and second-hand stores."
    hide kb hanbok
    show ig hanbok at left
    p "Right. Let's eat something since we're hungry."
    hide ig hanbok
    show kb hanbok at right
    kb "This is tteokbokki, a national snack that Koreans of all ages and genders love. "
    "It might be a little spicy, but is that okay?"
    hide kb hanbok
    "What should I say in response to that suggestion?"

    menu:
        "1. Yeah, I like spicy food. Wow~":
            ## Affinity increase
            $ affection += 3
            jump Ch2_S6_T1_IG

        "2. I can't eat spicy food well... I'll try it next time.":
            ## Affinity maintained
            $ affection += 0
            jump Ch2_S6_T2_IG

        "3. Hmm, I'll rinse it in water and try it. Give it to me.":
            ## Affinity decrease
            $ affection -= 5
            jump Ch2_S6_T3_IG

label Ch2_S6_T1_IG:

    jump Ch2_S7_T0_IG

label Ch2_S6_T2_IG:

    jump Ch2_S7_T0_IG

label Ch2_S6_T3_IG:

    jump Ch2_S7_T0_IG

label Ch2_S7_T0_IG:
    show kb hanbok at right
    kb "This is bindae-tteok, a specialty of Gwangjang Market. "
    "It is a dish made by mixing vegetables or meat into a dough made from ground soybeans and frying it."

    kb "This noodle is called janchi-guksu. "
    "It originated from the fact that it was enjoyed at weddings, birthday parties, and 60th birthday parties in the hopes of longevity."
    hide kb hanbok
    show ig hanbok at left
    p "The food here is really delicious."
    hide ig hanbok
    "Then they enjoy the food with a happy conversation."

    jump Ch3_S1_T0_IG


label Ch3_S1_T0_IG:
    show kb waterbomb vigorous at left
    kb "How about we try have fun somewhere new?"
    hide kb waterbomb vigorous
    show ig wterbomb at right
    p "Sounds good! Where should we go?"
    hide ig wterbomb 
    show kb waterbomb vigorous at left
    kb "Is there anything you'd like to try?"
    hide kb waterbomb vigorous
    show ig wterbomb at right
    p "Hmm... Could we maybe go to a famous festival in Korea?"
    hide ig wterbomb
    show kb waterbomb vigorous at left
    kb "Of course. How about we go to the largest music and water-themed festival in the country? "

    kb "It combines performances from various genres like K-POP, hip-hop, EDM, and large-scale water fights!"
    hide kb waterbomb vigorous
    show ig wterbomb at right
    p "Great! What's the name of that festival?"
    hide ig wterbomb 
    show kb waterbomb vigorous at left
    kb "Want to try guessing?"
    hide kb waterbomb vigorous

    menu:

        "Guess the name of the festival:"

        "1. Pentaport Rock Festival":
            $ affection -= 3
            jump Ch3_S2_T1_IG

        "2. Waterbomb Festival":
            $ affection += 3
            jump Ch3_S2_T2_IG

        "3. Boryeong Mud Festival":
            $ affection -= 3
            jump Ch3_S2_T3_IG

        "4. Seoul Jazz Festival":
            $ affection -= 3
            jump Ch3_S2_T4_IG

label Ch3_S2_T1_IG:
    show kb waterbomb vigorous at left
    kb "Ah, unfortunately the answer was Waterbomb :( Well then, shall we go to Waterbomb now?"

    jump Ch3_S3_T0_IG

label Ch3_S2_T2_IG:
    show kb waterbomb vigorous at left
    kb "That's right!! My darling! Then shall we go to Waterbomb?"

    jump Ch3_S3_T0_IG

label Ch3_S2_T3_IG:
    show kb waterbomb vigorous at left
    kb "Ah, unfortunately the answer was Waterbomb :( Well then, shall we go to Waterbomb now?"

    jump Ch3_S3_T0_IG

label Ch3_S2_T4_IG:
    show kb waterbomb vigorous at left
    kb "Ah, unfortunately the answer was Waterbomb :( Well then, shall we go to Waterbomb now?"

    jump Ch3_S3_T0_IG

label Ch3_S3_T0_IG:
    scene bg waterbomb:
        zoom 1.2
    show kb waterbomb vigorous at left
    "We arrived to the Waterbomb festival!"
    hide kb waterbomb vigorous
    show ig wterbomb at right
    p "Wow! This is really fun!!"
    hide ig wterbomb 
    "During the water gun play, I became the target of many people."
    show ig wterbomb at left
    p "Oh no..."
    hide ig wterbomb
    show kb waterbomb vigorous at right
    kb "[player_name]!!"
    hide kb waterbomb vigorous
    "[kb] shielded me with his whole body."
    show kb waterbomb vigorous at right
    kb "Are you okay??"
    hide kb waterbomb vigorous
    show ig wterbomb at left
    p "Yes!! Really thank you"
    hide ig wterbomb
    show kb waterbomb vigorous at right
    kb "How was it?"
    hide kb waterbomb vigorous
    show ig wterbomb at left
    p "This was so much fun!!"
    hide ig wterbomb
    show kb waterbomb vigorous at right
    kb "Great! Then let's go watch the performances now? We can buy some beers too!"
    hide kb waterbomb vigorous
    show ig wterbomb at left
    p "It was so much fun!! I especially enjoyed seeing the K-pop singers. I love music!"
    hide ig wterbmob
    show kb waterbomb vigorous at right
    kb "Oh really? Then should we go to Hongdae next time?"
    hide kb waterbomb vigorous
    show ig wterbomb at left
    p "Why Hongdae? Is it famous for music?"
    hide ig wterbomb 
    show kb waterbomb vigorous at right 
    kb "Many musicians do street performances in Hongdae! "
    hide kb waterbomb vigorous
    "I saw busking in Hongdae with [kb]"
    show ig wterbomb 
    p "This is so enjoyable~"
    hide ig wterbomb
    "I suddenly got a text message."
    show ig sadwaterbomb
    p "Oh no..."
    hide ig sadwaterbomb 
    show kb waterbomb sad at left
    kb "What's wrong? You don't look good."
    hide kb waterbomb sad 
    show ig sadwaterbomb at right
    p "I need to go back to India now."
    hide ig sadwaterbomb 
    show kb waterbomb sad at left
    kb "What? Didn't you have half a year left?"
    hide kb waterbomb sad 
    show ig sadwaterbomb at right 
    p "I loved Korea and you so much that I extended my exchange student program for another semester, "

    p "but I just got a message saying my mother met with an accident"
    hide ig sadwaterbomb
    show kb waterbomb sad at left
    kb "What? That's so unfortunate... I'm tearing up..."
    hide kb waterbomb sad 
    show ig sadwaterbomb at right
    p "Oh honey, don't cry... I'm miserable too.."
    hide ig sadwaterbomb
    show kb waterbomb sad at left
    kb "So we won't be able to see each other anymore?"
    hide kb waterbomb sad 

    menu:

        "Choose the right sentence to comfort the other person:"

        "1. I suppose so. I'm really sorry.":
            $ affection -= 2
            jump Ch3_S4_T1_IG

        "2. We were never meant to be together for long anyway.":
            $ affection += -5
            jump Ch3_S4_T2_IG

        "3. No, don't say that! Everything will be alright, don't worry; you will always be in my heart.":
            $ affection += 5
            jump Ch3_S4_T3_IG

label Ch3_S4_T1_IG:

    jump Ch3_S5_T0_IG

label Ch3_S4_T2_IG:

    jump Ch3_S5_T0_IG

label Ch3_S4_T3_IG:

    jump Ch3_S5_T0_IG

label Ch3_S5_T0_IG:
    scene bg kairport:
        zoom 1.2

    "_at the airport_"
    show kb airport
    kb "I wish we could meet again soon."
    hide kb airport
    show ig rushed
    p "Be happy even after I go back."
    hide ig airport
    show kb kurta
    kb "I prepared a gift for you. This is a traditional Korean costume, do you remember the name of it?"
    hide kb airport
    menu:

        "Guess the name of the costume:"

        "1. Hanbok":
            $ affection += 5
            jump Ch3_S6_T1_IG

        "2. Kimono":
            $ affection -= 5
            jump Ch3_S6_T2_IG

        "3. Ao Dai":
            $ affection -= 5
            jump Ch3_S6_T3_IG

        "4. Sari":
            $ affection -= 2
            jump Ch3_S6_T4_IG

label Ch3_S6_T1_IG:
    show kb airport
    kb "Right! You remember!"

    jump Ch3_S7_T0_IG

label Ch3_S6_T2_IG:
    show kb airport
    kb "Don't you remember that? The answer was Hanbok."

    jump Ch3_S7_T0_IG

label Ch3_S6_T3_IG:
    show kb airport
    kb "Don't you remember that? The answer was Hanbok."

    jump Ch3_S7_T0_IG

label Ch3_S6_T4_IG:
    show kb airport
    kb "Don't you remember that? The answer was Hanbok."

    jump Ch3_S7_T0_IG

label Ch3_S7_T0_IG:
    hide kb airport
    show ig rushed at left
    p "Thank you so much. This will remind me of you."
    hide ig rushed
    show kb airport at right 
    kb "Don't forget me when you go back to India."
    hide kb airport
    show ig rushed at left
    p "Of course not. We're under the same sky. You will be eternal to me."
    hide ig rushed
    show kb airport at right
    kb "Take care in India."
    hide kb airport
    show ig rushed
    p "Yes, you take care in Korea too. Let's meet in India next time."
    hide ig rushed
    jump Ch4_S1_T0_IG


label Ch4_S1_T0_IG:
    scene bg india_room:
        zoom 1.2

    "It's been two months since I returned to Bengaluru in a hurry. Fortunately, my mother's health is gradually improving."

    p "He must have been surprised that I left so suddenly. Will I be able to see him again?"

    "Without thinking, I opened my mailbox, and there it was, an email from him."

    menu:
        "Read the email":
            $ affection += 5
            jump Ch4_S1_T1_IG

        "Don't read the email":
            $ affection -= 5
            jump Ch4_S1_T2_IG

label Ch4_S1_T1_IG:

    "I thought I was the only one missing him, but he felt the same way. He is coming to our school as an exchange student. I can't believe it."

    jump Ch4_S2_T0_IG

label Ch4_S1_T2_IG:

    "I shouldn't hold on to past relationships. Reading this email will only make me miss him more. I won't read it."

    jump Ch4_S2_T0_IG

label Ch4_S2_T0_IG:
    show m at left
    m "We're going to visit your grandfather in Agra next week."
    hide m 
    show ig pyjamas
    p "Agra?"
    hide ig pyjamas
    show m
    m "Yes. We need to deliver these things to your grandfather."
    hide m
    "After visiting my grandfather's house, I had a bit of time before my flight. What should I do now?"

    menu:
        "Go to the Taj Mahal":
            $ affection += 5
            jump Ch4_S3_T1_IG

        "Go to Agra Fort":
            scene bg agra
            $ affection += 2
            jump Ch4_S3_T2_IG

        "Go shopping":
            scene bg india_shopping:
                zoom 1.7
            $ affection -= 5
            jump Ch4_S3_T3_IG

label Ch4_S3_T1_IG:

    jump Ch4_S4_T0_IG

label Ch4_S3_T2_IG:

    "There were too many people at Agra Fort, so I decided to go to the Taj Mahal."

    jump Ch4_S4_T0_IG

label Ch4_S3_T3_IG:

    "There were too many people at the shopping area, so I decided to go to the Taj Mahal."

    jump Ch4_S4_T0_IG

label Ch4_S4_T0_IG:
    scene bg tajmahal
    show ig kurti
    "Come to think of it, he also wanted to visit this place... I have a feeling he might be here today."
    hide ig kurti
    menu:
        "Observe the people following the tour guide":
            $ affection += 3
            jump Ch4_S5_T1_IG

        "Watch people getting their photos taken by peddlers":
            $ affection += 0
            jump Ch4_S5_T2_IG

        "No way, such a coincidence couldn't happen":
            $ affection -= 5
            jump Ch4_S5_T3_IG

label Ch4_S5_T1_IG:

    jump Ch4_S6_T0_IG

label Ch4_S5_T2_IG:

    jump Ch4_S6_T0_IG

label Ch4_S5_T3_IG:

    jump Ch4_S6_T0_IG

label Ch4_S6_T0_IG:

    "I see a Korean person over there! No way..."
    show kb kurta
    kb "Oh! It's you!"
    hide kb kurta
    show ig kurti
    p "What a coincidence to meet here..."
    hide ig kurti
    show kb kurta
    kb "I arrived in India yesterday. You said you would take me to the Taj Mahal, so I wanted to come even if it was alone."
    hide kb kurta
    show ig kurti
    p "I had a feeling you might be here today."
    hide ig kurti
    show kb kurta
    kb "The Taj Mahal is so beautiful! Just like you described it."
    hide kb kurta
    show ig kurti
    p "I thought you would like Agra. It has many historical sites that showcase Indian tradition. It's like..."
    hide ig kurti
    menu:

        "It's like... ( ) in Seoul."
        
        "Myeong-dong":
            $ affection += 0
            jump Ch4_S7_T1_IG

        "Jongno":
            $ affection += 3
            jump Ch4_S7_T2_IG

        "Itaewon":
            $ affection -= 3
            jump Ch4_S7_T3_IG

label Ch4_S7_T1_IG:

    jump Ch4_S8_T0_IG

label Ch4_S7_T2_IG:

    jump Ch4_S8_T0_IG

label Ch4_S7_T3_IG:

    jump Ch4_S8_T0_IG

label Ch4_S8_T0_IG:
    show kb kurta at right
    kb "That's right! You seem to know quite a lot about Korea now!"
    hide kb kurta
    show ig kurti at left
    p "Of course! It's always a place I miss."
    hide ig kurti
    show kb kurta at right
    kb "What should we do now?"
    hide kb kurta

    menu:

        "What should we do now?"
        
        "Let's go eat street food in Delhi":
            $ affection += 5
            jump Ch4_S9_T1_IG

        "I'll take a picture of you in front of the Taj Mahal":
            $ affection += 0
            jump Ch4_S9_T2_IG

        "Let's go back to the hotel and rest":
            $ affection -= 5
            jump Ch4_S9_T3_IG

label Ch4_S9_T1_IG:

    jump Ch4_S10_T0_IG

label Ch4_S9_T2_IG:

    jump Ch4_S10_T0_IG

label Ch4_S9_T3_IG:

    jump Ch4_S10_T0_IG

label Ch4_S10_T0_IG:
    scene bg india_train

    "We traveled around Agra and Delhi for a few days. Now it's time to return to Bangalore."

    "After spending a few memorable days in Delhi and Agra, it's time to head back to Bangalore. "

    "We decided to take the train together—an experience that would allow us to see more of India's diverse landscapes and cultures as we travel across regions."
    show kb training at left
    kb "I've heard that train journeys in India are quite an experience. I'm excited but also a bit nervous. How long will the journey take?"
    hide kb training
    show ig train at right
    p "It'll take around 36 to 40 hours, depending on the train. But trust me, it's going to be an unforgettable experience. "
    
    p "You'll get to see so much of India, from the bustling cities to the peaceful countryside."
    hide ig train
    show kb training at left
    kb "I can't wait! What should we expect during the journey?"
    hide kb training
    menu:

        "What should we expect during the journey?"

        "Discuss the history and significance of Indian Railways.":
            $ affection += 4
            jump Ch4_S11_T2_IG

        "Talk about the diversity of regions and cultures in India.":
            $ affection += 7
            jump Ch4_S11_T1_IG
        
        "Mention the culinary delights available on the train.":
            $ affection += 1
            jump Ch4_S11_T3_IG

        "Suggest sleeping or reading during the journey to pass the time.":
            $ affection -= 5
            jump Ch4_S11_T4_IG

label Ch4_S11_T1_IG:

    jump Ch4_S12_T0_IG

label Ch4_S11_T2_IG:

    jump Ch4_S12_T0_IG

label Ch4_S11_T3_IG:

    jump Ch4_S12_T0_IG

label Ch4_S11_T4_IG:

    jump Ch4_S12_T0_IG

label Ch4_S12_T0_IG:
    scene bg bangalore:
        zoom 1.1

    "After a long but enriching journey, we finally arrived in Bangalore. The city greeted us with its pleasant weather and vibrant atmosphere."
    show kb bangalore at right
    kb "Bangalore seems so lively! I've heard it's known as the Silicon Valley of India."
    hide kb bangalore 
    show ig smartcasuals at left
    p "That's right. Bangalore is a major hub for technology and startups, but it's also known for its parks, historic sites, and diverse culture."
    hide ig smartcasuals
    show kb bangalore at right
    kb "I'm excited to explore it. What should we do first?"
    hide kb bangalore 
    menu:

        "What should we do first?"

        "Propose heading straight to the hotel to rest.":
            $ affection -= 5
            jump Ch4_S13_T4_IG

        "Propose visiting the local parks and gardens.":
            $ affection += 4
            jump Ch4_S13_T2_IG

        "Suggest checking out the local markets.":
            $ affection += 0
            jump Ch4_S13_T3_IG
            
        "Suggest exploring the historic parts of Bangalore.":
            $ affection += 7
            jump Ch4_S13_T1_IG

        

label Ch4_S13_T1_IG:

    jump Ch4_S14_T0_IG

label Ch4_S13_T2_IG:

    jump Ch4_S14_T0_IG

label Ch4_S13_T3_IG:

    jump Ch4_S14_T0_IG

label Ch4_S13_T4_IG:

    jump Ch4_S14_T0_IG

label Ch4_S14_T0_IG:

    "After settling in, I thought it would be a great idea to introduce [kb] to Indian cinema—a vital part of the culture here."
    "We decided to go to a local theatre to watch a popular Indian film."
    show kb bangalore at left
    kb "I've heard so much about Indian cinema. Bollywood, right?"
    hide kb bangalore 
    show ig smartcasuals at right
    p "Yes, but there's so much more to Indian cinema than just Bollywood. "
    
    p "Each region has its own film industry—Kollywood in Tamil Nadu, Tollywood in Andhra Pradesh, and Sandalwood right here in Karnataka. "

    p "Indian cinema has a rich history, and it's evolved a lot over the years."
    hide ig smartcasuals
    menu:
        "Suggest watching the movie quietly without discussing it.":
            $ affection -= 5
            jump Ch4_S15_T4_IG
            
        "Talk about the influence of Indian cinema globally.":
            $ affection += 3
            jump Ch4_S15_T2_IG

        "Discuss the different film genres and what to expect.":
            $ affection += 1
            jump Ch4_S15_T3_IG
            
        "Explain the history and evolution of Indian cinema.":
            $ affection += 5
            jump Ch4_S15_T1_IG

label Ch4_S15_T1_IG:

    jump Ch4_S16_T0_IG

label Ch4_S15_T2_IG:

    jump Ch4_S16_T0_IG

label Ch4_S15_T3_IG:

    jump Ch4_S16_T0_IG

label Ch4_S15_T4_IG:

    jump Ch4_S16_T0_IG

label Ch4_S16_T0_IG:
    scene bg theatre:
        zoom 1.3

    "We entered the theatre, the air filled with the aroma of popcorn and the excitement of the audience. "
    
    "The movie started, and I could see [kb] was completely engrossed in the experience."
    show kb bangalore at left
    kb "That was incredible! The energy, the colors, the music—it's so different from what I'm used to, but I loved it."
    hide kb bangalore 
    show ig smartcasuals at right
    p "I'm glad you enjoyed it. Indian cinema is all about making you feel deeply, whether it's joy, sorrow, or excitement."
    hide ig smartcasuals 
    show kb bangalore at left
    kb "I can't wait to watch more. Thank you for introducing me to this part of your culture."
    hide kb bangalore 
    "As we left the theatre, I felt even closer to [kb]. Sharing these experiences together has deepened our bond, and I'm excited to see where our journey takes us next."

    jump Ch5_S1_T0_IG


### need codes to decide the ending. Sanghyuk fighting ^^
## I'm working until the night ;o;

label Ch5_S1_T0_IG:
    if affection >= 40:
        jump Ch5_S1_T1_IG
    elif affection >= 20:
        jump Ch5_S1_T2_IG
    else:
        jump Ch5_S1_T3_IG

label Ch5_S1_T1_IG:
    scene bg christ_dorm

    "After parting ways with [kb], I returned to my dormitory, trying to focus on my exams."
    show kb at right
    kb "We're both busy, so let's concentrate on studying."
    hide kb airport
    show ig kurti at left
    p "Yeah, let's do that."
    hide ig kurti
    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."
    show ig kurti
    p "When did [kb]'s exchange program end again?"

    "I found myself at [kb]'s dormitory. Seeing the empty room, I wondered if I would regret this day."

    "We were so happy together, but perhaps it was beautiful because it's now the past. But still... (reflects briefly). Will I meet someone like [kb] again?"
    hide ig kurti
    "Realizing today was [kb]'s departure, I called a taxi and headed to the airport."
    
    scene bg india_airport
    show ig rushed
    p "It was today! I still wanted to say goodbye..."

    "At the airport, I found the counter for flights to Korea and waited. Noticing missed calls, I called back."

    p "Are you at the airport? I saw the letter you left!"

    "Even now, [kb] was the best person I'd met. So kind and together often. I don't think I'll meet someone like [kb] again."
    hide ig rushed
    show kb airport
    kb "Yeah... but I don't want to go. I couldn't say it then, but I realize I need you."
    hide kb airport
    show ig rushed
    p "Smiles silently."

    "We got back together later, and continued our beautiful relationship between Korea and India."

    scene bg wedding:
        zoom 1.4
    
    "The bride is ready to enter!"
    show ig happyending
    p "Today is the happiest day of my life!!"
    hide ig happyending
    show kb happy ending
    kb "Me too, hehe."
    hide kb happy ending
    show ig happyending at left 
    p "Ready for the party? It's going to go late into the night!!"
    show kb at right
    "As we entered the hall, I remembered when I first met [kb]. If I hadn't met [kb], what would have happened? This beautiful story of mine will continue forever."
    
    "{b}Happy Ending{/b}"
    return

label Ch5_S1_T2_IG:
    scene bg christ_dorm

    "After parting ways with [kb], I returned to my dormitory, trying to focus on my exams."
    show kb airport
    kb "We're both busy, so let's concentrate on studying."
    hide kb airport
    show ig kurti
    p "Yeah, let's do that."
    hide ig kurti
    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."
    show ig kurti
    p "When does [kb]'s exchange program end?"

    "I found myself standing outside [kb]'s empty dormitory, wondering if I'd regret letting go."

    "We had some wonderful times together, perhaps more beautiful now as memories. I wondered if I'd meet anyone like [kb] again."
    "Realizing today was [kb]'s departure, I impulsively headed to the airport."

    scene bg india_airport
    show ig rushed
    p "Today's the day! I still wanted to say goodbye..."

    "At the airport, I looked for flights to Korea and decided to wait. I saw missed calls and dialed back."

    p "Are you at the airport? I saw your letter at the dorm!"
    hide ig rushed
    scene bg foreign_street

    "Reflecting on the past, [kb] was one of the kindest people I'd met. Though we parted ways, those memories stayed with me."

    "As time passed, life moved on. "
    "Years later, I joined a reunion trip for the exchange program. "
    "Among familiar faces, I saw [kb] again."
    show kb neutral ending
    kb "It's been a long time!"
    hide kb neutral ending
    show ig neutralending
    p "It really has. How have you been?"
    hide ig neutralending
    "We shared stories and laughter, reconnecting as friends. Those moments we shared were a cherished chapter, and seeing [kb] again felt like a new beginning, in a different way."

    "{b}Normal Ending{/b}"
    return

label Ch5_S1_T3_IG:
    scene bg christ_dorm

    "After parting ways with [kb], I returned to my dormitory, trying to focus on my exams."
    show kb airport
    kb "We're both busy, so let's concentrate on studying."
    hide kb airport
    show ig kurti
    p "Yeah, let's do that."
    hide ig kurti 
    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."
    show ig rushed
    p "When does [kb]'s exchange program end?"
    hide ig rushed
    "I found myself outside [kb]'s empty dormitory, wondering if I'd regret how things ended."

    "We had some wonderful times together, but they felt distant now. Our breakup was painful, leaving me with lingering doubts."
    "I knew today was [kb]'s departure, but I couldn't bring myself to go to the airport."
    show ig rushed
    p "I should have gone... but I just couldn't face it."
    hide ig rushed
    scene bg foreign_street
    show ig badending at left
    "Time passed, and life moved on. "
    show kb bad ending
    "Years later, I was on a business trip and unexpectedly saw [kb] again."

    "In a crowded conference room, our eyes met briefly. An awkward silence stretched between us, heavy with unspoken words."

    "I tried to focus on my work, but my thoughts kept drifting back to [kb]. Memories of our time together resurfaced, mingling with the bitterness of our breakup."

    p "I wish things had ended differently."

    "We passed each other in the hallway, pretending not to notice, but the weight of our shared history was palpable."

    "All I could do was think about [kb], trapped by what once was, but unable to bridge the gap between us. "
    hide ig badending
    hide kb bad ending
    "The silence spoke louder than words, and we both walked away, unable to reconnect or find closure."

    "{b}Bad ending{/b}"
    return


### IB ver. ###


### IB

label Ch1_S1_T0_IB:

    scene bg building_220:
        zoom 1.2

    "Today was my first day as an exchange student in Korea. The wind felt particularly refreshing that day."

    p "Hmm... I have no idea where anything is since it's my first time here. Let's head to the lounge in Building 220 and think things over."

    "I headed towards the lounge in Building 220 and opened the door."

    scene bg lounge_220:
        zoom 4.5
    with dissolve
    
    f1 "Oh? A new face. Are you an exchange student by any chance?"
    show ib cafeteria at left
    p "Yeah, I just arrived as an exchange student from Christ University. My name is [player_name]."

    f1 "Nice to meet you! If you have any questions, feel free to ask!"

    "Just then, someone suddenly grabbed my shoulder."
    hide ib cafeteria
    show kg cafeteria at right
    kg "Hey! What were you guys talking about?"
    hide kg cafeteria 
    show ib cafeteria at left
    
    p "Uh?"
    hide ib cafeteria
    show kg cafeteria at right
    
    kg "Uh? Who... are you?"
    hide kg cafeteria 
    "That was how we first met. She was quite flustered, and her cheeks turned a bit red with embarrassment. Haha."

    kg "Oh!! I'm so sorry!!"
    hide kg  cafeteria 
    
    
    f1 "Haha, introduce yourself. She's an exchange student who just joined the College of Liberal Studies today."

    p "Hi, I'm [player_name]. I'm an exchange student from Christ University in India, now studying at SNU's College of Liberal Studies."
    hide ib cafeteria 
    show kg  cafeteria at right
    kg "Oh, nice to meet you!! I'm [kg]. I heard an SNU student went to India, and now we have an exchange student here, too!"

    kg "Anyway, if you need help with anything, feel free to ask! Oh, wait, I don't have your number yet! What's your number?"
    hide kg  cafeteria 
    show ib caferia at left
    p "My number is ~~!"
    hide ib cafeteria 
    show kg cafeteria at right
    kg "Great, thanks!"

    "(Growling sound)"

    kg "(Quickly changing the subject) Uh, did you have lunch yet? Haha"
    hide kg cafeteria 
    f1 "Haha, we were just about to grab something. Let's go together!"
    show ib cafeteria at left
    p "Sounds good!"
    hide ib cafeteria 
    "We headed to the cafeteria together..."
    
    scene bg snu_cafeteria:
        zoom 1.4
    with dissolve

    f1 "Oh, shoot! I forgot I had an assignment due! You two go ahead and eat! I'll see you later!"

    "Being left awkwardly alone... Well, let's go eat."

    jump Ch1_S2_T0_IB

label Ch1_S2_T0_IB:

    ## Cafeteria

    "We arrive at the cafeteria, and today's menu is bibimbap. We each grab a bowl and sit down."

    kg "This must be your first time at the cafeteria, right? This is SNU's cafeteria!"

    kg "This is bibimbap, a Korean dish where you mix rice with various vegetables and gochujang (Korean chili paste)!"
    hide kg cafeteria 
    show ib cafeteria at right
    p "Oh!! It looks delicious!! I've never had bibimbap before!"
    hide ib cafeteria
    show kg cafeteria at left
    kg "Let me mix it for you!"

    "I put all my effort into mixing it."

    "But I get so into it that I accidentally bump into someone's arm, causing the spoon to fling a grain of rice onto their face."

    "What would you do?"

    "(Tutorial) This game requires you to make choices at key moments! Depending on your choices, the relationship level can increase or decrease. The final ending will be different based on your decisions, so choose carefully!"

    menu:

        "What would you do?"

        "1. Remove the grain of rice stuck on [kg]'s face with your hand.":
            $ affection += 5
            jump Ch1_S3_T1_IB

        "2. Hand [kg] a handkerchief.":
            $ affection += 2
            jump Ch1_S3_T2_IB

        "3. Glare at the person next to you.":
            $ affection -= 5
            jump Ch1_S3_T3_IB

label Ch1_S3_T1_IB:

    jump Ch1_S4_T0_IB

label Ch1_S3_T2_IB:

    jump Ch1_S4_T0_IB

label Ch1_S3_T3_IB:

    jump Ch1_S4_T0_IB

label Ch1_S4_T0_IB:

    p "Haha, it's okay. I have a handkerchief. You got some rice on your face."

    p "This bibimbap is really good! The flavors are mild, and it goes well with the gochujang!"
    hide ib cafeteria
    show kg cafeteria at left 
    kg "Really? I'm glad you like it, haha. By the way, are you busy these days? Have you explored Seoul much?"
    hide kg cafeteria 
    show ib cafeteria at right
    p "Huh? No, I haven't really had the chance to see much outside the campus... Do you have time tomorrow? Maybe you could show me around Seoul?"
    hide ib cafeteria 
    show kg cafeteria at left
    kg "Yeah, I'm free tomorrow! Let's meet up after class! I'll text you!"
    hide kg cafeteria 
    show ib cafeteria at right
    p "Sounds good. See you tomorrow then!"
    hide ib cafeteria 
    jump Ch2_S1_T0_IB


label Ch2_S1_T0_IB:

    "_Chatting app_"

    kg "[player_name], have you ever been to Seol-ip?"
    hide kg pyjamas
    show ib pyjamas
    p "Seol-ip..? You mean Seoul National University Station, right? I've never been there!"
    hide ib pyjamas
    show kg pyjamas
    kg "Then do you want to go with me? I'll show you around."
    hide kg pyjamas
    show ib pyjamas 
    p "Okay, good!"
    hide ib pyjamas
    scene bg seolip:
        zoom 1.2

    "The next day. we two met in Seol-ip."

    kg "Ta-da! Students from our school usually come here to hang out."
    hide kg date
    show ib date at left
    p "Wow, there are a lot of people."
    hide ib date
    show kg date at right
    kg "Um... Since we just had lunch, how about going to a cafe I know and having some dessert?"
    hide kg date
    show ib date at left
    p "Okay."
    hide ib date 
    show kg date at right
    kg "I'll buy you some for your first time at Seol-ip."
    hide kg date
    show ib date at left
    p "Oh really?? Thank you. I'll eat well~"
    hide ib date 
    show kg date at right 
    kg "Huh? It's a karaoke! I wanted to go to a karaoke, haha."
    hide kg date
    show ib date at left
    p "Really? Then let's go in now."
    hide ib date 
    scene bg karaoke:
        zoom 2.8
    with dissolve

    kg "You can pay for the time you want, and select the song you want to sing with the remote control. Here, the mic."
    hide kg date
    show ib date at right
    p "Thank you. You're so kind. I'll sing first!"
    hide ib date 
    show kg date at left
    "I am confident in my singing skills, so I sing my favorite song with great enthusiasm."
    "I look to the side while singing and see the other person staring at me."
    "I was a little nervous about the other person until the song ended."
    hide kg date
    show ib date at right
    p "Wow, you sing really well!"

    kg "Haha, no. Now sing too."
    hide kg date
    "The other person chose a duet song that is famous for being romantic."
    "Blah blah~"
    
    "Which of the following actions should I choose?"

    menu:

        "Which of the following actions should I choose?"

        "1. Sing along to the duet song.":
            ## $ affection level increases.
            $ affection += 5
            jump Ch2_S2_T1_IB

        "2. Stay still.":
            ## $ affection level decreases.
            $ affection -= 5
            jump Ch2_S2_T2_IB

        "3. Pick up a tambourine and dance like crazy.":
            ## $ affection level increases slightly.
            $ affection += 2
            jump Ch2_S2_T3_IB

label Ch2_S2_T1_IB:

    jump Ch2_S3_T0_IB

label Ch2_S2_T2_IB:

    jump Ch2_S3_T0_IB

label Ch2_S2_T3_IB:

    jump Ch2_S3_T0_IB

label Ch2_S3_T0_IB:

    kg "Phew, I had fun. Where should we go now... Is there a place you want to go?"
    hide kg date
    show ib date at right
    p "Um... Actually, I wanted to see the palaces of Korea."
    hide ib date
    show kg date at left
    kg "Really? Then do you want to go to Gyeongbokgung Palace together?"
    hide kg date
    show ib date at right
    p "Okay, fine."
    hide ib date
    scene bg gyunbok:
        zoom 2.8
    with dissolve

    "We two take a bus and arrive at Gyeongbokgung Palace."

    "There are many people walking around the palace wearing hanbok."
    show ib date at left
    p "What are those clothes?"
    hide ib date
    show kg date at right
    kg "That's a traditional Korean costume called hanbok. Hanbok is a costume that our people have worn since ancient times, "
    hide kg date
    show ib date at left     
    kg "and it has changed over time based on the basics of a jacket, pants, and skirt. "
    hide ib date
    show kg date at right   
    kg "Today's hanbok follows the style that was popular during the Joseon Dynasty, "
    
    kg "and modernized hanbok, which is designed to be worn in everyday life, is also popular. "
    
    kg "You can rent a hanbok nearby. Shall we try it on together?"
    hide kg date
    show ib date at left
    p "Okay, let's do that!"
    hide ib date
    "The two change into hanbok."
    show kg hanbok at right
    kg "Now let's take a look around Gyeongbokgung Palace."
    hide kg hanbok
    gd "Gyeongbokgung Palace is the first palace built when Joseon was founded and Hanyang (present-day Seoul) became the capital. "
 
    gd "It was used for banquets and receptions by the king and his subjects, as well as for receiving envoys, "
 
    gd "by building a large pond and a grand pavilion. "
 
    gd "Although many buildings were destroyed during the war and colonial period, "
 
    gd "restoration work has been steadily carried out to this day. "

    gd "It is a symbolic palace of the Joseon Dynasty that still maintains its original location since its founding."

    "The two leisurely stroll through Geunjeongjeon and Gyeonghoeru, enjoying the tranquil atmosphere of Gyeongbokgung Palace."
    show kg hanbok at right
    kg "I think we've seen all the palaces. How was it?"
    hide kg hanbok
    show ib hanbok at left
    p "It was really beautiful! The color arrangement and elaborate design were really impressive. "
    "It was touching to be able to experience Korean history and tradition in person while wearing hanbok. "
    "It felt like a harmony of tradition and modernity, considering that there is a palace like this in the middle of Seoul."
    hide ib hanbok
    show kg hanbok at right
    kg "I'm glad it was a good experience haha. Next, I'll introduce you to the famous traditional market in this area."
    hide kg hanbok
    show ib hanbok at left
    p "Right!"

    p "Oh, it's cold."

    scene bg gyunbok_raining:
        zoom 1.8
    hide ib hanbok
    show kg hanbok at left
    kg "Huh? It's raining."

    "(Shooting, swoosh, the sound of rain falling)"

    kg "Do you have an umbrella? I only have one for myself…"
    hide kg hanbok
    show ib hanbok at right
    p "No. It seems like Korea gets a lot of rain showers."
    hide ib hanbok
    show kg hanbok at left
    kg "Let's go under the eaves and wait for it to stop."
    hide kg hanbok
    "The two moved under the skirts to take shelter from the rain for a while, but the rain showed no sign of stopping."
    show kg hanbok at left
    kg "Hmm, the rain won't stop. We have to get to the market on time, but..."
    hide kg hanbok
    
    
    "How should I respond to an unexpected downpour?"

    menu:
        "1. Go to a nearby convenience store and buy an umbrella each.":
            ## Slightly decrease in favorability
            $ affection +=  3
            jump Ch2_S4_T1_IB

        "2. Share an umbrella and run to the market.":
            ## $ affection level goes up significantly
            $ affection += 5
            jump Ch2_S4_T2_IB

        "3. Suggest that we both just go while getting rained on.":
            ## $ affection level goes down significantly
            $ affection += 3
            jump Ch2_S4_T3_IB

label Ch2_S4_T1_IB:
    
    jump Ch2_S5_T0_IB

label Ch2_S4_T2_IB:

    jump Ch2_S5_T0_IB

label Ch2_S4_T3_IB:

    jump Ch2_S5_T0_IB

label Ch2_S5_T0_IB:
    scene bg kmarket:
        zoom 1.7

    "After many twists and turns, the two arrive at Gwangjang Market."
    show kg hanbok at right
    kg "Okay, this is Gwangjang Market."
    hide kg hanbok
    show ib hanbok at left
    p "It's bigger and more crowded than I thought."
    hide ib hanbok 
    show kg hanbok at right 
    kg "That's right. Gwangjang Market is the largest and oldest traditional market in Korea. "
    "There are various food alleys in Gwangjang Market, hanbok stores where you can buy daily necessities, and second-hand stores."
    hide kg hanbok
    show ib hanbok at left
    p "Right. Let's eat something since we're hungry."
    hide ib hanbok
    show kg hanbok at right
    kg "This is tteokbokki, a national snack that Koreans of all ages and genders love. "
    "It might be a little spicy, but is that okay?"
    hide kg hanbok
    "What should I say in response to that suggestion?"

    menu:
        "1. Yeah, I like spicy food. Wow~":
            ## Affinity increase
            $ affection += 3
            jump Ch2_S6_T1_IB

        "2. I can't eat spicy food well... I'll try it next time.":
            ## Affinity maintained
            $ affection += 0
            jump Ch2_S6_T2_IB

        "3. Hmm, I'll rinse it in water and try it. Give it to me.":
            ## Affinity decrease
            $ affection += -5
            jump Ch2_S6_T3_IB

label Ch2_S6_T1_IB:

    jump Ch2_S7_T0_IB

label Ch2_S6_T2_IB:

    jump Ch2_S7_T0_IB

label Ch2_S6_T3_IB:

    jump Ch2_S7_T0_IB

label Ch2_S7_T0_IB:

    kg "This is bindae-tteok, a specialty of Gwangjang Market. "
    "It is a dish made by mixing vegetables or meat into a dough made from ground soybeans and frying it."

    kg "This noodle is called janchi-guksu. "
    "It originated from the fact that it was enjoyed at weddings, birthday parties, and 60th birthday parties in the hopes of longevity."
    hide kg hanbok
    show ib hanbok at left
    p "The food here is really delicious."
    hide ib hanbok
    "Then they enjoy the food with a happy conversation."

    jump Ch3_S1_T0_IB


label Ch3_S1_T0_IB:

    kg "How about we try dating somewhere new?"
    hide kg waterbomb vigorous
    show ib wterbomb at right
    p "Sounds good! Where should we go?"
    hide ib wterbomb 
    show kg waterbomb vigorous at left
    kg "Is there anything you'd like to try?"
    hide kg waterbomb vigorous
    show ib wterbomb at right
    p "Hmm... Could we maybe go to a famous festival in Korea?"
    hide ib wterbomb
    show kg waterbomb vigorous at left
    kg "Of course! How about we go to the largest music and water-themed festival in the country? "
    kg "It combines performances from various genres like K-POP, hip-hop, EDM, and large-scale water fights!"
    hide kg waterbomb vigorous
    show ib wterbomb at right
    p "Great! What's the name of that festival?"
    hide ib wterbomb 
    show kg waterbomb vigorous at left
    kg "Want to try guessing?"
    hide kg waterbomb vigorous

    menu:

        "Guess the name of the festival:"

        "1. Pentaport Rock Festival":
            $ affection += -3
            jump Ch3_S2_T1_IB

        "2. Waterbomb Festival":
            $ affection += 3
            jump Ch3_S2_T2_IB

        "3. Boryeong Mud Festival":
            $ affection += -3
            jump Ch3_S2_T3_IB

        "4. Seoul Jazz Festival":
            $ affection += -3
            jump Ch3_S2_T4_IB

label Ch3_S2_T1_IB:
    show kg waterbomb vigorous at left
    kg "Ah, unfortunately the answer was Waterbomb :( Well then, shall we go to Waterbomb now?"

    jump Ch3_S3_T0_IB

label Ch3_S2_T2_IB:
    show kg waterbomb vigorous at left
    kg "That's right!! My darling! Then shall we go to Waterbomb?"

    jump Ch3_S3_T0_IB

label Ch3_S2_T3_IB:
    show kg waterbomb vigorous at left
    kg "Ah, unfortunately the answer was Waterbomb :( Well then, shall we go to Waterbomb now?"

    jump Ch3_S3_T0_IB

label Ch3_S2_T4_IB:
    show kg waterbomb vigorous at left
    kg "Ah, unfortunately the answer was Waterbomb :( Well then, shall we go to Waterbomb now?"

    jump Ch3_S3_T0_IB

label Ch3_S3_T0_IB:
    scene bg waterbomb:
        zoom 1.2

    "We really enjoyed Waterbomb."
    hide kg waterbomb vigorous
    show ib wterbomb at right
    p "Wow! This is really fun!!"
    hide ib wterbomb 
    "During the water gun play, I became the target of many people."
    show ib wterbomb at left
    p "Oh no..."
    hide ib wterbomb
    show kg waterbomb vigorous at right
    kg "[player_name]!!"
    hide kg waterbomb vigorous
    "[kg] shielded me with her whole body."
    show kg waterbomb vigorous at right
    kg "Are you okay??"
    hide kg waterbomb vigorous
    show ib wterbomb at left
    p "Yes!! Really thank you"
    hide ib wterbomb
    show kg waterbomb vigorous at right
    kg "How was it?"
    hide kg waterbomb vigorous
    show ib wterbomb at left
    p "This was so much fun!!"
    hide ib wterbomb
    show kg waterbomb vigorous at right
    kg "Great! Then let's go watch the performances now? We can buy some beers too!"
    hide kg waterbomb vigorous
    show ib wterbomb at left
    #"*Performance photos attached*"

    p "It was so much fun!! I especially enjoyed seeing the K-pop singers. I love music!"
    hide ib wterbmob
    show kg waterbomb vigorous at right
    kg "Oh really? Then should we go to Hongdae next time?"
    hide kg waterbomb vigorous
    show ib wterbomb at left
    p "Why Hongdae? Is it famous for music?"
    hide ib wterbomb 
    show kg waterbomb vigorous at right 
    "I saw busking in Hongdae with [kg]"
    hide kg waterbomb vigorous
    show ib wterbomb 
    p "This is so enjoyable~"
    hide ib wterbomb
    "I suddenly got a text message."
    show ib sadwaterbomb
    p "Oh no..."
    hide ib sadwaterbomb 
    show kg waterbomb sad at left
    kg "What's wrong? You don't look good."
    hide kg waterbomb sad 
    show ib sadwaterbomb at right
    p "I think I need to go back to India now."
    hide ib sadwaterbomb 
    show kg waterbomb sad at left
    kg "What? Didn't you have half a year left?"
    hide kg waterbomb sad 
    show ib sadwaterbomb at right 
    p "I loved Korea and you so much that I extended my exchange student program for another semester, "

    p "but I just got a message saying my application was rejected."
    hide ib sadwaterbomb
    show kg waterbomb sad at left
    kg "What? I'm so disappointed... I'm tearing up..."
    hide kg waterbomb sad 
    show ib sadwaterbomb at right
    p "Oh honey, don't cry... I'm really disappointed too.."
    hide ib sadwaterbomb
    show kg waterbomb sad at left
    kg "So we won't be able to see each other anymore?"
    hide kg waterbomb sad 
    menu:

        "Choose the right sentence to comfort the other person:"

        "1. I suppose so. I'm really sorry.":
            $ affection -= 2
            jump Ch3_S4_T1_IB

        "2. We were never meant to be together for long anyway.":
            $ affection += -5
            jump Ch3_S4_T2_IB

        "3. No, don't say that! Everything will be alright, don't worry my dear.":
            $ affection += 5
            jump Ch3_S4_T3_IB

label Ch3_S4_T1_IB:

    jump Ch3_S5_T0_IB

label Ch3_S4_T2_IB:

    jump Ch3_S5_T0_IB

label Ch3_S4_T3_IB:

    jump Ch3_S5_T0_IB

label Ch3_S5_T0_IB:
    scene bg kairport:
        zoom 1.2

    "at the airport"
    show kg airport
    kg "I wish we could meet again soon."
    hide kg airport
    show ib rushed
    p "Be happy even after you go back."
    hide ib airport
    show kg kurta
    kg "I prepared a gift for you. This is a traditional Korean costume, do you remember the name of it?"
    hide kg airport
    menu:

        "Guess the name of the costume:"

        "1. Hanbok":
            $ affection += 5
            jump Ch3_S6_T1_IB

        "2. Kimono":
            $ affection += -5
            jump Ch3_S6_T2_IB

        "3. Ao Dai":
            $ affection += -5
            jump Ch3_S6_T3_IB

        "4. Sari":
            $ affection += -2
            jump Ch3_S6_T4_IB

label Ch3_S6_T1_IB:
    show kg airport
    "Right! You remember!"

    jump Ch3_S7_T0_IB

label Ch3_S6_T2_IB:
    show kg airport
    "Don't you remember that? The answer was Hanbok."

    jump Ch3_S7_T0_IB

label Ch3_S6_T3_IB:
    show kg airport
    "Don't you remember that? The answer was Hanbok."

    jump Ch3_S7_T0_IB

label Ch3_S6_T4_IB:
    show kg airport
    "Don't you remember that? The answer was Hanbok."

    jump Ch3_S7_T0_IB

label Ch3_S7_T0_IB:
    hide kg airport
    show ib rushed at left
    p "Wow, thank you so much. This will remind me of you."
    hide ib rushed
    show kg airport at right 
    kg "Don't forget me when you go back to India."
    hide kg airport
    show ib rushed at left
    p "Of course not. We're under the same sky. Our love will be eternal."
    hide ib rushed
    show kg airport at right
    kg "Take care in Korea."
    hide kg airport
    show ib rushed
    p "Yes, you take care in India too. Let's meet in India next time."
    hide ib rushed
    jump Ch4_S1_T0_IG
    jump Ch4_S1_T0_IB


label Ch4_S1_T0_IB:
    scene bg india_room:
        zoom 1.2

    "It's been two months since I returned to Bengaluru in a hurry. Fortunately, my mother's health is gradually improving."

    p "She must have been surprised that I left so suddenly. Will I be able to see her again?"

    "Without thinking, I opened my mailbox, and there it was, an email from her."

    menu:
        "Read the email":
            $ affection += 5
            jump Ch4_S1_T1_IB

        "Don't read the email":
            $ affection += -5
            jump Ch4_S1_T2_IB

label Ch4_S1_T1_IB:

    "I thought I was the only one missing her, but she felt the same way. She is coming to our school as an exchange student. I can't believe it."

    jump Ch4_S2_T0_IB

label Ch4_S1_T2_IB:

    "I shouldn't hold on to past relationships. Reading this email will only make me miss her more. I won't read it."

    jump Ch4_S2_T0_IB

label Ch4_S2_T0_IB:
    show m at left
    m "We're going to visit your grandfather in Agra next week."
    hide m 
    show ib pyjamas
    p "Agra?"
    hide ib pyjamas
    show m
    m "Yes. We need to deliver these things to your grandfather."
    hide m
    "After visiting my grandfather's house, I had a bit of time before my flight. What should I do now?"

    menu:

        "What should I do now?"

        "Go to the Taj Mahal":
            $ affection += 5
            jump Ch4_S3_T1_IB

        "Go to Agra Fort":
            scene bg agra
            $ affection += 2
            jump Ch4_S3_T2_IB

        "Go shopping":
            scene bg india_shopping:
                zoom 1.7
            $ affection += -5
            jump Ch4_S3_T3_IB

label Ch4_S3_T1_IB:

    jump Ch4_S4_T0_IB

label Ch4_S3_T2_IB:

    "There were too many people at Agra Fort, so I decided to go to the Taj Mahal."

    jump Ch4_S4_T0_IB

label Ch4_S3_T3_IB:

    "There were too many people at the shopping area, so I decided to go to the Taj Mahal."

    jump Ch4_S4_T0_IB

label Ch4_S4_T0_IB:
    scene bg tajmahal
    show ib kurti
    "Come to think of it, she also wanted to visit this place... I have a feeling she might be here today."
    hide ib kurti
    menu:
        "Observe the people following the tour guide":
            $ affection += 3
            jump Ch4_S5_T1_IB

        "Watch people getting their photos taken by peddlers":
            $ affection += 0
            jump Ch4_S5_T2_IB

        "No way, such a coincidence couldn't happen":
            $ affection -= 5
            jump Ch4_S5_T3_IB

label Ch4_S5_T1_IB:

    jump Ch4_S6_T0_IB

label Ch4_S5_T2_IB:

    jump Ch4_S6_T0_IB

label Ch4_S5_T3_IB:

    jump Ch4_S6_T0_IB

label Ch4_S6_T0_IB:

    "I see a Korean person over there! No way..."
    show kg kurta
    kg "Oh! It's you!"
    hide kg kurta
    show ib kurti
    p "What a coincidence to meet here..."
    hide ib kurti
    show kg kurta
    kg "I arrived in India yesterday. You said you would take me to the Taj Mahal, so I wanted to come even if it was alone."
    hide kg kurta
    show ib kurti
    p "I had a feeling you might be here today."
    hide ib kurti
    show kg kurta
    kg "The Taj Mahal is so beautiful! Just like you described it."
    hide kg kurta
    show ib kurti
    p "I thought you would like Agra. It has many historical sites that showcase Indian tradition. It's like..."
    hide ib kurti
    menu:

        "It's like ( ) in Seoul."

        "Myeong-dong":
            $ affection += 0
            jump Ch4_S7_T1_IB

        "Jongno":
            $ affection += 3
            jump Ch4_S7_T2_IB

        "Itaewon":
            $ affection += -3
            jump Ch4_S7_T3_IB

label Ch4_S7_T1_IB:

    jump Ch4_S8_T0_IB

label Ch4_S7_T2_IB:

    jump Ch4_S8_T0_IB

label Ch4_S7_T3_IB:

    jump Ch4_S8_T0_IB

label Ch4_S8_T0_IB:
    show kg at right
    kg "That's right! You seem to know quite a lot about Korea now!"
    hide kg kurta
    show ib kurti at left
    p "Of course! It's always a place I miss."
    hide ib kurti
    show kg at right
    kg "What should we do now?"
    hide kg kurta

    menu:
        "Let's go eat street food in Delhi":
            $ affection += 5
            jump Ch4_S9_T1_IB

        "I'll take a picture of you in front of the Taj Mahal":
            $ affection += 0
            jump Ch4_S9_T2_IB

        "Let's go back to the hotel and rest":
            $ affection += -5
            jump Ch4_S9_T3_IB

label Ch4_S9_T1_IB:

    jump Ch4_S10_T0_IB

label Ch4_S9_T2_IB:

    jump Ch4_S10_T0_IB

label Ch4_S9_T3_IB:

    jump Ch4_S10_T0_IB

label Ch4_S10_T0_IB:
    scene bg india_train

    "We traveled around Agra and Delhi for a few days. Now it's time to return to Bangalore."

    "After spending a few memorable days in Delhi and Agra, it's time to head back to Bangalore. "

    "We decided to take the train together—an experience that would allow us to see more of India's diverse landscapes and cultures as we travel across regions."
    show kg training at left
    kg "I've heard that train journeys in India are quite an experience. I'm excited but also a bit nervous. How long will the journey take?"
    hide kg training
    show ib train at right
    p "It'll take around 36 to 40 hours, depending on the train. But trust me, it's going to be an unforgettable experience. "

    p "You'll get to see so much of India, from the bustling cities to the peaceful countryside."
    hide ib train
    show kg training at left
    kg "I can't wait! What should we expect during the journey?"
    hide kg training
    menu:

        "Discuss the history and significance of Indian Railways.":
            $ affection += 4
            jump Ch4_S11_T2_IB

        "Talk about the diversity of regions and cultures in India.":
            $ affection += 7
            jump Ch4_S11_T1_IB
            
        "Mention the culinary delights available on the train.":
            $ affection += 1
            jump Ch4_S11_T3_IB

        "Suggest sleeping or reading during the journey to pass the time.":
            $ affection += -5
            jump Ch4_S11_T4_IB

label Ch4_S11_T1_IB:

    jump Ch4_S12_T0_IB

label Ch4_S11_T2_IB:

    jump Ch4_S12_T0_IB

label Ch4_S11_T3_IB:

    jump Ch4_S12_T0_IB

label Ch4_S11_T4_IB:

    jump Ch4_S12_T0_IB

label Ch4_S12_T0_IB:
    scene bg bangalore:
        zoom 1.1

    "After a long but enriching journey, we finally arrived in Bangalore. The city greeted us with its pleasant weather and vibrant atmosphere."
    show kg bangalore at right
    kg "Bangalore seems so lively! I've heard it's known as the Silicon Valley of India."
    hide kg bangalore 
    show ib smartcasuals at left
    p "That's right. Bangalore is a major hub for technology and startups, but it's also known for its parks, historic sites, and diverse culture."
    hide ib smartcasuals
    show kg bangalore at right
    kg "I'm excited to explore it. What should we do first?"
    hide kg bangalore 
    menu:
        "Propose heading straight to the hotel to rest.":
            $ affection -= 5
            jump Ch4_S13_T4_IB

        "Propose visiting the local parks and gardens.":
            $ affection += 4
            jump Ch4_S13_T2_IB

        "Suggest checking out the local markets.":
            $ affection += 0
            jump Ch4_S13_T3_IB
            
        "Suggest exploring the historic parts of Bangalore.":
            $ affection += 7
            jump Ch4_S13_T1_IB


label Ch4_S13_T1_IB:

    jump Ch4_S14_T0_IB

label Ch4_S13_T2_IB:

    jump Ch4_S14_T0_IB

label Ch4_S13_T3_IB:

    jump Ch4_S14_T0_IB

label Ch4_S13_T4_IB:

    jump Ch4_S14_T0_IB

label Ch4_S14_T0_IB:

    "After settling in, I thought it would be a great idea to introduce K to Indian cinema—a vital part of the culture here."
    
    "We decided to go to a local theatre to watch a popular Indian film."
    show kg bangalore at left
    kg "I've heard so much about Indian cinema. Bollywood, right?"
    hide kg bangalore 
    show ib smartcasuals at right
    p "Yes, but there's so much more to Indian cinema than just Bollywood."
    
    p "Each region has its own film industry—Kollywood in Tamil Nadu, Tollywood in Andhra Pradesh, and Sandalwood right here in Karnataka. "

    p "Indian cinema has a rich history, and it's evolved a lot over the years."
    hide ib smartcasuals
    menu:
        "Suggest watching the movie quietly without discussing it.":
            $ affection += -5
            jump Ch4_S15_T4_IB
        
        "Explain the history and evolution of Indian cinema.":
            $ affection += 5
            jump Ch4_S15_T1_IB

        "Talk about the influence of Indian cinema globally.":
            $ affection += 3
            jump Ch4_S15_T2_IB

        "Discuss the different film genres and what to expect.":
            $ affection += 1
            jump Ch4_S15_T3_IB

label Ch4_S15_T1_IB:

    jump Ch4_S16_T0_IB

label Ch4_S15_T2_IB:

    jump Ch4_S16_T0_IB

label Ch4_S15_T3_IB:

    jump Ch4_S16_T0_IB

label Ch4_S15_T4_IB:

    jump Ch4_S16_T0_IB

label Ch4_S16_T0_IB:
    scene bg theatre:
        zoom 1.3

    "We entered the theatre, the air filled with the aroma of popcorn and the excitement of the audience. "
    
    "The movie started, and I could see K was completely engrossed in the experience."
    show kg bangalore at left
    kg "That was incredible! The energy, the colors, the music—it's so different from what I'm used to, but I loved it."
    hide kg bangalore 
    show ib smartcasuals at right
    p "I'm glad you enjoyed it. Indian cinema is all about making you feel deeply, whether it's joy, sorrow, or excitement."
    hide ib smartcasuals 
    show kg bangalore at left
    kg "I can't wait to watch more. Thank you for introducing me to this part of your culture."
    hide kg bangalore 
    "As we left the theatre, I felt even closer to [kg]. Sharing these experiences together has deepened our bond, and I'm excited to see where our journey takes us next."

    jump Ch5_S1_T0_IB


label Ch5_S1_T0_IB:

    if affection >= 40:
        jump Ch5_S1_T1_IB
    elif affection >= 20:
        jump Ch5_S1_T2_IB
    else:
        jump Ch5_S1_T3_IB

label Ch5_S1_T1_IB:
    scene bg christ_dorm

    "After parting ways with [kg], I returned to my dormitory, trying to focus on my exams."
    show kg at right
    kg "We're both busy, so let's concentrate on studying."
    hide kg airport
    show ib kurti at left
    p "Yeah, let's do that."
    hide ib kurti
    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."
    show ib kurti
    p "When did [kg]'s exchange program end again?"

    "I found myself at [kg]'s dormitory. Seeing the empty room, I wondered if I would regret this day."

    "We were so happy together, but perhaps it was beautiful because it's now the past. But still... (reflects briefly). Will I meet someone like [kg] again?"
    hide ib kurti
    "Realizing today was [kg]'s departure, I called a taxi and headed to the airport."

    scene bg india_airport
    show ib rushed

    p "It was today! I still wanted to say goodbye..."

    "At the airport, I found the counter for flights to Korea and waited. Noticing missed calls, I called back."

    p "Are you at the airport? I saw the letter you left!"

    "Even now, [kg] was the best person I'd met. So kind and together often. I don't think I'll meet someone like [kg] again."
    hide ib rushed
    show kg airport
    kg "Yeah... but I don't want to go. I couldn't say it then, but I realize I need you."
    hide kg airport
    show ib rushed
    p "Smiles silently."

    "We persuaded our parents, got back together, and continued our relationship between Korea and India."

    scene bg wedding:
        zoom 1.4

    "A vibrant Indian wedding with flowers."

    "Officiant" 
    
    "The groom is ready to enter!"
    show ib happyending
    p "Today is the happiest day of my life!!"
    hide ib happyending
    show kg happy ending
    kg "Me too, hehe."
    hide kg happy ending
    show ib happyending at left 
    p "Ready for the party? It's going to go late into the night!!"
    show kg at right
    "As we entered the hall, I remembered when I first met [kg]. If I hadn't met [kg], what would have happened? This beautiful story of mine will continue forever."
    "{b}Happy ending{/b}"
    return

label Ch5_S1_T2_IB:
    scene bg christ_dorm

    "After parting ways with [kg], I returned to my dormitory, trying to focus on my exams."
    show kg airport
    kg "We're both busy, so let's concentrate on studying."
    hide kg airport
    show ib kurti
    p "Yeah, let's do that."
    hide ib kurti
    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."
    show ib kurti
    p "When does [kg]'s exchange program end?"

    "I found myself standing outside [kg]'s empty dormitory, wondering if I'd regret letting go."

    "We had some wonderful times together, perhaps more beautiful now as memories. I wondered if I'd meet anyone like [kg] again."
    "Realizing today was [kg]'s departure, I impulsively headed to the airport."

    scene bg india_airport
    show ib rushed

    p "Today's the day! I still wanted to say goodbye..."

    "At the airport, I looked for flights to Korea and decided to wait. I saw missed calls and dialed back."

    p "Are you at the airport? I saw your letter at the dorm!"
    hide ib rushed
    scene bg foreign_street

    "Reflecting on the past, [kg] was one of the kindest people I'd met. Though we parted ways, those memories stayed with me."

    "As time passed, life moved on. "
    "Years later, I joined a reunion trip for the exchange program. "
    "Among familiar faces, I saw [kg] again."
    show kg neutral ending
    kg "It's been a long time!"
    hide kg neutral ending
    show ib neutralending
    p "It really has. How have you been?"
    hide ib neutralending
    "We shared stories and laughter, reconnecting as friends. Those moments we shared were a cherished chapter, and seeing [kg] again felt like a new beginning, in a different way."

    "{b}Normal Ending{/b}"
    return

label Ch5_S1_T3_IB:
    scene bg christ_dorm

    "After parting ways with [kg], I returned to my dormitory, trying to focus on my exams."
    show kg airport
    kg "We're both busy, so let's concentrate on studying."
    hide kg airport
    show ib kurti
    p "Yeah, let's do that."
    hide ib kurti 
    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."
    show ib rushed
    p "When does [kg]'s exchange program end?"
    hide ib rushed
    "I found myself outside [kg]'s empty dormitory, wondering if I'd regret how things ended."

    "We had some wonderful times together, but they felt distant now. Our breakup was painful, leaving me with lingering doubts."
    "I knew today was [kg]'s departure, but I couldn't bring myself to go to the airport."
    show ib rushed
    p "I should have gone... but I just couldn't face it."

    hide ib rushed
    scene bg foreign_street
    show ib badending at left
    "Time passed, and life moved on. "
    show kg bad ending
    
    
    "Years later, I was on a business trip and unexpectedly saw [kg] again."

    "In a crowded conference room, our eyes met briefly. An awkward silence stretched between us, heavy with unspoken words."

    "I tried to focus on my work, but my thoughts kept drifting back to [kg]. Memories of our time together resurfaced, mingling with the bitterness of our breakup."

    p "I wish things had ended differently."

    "We passed each other in the hallway, pretending not to notice, but the weight of our shared history was palpable."

    "All I could do was think about [kg], trapped by what once was, but unable to bridge the gap between us. "
    hide ib badending
    hide kg bad ending
    "The silence spoke louder than words, and we both walked away, unable to reconnect or find closure."

    "{b}Bad ending{/b}"
    return



### KG ver. ###

label Ch1_S1_T0_KG:
    scene bg building_220:
        zoom 1.2

    "It was a breezy day. I didn't know at the time that this semester would be a bit more special."

    p "The semester is starting soon! I can't believe I have to go back to school already!"

    p "Hmm, but I have some time to kill... "
    
    p "Maybe I'll hang out at the 220 lounge and chat with some friends."

    scene bg lounge_220:
        zoom 4.5
    with dissolve

    "I arrive at the lounge and see my friends talking. "
    "I walk over, put my hand on someone's shoulder, and start talking."

    p "Hey! What were you guys talking about?"

    ib "Huh?"

    p "Huh? Who... are you?"

    "That was my first meeting with him."

    p "Oh!! I'm so sorry!!"

    f1 "Haha, introduce yourself. He's an exchange student who just joined the College of Liberal Studies today."

    ib "Hi, I'm [ib]. I'm an exchange student from Christ University in India, now studying at SNU's College of Liberal Studies."

    p "Oh, nice to meet you!! I'm [p]. I heard an SNU student went to India, and now we have an exchange student here, too!"

    p "Anyway, if you need help with anything, feel free to ask! "
    
    p "Oh, wait, I don't have your number yet! What's your number?"

    ib "My number is ~~!"

    p "Great, thanks!"

    "(Growling sound)"

    p "(Quickly changing the subject) Uh, did you have lunch yet? Haha"

    f1 "Haha, we were just about to grab something. Let's go together!"

    ib "Sounds good!"

    "We headed to the cafeteria together..."
    scene bg snu_cafeteria:
        zoom 1.4
    with dissolve

    f1 "Oh, shoot! I forgot I had an assignment due! You two go ahead and eat! I'll see you later!"

    "Being left awkwardly alone... Well, let's go eat."

    jump Ch1_S2_T0_KG

label Ch1_S2_T0_KG:

    "We arrive at the cafeteria, and today's menu is bibimbap. We each grab a bowl and sit down."

    p "This must be your first time at the cafeteria, right? This is SNU's cafeteria!"

    p "This is bibimbap, a Korean dish where you mix rice with various vegetables and gochujang (Korean chili paste)!"

    ib "Oh!! It looks delicious!! I've never had bibimbap before!"

    p "Let me mix it for you!"

    "I put all my effort into mixing it."

    "But I get so into it that I accidentally bump into someone's arm, causing the spoon to fling a grain of rice onto their face."

    "What would you do?"

    "(Tutorial) This game requires you to make choices at key moments! Depending on your choices, the relationship level can increase or decrease. The final ending will be different based on your decisions, so choose carefully!"

    menu:

        "What would you do?"

        "1. Quickly dash to grab a tissue.":
            $ affection += 5
            jump Ch1_S3_T1_KG

        "2. Apologize to [ib] in embarrassment.":
            $ affection += 1
            jump Ch1_S3_T2_KG

        "3. Apologize to the person you bumped into first.":
            $ affection += -5
            jump Ch1_S3_T3_KG

label Ch1_S3_T1_KG:
    jump Ch1_S4_T0_KG

label Ch1_S3_T2_KG:
    jump Ch1_S4_T0_KG

label Ch1_S3_T3_KG:
    jump Ch1_S4_T0_KG

label Ch1_S4_T0_KG:

    ib "Haha, it's okay. I have a handkerchief. You got some rice on your face."

    "He wipes my face with his handkerchief and tidies up the area."

    "Suddenly, I feel a bit embarrassed, and my face turns slightly red."

    ib "This bibimbap is really good! The flavors are mild, and it goes well with the gochujang!"

    p "Really? I'm glad you like it, haha. By the way, are you busy these days? Have you explored Seoul much?"

    ib "Huh? No, I haven't really had the chance to see much outside the campus... "
    
    ib "Do you have time tomorrow? Maybe you could show me around Seoul?"

    p "Yeah, I'm free tomorrow! Let's meet up after class! I'll text you!"

    ib "Sounds good. See you tomorrow then!"

    jump Ch2_S1_T0_KG

label Ch2_S1_T0_KG:

    "_Chatting app_"

    ib "[player_name], do you often go to Seol-ip?"

    p "Yeah, I go often."

    ib "Then will you go with me? I've never been there before, so I'm curious.."

    p "Okay, I'll show you around."

    scene bg seolip:
        zoom 1.2

    "The next day, the two met in Seol-ip."

    ib "Wow! there are a lot of people."

    p "Ta-da! Students from our school usually come here to hang out."

    ib "Then what kind of food do you usually eat? I want to eat dessert."

    p "There's a cafe nearby that I often go to. Do you want to go and have some shaved ice?"
    
    menu:
        "What should I say to [ib] who's visiting Seol-ip for the first time?"

        "1. I'll buy it for you as a souvenir of your first visit to Seol-ip!":
            $ affection += 5

        "2. You know we split the bill, right? Haha..":
            $ affection += -2

        "3. You'll pay instead~~! I'll eat well ^^":
            $ affection += -5
    ib "Phew, I'm full. The shaved ice here is really delicious."

    p " I'm glad you enjoyed it."
    
    
    ib "Huh? It's a karaoke! I wanted to go to a karaoke, haha."

    p "Really? Then let's go in now."

    scene bg karaoke:
        zoom 2.8
    with dissolve

    p "You can pay for the time you want, and select the song you want to sing with the remote control. Here, the mic."

    ib "Thank you. You're so kind TT. I'll sing first!"

    "I am confident in my singing skills, so I sing my favorite song with great enthusiasm."
    "I look to the side while singing and see the other person staring at me."
    "I was a little nervous about the other person until the song ended."

    ib "Wow, you sing really well!"

    p "Haha, no. Now sing too."

    "The other person chose a duet song that is famous for being romantic."
    "Blah blah~"

    "Which of the following actions should I choose?"

    menu:

        "Which of the following actions should I choose?"

        "1. Sing along to the duet song.":
            ## Affection level increases.
            $ affection += 5
            jump Ch2_S2_T1_KG

        "2. Stay still.":
            ## Affection level decreases.
            $ affection -= 5
            jump Ch2_S2_T2_KG

        "3. Pick up a tambourine and dance like crazy.":
            ## Affection level increases slightly.
            $ affection += 2
            jump Ch2_S2_T3_KG

label Ch2_S2_T1_KG:

    jump Ch2_S3_T0_KG

label Ch2_S2_T2_KG:

    jump Ch2_S3_T0_KG

label Ch2_S2_T3_KG:

    jump Ch2_S3_T0_KG

label Ch2_S3_T0_KG:

    p "Phew, I had fun. Where should we go now... Is there a place you want to go?"

    ib "Um... Actually, I wanted to see the palaces of Korea."

    p "Really? Then do you want to go to Gyeongbokgung Palace together?"

    ib "Okay, fine."

    scene bg gyunbok:
        zoom 2.8
    with dissolve

    "We two take a bus and arrive at Gyeongbokgung Palace."

    "There are many people walking around the palace wearing hanbok."

    ib "What are those clothes?"

    p "That's a traditional Korean costume called hanbok. Hanbok is a costume that our people have worn since ancient times, "
    
    p "and it has changed over time based on the basics of a skirt, jeogori, and pants. "
    
    p "Today's hanbok follows the style that was popular during the Joseon Dynasty, "
    
    p "and modernized hanbok, which is designed to be worn in everyday life, is also popular. "
    
    p "You can rent a hanbok nearby. Shall we try it on together?"

    ib "Okay, let's do that!"

    "The two change into hanbok."

    p "Now let's take a look around Gyeongbokgung Palace."

    gd "Gyeongbokgung Palace is the first palace built when Joseon was founded and Hanyang (present-day Seoul) became the capital. "
 
    gd "It was used for banquets and receptions by the king and his subjects, as well as for receiving envoys, "
 
    gd "by building a large pond and a grand pavilion. "
 
    gd "Although many buildings were destroyed during the war and colonial period, "
 
    gd "restoration work has been steadily carried out to this day. "

    gd "It is a symbolic palace of the Joseon Dynasty that still maintains its original location since its founding."

    "The two leisurely stroll through Geunjeongjeon and Gyeonghoeru, enjoying the tranquil atmosphere of Gyeongbokgung Palace."

    p "I think we've seen all the palaces. How was it?"

    ib "It was really beautiful! The color arrangement and elaborate design were really impressive. "
    ib "It was touching to be able to experience Korean history and tradition in person while wearing hanbok. "
    ib "It felt like a harmony of tradition and modernity, considering that there is a palace like this in the middle of Seoul."

    p "I'm glad it was a good experience haha. Next, I'll introduce you to the famous traditional market in this area."

    ib "Right!"

    ib "Oh, it's cold."

    scene bg gyunbok_raining:
        zoom 1.8

    p "Huh? It's raining."

    "_Shooting, swoosh, the sound of rain falling_"

    p "Do you have an umbrella? I only have one for myself…"

    ib "No. It seems like Korea gets a lot of rain showers."

    p "Let's go under the eaves and wait for it to stop."

    "The two moved under the skirts to take shelter from the rain for a while, but the rain showed no sign of stopping."

    p "Hmm, the rain won't stop. We have to get to the market on time, but..."

    "How should I respond to an unexpected downpour?"

    menu:

        "How should I respond to an unexpected downpour?"

        "1. Go to a nearby convenience store and buy an umbrella each.":
            $ affection += -2
            ## Slightly decrease in favorability
            jump Ch2_S4_T1_KG

        "2. Share an umbrella and run to the market.":
            ## Affection level goes up significantly
            $ affection += 5
            jump Ch2_S4_T2_KG

        "3. Suggest that we both just go while getting rained on.":
            ## Affection level goes down significantly
            $ affection += -5
            jump Ch2_S4_T3_KG

label Ch2_S4_T1_KG:
    
    jump Ch2_S5_T0_KG

label Ch2_S4_T2_KG:

    jump Ch2_S5_T0_KG

label Ch2_S4_T3_KG:

    jump Ch2_S5_T0_KG

label Ch2_S5_T0_KG:

    scene bg kmarket:
        zoom 1.7

    "After many twists and turns, the two arrive at Gwangjang Market."

    p "Okay, this is Gwangjang Market."

    ib "It's bigger and more crowded than I thought."

    p "That's right. Gwangjang Market is the largest and oldest traditional market in Korea. "
    p "There are various food alleys in Gwangjang Market, hanbok stores where you can buy daily necessities, and second-hand stores."

    ib "Right. Let's eat something since we're hungry."

    "I look around and see various foods. What kind of food should I recommend that the opponent like?"

    menu:
        "1. Tteokbokki ":
            ## Affinity increase
            $ affection += 3
            jump Ch2_S6_T1_KG

        "2. Bindaetteok":
            ## Affinity maintained
            $ affection += 3
            jump Ch2_S6_T2_KG

        "3. Janchi noodles":
            $ affection += 3
            jump Ch2_S6_T3_KG

label Ch2_S6_T1_KG:

    jump Ch2_S7_T0_KG

label Ch2_S6_T2_KG:

    jump Ch2_S7_T0_KG

label Ch2_S6_T3_KG:

    jump Ch2_S7_T0_KG

label Ch2_S7_T0_KG:

    p "This is bindae-tteok, a specialty of Gwangjang Market. "
    p "It is a dish made by mixing vegetables or meat into a dough made from ground soybeans and frying it."

    p "This noodle is called janchi-guksu. "
    p "It originated from the fact that it was enjoyed at weddings, birthday parties, and 60th birthday parties in the hopes of longevity."

    ib "Oh, I love it!"

    "Then they enjoy the food with a happy conversation."

    jump Ch3_S1_T0_KG



label Ch3_S1_T0_KG:

    p "How about we try dating somewhere new?"

    ib "Sounds good! Where should we go?"

    p "Is there anything you'd like to try?"

    ib "Hmm... Could we maybe go to a famous festival in Korea?"

    p "Of course! How about we go to the largest music and water-themed festival in the country? It combines performances from various genres like K-POP, hip-hop, EDM, and large-scale water fights! The name of the festival is **'Waterbomb'**"

    ib "Great! I really want to go there!!"

    p "That's right!! My darling! Then shall we go to Waterbomb?"

    scene bg waterbomb:
        zoom 1.2

    "_Enjoy Waterbomb_"

    ib "Wow! This is really fun!!"

    "During the water gun play, [ib] became the target of many people."

    p "[ib] got targeted by many people during the water gun play, but they don't seem to realize it yet."

    menu:
        "1. I'll surprise them by spraying them with a water gun too, since it's so fun!":
            $ affection += 3
            jump Ch3_S2_T1_KG

        "2. I'm my partner's bodyguard! I'll shield them with my own body.":
            $ affection += 5
            jump Ch3_S2_T2_KG

        "3. I'll just give them a quick heads up in English.":
            $ affection += -4
            jump Ch3_S2_T3_KG

label Ch3_S2_T1_KG:
    jump Ch3_S3_T0_KG

label Ch3_S2_T2_KG:
    jump Ch3_S3_T0_KG

label Ch3_S2_T3_KG:
    jump Ch3_S3_T0_KG

label Ch3_S3_T0_KG:

    p "Are you okay?"

    ib "Yes, I'm fine."

    p "How was it?"

    ib "This was so much fun!!"

    p "Great! Then let's go watch the performances now? We can buy some beers too!"

    #Performance photos attached

    ib "It was so much fun!! I especially enjoyed seeing the K-pop singers. I love music!"

    p "Oh really? Then should we go to Hongdae next time?"

    ib "Why Hongdae? Is it famous for music?"

    p "Many musicians do street performances in Hongdae!"
    
    "I saw busking in Hongdae with [ib]"

    ib "This is so enjoyable~"

    "[ib] suddenly got a text message."

    ib "Oh no..."

    p "What's wrong? You don't look good."

    ib "I think I need to go back to India now."

    p "What? Didn't you have half a year left?"

    ib "I loved Korea and you so much that I extended my exchange student program for another semester, but I just got a message saying my application was rejected."

    p "What? I'm so disappointed... I'm tearing up..."

    ib "Oh honey, don't cry... I'm really disappointed too.."

    p "Choose the right sentence to comfort the other person:"

    menu:
        "1. I suppose so. I'm really sorry.":
            $ affection += -2
            jump Ch3_S4_T1_KG

        "2. We were never meant to be together for long anyway.":
            $ affection += -5
            jump Ch3_S4_T2_KG

        "3. No, don't say that! Everything will be alright, don't worry my dear.":
            $ affection += 5
            jump Ch3_S4_T3_KG

label Ch3_S4_T1_KG:
    jump Ch3_S5_T0_KG

label Ch3_S4_T2_KG:
    jump Ch3_S5_T0_KG

label Ch3_S4_T3_KG:
    jump Ch3_S5_T0_KG

label Ch3_S5_T0_KG:

    scene bg kairport:
        zoom 1.2

    "_at the airport_"

    p "I wish we could meet again soon."

    ib "Be happy even after you go back."

    p "I prepared a gift for you. This is a traditional Korean costume, do you remember the name of it?"

    ib "Of course!! It's Hanbok!"

    p "You remembered it well, didn't you?"

    ib "Of course! It's the gift you gave me!"

    p "Don't forget me when you go back to India."

    ib "Of course not. We're under the same sky. Our love will be eternal."

    jump Ch4_S1_T0_KG

label Ch4_S1_T0_KG:
    scene bg kstreet

    "It's already been two months since he suddenly left. Even though he's not here, time keeps moving forward."

    "Before I met him, I had applied for the exchange student program at Christ University in India, and now I've been accepted and am about to depart. "
    
    "Will I be able to meet him again if I go to the school he attends?"

    p "Should I text him to say I'll be at Christ University starting next week?"

    menu:
        "Send the text":
            $ affection += 5
            jump Ch4_S1_T1_KG

        "Don't send the text":
            $ affection += -5
            jump Ch4_S1_T2_KG

label Ch4_S1_T1_KG:
    "I thought I was the only one missing him, but he felt the same way. He is coming to our school as an exchange student. I can't believe it."
    jump Ch4_S2_T0_KG

label Ch4_S1_T2_KG:
    "I shouldn't hold on to past relationships. Reading this email will only make me miss him more. I won't read it."
    jump Ch4_S2_T0_KG

label Ch4_S2_T0_KG:

    scene bg india_airport
    "He didn't reply. I've arrived in India. It's a lively city."

    scene bg tajmahal
    "Before heading to Bangalore, I decided to visit the Taj Mahal alone. He once told me that if I ever came to India, he would show me the Taj Mahal."

    #A: 
    m1 "Take a photo! I'll take it with the Taj Mahal in the background!"

    #B:
    m2 "Don't go to him, I'll take your photo for a cheaper price."

    p "Trying to avoid the touting photographers, I joined a guided tour group."

    gd "The Taj Mahal was built by the fifth Mughal Emperor, Shah Jahan. He loved his wife dearly, and after she passed away, he built the Taj Mahal in her memory." 
    
    gd "He wanted to give her a perfect architectural gift, which is why it took 22 years to complete."

    #(Narration)
    p "The Taj Mahal has such a romantic history."

    ib "Hey! [p]!"

    #(Narration)
    p "No way! Why is he here?"

    ib "I got your text and thought you might be here around this time, so I came."

    #(Narration)
    p "No way... I can't believe he's here."

    ib "Do you like the Taj Mahal?"

    p "I'm glad I came here!"

    menu:
        "This place is such a beautiful palace.":
            $ affection += -3
            jump Ch4_S3_T1_KG

        "This place is such a beautiful tomb.":
            $ affection += 5
            jump Ch4_S3_T2_KG

        "This place is such a beautiful government building.":
            $ affection += -5
            jump Ch4_S3_T3_KG

label Ch4_S3_T1_KG:
    jump Ch4_S4_T0_KG

label Ch4_S3_T2_KG:
    jump Ch4_S4_T0_KG

label Ch4_S3_T3_KG:
    jump Ch4_S4_T0_KG

label Ch4_S4_T0_KG:

    ib "I'm glad you like it. Have you had lunch yet?"

    p "Not yet!"

    ib "Then let's try some Indian street food. I'll guide you."

    #(Narration)
    scene bg india_street
    "We walk the streets of India together. In the exotic scenery."

    ib "This is Paratha. Paratha is a flatbread made by rolling out dough and stuffing it with potatoes or beans. It's eaten with butter or yogurt."

    p "Oh, interesting."

    ib "This is Chaat. It's made with potatoes, beans, yogurt, various sauces, and spices."

    ib "That's Aloo Tikki. It's a potato patty that's fried and served with sauces. The crispy potato patty with spices gives it a unique taste."

    p "It smells exotic and delicious."

    ib "Which one do you want to try?"

    menu:

        "Which one do you want to try?"

        "I want to try Paratha!":
            $ affection += 3
            jump Ch4_S5_T1_KG

        "I want to try Chaat!":
            $ affection += 3
            jump Ch4_S5_T2_KG

        "I want to try Aloo Tikki!":
            $ affection += 3
            jump Ch4_S5_T3_KG

        "I don't think I'll like any of them.":
            $ affection += -5
            jump Ch4_S5_T4_KG

label Ch4_S5_T1_KG:
    jump Ch4_S6_T0_KG

label Ch4_S5_T2_KG:
    jump Ch4_S6_T0_KG

label Ch4_S5_T3_KG:
    jump Ch4_S6_T0_KG

label Ch4_S5_T4_KG:
    jump Ch4_S6_T0_KG

label Ch4_S6_T0_KG:

    ib "Are you going to Christ University today? Let's go together."

    #(Narration)
    "I'm so happy to meet him again. Is this how our connection resumes?"

    menu:
        "Sure!":
            $ affection += 3
            jump Ch4_S7_T1_KG

        "I want to go alone.":
            $ affection += -3
            jump Ch4_S7_T2_KG

label Ch4_S7_T1_KG:
    jump Ch4_S8_T0_KG

label Ch4_S7_T2_KG:
    jump Ch4_S8_T0_KG

label Ch4_S8_T0_KG:

    scene bg india_train

    #(Narration)
    "After exploring Delhi and Agra, it was time to continue our journey to Bangalore."
    
    p "I was excited and a little nervous about the long train ride. It's going to be a unique way to see more of India."

    p "I've heard that train journeys in India are quite an experience. I'm excited but also a bit nervous. How long will the journey take?"

    ib "It'll take around 36 to 40 hours, depending on the train. But trust me, it's going to be an unforgettable experience. "
    
    ib "You'll get to see so much of India, from the bustling cities to the peaceful countryside."

    p "I can't wait! What should we expect during the journey?"

    menu:
        "Encourage I to tell me more about the diversity of regions and cultures in India.":
            $ affection += 7
            jump Ch4_S9_T1_KG

        "Ask about the history and significance of Indian Railways.":
            $ affection += 4
            jump Ch4_S9_T2_KG

        "Inquire about the food available on the train.":
            $ affection += 1
            jump Ch4_S9_T3_KG

        "Suggest we rest or read to pass the time during the journey.":
            $ affection += -5
            jump Ch4_S9_T4_KG

label Ch4_S9_T1_KG:
    jump Ch4_S10_T0_KG

label Ch4_S9_T2_KG:
    jump Ch4_S10_T0_KG

label Ch4_S9_T3_KG:
    jump Ch4_S10_T0_KG

label Ch4_S9_T4_KG:
    jump Ch4_S10_T0_KG

label Ch4_S10_T0_KG:

    scene bg bangalore:
        zoom 1.1
    "After a long journey, we finally arrived in Bangalore. The city felt alive with energy, and the weather was so pleasant."
    "I could see why it's such a popular place."

    p "Bangalore seems so lively! I've heard it's known as the Silicon Valley of India."

    ib "That's right. Bangalore is a major hub for technology and startups, but it's also known for its parks, historic sites, and diverse culture."

    p "I'm excited to explore it. What should we do first?"

    menu:
        "Propose heading straight to the hotel to rest.":
            $ affection += -5
            jump Ch4_S11_T4_KG
            
        "Express interest in exploring the historic parts of Bangalore.":
            $ affection += 7
            jump Ch4_S11_T1_KG

        "Show enthusiasm for visiting the local parks and gardens.":
            $ affection += 4
            jump Ch4_S11_T2_KG

        "Suggest exploring the local markets.":
            $ affection += 0
            jump Ch4_S11_T3_KG


label Ch4_S11_T1_KG:
    jump Ch4_S12_T0_KG

label Ch4_S11_T2_KG:
    jump Ch4_S12_T0_KG

label Ch4_S11_T3_KG:
    jump Ch4_S12_T0_KG

label Ch4_S11_T4_KG:
    jump Ch4_S12_T0_KG

label Ch4_S12_T0_KG:

    scene bg theatre:
        zoom 1.3

    #(Narration)
    "After settling in, [ib] suggested we experience something truly unique—watching an Indian movie at a local theatre."
    "I'd heard a lot about Indian cinema, and I was eager to see it for myself."

    p "I've heard so much about Indian cinema. Bollywood, right?"

    ib "Yes, but there's so much more to Indian cinema than just Bollywood. "
    
    ib "Each region has its own film industry—Kollywood in Tamil Nadu, Tollywood in Andhra Pradesh, and Sandalwood right here in Karnataka." 
    
    ib "Indian cinema has a rich history, and it's evolved a lot over the years."

    menu:
        "Suggest watching the movie quietly without much discussion.":
            $ affection += -5
            jump Ch4_S13_T4_KG

        "Inquire about the global influence of Indian cinema.":
            $ affection += 4
            jump Ch4_S13_T2_KG

        "Express curiosity about different film genres.":
            $ affection += 1
            jump Ch4_S13_T3_KG
        "Ask about the history and evolution of Indian cinema.":
            $ affection += 7
            jump Ch4_S13_T1_KG

label Ch4_S13_T1_KG:
    jump Ch4_S14_T0_KG

label Ch4_S13_T2_KG:
    jump Ch4_S14_T0_KG

label Ch4_S13_T3_KG:
    jump Ch4_S14_T0_KG

label Ch4_S13_T4_KG:
    jump Ch4_S14_T0_KG

label Ch4_S14_T0_KG:

    
    "The theatre was buzzing with excitement. The air was filled with the scent of popcorn, and I could feel the anticipation in the audience. "
    "As the movie began, I was completely drawn in by the vibrant colors, music, and emotions on screen."

    p "That was incredible! The energy, the colors, the music—it's so different from what I'm used to, but I loved it."

    ib "I'm glad you enjoyed it. Indian cinema is all about making you feel deeply, whether it's joy, sorrow, or excitement."

    p "I can't wait to watch more. Thank you for introducing me to this part of your culture."

    #(Narration)
    "As we left the theatre, I felt even closer to [ib]. Sharing these experiences together has deepened our bond, and I'm excited to see where our journey takes us next."

    jump Ch5_S1_T0_KG    

label Ch5_S1_T0_KG:
    if affection >= 40:
        jump Ch5_S1_T1_KG
    elif affection >= 20:
        jump Ch5_S1_T2_KG
    else:
        jump Ch5_S1_T3_KG

label Ch5_S1_T1_KG:
    scene bg christ_dorm
    "After parting ways with [ib], I returned to my dormitory, trying to focus on my exams."

    ib "We're both busy, so let's concentrate on studying."

    p "Yeah, let's do that."

    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."

    p "When did [ib]'s exchange program end again?"

    "I found myself at [ib]'s dormitory. Seeing the empty room, I wondered if I would regret this day."

    "We were so happy together, but perhaps it was beautiful because it's now the past. But still... (reflects briefly). Will I meet someone like [ib] again?"
    "Realizing today was [ib]'s departure, I called a taxi and headed to the airport."

    scene bg india_airport
    
    p "It was today! I still wanted to say goodbye..."

    "At the airport, I found the counter for flights to India and waited. Noticing missed calls, I called back."

    p "Are you at the airport? I saw the letter you left!"

    "Even now, [ib] was the best person I'd met. So kind and together often. I don't think I'll meet someone like [ib] again."

    ib "Yeah... but I don't want to go. I couldn't say it then, but I realize I need you."

    p "Smiles silently."

    "We persuaded our parents, got back together, and continued our relationship between Korea and India."

    scene bg wedding:
        zoom 1.4
    
    "The bride is ready to enter!"

    p "Today is the happiest day of my life!!"

    ib "Me too, hehe."

    p "Ready for the party? It's going to go late into the night!!"

    "As we entered the hall, I remembered when I first met [ib]. If I hadn't met [ib], what would have happened? This beautiful story of mine will continue forever."
    "{b}Happy Ending{/b}"
    
    return

label Ch5_S1_T2_KG:
    scene bg christ_dorm

    "After parting ways with [ib], I returned to my dormitory, trying to focus on my exams."

    ib "We're both busy, so let's concentrate on studying."

    p "Yeah, let's do that."

    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."

    p "When does [ib]'s exchange program end?"

    "I found myself standing outside [ib]'s empty dormitory, wondering if I'd regret letting go."

    "We had some wonderful times together, perhaps more beautiful now as memories. I wondered if I'd meet anyone like [ib] again."
    "Realizing today was [ib]'s departure, I impulsively headed to the airport."

    p "Today's the day! I still wanted to say goodbye..."

    scene bg india_airport
    "At the airport, I looked for flights to India and decided to wait. I saw missed calls and dialed back."

    p "Are you at the airport? I saw your letter at the dorm!"

    "Reflecting on the past, [ib] was one of the kindest people I'd met. Though we parted ways, those memories stayed with me."

    scene bg foreign_street
    "As time passed, life moved on."
    "Years later, I joined a reunion trip for the exchange program. "
    "Among familiar faces, I saw [ib] again."

    ib "It's been a long time!"

    p "It really has. How have you been?"

    "We shared stories and laughter, reconnecting as friends."
    "Those moments we shared were a cherished chapter, and seeing [ib] again felt like a new beginning, in a different way."
    "{b}Normal Ending{/b}"
    return

label Ch5_S1_T3_KG:
    scene bg christ_dorm

    "After parting ways with [ib], I returned to my dormitory, trying to focus on my exams."

    ib "We're both busy, so let's concentrate on studying."

    p "Yeah, let's do that."

    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."

    p "When does [ib]'s exchange program end?"

    "I found myself outside [ib]'s empty dormitory, wondering if I'd regret how things ended."

    "We had some wonderful times together, but they felt distant now. Our breakup was painful, leaving me with lingering doubts."
    "I knew today was [ib]'s departure, but I couldn't bring myself to go to the airport."

    p "I should have gone... but I just couldn't face it."

    scene bg foreign_street

    "Time passed, and life moved on. "
    "Years later, I was on a business trip and unexpectedly saw [ib] again."

    "In a crowded conference room, our eyes met briefly. An awkward silence stretched between us, heavy with unspoken words."

    "I tried to focus on my work, but my thoughts kept drifting back to [ib]. Memories of our time together resurfaced, mingling with the bitterness of our breakup."

    p "I wish things had ended differently."

    "We passed each other in the hallway, pretending not to notice, but the weight of our shared history was palpable."

    "All I could do was think about [ib], trapped by what once was, but unable to bridge the gap between us. The silence spoke louder than words, and we both walked away, unable to reconnect or find closure."
    "{b}Bad ending{/b}"
    return

### KB ver. ###

label Ch1_S1_T0_KB:
    scene bg building_220:
        zoom 1.2

    "It was a breezy day. I didn't know at the time that this semester would be a bit more special."

    p "The semester is starting soon! I can't believe I have to go back to school already!"

    p "Hmm, but I have some time to kill... Maybe I'll hang out at the 220 lounge and chat with some friends."

    scene bg lounge_220:
        zoom 4.5
    with dissolve
    
    "I arrive at the lounge and see my friends talking. I walk over, put my hand on someone's shoulder, and start talking."

    p "Hey! What were you guys talking about?"

    ig "Huh?"

    p "Huh? Who... are you?"

    "That was my first meeting with her."

    p "Oh!! I'm so sorry!!"

    f1 "Haha, introduce yourself. She's an exchange student who just joined the College of Liberal Studies today."

    ig "Hi, I'm [ig]. I'm an exchange student from Christ University in India, now studying at SNU's College of Liberal Studies."

    p "Oh, nice to meet you!! I'm [p]. I heard an SNU student went to India, and now we have an exchange student here, too!"

    p "Anyway, if you need help with anything, feel free to ask! Oh, wait, I don't have your number yet! What's your number?"

    ig "My number is ~~!"

    p "Great, thanks!"

    "(Growling sound)"

    p "(Quickly changing the subject) Uh, did you have lunch yet? Haha"

    f1 "Haha, we were just about to grab something. Let's go together!"

    ig "Sounds good!"

    "We headed to the cafeteria together..."

    scene bg snu_cafeteria:
        zoom 1.4
    with dissolve

    f1 "Oh, shoot! I forgot I had an assignment due! You two go ahead and eat! I'll see you later!"

    "Being left awkwardly alone... Well, let's go eat."

    jump Ch1_S2_T0_KB

label Ch1_S2_T0_KB:

    "Cafeteria"

    "We arrive at the cafeteria, and today's menu is bibimbap. We each grab a bowl and sit down."

    p "This must be your first time at the cafeteria, right? This is SNU's cafeteria!"

    p "This is bibimbap, a Korean dish where you mix rice with various vegetables and gochujang (Korean chili paste)!"

    ig "Oh!! It looks delicious!! I've never had bibimbap before!"

    p "Let me mix it for you!"

    "I put all my effort into mixing it."

    "But I get so into it that I accidentally bump into someone's arm, causing the spoon to fling a grain of rice onto their face."

    "What would you do?"

    "(Tutorial) This game requires you to make choices at key moments! Depending on your choices, the relationship level can increase or decrease. The final ending will be different based on your decisions, so choose carefully!"

    menu:
        "1. Quickly dash to grab a tissue.":
            $ affection += 5
            jump Ch1_S3_T1_KB

        "2. Apologize to [ig] in embarrassment.":
            $ affection += 1
            jump Ch1_S3_T2_KB

        "3. Apologize to the person you bumped into first.":
            $ affection += -5
            jump Ch1_S3_T3_KB

label Ch1_S3_T1_KB:
    jump Ch1_S4_T0_KB

label Ch1_S3_T2_KB:
    jump Ch1_S4_T0_KB

label Ch1_S3_T3_KB:
    jump Ch1_S4_T0_KB

label Ch1_S4_T0_KB:

    ig "Haha, it's okay. I have a handkerchief. You got some rice on your face."

    "She wipes my face with her handkerchief and tidies up the area."

    "Suddenly, I feel a bit embarrassed, and my face turns slightly red."

    ig "This bibimbap is really good! The flavors are mild, and it goes well with the gochujang!"

    p "Really? I'm glad you like it, haha. By the way, are you busy these days? Have you explored Seoul much?"

    ig "Huh? No, I haven't really had the chance to see much outside the campus... Do you have time tomorrow? Maybe you could show me around Seoul?"

    p "Yeah, I'm free tomorrow! Let's meet up after class! I'll text you!"

    ig "Sounds good. See you tomorrow then!"

    jump Ch2_S1_T0_KB


label Ch2_S1_T0_KB:

    "_Chatting app_"

    ig "[player_name], do you often go to Seol-ip?"

    p "Yeah, I go often."

    ig "Then will you go with me? I've never been there before, so I'm curious.."

    p "Okay, I'll show you around."

    scene bg seolip:
        zoom 1.2

    "The next day. the two met in Seol-ip."

    ig "Wow, there are a lot of people."

    p "Ta-da! Students from our school usually come here to hang out."

    ig "Then what kind of food do you usually eat? I want to eat dessert."

    p "There's a cafe nearby that I often go to. Do you want to go and have some shaved ice?"

    "What should I say to the opponent who's visiting Seol-ip for the first time?"
    menu:
        "1. I'll buy it for you as a souvenir of your first visit to Seol-ip!":
            $ affection += 5

        "2. You know we split the bill, right? Haha..":
            $ affection += -2

        "3. You'll pay instead~~! I'll eat well ^^":
            $ affection += -5
            
    ig "Phew, I'm full. The shaved ice here is really delicious."

    p " I'm glad you enjoyed it."

    ig "Huh? It's a karaoke! I wanted to go to a karaoke, haha."

    p "Really? Then let's go in now."

    scene bg karaoke:
        zoom 2.8
    with dissolve

    p "You can pay for the time you want, and select the song you want to sing with the remote control. Here, the mic."

    ig "Thank you. You're so kind TT. I'll sing first!"

    "I am confident in my singing skills, so I sing my favorite song with great enthusiasm."
    "I look to the side while singing and see the other person staring at me."
    "I was a little nervous about the other person until the song ended."

    ig "Wow, you sing really well!"

    p "Haha, no. Now sing too."

    "The other person chose a duet song that is famous for being romantic."
    "Blah blah~"

    "Which of the following actions should I choose?"

    menu:

        "Which of the following actions should I choose?"

        "1. Sing along to the duet song.":
            $ affection += 5
            jump Ch2_S2_T1_KB

        "2. Stay still.":
            $ affection += -5
            jump Ch2_S2_T2_KB

        "3. Pick up a tambourine and dance like crazy.":
            $ affection += 2
            jump Ch2_S2_T3_KB

label Ch2_S2_T1_KB:

    jump Ch2_S3_T0_KB

label Ch2_S2_T2_KB:

    jump Ch2_S3_T0_KB

label Ch2_S2_T3_KB:

    jump Ch2_S3_T0_KB

label Ch2_S3_T0_KB:

    p "Phew, I had fun. Where should we go now... Is there a place you want to go?"

    ig "Um... Actually, I wanted to see the palaces of Korea."

    p "Really? Then do you want to go to Gyeongbokgung Palace together?"

    ig "Okay, fine."

    scene bg gyunbok:
        zoom 2.8
    with dissolve

    "The two take a bus and arrive at Gyeongbokgung Palace."

    "There are many people walking around the palace wearing hanbok."

    ig "What are those clothes?"

    p "That's a traditional Korean costume called hanbok. Hanbok is a costume that our people have worn since ancient times, "
    
    p "and it has changed over time based on the basics of a skirt, jeogori, and pants. "
    
    p "Today's hanbok follows the style that was popular during the Joseon Dynasty, "
    
    p "and modernized hanbok, which is designed to be worn in everyday life, is also popular. "
    
    p "You can rent a hanbok nearby. Shall we try it on together?"

    ig "Okay, let's do that!"

    "The two change into hanbok."

    p "Now let's take a look around Gyeongbokgung Palace."

    gd "Gyeongbokgung Palace is the first palace built when Joseon was founded and Hanyang (present-day Seoul) became the capital. "
 
    gd "It was used for banquets and receptions by the king and his subjects, as well as for receiving envoys, "
 
    gd "by building a large pond and a grand pavilion. "
 
    gd "Although many buildings were destroyed during the war and colonial period, "
 
    gd "restoration work has been steadily carried out to this day. "

    gd "It is a symbolic palace of the Joseon Dynasty that still maintains its original location since its founding."

    "The two leisurely stroll through Geunjeongjeon and Gyeonghoeru, enjoying the tranquil atmosphere of Gyeongbokgung Palace."

    p "I think we've seen all the palaces. How was it?"

    ig "It was really beautiful! The color arrangement and elaborate design were really impressive. "
    ig "It was touching to be able to experience Korean history and tradition in person while wearing hanbok. "
    ig "It felt like a harmony of tradition and modernity, considering that there is a palace like this in the middle of Seoul."

    p "I'm glad it was a good experience haha. Next, I'll introduce you to the famous traditional market in this area."

    ig "Right!"

    ig "Oh, it's cold."

    scene bg gyunbok_raining:
        zoom 1.8

    p "Huh? It's raining."

    "(Shooting, swoosh, the sound of rain falling)"

    p "Do you have an umbrella? I only have one for myself…"

    ig "No. It seems like Korea gets a lot of rain showers."

    p "Let's go under the eaves and wait for it to stop."

    "The two moved under the skirts to take shelter from the rain for a while, but the rain showed no sign of stopping."

    p "Hmm, the rain won't stop. We have to get to the market on time, but..."

    "How should I respond to an unexpected downpour?"

    menu:
        "1. Go to a nearby convenience store and buy an umbrella each.":
            $ affection += -2
            jump Ch2_S4_T1_KB

        "2. Share an umbrella and run to the market.":
            $ affection += 5
            jump Ch2_S4_T2_KB

        "3. Suggest that we both just go while getting rained on.":
            $ affection += -5
            jump Ch2_S4_T3_KB

label Ch2_S4_T1_KB:
    
    jump Ch2_S5_T0_KB

label Ch2_S4_T2_KB:

    jump Ch2_S5_T0_KB

label Ch2_S4_T3_KB:

    jump Ch2_S5_T0_KB

label Ch2_S5_T0_KB:

    scene bg kmarket:
        zoom 1.7

    "After many twists and turns, the two arrive at Gwangjang Market."

    p "Okay, this is Gwangjang Market."

    ig "It's bigger and more crowded than I thought."

    p "That's right. Gwangjang Market is the largest and oldest traditional market in Korea. "
    p "There are various food alleys in Gwangjang Market, hanbok stores where you can buy daily necessities, and second-hand stores."

    ig "Right. Let's eat something since we're hungry."

    "I look around and see various foods. What kind of food should I recommend that the opponent like?"

    menu:
        "1. Tteokbokki ":
            ## Affinity increase
            $ affection += 3
            jump Ch2_S6_T1_KB

        "2. Bindaetteok":
            ## Affinity maintained
            $ affection += 3
            jump Ch2_S6_T2_KB

        "3. Janchi noodles":
            $ affection += 3
            jump Ch2_S6_T3_KB

label Ch2_S6_T1_KB:

    jump Ch2_S7_T0_KB

label Ch2_S6_T2_KB:

    jump Ch2_S7_T0_KB

label Ch2_S6_T3_KB:

    jump Ch2_S7_T0_KB

label Ch2_S7_T0_KB:

    p "This is bindae-tteok, a specialty of Gwangjang Market. "
    p "It is a dish made by mixing vegetables or meat into a dough made from ground soybeans and frying it."

    p "This noodle is called janchi-guksu. "
    p "It originated from the fact that it was enjoyed at weddings, birthday parties, and 60th birthday parties in the hopes of longevity."

    ig "The food here is really delicious."

    "Then they enjoy the food with a happy conversation."

    jump Ch3_S1_T0_KB


label Ch3_S1_T0_KB:

    p "How about we try dating somewhere new?"

    ig "Sounds good! Where should we go?"

    p "Is there anything you'd like to try?"

    ig "Hmm... Could we maybe go to a famous festival in Korea?"

    p "Of course! How about we go to the largest music and water-themed festival in the country? It combines performances from various genres like K-POP, hip-hop, EDM, and large-scale water fights! The name of the festival is **'Waterbomb'**"

    ig "Great! I really want to go there!!"

    p "That's right!! My darling! Then shall we go to Waterbomb?"

    scene bg waterbomb:
        zoom 1.2

    "_Enjoy Waterbomb_"

    ig "Wow! This is really fun!!"

    "During the water gun play, [ig] became the target of many people."

    p "[ig] got targeted by many people during the water gun play, but they don't seem to realize it yet."

    menu:
        "1. I'll surprise them by spraying them with a water gun too, since it's so fun!":
            $ affection += 3
            jump Ch3_S2_T1_KB

        "2. I'm my partner's bodyguard! I'll shield them with my own body.":
            $ affection += 5
            jump Ch3_S2_T2_KB

        "3. I'll just give them a quick heads up in English.":
            $ affection += -4
            jump Ch3_S2_T3_KB

label Ch3_S2_T1_KB:
    jump Ch3_S3_T0_KB

label Ch3_S2_T2_KB:
    jump Ch3_S3_T0_KB

label Ch3_S2_T3_KB:
    jump Ch3_S3_T0_KB

label Ch3_S3_T0_KB:

    p "Are you okay?"

    ig "Yes, I'm fine."

    p "How was it?"

    ig "This was so much fun!!"

    p "Great! Then let's go watch the performances now? We can buy some beers too!"

    #Performance photos attached

    ig "It was so much fun!! I especially enjoyed seeing the K-pop singers. I love music!"

    p "Oh really? Then should we go to Hongdae next time?"

    ig "Why Hongdae? Is it famous for music?"

    p "Many musicians do street performances in Hongdae!"
    
    "I saw busking in Hongdae with [ig]"

    ig "This is so enjoyable~"

    "[ig] suddenly got a text message."

    ig "Oh no..."

    p "What's wrong? You don't look good."

    ig "I think I need to go back to India now."

    p "What? Didn't you have half a year left?"

    ig "I loved Korea and you so much that I extended my exchange student program for another semester, but I just got a message saying my application was rejected."

    p "What? I'm so disappointed... I'm tearing up..."

    ig "Oh honey, don't cry... I'm really disappointed too.."

    p "Choose the right sentence to comfort the other person:"

    menu:
        "1. I suppose so. I'm really sorry.":
            $ affection += -2
            jump Ch3_S4_T1_KB

        "2. We were never meant to be together for long anyway.":
            $ affection += -5
            jump Ch3_S4_T2_KB

        "3. No, don't say that! Everything will be alright, don't worry my dear.":
            $ affection += 5
            jump Ch3_S4_T3_KB

label Ch3_S4_T1_KB:
    jump Ch3_S5_T0_KB

label Ch3_S4_T2_KB:
    jump Ch3_S5_T0_KB

label Ch3_S4_T3_KB:
    jump Ch3_S5_T0_KB

label Ch3_S5_T0_KB:

    scene bg kairport:
        zoom 1.2

    "_at the airport_"

    p "I wish we could meet again soon."

    ig "Be happy even after you go back."

    p "I prepared a gift for you. This is a traditional Korean costume, do you remember the name of it?"

    ig "Of course!! It's Hanbok!"

    p "You remembered it well, didn't you?"

    ig "Of course! It's the gift you gave me!"

    p "Don't forget me when you go back to India."

    ig "Of course not. We're under the same sky. Our love will be eternal."

    jump Ch4_S1_T0_KB


label Ch4_S1_T0_KB:
    scene bg kstreet

    "It's already been two months since she suddenly left. Even though she's not here, time keeps moving forward. "
    
    "Before I met her, I had applied for the exchange student program at Christ University in India, and now I've been accepted and am about to depart. "
    
    "Will I be able to meet her again if I go to the school she attends?"

    p "Should I text her to say I'll be at Christ University starting next week?"

    menu:
        "Send the text":
            $ affection += 5
            jump Ch4_S1_T1_KB

        "Don't send the text":
            $ affection += -5
            jump Ch4_S1_T2_KB

label Ch4_S1_T1_KB:
    "I thought I was the only one missing her, but she felt the same way. She is coming to our school as an exchange student. I can't believe it."
    jump Ch4_S2_T0_KB

label Ch4_S1_T2_KB:
    "I shouldn't hold on to past relationships. Reading this email will only make me miss her more. I won't read it."
    jump Ch4_S2_T0_KB

label Ch4_S2_T0_KB:
    scene bg india_airport

    "She didn't reply. I've arrived in India. It's a lively city."

    scene bg tajmahal
    "Before heading to Bangalore, I decided to visit the Taj Mahal alone. She once told me that if I ever came to India, she would show me the Taj Mahal."

    m1 "Take a photo! I'll take it with the Taj Mahal in the background!"

    m2 "Don't go to him, I'll take your photo for a cheaper price."

    p "Trying to avoid the touting photographers, I joined a guided tour group."

    gd "The Taj Mahal was built by the fifth Mughal Emperor, Shah Jahan. "
    
    gd "He loved his wife dearly, and after she passed away, he built the Taj Mahal in her memory." 
    
    gd "He wanted to give her a perfect architectural gift, which is why it took 22 years to complete."

    p "The Taj Mahal has such a romantic history."

    ig "Hey! [p]!"

    p "No way! Why is she here?"

    ig "I got your text and thought you might be here around this time, so I came."

    p "No way... I can't believe she's here."

    ig "Do you like the Taj Mahal?"

    p "I'm glad I came here!"

    menu:
        "This place is such a beautiful palace.":
            $ affection += -3
            jump Ch4_S3_T1_KB

        "This place is such a beautiful tomb.":
            $ affection += 5
            jump Ch4_S3_T2_KB

        "This place is such a beautiful government building.":
            $ affection += -5
            jump Ch4_S3_T3_KB

label Ch4_S3_T1_KB:
    jump Ch4_S4_T0_KB

label Ch4_S3_T2_KB:
    jump Ch4_S4_T0_KB

label Ch4_S3_T3_KB:
    jump Ch4_S4_T0_KB

label Ch4_S4_T0_KB:

    ig "I'm glad you like it. Have you had lunch yet?"

    p "Not yet!"

    ig "Then let's try some Indian street food. I'll guide you."

    scene bg india_street

    "We walk the streets of India together. In the exotic scenery."

    ig "This is Paratha. Paratha is a flatbread made by rolling out dough and stuffing it with potatoes or beans. It's eaten with butter or yogurt."

    p "Oh, interesting."

    ig "This is Chaat. It's made with potatoes, beans, yogurt, various sauces, and spices."

    ig "That's Aloo Tikki. It's a potato patty that's fried and served with sauces. The crispy potato patty with spices gives it a unique taste."

    p "It smells exotic and delicious."

    ig "Which one do you want to try?"

    menu:
        "I want to try Paratha!":
            $ affection += 3
            jump Ch4_S5_T1_KB

        "I want to try Chaat!":
            $ affection += 3
            jump Ch4_S5_T2_KB

        "I want to try Aloo Tikki!":
            $ affection += 3
            jump Ch4_S5_T3_KB

        "I don't think I'll like any of them.":
            $ affection += -5
            jump Ch4_S5_T4_KB

label Ch4_S5_T1_KB:
    jump Ch4_S6_T0_KB

label Ch4_S5_T2_KB:
    jump Ch4_S6_T0_KB

label Ch4_S5_T3_KB:
    jump Ch4_S6_T0_KB

label Ch4_S5_T4_KB:
    jump Ch4_S6_T0_KB

label Ch4_S6_T0_KB:

    ig "Are you going to Christ University today? Let's go together."

    p "I'm so happy to meet her again. Is this how our connection resumes?"

    menu:
        "Sure!":
            $ affection += 3
            jump Ch4_S7_T1_KB

        "I want to go alone.":
            $ affection += -3
            jump Ch4_S7_T2_KB

label Ch4_S7_T1_KB:
    jump Ch4_S8_T0_KB

label Ch4_S7_T2_KB:
    jump Ch4_S8_T0_KB

label Ch4_S8_T0_KB:

    scene bg india_train

    "After exploring Delhi and Agra, it was time to continue our journey to Bangalore. "
    
    p "I was excited and a little nervous about the long train ride. It's going to be a unique way to see more of India."

    p "I've heard that train journeys in India are quite an experience. I'm excited but also a bit nervous. How long will the journey take?"

    ig "It'll take around 36 to 40 hours, depending on the train. But trust me, it's going to be an unforgettable experience. "
    ig "You'll get to see so much of India, from the bustling cities to the peaceful countryside."

    p "I can't wait! What should we expect during the journey?"

    menu:
        "Encourage I to tell me more about the diversity of regions and cultures in India.":
            $ affection += 7
            jump Ch4_S9_T1_KB

        "Ask about the history and significance of Indian Railways.":
            $ affection += 4
            jump Ch4_S9_T2_KB

        "Inquire about the food available on the train.":
            $ affection += 1
            jump Ch4_S9_T3_KB

        "Suggest we rest or read to pass the time during the journey.":
            $ affection += -5
            jump Ch4_S9_T4_KB

label Ch4_S9_T1_KB:
    jump Ch4_S10_T0_KB

label Ch4_S9_T2_KB:
    jump Ch4_S10_T0_KB

label Ch4_S9_T3_KB:
    jump Ch4_S10_T0_KB

label Ch4_S9_T4_KB:
    jump Ch4_S10_T0_KB

label Ch4_S10_T0_KB:

    scene bg bangalore:
        zoom 1.1

    "After a long journey, we finally arrived in Bangalore. "
    "The city felt alive with energy, and the weather was so pleasant. I could see why it's such a popular place."

    p "Bangalore seems so lively! I've heard it's known as the Silicon Valley of India."

    ig "That's right. Bangalore is a major hub for technology and startups, but it's also known for its parks, historic sites, and diverse culture."

    p "I'm excited to explore it. What should we do first?"

    menu:
        "Propose heading straight to the hotel to rest.":
            $ affection += -5
            jump Ch4_S11_T4_KB
            
        "Express interest in exploring the historic parts of Bangalore.":
            $ affection += 7
            jump Ch4_S11_T1_KB

        "Show enthusiasm for visiting the local parks and gardens.":
            $ affection += 4
            jump Ch4_S11_T2_KB

        "Suggest exploring the local markets.":
            $ affection += 0
            jump Ch4_S11_T3_KB

label Ch4_S11_T1_KB:
    jump Ch4_S12_T0_KB

label Ch4_S11_T2_KB:
    jump Ch4_S12_T0_KB

label Ch4_S11_T3_KB:
    jump Ch4_S12_T0_KB

label Ch4_S11_T4_KB:
    jump Ch4_S12_T0_KB

label Ch4_S12_T0_KB:

    scene bg theatre:
        zoom 1.3

    "After settling in, [ig] suggested we experience something truly unique—watching an Indian movie at a local theatre. "
    "I'd heard a lot about Indian cinema, and I was eager to see it for myself."

    p "I've heard so much about Indian cinema. Bollywood, right?"

    ig "Yes, but there's so much more to Indian cinema than just Bollywood. "
    ig "Each region has its own film industry—Kollywood in Tamil Nadu, Tollywood in Andhra Pradesh, and Sandalwood right here in Karnataka. "
    ig "Indian cinema has a rich history, and it's evolved a lot over the years."

    menu:
        "Suggest watching the movie quietly without much discussion.":
            $ affection += -5
            jump Ch4_S13_T4_KB

        "Inquire about the global influence of Indian cinema.":
            $ affection += 4
            jump Ch4_S13_T2_KB

        "Express curiosity about different film genres.":
            $ affection += 1
            jump Ch4_S13_T3_KB
        "Ask about the history and evolution of Indian cinema.":
            $ affection += 7
            jump Ch4_S13_T1_KB

label Ch4_S13_T1_KB:
    jump Ch4_S14_T0_KB

label Ch4_S13_T2_KB:
    jump Ch4_S14_T0_KB

label Ch4_S13_T3_KB:
    jump Ch4_S14_T0_KB

label Ch4_S13_T4_KB:
    jump Ch4_S14_T0_KB

label Ch4_S14_T0_KB:

    "The theatre was buzzing with excitement. The air was filled with the scent of popcorn, and I could feel the anticipation in the audience. "
    "As the movie began, I was completely drawn in by the vibrant colors, music, and emotions on screen."

    p "That was incredible! The energy, the colors, the music—it's so different from what I'm used to, but I loved it."

    ig "I'm glad you enjoyed it. Indian cinema is all about making you feel deeply, whether it's joy, sorrow, or excitement."

    p "I can't wait to watch more. Thank you for introducing me to this part of your culture."

    "As we left the theatre, I felt even closer to [ig]. Sharing these experiences together has deepened our bond, and I'm excited to see where our journey takes us next."

    jump Ch5_S1_T0_KB


label Ch5_S1_T0_KB:
    if affection >= 40:
        jump Ch5_S1_T1_KB
    elif affection >= 20:
        jump Ch5_S1_T2_KB
    else:
        jump Ch5_S1_T3_KB

label Ch5_S1_T1_KB:
    scene bg christ_dorm

    "After parting ways with [ig], I returned to my dormitory, trying to focus on my exams."

    ig "We're both busy, so let's concentrate on studying."

    p "Yeah, let's do that."

    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."

    p "When did [ig]'s exchange program end again?"

    "I found myself at [ig]'s dormitory. Seeing the empty room, I wondered if I would regret this day."

    "We were so happy together, but perhaps it was beautiful because it's now the past. But still... (reflects briefly). Will I meet someone like [ig] again?"
    "Realizing today was [ig]'s departure, I called a taxi and headed to the airport."

    scene bg india_airport
    p "It was today! I still wanted to say goodbye..."

    "At the airport, I found the counter for flights to India and waited. Noticing missed calls, I called back."

    p "Are you at the airport? I saw the letter you left!"

    "Even now, [ig] was the best person I'd met. So kind and together often. I don't think I'll meet someone like [ig] again."

    ig "Yeah... but I don't want to go. I couldn't say it then, but I realize I need you."

    p "Smiles silently."

    "We persuaded our parents, got back together, and continued our relationship between Korea and India."

    scene bg wedding:
        zoom 1.4
    
    "The bride is ready to enter!"

    p "Today is the happiest day of my life!!"

    ig "Me too, hehe."

    p "Ready for the party? It's going to go late into the night!!"

    "As we entered the hall, I remembered when I first met [ig]. If I hadn't met [ig], what would have happened? This beautiful story of mine will continue forever."
    "{b}Happy Ending{/b}"
    return

label Ch5_S1_T2_KB:
    scene bg christ_dorm

    "After parting ways with [ig], I returned to my dormitory, trying to focus on my exams."

    ig "We're both busy, so let's concentrate on studying."

    p "Yeah, let's do that."

    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."

    p "When does [ig]'s exchange program end?"

    "I found myself standing outside [ig]'s empty dormitory, wondering if I'd regret letting go."

    "We had some wonderful times together, perhaps more beautiful now as memories. I wondered if I'd meet anyone like [ig] again."
    "Realizing today was [ig]'s departure, I impulsively headed to the airport."

    p "Today's the day! I still wanted to say goodbye..."

    scene bg india_airport
    "At the airport, I looked for flights to India and decided to wait. I saw missed calls and dialed back."

    p "Are you at the airport? I saw your letter at the dorm!"

    "Reflecting on the past, [ig] was one of the kindest people I'd met. Though we parted ways, those memories stayed with me."

    scene bg foreign_street
    "As time passed, life moved on. "
    "Years later, I joined a reunion trip for the exchange program. "
    "Among familiar faces, I saw [ig] again."

    ig "It's been a long time!"

    p "It really has. How have you been?"

    "We shared stories and laughter, reconnecting as friends. "
    "Those moments we shared were a cherished chapter, and seeing [ig] again felt like a new beginning, in a different way."
    "{b}Normal Ending{/b}"
    return

label Ch5_S1_T3_KB:
    scene bg christ_dorm

    "After parting ways with [ig], I returned to my dormitory, trying to focus on my exams."

    ig "We're both busy, so let's concentrate on studying."

    p "Yeah, let's do that."

    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."

    p "When does [ig]'s exchange program end?"

    "I found myself outside [ig]'s empty dormitory, wondering if I'd regret how things ended."

    "We had some wonderful times together, but they felt distant now. Our breakup was painful, leaving me with lingering doubts."
    "I knew today was [ig]'s departure, but I couldn't bring myself to go to the airport."

    p "I should have gone... but I just couldn't face it."

    scene bg foreign_street
    "Time passed, and life moved on. "
    "Years later, I was on a business trip and unexpectedly saw [ig] again."

    "In a crowded conference room, our eyes met briefly. An awkward silence stretched between us, heavy with unspoken words."

    "I tried to focus on my work, but my thoughts kept drifting back to [ig]. Memories of our time together resurfaced, mingling with the bitterness of our breakup."

    p "I wish things had ended differently."

    "We passed each other in the hallway, pretending not to notice, but the weight of our shared history was palpable."

    "All I could do was think about [ig], trapped by what once was, but unable to bridge the gap between us. "
    "The silence spoke louder than words, and we both walked away, unable to reconnect or find closure."
    "{b}Bad ending{/b}"
    return
    "test"