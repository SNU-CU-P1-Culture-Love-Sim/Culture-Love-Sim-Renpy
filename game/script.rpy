# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Professor. Oh", color="#c8ffc8")

define p = Character("[player_name]", color="#f4c8ff")

define ib = Character("Prem", color="#c8caff")

define ig = Character("Priyanka", color="#c8caff")

define kb = Character("Seonjae", color="#c8caff")

define kg = Character("Sol", color="#c8caff")

define f1 = Character("Inhyeok", color="#c8caff")

define gd = Character("Guide", color="#c8caff")

define m = Character("mom", color="#c8caff")


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

    jump Ch1_S1_T0_IG



### IG

label Ch1_S1_T0_IG:

    "Today was my first day as an exchange student in Korea. The wind felt particularly refreshing that day."

    p "Hmm... I have no idea where anything is since it's my first time here. Let's head to the lounge in Building 220 and think things over."

    "I headed towards the lounge in Building 220 and opened the door."

    f1 "Oh? A new face. Are you an exchange student by any chance?"

    p "Yeah, I just arrived as an exchange student from Christ University. My name is [player_name]."

    f1 "Nice to meet you! If you have any questions, feel free to ask!"

    "Just then, someone suddenly grabbed my shoulder."

    kb "Hey! What were you guys talking about?"

    p "Uh?"

    kb "Uh? Who... are you?"

    "That was how we first met. He was quite flustered, and his cheeks turned a bit red with embarrassment. Haha."

    kb "Oh!! I'm so sorry!!"

    f1 "Haha, introduce yourself. He's an exchange student who just joined the College of Liberal Studies today."

    p "Hi, I'm [player_name]. I'm an exchange student from Christ University in India, now studying at SNU's College of Liberal Studies."

    kb "Oh, nice to meet you!! I'm {kb}. I heard an SNU student went to India, and now we have an exchange student here, too!"

    kb "Anyway, if you need help with anything, feel free to ask! Oh, wait, I don't have your number yet! What's your number?"

    p "My number is ~~!"

    kb "Great, thanks!"

    "(Growling sound)"

    kb "(Quickly changing the subject) Uh, did you have lunch yet? Haha"

    f1 "Haha, we were just about to grab something. Let's go together!"

    p "Sounds good!"

    "We headed to the cafeteria together..."

    f1 "Oh, shoot! I forgot I had an assignment due! You two go ahead and eat! I'll see you later!"

    "Being left awkwardly alone... Well, let's go eat."

    jump Ch1_S2_T0_IG

label Ch1_S2_T0_IG:

    ## Cafeteria

    "We arrive at the cafeteria, and today's menu is bibimbap. We each grab a bowl and sit down."

    kb "This must be your first time at the cafeteria, right? This is SNU's cafeteria!"

    kb "This is bibimbap, a Korean dish where you mix rice with various vegetables and gochujang (Korean chili paste)!"

    p "Oh!! It looks delicious!! I've never had bibimbap before!"

    kb "Let me mix it for you!"

    "I put all my effort into mixing it."

    "But I get so into it that I accidentally bump into someone's arm, causing the spoon to fling a grain of rice onto their face."

    "What would you do?"

    "(Tutorial) This game requires you to make choices at key moments! Depending on your choices, the relationship level can increase or decrease. The final ending will be different based on your decisions, so choose carefully!"

    menu:

        "What would you do?"

        "1. Remove the grain of rice stuck on {kb}'s face with your hand.":

            jump Ch1_S3_T1_IG

        "2. Hand {kb} a handkerchief.":
            
            jump Ch1_S3_T2_IG

        "3. Glare at the person next to you.":

            jump Ch1_S3_T3_IG

label Ch1_S3_T1_IG:

    jump Ch1_S4_T0_IG

label Ch1_S3_T2_IG:

    jump Ch1_S4_T0_IG

label Ch1_S3_T3_IG:

    jump Ch1_S4_T0_IG

label Ch1_S4_T0_IG:

    p "Haha, it's okay. I have a handkerchief. You got some rice on your face."

    p "This bibimbap is really good! The flavors are mild, and it goes well with the gochujang!"

    kb "Really? I'm glad you like it, haha. By the way, are you busy these days? Have you explored Seoul much?"

    p "Huh? No, I haven't really had the chance to see much outside the campus... Do you have time tomorrow? Maybe you could show me around Seoul?"

    kb "Yeah, I'm free tomorrow! Let's meet up after class! I'll text you!"

    p "Sounds good. See you tomorrow then!"

    jump Ch2_S1_T0_IG


label Ch2_S1_T0_IG:

    ## Chatting app

    kb "[player_name], have you ever been to Seol-ip?"

    p "Seol-ip..? You mean Seoul National University Station, right? I've never been there!"

    kb "Then do you want to go with me? I'll show you around."

    p "Okay, good!"

    "The next day. the two met in Seol-ip."

    kb "Ta-da! Students from our school usually come here to hang out."

    p "Wow, there are a lot of people."

    kb "Um... Since we just had lunch, how about going to a cafe I know and having some dessert?"

    p "Okay."

    kb "I'll buy you some for your first time at Seol-ip."

    p "Oh really?? Thank you. I'll eat well~"

    kb "Huh? It's a karaoke! I wanted to go to a karaoke, haha."

    p "Really? Then let's go in now."

    kb "You can pay for the time you want, and select the song you want to sing with the remote control. Here, the mic."

    p "Thank you. You're so kind ㅜㅜ. I'll sing first!"

    "I am confident in my singing skills, so I sing my favorite song with great enthusiasm."
    "I look to the side while singing and see the other person staring at me."
    "I was a little nervous about the other person until the song ended."

    p "Wow, you sing really well!"

    kb "Haha, no. Now sing too."

    "The other person chose a duet song that is famous for being romantic."
    "Blah blah~"

    "Which of the following actions should I choose?"

    menu:

        "Which of the following actions should I choose?"

        "1. Sing along to the duet song.":
            ## Affection level increases.
            jump Ch2_S2_T1_IG

        "2. Stay still.":
            ## Affection level decreases.
            jump Ch2_S2_T2_IG

        "3. Pick up a tambourine and dance like crazy.":
            ## Affection level increases slightly.
            jump Ch2_S2_T3_IG

label Ch2_S2_T1_IG:

    jump Ch2_S3_T0_IG

label Ch2_S2_T2_IG:

    jump Ch2_S3_T0_IG

label Ch2_S2_T3_IG:

    jump Ch2_S3_T0_IG

label Ch2_S3_T0_IG:

    kb "Phew, I had fun. Where should we go now... Is there a place you want to go?"

    p "Um... Actually, I wanted to see the palaces of Korea."

    kb "Really? Then do you want to go to Gyeongbokgung Palace together?"

    p "Okay, fine."

    "The two take a bus and arrive at Gyeongbokgung Palace."

    "There are many people walking around the palace wearing hanbok."

    p "What are those clothes?"

    kb "That's a traditional Korean costume called hanbok. Hanbok is a costume that our people have worn since ancient times, "
    
    kb "and it has changed over time based on the basics of a skirt, jeogori, and pants. "
    
    kb "Today's hanbok follows the style that was popular during the Joseon Dynasty, "
    
    kb "and modernized hanbok, which is designed to be worn in everyday life, is also popular. "
    
    kb "You can rent a hanbok nearby. Shall we try it on together?"

    p "Okay, let's do that!"

    "The two change into hanbok."

    kb "Now let's take a look around Gyeongbokgung Palace."

    gd "Gyeongbokgung Palace is the first palace built when Joseon was founded and Hanyang (present-day Seoul) became the capital. "
 
    gd "It was used for banquets and receptions by the king and his subjects, as well as for receiving envoys, "
 
    gd "by building a large pond and a grand pavilion. "
 
    gd "Although many buildings were destroyed during the war and colonial period, "
 
    gd "restoration work has been steadily carried out to this day. "

    gd "It is a symbolic palace of the Joseon Dynasty that still maintains its original location since its founding."

    "The two leisurely stroll through Geunjeongjeon and Gyeonghoeru, enjoying the tranquil atmosphere of Gyeongbokgung Palace."

    kb "I think we've seen all the palaces. How was it?"

    p "It was really beautiful! The color arrangement and elaborate design were really impressive. "
    "It was touching to be able to experience Korean history and tradition in person while wearing hanbok. "
    "It felt like a harmony of tradition and modernity, considering that there is a palace like this in the middle of Seoul."

    kb "I'm glad it was a good experience haha. Next, I'll introduce you to the famous traditional market in this area."

    p "Right!"

    p "Oh, it's cold."

    kb "Huh? It's raining."

    "(Shooting, swoosh, the sound of rain falling)"

    kb "Do you have an umbrella? I only have one for myself…"

    p "No, ㅜㅜ. It seems like Korea gets a lot of rain showers."

    kb "Let's go under the eaves and wait for it to stop."

    "The two moved under the skirts to take shelter from the rain for a while, but the rain showed no sign of stopping."

    kb "Hmm, the rain won't stop. We have to get to the market on time, but..."

    "How should I respond to an unexpected downpour?"

    menu:
        "1. Go to a nearby convenience store and buy an umbrella each.":
            ## Slightly decrease in favorability
            jump Ch2_S4_T1_IG

        "2. Share an umbrella and run to the market.":
            ## Affection level goes up significantly
            jump Ch2_S4_T2_IG

        "3. Suggest that we both just go while getting rained on.":
            ## Affection level goes down significantly
            jump Ch2_S4_T3_IG

label Ch2_S4_T1_IG:
    
    jump Ch2_S5_T0_IG

label Ch2_S4_T2_IG:

    jump Ch2_S5_T0_IG

label Ch2_S4_T3_IG:

    jump Ch2_S5_T0_IG

label Ch2_S5_T0_IG:

    "After many twists and turns, the two arrive at Gwangjang Market."

    kb "Okay, this is Gwangjang Market."

    p "It's bigger and more crowded than I thought."

    kb "That's right. Gwangjang Market is the largest and oldest traditional market in Korea. "
    "There are various food alleys in Gwangjang Market, hanbok stores where you can buy daily necessities, and second-hand stores."

    p "Right. Let's eat something since we're hungry."

    kb "This is tteokbokki, a national snack that Koreans of all ages and genders love. "
    "It might be a little spicy, but is that okay?"

    "What should I say in response to that suggestion?"

    menu:
        "1. Yeah, I like spicy food. Wow~":
            ## Affinity increase
            jump Ch2_S6_T1_IG

        "2. I can't eat spicy food well... I'll try it next time.":
            ## Affinity maintained
            jump Ch2_S6_T2_IG

        "3. Hmm, I'll rinse it in water and try it. Give it to me.":
            ## Affinity decrease
            jump Ch2_S6_T3_IG

label Ch2_S6_T1_IG:

    jump Ch2_S7_T0_IG

label Ch2_S6_T2_IG:

    jump Ch2_S7_T0_IG

label Ch2_S6_T3_IG:

    jump Ch2_S7_T0_IG

label Ch2_S7_T0_IG:

    kb "This is bindae-tteok, a specialty of Gwangjang Market. "
    "It is a dish made by mixing vegetables or meat into a dough made from ground soybeans and frying it."

    kb "This noodle is called janchi-guksu. "
    "It originated from the fact that it was enjoyed at weddings, birthday parties, and 60th birthday parties in the hopes of longevity."

    p "The food here is really delicious."

    "Then they enjoy the food with a happy conversation."

    jump Ch3_S1_T0_IG


label Ch3_S1_T0_IG:

    kb "How about we try dating somewhere new?"

    p "Sounds good! Where should we go?"

    kb "Is there anything you'd like to try?"

    p "Hmm... Could we maybe go to a famous festival in Korea?"

    kb "Of course! How about we go to the largest music and water-themed festival in the country? "
    kb "It combines performances from various genres like K-POP, hip-hop, EDM, and large-scale water fights!"

    p "Great! What's the name of that festival?"

    kb "Want to try guessing?"


    menu:

        "Guess the name of the festival:"

        "1. Pentaport Rock Festival":

            jump Ch3_S2_T1_IG

        "2. Waterbomb Festival":

            jump Ch3_S2_T2_IG

        "3. Boryeong Mud Festival":

            jump Ch3_S2_T3_IG

        "4. Seoul Jazz Festival":

            jump Ch3_S2_T4_IG

label Ch3_S2_T1_IG:

    kb "Ah, unfortunately the answer was Waterbomb :( Well then, shall we go to Waterbomb now?"

    jump Ch3_S3_T0_IG

label Ch3_S2_T2_IG:

    kb "That's right!! My darling! Then shall we go to Waterbomb?"

    jump Ch3_S3_T0_IG

label Ch3_S2_T3_IG:

    kb "Ah, unfortunately the answer was Waterbomb :( Well then, shall we go to Waterbomb now?"

    jump Ch3_S3_T0_IG

label Ch3_S2_T4_IG:

    kb "Ah, unfortunately the answer was Waterbomb :( Well then, shall we go to Waterbomb now?"

    jump Ch3_S3_T0_IG

label Ch3_S3_T0_IG:

    "Enjoy Waterbomb water gun play photos attached"

    p "Wow! This is really fun!!"

    "During the water gun play, I became the target of many people."

    p "Oh no..."

    kb "[player_name]!!"

    "My partner shielded me with their whole body."

    kb "Are you okay??"

    p "Yes!! Really thank you"

    kb "How was it?"

    p "This was so much fun!!"

    kb "Great! Then let's go watch the performances now? We can buy some beers too!"

    "*Performance photos attached*"

    p "It was so much fun!! I especially enjoyed seeing the K-pop singers. I love music!"

    kb "Oh really? Then should we go to **Hongdae** next time?"

    p "Why Hongdae? Is it famous for music?"

    kb "Many musicians do street performances in Hongdae! *Watching busking in Hongdae*"

    p "This is so enjoyable~"

    "*gets a text message*"

    p "Oh no..."

    kb "What's wrong? You don't look good."

    p "I think I need to go back to India now."

    kb "What? Didn't you have half a year left?"

    p "I loved Korea and you so much that I extended my exchange student program for another semester, "

    p "but I just got a message saying my application was rejected."

    kb "What? I'm so disappointed... I'm tearing up..."

    p "Oh honey, don't cry... I'm really disappointed too.."

    kb "So we won't be able to see each other anymore?"

    p "Choose the right sentence to comfort the other person:"

    menu:
        "1. I suppose so. I'm really sorry.":

            jump Ch3_S4_T1_IG

        "2. We were never meant to be together for long anyway.":
            
            jump Ch3_S4_T2_IG

        "3. No, don't say that! Everything will be alright, don't worry my dear.":

            jump Ch3_S4_T3_IG

label Ch3_S4_T1_IG:

    jump Ch3_S5_T0_IG

label Ch3_S4_T2_IG:

    jump Ch3_S5_T0_IG

label Ch3_S4_T3_IG:

    jump Ch3_S5_T0_IG

label Ch3_S5_T0_IG:

    "*at the airport*"

    kb "I wish we could meet again soon."

    p "Be happy even after you go back."

    kb "I prepared a gift for you. This is a traditional Korean costume, do you remember the name of it?"

    p "Guess the name of the costume:"

    menu:
        "1. Hanbok":
            jump Ch3_S6_T1_IG

        "2. Kimono":
            jump Ch3_S6_T2_IG

        "3. Ao Dai":
            jump Ch3_S6_T3_IG

        "4. Sari":
            jump Ch3_S6_T4_IG

label Ch3_S6_T1_IG:

    jump Ch3_S7_T0_IG

label Ch3_S6_T2_IG:

    jump Ch3_S7_T0_IG

label Ch3_S6_T3_IG:

    jump Ch3_S7_T0_IG

label Ch3_S6_T4_IG:

    jump Ch3_S7_T0_IG

label Ch3_S7_T0_IG:

    p "Wow, thank you so much. This will remind me of you."

    kb "Don't forget me when you go back to India."

    p "Of course not. We're under the same sky. Our love will be eternal."

    kb "Take care in Korea."

    p "Yes, you take care in India too. Let's meet in India next time."

    jump Ch4_S1_T0_IG


label Ch4_S1_T0_IG:

    "It's been two months since I returned to Bengaluru in a hurry. Fortunately, my mother's health (or the specific reason why I returned) is gradually improving."

    p "He must have been surprised that I left so suddenly. Will I be able to see him again?"

    "Without thinking, I opened my mailbox, and there it was, an email from him."

    menu:
        "Read the email":

            jump Ch4_S1_T1_IG

        "Don't read the email":

            jump Ch4_S1_T2_IG

label Ch4_S1_T1_IG:

    "I thought I was the only one missing him, but he felt the same way. He is coming to our school as an exchange student. I can't believe it."

    jump Ch4_S2_T0_IG

label Ch4_S1_T2_IG:

    "I shouldn't hold on to past relationships. Reading this email will only make me miss him more. I won't read it."

    jump Ch4_S2_T0_IG

label Ch4_S2_T0_IG:

    m "We're going to visit your grandfather in Agra next week."

    p "Agra?"

    m "Yes. We need to deliver these things to your grandfather."

    "After visiting my grandfather's house, I had a bit of time before my flight. What should I do now?"

    menu:
        "Go to the Taj Mahal":

            jump Ch4_S3_T1_IG

        "Go to Agra Fort":

            jump Ch4_S3_T2_IG

        "Go shopping":

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

    "Come to think of it, he also wanted to visit this place... I have a feeling he might be here today."

    menu:
        "Observe the people following the tour guide":

            jump Ch4_S5_T1_IG

        "Watch people getting their photos taken by peddlers":

            jump Ch4_S5_T2_IG

        "No way, such a coincidence couldn't happen":

            jump Ch4_S5_T3_IG

label Ch4_S5_T1_IG:

    jump Ch4_S6_T0_IG

label Ch4_S5_T2_IG:

    jump Ch4_S6_T0_IG

label Ch4_S5_T3_IG:

    jump Ch4_S6_T0_IG

label Ch4_S6_T0_IG:

    "I see a Korean person over there! No way..."

    kb "Oh! It's you!"

    p "What a coincidence to meet here..."

    kb "I arrived in India yesterday. You said you would take me to the Taj Mahal, so I wanted to come even if it was alone."

    p "I had a feeling you might be here today."

    kb "The Taj Mahal is so beautiful! Just like you described it."

    p "I thought you would like Agra. It has many historical sites that showcase Indian tradition. It's like ( ) in Seoul."

    menu:
        "Myeong-dong":

            jump Ch4_S7_T1_IG

        "Jongno":

            jump Ch4_S7_T2_IG

        "Itaewon":

            jump Ch4_S7_T3_IG

label Ch4_S7_T1_IG:

    jump Ch4_S8_T0_IG

label Ch4_S7_T2_IG:

    jump Ch4_S8_T0_IG

label Ch4_S7_T3_IG:

    jump Ch4_S8_T0_IG

label Ch4_S8_T0_IG:

    kb "That's right! You seem to know quite a lot about Korea now!"

    p "Of course! It's always a place I miss."

    kb "What should we do now?"

    menu:
        "Let's go eat street food in Delhi":

            jump Ch4_S9_T1_IG

        "I'll take a picture of you in front of the Taj Mahal":

            jump Ch4_S9_T2_IG

        "Let's go back to the hotel and rest":

            jump Ch4_S9_T3_IG

label Ch4_S9_T1_IG:

    jump Ch4_S10_T0_IG

label Ch4_S9_T2_IG:

    jump Ch4_S10_T0_IG

label Ch4_S9_T3_IG:

    jump Ch4_S10_T0_IG

label Ch4_S10_T0_IG:

    "We traveled around Agra and Delhi for a few days. Now it's time to return to Bangalore."

    "After spending a few memorable days in Delhi and Agra, it's time to head back to Bangalore. "

    "We decided to take the train together—an experience that would allow us to see more of India's diverse landscapes and cultures as we travel across regions."

    kb "I've heard that train journeys in India are quite an experience. I'm excited but also a bit nervous. How long will the journey take?"

    p "It'll take around 36 to 40 hours, depending on the train. But trust me, it's going to be an unforgettable experience. "

    p "You'll get to see so much of India, from the bustling cities to the peaceful countryside."

    kb "I can't wait! What should we expect during the journey?"

    menu:
        "Talk about the diversity of regions and cultures in India.":

            jump Ch4_S11_T1_IG

        "Discuss the history and significance of Indian Railways.":

            jump Ch4_S11_T2_IG

        "Mention the culinary delights available on the train.":

            jump Ch4_S11_T3_IG

        "Suggest sleeping or reading during the journey to pass the time.":

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

    "After a long but enriching journey, we finally arrived in Bangalore. The city greeted us with its pleasant weather and vibrant atmosphere."

    kb "Bangalore seems so lively! I've heard it's known as the Silicon Valley of India."

    p "That's right. Bangalore is a major hub for technology and startups, but it's also known for its parks, historic sites, and diverse culture."

    kb "I'm excited to explore it. What should we do first?"

    menu:
        "Suggest exploring the historic parts of Bangalore.":

            jump Ch4_S13_T1_IG

        "Propose visiting the local parks and gardens.":

            jump Ch4_S13_T2_IG

        "Suggest checking out the local markets.":

            jump Ch4_S13_T3_IG

        "Propose heading straight to the hotel to rest.":

            jump Ch4_S13_T4_IG

label Ch4_S13_T1_IG:

    jump Ch4_S14_T0_IG

label Ch4_S13_T2_IG:

    jump Ch4_S14_T0_IG

label Ch4_S13_T3_IG:

    jump Ch4_S14_T0_IG

label Ch4_S13_T4_IG:

    jump Ch4_S14_T0_IG

label Ch4_S14_T0_IG:

    "After settling in, I thought it would be a great idea to introduce K to Indian cinema—a vital part of the culture here. We decided to go to a local theatre to watch a popular Indian film."

    kb "I've heard so much about Indian cinema. Bollywood, right?"

    p "Yes, but there's so much more to Indian cinema than just Bollywood. Each region has its own film industry—Kollywood in Tamil Nadu, Tollywood in Andhra Pradesh, and Sandalwood right here in Karnataka. "

    p "Indian cinema has a rich history, and it's evolved a lot over the years."

    menu:
        "Explain the history and evolution of Indian cinema.":

            jump Ch4_S15_T1_IG

        "Talk about the influence of Indian cinema globally.":

            jump Ch4_S15_T2_IG

        "Discuss the different film genres and what to expect.":

            jump Ch4_S15_T3_IG

        "Suggest watching the movie quietly without discussing it.":

            jump Ch4_S15_T4_IG

label Ch4_S15_T1_IG:

    jump Ch4_S16_T0_IG

label Ch4_S15_T2_IG:

    jump Ch4_S16_T0_IG

label Ch4_S15_T3_IG:

    jump Ch4_S16_T0_IG

label Ch4_S15_T4_IG:

    jump Ch4_S16_T0_IG

label Ch4_S16_T0_IG:

    "We entered the theatre, the air filled with the aroma of popcorn and the excitement of the audience. The movie started, and I could see K was completely engrossed in the experience."

    kb "That was incredible! The energy, the colors, the music—it's so different from what I'm used to, but I loved it."

    p "I'm glad you enjoyed it. Indian cinema is all about making you feel deeply, whether it's joy, sorrow, or excitement."

    kb "I can't wait to watch more. Thank you for introducing me to this part of your culture."

    "As we left the theatre, I felt even closer to {kb}. Sharing these experiences together has deepened our bond, and I'm excited to see where our journey takes us next."

    jump Ch5_S1_T0_IG


### need codes to decide the ending. Sanghyuk fighting ^^

label Ch5_S1_T0_IG:

    jump Ch5_S1_T1_IG

label Ch5_S1_T1_IG:

    "After parting ways with {kb}, I returned to my dormitory, trying to focus on my exams."

    kb "We're both busy, so let's concentrate on studying."

    p "Yeah, let's do that."

    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."

    p "When did {kb}'s exchange program end again?"

    "I found myself at {kb}'s dormitory. Seeing the empty room, I wondered if I would regret this day."

    "We were so happy together, but perhaps it was beautiful because it's now the past. But still... (reflects briefly). Will I meet someone like {kb} again?"
    "Realizing today was {kb}'s departure, I called a taxi and headed to the airport."

    p "It was today! I still wanted to say goodbye..."

    "At the airport, I found the counter for flights to Korea and waited. Noticing missed calls, I called back."

    p "Are you at the airport? I saw the letter you left!"

    "Even now, {kb} was the best person I'd met. So kind and together often. I don't think I'll meet someone like {kb} again."

    kb "Yeah... but I don't want to go. I couldn't say it then, but I realize I need you."

    p "Smiles silently."

    "We persuaded our parents, got back together, and continued our relationship between Korea and India."

    "A vibrant Indian wedding with flowers."

    "Officiant" 
    
    "The bride is ready to enter!"

    p "Today is the happiest day of my life!!"

    kb "Me too, hehe."

    p "Ready for the party? It's going to go late into the night!!"

    "As we entered the hall, I remembered when I first met {kb}. If I hadn't met {kb}, what would have happened? This beautiful story of mine will continue forever."

    return

label Ch5_S1_T2_IG:

    "After parting ways with {kb}, I returned to my dormitory, trying to focus on my exams."

    kb "We're both busy, so let's concentrate on studying."

    p "Yeah, let's do that."

    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."

    p "When does {kb}'s exchange program end?"

    "I found myself standing outside {kb}'s empty dormitory, wondering if I'd regret letting go."

    "We had some wonderful times together, perhaps more beautiful now as memories. I wondered if I'd meet anyone like {kb} again."
    "Realizing today was {kb}'s departure, I impulsively headed to the airport."

    p "Today's the day! I still wanted to say goodbye..."

    "At the airport, I looked for flights to Korea and decided to wait. I saw missed calls and dialed back."

    p "Are you at the airport? I saw your letter at the dorm!"

    "Reflecting on the past, {kb} was one of the kindest people I'd met. Though we parted ways, those memories stayed with me."

    "As time passed, life moved on. Years later, I joined a reunion trip for the exchange program. Among familiar faces, I saw {kb} again."

    kb "It's been a long time!"

    p "It really has. How have you been?"

    "We shared stories and laughter, reconnecting as friends. Those moments we shared were a cherished chapter, and seeing {kb} again felt like a new beginning, in a different way."

    return

label Ch5_S1_T3_IG:

    "After parting ways with {kb}, I returned to my dormitory, trying to focus on my exams."

    kb "We're both busy, so let's concentrate on studying."

    p "Yeah, let's do that."

    "Back then, if I'd acted differently, could we have stayed closer? This question lingered in my mind as the days passed."

    "With the semester ending, I immersed myself in exams. Uncertain about my feelings, I hesitated."

    p "When does {kb}'s exchange program end?"

    "I found myself outside {kb}'s empty dormitory, wondering if I'd regret how things ended."

    "We had some wonderful times together, but they felt distant now. Our breakup was painful, leaving me with lingering doubts."
    "I knew today was {kb}'s departure, but I couldn't bring myself to go to the airport."

    p "I should have gone... but I just couldn't face it."

    "Time passed, and life moved on. Years later, I was on a business trip and unexpectedly saw {kb} again."

    "In a crowded conference room, our eyes met briefly. An awkward silence stretched between us, heavy with unspoken words."

    "I tried to focus on my work, but my thoughts kept drifting back to {kb}. Memories of our time together resurfaced, mingling with the bitterness of our breakup."

    p "I wish things had ended differently."

    "We passed each other in the hallway, pretending not to notice, but the weight of our shared history was palpable."

    "All I could do was think about {kb}, trapped by what once was, but unable to bridge the gap between us. The silence spoke louder than words, and we both walked away, unable to reconnect or find closure."

    return