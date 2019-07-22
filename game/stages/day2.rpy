label day2:
  
  if restart:

    "..." """
    You couldn't make it different

    This doesn't make any sense.

    It was fun what it lasted. Now let it end.
    """

    scene bg dark
    with Fade(0.1, 0.1, 3.0)

    return

  itawa """
  You did it very well, Professor

  Congratulations. My daugther is safe because of you

  Everyone is safe because of you. You are a hero, haha.
  """

  """
  A hero...

  Am I?
  """

  itawa """
  Do not listen to anyone else, Professor. You are okay.

  Everything is okay.
  """

  "..." "So, you are a High School professor, aren't you?"

  """
  Who's that?

  Where am I?

  Kanae's house?... no
  """

  "..." "Hey, wake up!"

  scene bg police_station
  with Fade(0.1, 0.3, 0.1)

  """
  Makawa died.

  Kanae!
  """

  show alan young speaking
  with dissolve

  "..." """
  Hey, wait a sec

  Your face is like if you forgot your condom inside your wife

  Calm down a little bit, everything ended hours ago.
  """

  play music dramatic fadein 1.0 fadeout 1.0

  show alan young normal

  """
  Who's he?

  I can't remember what happened after...

  After I killed Makawa...{w=1.0} and Itawa?

  I don't understand
  """

  show alan young serious talk

  "..." """
  The young Kanae pleads for you, she says it was in self defense. 

  She says that her brother had become aggressive and planned this whole scenario

  He wanted a dead, although in this case was himself
  """

  show alan young normal

  """
  But Itawa... how could that have happened?
  """

  show alan young serious talk

  "..." """
  Kanae will not file any charges against you, in fact she seems grateful.
  """

  show alan young smiling

  "..." """
  Her brother had a pretty dangerous organization in the shadows. Between us... Thanks for taking out the garbage.
  """

  show alan young normal

  """
  He says that with that smile on his face. I just feel some contempt for the words.

  I shared with Makawa much more than a single day, even if it wasn't this version of him with who I spent all that.
  """

  show alan young serious talk

  "..." """
  Someone is going to have to take care of her.

  She has sixteen years, she can't stay in that house alone.

  Someone should serve as a tutor until she gets legal age. And yes, she wants to see you
  """

  show alan young normal

  """
  He was practically speaking on his own since my mind was elsewhere, but by mentioning the situation in what Kanae is going to be now, he makes me land my thoughts

  Knowing that she is willing to talk to me makes me feel a great anxiety between talking to her or not

  If I don't talk to her, I'll be like an ass, although it may be understandable to others. I just killed her only brother

  On the contrary, if I decide to speak to her, how do I explain that while I incrusted a knife in the stomach of the only relative she had left, I also visualized me doing the same to her mother?

  Kanae doesn't have anyone else in the country. Hell, I don't know if she has someone else left anywhere.
  """

  show alan young serious talk

  "..." "So, what do you want to do?"

  show alan young normal

  menu:
    "I want to..."

    "Talk to her":
      $ day2_talk_kanae_police = True

    "Know about Makawa":
      $ day2_talk_kanae_police = False

  if not day2_talk_kanae_police:
    call day2_not_talk_with_kanae from _call_day2_not_talk_with_kanae
  else:
    show alan young serious talk
    "..." """
    I see...{w=1.0} she is somehow shocked for all that has happened.

    The only time she spoke was when we pronounced your name, so...
    """

  "..." "Go and see her."

  hide alan
  with dissolve

  show my_kanae worried soft
  with dissolve

  """
  There she is. I don't know what should I say

  She didn't seem bothered or sad, she is just there.
  """

  show my_kanae surprised 
  with dissolve

  my_kanae """
  You should not feel bad... Makawa sought his end. 

  Before he was not like that. When we were children, he always protected me, until one day he simply decided to destroy everything.

  There he stopped being that brother who I appreciated and became the monster that terrified me. 
  """

  show my_kanae worried soft
  
  """
  Kanae thinks that Makawa killed her mother as well.

  I can't tell Kanae that I was the cause of her misfortune... Both in the past and in the present
  """

  show my_kanae sad 
  with dissolve

  my_kanae "Professor...{w=1.8} Please, do not leave me you too."

  """
  As she said it, I raise my face to see her eyes

  She had been incredibly strong, I had never seen her like that before

  She broke completely, her tears were running all over her face

  The pain permeated her soul, and guilt invaded me even more. In spite of everything, Makawa was what was left of her family and I took it from her
  """

  show my_kanae worried soft
  with dissolve

  """
  I could only think of giving her a hug to calm her down... It worked to reassure both of us
  """

  show my_kanae surprised

  my_kanae "Professor, What happened to your hand? The scar that you had…"

  show my_kanae worried soft

  """
  Yes, a ring that seems to be marked when I take someone's life

  Now I had to explain to her what this strange witchcraft was and, that apart, I didn't even understand!
  """

  me "I don't know. Perhaps it was in the fight"

  if day1_stabbed:
    show my_kanae surprised
    my_kanae """
    The doctors saw the wound in your stomach? Makawa almost killed you
    """

    show my_kanae worried soft

    me "Yeah, don't worry. I am fine."

  show my_kanae worried soft at left:
    xalign 0.2
  with MoveTransition(0.7)

  show alan young normal at center
  with dissolve

  show alan young speaking
  with dissolve

  "..." """
  Sorry for keeping you for so long, but the circumstances of this deserved it. 

  Don't worry, you're free to go home. Does anyone can come for you?
  """

  show alan young normal

  """
  Kanae's face shows again that catatonic and lifeless state that she had before I entered
  """

  show my_kanae surprised

  my_kanae "Can we both go now? Have you cleared everything up to let us go?"

  "She asks insistently. I will not deny it, I also wanted to leave"

  show my_kanae worried soft
  show alan young speaking

  "..." """
  Ahhm... Yes, both can leave in fact.

  The fiscal said that, for now, you can be with the Professor until we can found a new home for you.
  """

  show alan young normal
  "It's okay that after all that happened that she stay in my house?"

  show alan young speaking
  "..." "You are okay with that, Professor?"

  show alan young normal
  me "If Kanae is okay with it."

  show my_kanae surprised
  my_kanae "Yes."

  show my_kanae worried soft

  show alan young speaking

  "..." "Good."
  "..." """
  Before you leave, I need to speak with you a moment, Professor. I'd really apreciate it
  """

  """
  Kanae looks at me with some concern. Every action around us was built on uncertainty. 

  No wonder, I was part of a murder... author of one, actually.

  Although it was in self defense, the fact that the victim was the brother of the person with whom I retire makes everything a little more uncomfortable.
  """
  hide my_kanae
  with dissolve

  show alan young serious talk at center
  with move

  "..." """
  I don't know what the hell happened in that house, really

  I'm not going to deny that seeing the case, not only seems that he set the stage for this, but it also seems that you agreed to that result from the beginning

  If that guy had not been a social crap or if that little girl had put charges against you, believe me you wouldn't be leaving now. 

  Like I told you, you did us a favor by getting rid of him. 

  She will get over it sooner or later. 
  """

  show alan young speaking
  "..." """

  Now she is in shock, but I want to be clear. If something happens to that young girl, and I mean anything bad

  I'll move this whole station to find you and leave you the same or worse than Makawa
  """

  show alan young normal

  """
  His face carefree, but his tone of firmness made things clear and scored my priority, which in fact was not exactly Kanae. 

  If I want to protect her, I have to understand well what is happening to me
  """

  hide alan
  with dissolve

  stop music fadeout 3.0

  scene bg dark
  with fade

  """
  We leaved the police station in a taxi.

  The trip was marked by the sound of the wind blowing through the car window, nothing more. 

  There was no exchange of words between Kanae and me, not even among the taxi driver 

  Her gaze was lost in the window... no fixed point
  """

  scene bg itawa_house_front_night
  with fade

  show my_kanae worried soft
  with dissolve

  show my_kanae surprised
  with dissolve

  my_kanae "Professor... please.{w=1.0} Can I stay at your house today? I do not want to go back there...{w=1.0} at least not for now"

  show my_kanae worried soft

  """
  I can't say no to her right now.
  """

  me "Okay, Kanae."

  scene bg dark
  with fade 

  """
  The driver, without asking anything at all, just kept driving towards my house, returning to the uncomfortable and marked silence that she imposed
  """

  scene bg main_living
  with fade

  me "Do you want to shower, Kanae?"

  show my_kanae surprised
  with dissolve

  my_kanae "Okay."

  show my_kanae worried soft

  """
  Her state of shock kept her almost in catatonic mode where she only worked with the basic actions of a living being. It was scary

  That young girl who, although shy, was always with a smile full of life, now simply shows an expression full of emptiness

  She was now a cocoon that kept her emotions and only showed a shell with which she tried to protect herself from the reality she faces
  """

  show my_kanae surprised
  my_kanae "Thanks, Professor."

  show my_kanae worried soft

  me "You can sleep in my room if you want. This is your house."

  show my_kanae blushed
  with dissolve

  my_kanae "Thank you, Professor. But where are you gooing to sleep?."

  me "Don't worry, I'll sleep in the couch. Just rest, Kanae."

  show my_kanae worried soft
  my_kanae "Thank you, Professor"

  """
  Although I was really worried about leaving her alone in a room, I felt that she needed it. 
  """

  hide my_kanae worried soft
  with dissolve

  """
  Whatever the decision she was going to make was going to be there and I wouldn't be able to interfere. 

  At least I should leave her this choice after ruining all her life
  """

  scene bg dark
  with Fade(0.5, 1.5, 0.5)

  """
  I don't want to get out of bed, I don't know how I am going to face this day. 
  """

  play music dramatic fadein 1.0 fadeout 1.0 loop
  scene bg main_living
  with fade

  """
  I keep watching the scar marked on my hand. I was searching the internet all night regarding something, but I didn't get anything

  I haven't slept either, by now I was a greater disaster than yesterday. However, I had to see how Kanae was doing.

  I feel pathetic for leave her alone all night, but what she was going to do, it would do it with or without me
  """

  #cooking sounds overhere

  """
  What's that?

  What's that smeel?
  """

  stop music fadeout 1.0

  #more cooking sounds

  scene bg kitchen
  with fade

  play music happy_loop fadein 1.0 fadeout 1.0 loop

  """
  She is in the kitchen. 

  The house is perfumed with an smell that unbelievably opens my appetite
  """

  show my_kanae surprised
  with dissolve

  my_kanae """
  Oh, Professor
  """

  "She is there. Just enjoying cooking."

  show my_kanae normal
  my_kanae """
  I did not though you were awake yet

  I hope you like it, Professor. There was not much to choose from in your refrigerator. You should ask someone to do the shopping.
  """

  """
  I must say that this food that she prepared is much better than anything I could cook

  Besides, her little smile gave me an extra boost on this day
  """

  show my_kanae surprised
  my_kanae """
  Professor, I know something is happening

  You are hiding from me what really happened last night with Makawa

  I remember that in the morning you acted very rare, I did not mention it in the interrogation because I know that you are not like that, but I need you to tell me the truth. 

  I saw that that scar on the finger of your hand was not marked in the morning, I remember it. 

  Please, tell me what happened to you?
  """

  show my_kanae worried soft

  """
  A breakfast next to an apple juice to say that I can jump in time and because of that I killed her mother and brother. 

  I must tell her. This is no longer something I can hide, at least not to her
  """

  menu:
    "Kanae..."

    "The dream" if not day1_asked_garden:
      $ day2_say_dream = True
      call day2_dream_breakfast from _call_day2_dream_breakfast

    "Time":
      call day2_time_breakfast from _call_day2_time_breakfast

  """
  The silence was there for a minute again.
  """

  show my_kanae surprised
  my_kanae "I believe in you"

  show my_kanae worried soft

  """
  She does?
  """

  show my_kanae surprised
  my_kanae """
  Something happened this week that made me realize that this does not feel right. 

  As if it were out of place. Maybe it's an illusion of mine and we are both crazy, but I can not deny that all this is not normal

  Something is happening with us... with you, Professor
  """

  show my_kanae worried soft

  """
  She is right. I have to see what's all this

  Not only for me, but for her. To restore everything...
  """

  me """
  I think I know someone who could help us

  I've search everywhere and haven't found anything, he is kinda like my last resource.

  He is very... peculiar. Is far from here, but it can bring us more answers about what's happening.
  """

  show my_kanae normal

  my_kanae "Okay, Professor. Let's do it!"

  hide my_kanae normal 
  with dissolve

  """
  It was a trip of three hours in car to his house

  Kanae and I decided to leave in search of some answer or indication to understand these temporary jumps. 
  """

  stop music fadeout 4.0

  scene bg oyab motorhome
  with fade

  $ renpy.pause(delay=3.0)

  play music main fadein 2.0 fadeout 1.0 loop

  """
  We arrived and nothing was like I remember it

  The truth is that there wasn't even a house.

  The only thing that was there was a small motorhome just outside this desolated place. It looked as if it was taken to make some blue meth.
  """

  show my_kanae worried soft
  with dissolve

  show my_kanae surprised
  with dissolve

  my_kanae """
  Professor, are you sure someone lives here?

  Everything looks abandoned
  """

  show my_kanae worried soft

  """
  Really looks like nonone lives here
  """

  me "We have traveled this far. I know he still lives here."

  hide my_kanae worried soft
  with dissolve

  play sound knock
  $ renpy.pause(delay=0.3)
  play sound knock

  "I knocked the motorhome door"

  me "Hello, is someone here?"

  $ renpy.music.set_volume(0.5, channel='sound')

  play sound crash

  "..."

  $ renpy.music.set_volume(1.0, channel='sound')

  show oyab dirty screaming
  with dissolve

  "..." "The hell you two want? This is not a motel, go elsewhere. The house is...{w=1.3} closed or something like that"

  "The conglomeration of odors that came out was indescribable and the least unpleasant was the putrefaction to liquor that he gave off"

  show oyab dirty speaking serious
  "..." "She's not very too young for you, son? Ain't gonna judge your shit or anything at all, but…"

  show oyab dirty normal

  me "Emm... hi. Excuse me, do you know someone called Oyab?"

  show oyab dirty listening
  oyab "Hell, I hadn't heard that name in years..."

  show oyab dirty speaking serious
  oyab """
  I only have something to tell you, son...

  If you come looking for that pathetic dude who pretends to know things to take money from the morons who believed them

  Let me tell you that now I'm more pathetic and no one wants me to tell those lies without meaning

  Although at least now I have the freedom to not pretend I can
  """

  show oyab dirty normal
  me """
  Listen, I know all that. Seems pretty clear

  But I also know that you know more than you said. A lot more.
  """

  show oyab dirty listening
  me """
  Do you know something about this?
  """

  """
  I show him the scar on my finger
  """

  show oyab dirty screaming
  oyab "What the hell are you doing here?"

  show oyab dirty speaking serious
  oyab "Get out of here... out"

  show oyab dirty listening
  me "So you do know about this, dont you?"

  show oyab dirty speaking serious

  oyab """
  I don't know if you two are drugged or are playing a joke or both, but I'm not interested. 

  Get away from here, I prefer to immerse myself in my own shit than to get up and listen to these stupid things.
  """
  play sound door_close

  hide oyab dirty speaking serious
  with dissolve
  with hpunch


  show my_kanae angry
  with dissolve

  my_kanae """
  Do not be a dick

  At least take the only bit of person you still have left and stop being pathetic in your life

  Even for now, stop putting your head in your butt to breathe the same excrement that you really like to talk about and tell us what you really know

  Because I know you know something, and I ask you to tell us.
  """

  show my_kanae mad

  """
  Where all that came from?
  
  I don't know at what moment Kanae suffered the transformation of a quiet girl to this woman who had more character than any other person
  """

  show my_kanae blushed
  with dissolve

  stop music fadeout 1.0
  play music dramatic fadein 1.0 fadeout 1.0 loop

  my_kanae """
  Please...{w=1.0} I lost my mother and now my brother too

  I know that does not matter to you in the least, but I need an explanation

  Please, I beg you
  """

  """
  Kanae said, with her fist and forehead settling on the door while tears ran down her cheeks
  """

  show my_kanae sad
  with dissolve

  my_kanae "Please… I am begging you."
  my_kanae "I am begging you."
  my_kanae "Please…"

  show my_kanae blushed
  with dissolve

  """
  She insisted again and again, but it didn't help. For Oyab it was as if we weren't there

  I take Kanae by her shoulders and decied to go back to the house

  The travel was quite long and since we wouldn't get answers here, it was better to leave with the disappointment impregnated in us.
  """
  stop music fadeout 3.0

  scene bg road car
  with Fade(0.5, 2.0, 0.5)


  """
  Lonely and sunny path full of silence, gray by its loss and broken by uncertainty.
  """

  play sound wind fadein 2.0 fadeout 2.0 loop

  """
  The breeze coming through the window moving her hair while her gaze was lost on a road that seems infinite in the distance
  """

  show my_kanae worried soft
  with dissolve

  my_kanae "..."

  """
  There was nothing to say. We were just like at the beginning of the day... no, worse, we don't even have a false hope.
  """

  show my_kanae surprised
  my_kanae "hcraes sselgninaem a"

  """
  What?
  """

  my_kanae "gnihton si ereht"

  me "Kanae?"
  my_kanae "hcraes sselgninaem a"

  me "Kanae? What's happening?"

  my_kanae "gnihton si ereht"

  show my_kanae worried soft

  """
  I turn my head to see what happened and I see that, from the actions of her body, to the movement of her hair by the breeze of the air, everything was being repeated

  It was like a loop
  """

  me "Kanae! Wake up!"

  """
  My car, after going back a few meters, moved to a point again and returned

  Everything was iterating at an arbitrarily specified interval
  """

  menu:
    "I try to"

    "Open the door of the car":
      $ day2_open_door = True
    "Stop Kanae":
      $ day2_open_door = False
  
  if day2_open_door:
    "I pull the handle really hard, but it doesn't work"
  else:
    "I try to stop Kanae's movements. Maybe if I can stop her, the loop will break"

  """
  While this sequence happened repeatedly, I could observe how the sky was changing continuously without being affected by the loop
  """

  show bg road car cooled
  with dissolve

  stop sound fadeout 1.0
  $ renpy.pause(delay=0.3)
  play sound glass_cracking
  $ renpy.pause(delay=1.3)
  play sound wind fadein 1.0 fadeout 1.0 loop 

  """
  The sky was getting more and more gray after a polar cold rose from the wheels to the roof of the car fogging the windshield and freezing my thought
  """

  if day2_open_door:
    me "This damn door doesn't even move!"
  else:

    "It doesn't matter how hard I try to stop Kanae, I can't do anything"

  hide my_kanae worried soft
  with dissolve

  menu:
    "Perhaps if I..."

    "Break the window":
      $ day2_break_window = True

    "Move to the back of the car":
      $ day2_break_window = False

  if day2_break_window:

    stop sound fadeout 1.0
    $ renpy.pause(delay=0.6)
    play sound punch

    hide my_kanae worried soft
    with hpunch
    $ renpy.pause(delay=0.6)
    play sound bones
    $ renpy.pause(delay=1.7)
    play sound wind fadein 1.0 fadeout 1.0 loop 

    "I try to punch the window to break it"
    "It hurst almost like if I've broken all my fingers"
  else:

    "I try to move to the back seat of the car"

  scene bg flash
  with ImageDissolve(flash_img, 0.3)

  play sound thunder

  scene bg road car cooled
  with ImageDissolve(road_car_cooled, 1.0)

  $ renpy.pause(delay=1.4)

  play sound glass_cracking
  $ renpy.pause(delay=1.3)
  play sound wind fadein 1.0 fadeout 1.0 loop 

  """
  No...{w=0.6} No...

  Not again.
  """

  $ renpy.sound.set_volume(0.05, channel='sound')
  play sound beeep fadein 1.0 fadeout 1.0 loop

  """
  The silence covered all around, followed by a whirring sound that penetrated my ears and reached my head with such force that I thought it was going to explode
  """

  "..." "{i}.oot flesym em ti od evael ot evah ton od tub esa yadot elP sdne ...rosseforP sihT{/i}"

  $ renpy.sound.set_volume(0.15, delay=2.0, channel='sound')

  scene bg dark
  with fade

  """
  The beeping makes me close my eyes and grab my head by the pressure that exerted

  I know this feeling. Makawa!
  """

  stop sound fadeout 4.0

  """
  What's happening now?

  I know I have my eyes open, but I can't see anything

  I feel like I'm floating. Am I falling? 
  """

  """
  I bring my hands forward. There is the steering wheel of the car

  I try to touch the other seat, and I can feel Kanae's face and hair

  This is the closest thing to a vacuum I experienced until that moment
  """

  $ renpy.sound.set_volume(1.0, delay=2.0, channel='sound')

  "My veins... I can hear my blood"

  "I don't know if my eyes are open or closed"

  if day2_break_window:
    "I try to touch the window that I punched. It was there"
    "I am still inside the car"
  else:
    "I try to feel the handler of the door, but it's as locked as before"

  play sound wind fadein 1.0 fadeout 1.0 loop 

  "The wind... I feel it."
  "We are moving"

  scene bg road car
  with Fade(1.0, 2.0, 1.0)

  me "Oh fuck fuck fuck fuc..."

  "I pull the handwheel as fast as I can to avoid the two persons that are infront of me" with hpunch

  play sound glass_breaking
  $ renpy.pause(delay=1.2)
  play sound crash

  show my_kanae sad
  with dissolve
  with hpunch

  play sound crash
  $ renpy.pause(delay=1.2)
  play sound glass_breaking
  
  """
  I watched in a span that felt almost infinite as we rolled over and over again. 
  """

  "My eyes on Kanae watching her put her hands to the front trying to protect herself"

  hide my_kanae sad
  with dissolve

  """
  Crystals impacting our faces

  More rolls...
  """
  with hpunch
  play sound glass_breaking
  $ renpy.pause(delay=1.2)
  play sound crash
  
  """
  Everything stopped

  With my head hit and dizzy, I turn to see Kanae and she has her eyes closed... no

  No! I can't move

  I...{w=1.0} need...{w=1.0} Kanae!
  """

  scene bg dark
  with Fade(1.0, 2.0, 1.0)
  call day3 from _call_day3