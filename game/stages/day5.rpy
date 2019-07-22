label day5:

  """
  ...

  ....

  Warmth. I feel warmth on my face.
  """

  scene bg oyab house room morning
  with fade

  """
  I rested as if I had not slept in centuries.

  Incredibly, it was really pleasant to sleep in a dining chair.

  Kanae is still sleeping in the bed.
  """

  """
  She's totally off with such innocence that it'd be impossible to even think about everything that has happened to her

  Everything she has had to do.

  I've only witnessed a part of her story with what happened yesterday
  """

  if day4_instinct:

    """
    Having ended the life of those persons in such a way is something that is not even in a fairy tale
    """
  else:

    """
    Killing those persons like that, without hesitation

    I don't know what else she had done.
    """

  """
  While checking the room again trying to make the slightest noise to not wake up Kanae, I see in the distance through the window

  The desert arid plain that surrounds us, and between that plain desert approaches a figure running at full speed in the direction of the house. It was Oyab.
  """

  """
  He enters the house abruptly, I try to hear what Oyab says to Naila, who was on the ground floor
  """

  show kanae_alt surprised at center
  with dissolve

  show kanae_alt calm speak
  with dissolve

  kanae_alt "What is happening? WHy you are there?"

  show kanae_alt surprised
  with dissolve

  show kanae_alt surprised:
    xalign 0.8
  with move

  show oyab surprised at right:
    xalign 0.2
  with move

  oyab "We have to go. NOW!"

  play music solo_music fadein 1.0 fadeout 1.0 loop

  show kanae_alt normal
  with dissolve

  show oyab mad
  oyab "I don't know who you fucked in the city, but a lot of crows are coming for you... the cops"
  oyab "They're too many"

  hide oyab mad
  hide kanae_alt normal
  with dissolve

  scene bg oyab house
  with fade

  show oyab speaking soft at right:
    xalign 0.8
  with dissolve

  if not day4_they_suffered and day4_instinct:
    show keeper soft worried at center
    with dissolve
  
  show kanae_alt normal at left:
    xalign 0.2
  with dissolve

  me "How they could have found us?"

  show kanae_alt speaking
  with dissolve

  kanae_alt "That does not matter now, we have to go"

  show kanae_alt normal
  with dissolve

  if not day4_they_suffered and day4_instinct:

    show keeper surprised
    show oyab surprised
    keeper "They are too close, what are you gonna do Oyab?"
    show keeper soft worried
    show oyab speaking soft

    oyab "Don't worry. Everything'll be fine"

    show oyab winking
    oyab "Get dinner ready, Nai. I'll be right back."

    show keeper soft sad
    keeper "Oyab..."

    show oyab speaking soft
    oyab "Let's go."

    hide keeper soft sad
    with dissolve

  else:

    oyab "The twat is right, we have to go"

    show oyab surprised

    me "What about Naila?"

    show oyab speaking soft

    me "She'll be ok. They are coming for you. So I just have to get you far from here."

  hide oyab speaking soft
  with dissolve
  hide kanae_alt normal
  with dissolve

  """
  Another chase, This is never going to stop
  """

  scene bg oyab house faraway
  with fade

  """
  They are too close
  """

  me "It doesn't matter if we keep running, they are too close"

  show kanae_alt normal at center
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt "Stop!"
  kanae_alt "You are right, Professor."

  show kanae_alt normal
  with dissolve

  show kanae_alt normal at left:
    xalign 0.2
  with move

  show oyab normal at right:
    xalign 0.8
  with dissolve

  show oyab speaking soft

  oyab "So what's your plan?"

  show oyab surprised

  show kanae_alt speaking
  with dissolve

  kanae_alt "Step back."

  show kanae_alt normal
  with dissolve

  "She stands in front of us and takes a totally firm stance separating her feet and raising her mutilated hand in front of her"

  hide oyab surprised
  with dissolve

  show kanae_alt normal at center
  with move

  show kanae_alt focus
  with dissolve

  """
  She concentrates with her eyes closed

  Suddenly a current of air begins to feel around us making her hair wave

  This current gathers towards her in a swirling way as it intensifies. 
  """

  python:
    renpy.pause(delay=1.0)

  show kanae_alt loud speaking
  with Dissolve(0.3)
  with hpunch

  show bg oyab house faraway dust
  with Dissolve(0.3)

  play sound wind_crash fadein 0.5

  """
  A big wave of winds goes in the direction of the polices that came for us
  """

  show kanae_alt normal
  with dissolve

  play sound crash
  play sound crash

  """
  Kanae paralyzed some pieces of the vehicles that were approaching to us, making a total disaster to the caravan

  Kanae's fingers weren't marked. At the moment nobody died.
  """

  show kanae_alt normal at left:
    xalign 0.2
  with move

  show oyab surprised at right:
    xalign 0.8
  with dissolve

  oyab "What the hell was that?"

  """
  We can't stay in this place 

  Even though Kanae has managed to stop most of them, I can see that she is exhausted by such action

  I was our only way out
  """

  me "We should go now!"

  scene bg dark
  with fade

  """
  I have to focus, I have done it before, I can do it again.
  """

  $ renpy.music.set_volume(0.0, delay=2.5, channel='music')

  scene bg flash
  with ImageDissolve(flash_img, 0.3)
  scene bg town morning
  with ImageDissolve(town_morning, 0.3)
  with Fade(0.1, 0.0, 1.5)

  """
  I brought us to the town where the Supervisor died.

  The only one who notice us is a homeless is looking at us from some cardboard next to where we were

  It seemed that he lived there. However, it doesn't give us more attention.

  We are close to Kanae's hospital. My Kanae.
  """

  $ renpy.music.set_volume(1.0, delay=2.5, channel='music')

  show oyab surprised at right:
    xalign 0.8
  with dissolve

  show kanae_alt normal at left:
    xalign 0.2
  with dissolve

  show oyab speaking soft
  oyab """
  You are really stupid, lunatic midget

  How the hell are you going to destroy all those patrols?

  Now they aren't only looking for you, they are also looking for me and for a much greater disaster... 

  Anyway, how did we end up here?
  """

  show kanae_alt focus
  with dissolve

  python:
    renpy.pause(delay=0.5)

  show kanae_alt speaking
  with dissolve

  show oyab surprised
  kanae_alt "It does not matter how we ended up here, you would not understand it."

  show kanae_alt normal
  with dissolve

  show oyab speaking soft
  oyab "Whatever... What is the plan now, pair of geniuses?"

  show kanae_alt speaking
  with dissolve

  kanae_alt "It does not matter what we choose, there is already a plan in progress and was not even communicated to us, Is not it, Professor?"

  show kanae_alt normal
  with dissolve

  me "Listen, I know I can help Kanae."

  if day4_instinct:

    me "After what happened yesterday don't you think we can do it?"

    me "You said it yourself, that was different to all the other times"

    show kanae_alt speaking
    with dissolve

    kanae_alt """
    It was, but we should not trust in this, Professor.

    How could be that, we can save someone's life, but have to take the life of other person instead.
    """

    show kanae_alt normal
    with dissolve

    
  else:

    me "I don't know how, I just feel it."

    me "Kanae, you said that we can feel things others don't with this curse."

    show kanae_alt speaking
    with dissolve

    kanae_alt """
    I never said anything about healing someone.
    """

    show kanae_alt normal
    with dissolve

    me "I know, but you said that this can be like a muscle. Perhaps if we train it, it can do it."

    show kanae_alt speaking
    with dissolve

    kanae_alt """
    Until you are able to do it, should not Kanae stay in the hospital?

    She is safer there.
    """

    show kanae_alt normal
    with dissolve

    me """
    The doctors said that she isn't recovering

    They don't know why, perhaps I can do it.
    """

  me "I know. I am not asking you to trust in this, I am asking you to trust in me, Kanae."

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I do not like it.
  """

  show kanae_alt normal
  with dissolve

  show oyab surprised
  oyab """
  You'll end up dead, you must be very stupid to go to that shit again

  I don't know how they'll handle things, but I'd secure that girl's room, even more after what has just happened.

  Hell, you're taking us straight to jail...
  """

  me "You are shitting your pants, Oyab. You wouldn't left us even if you wanted."

  show oyab smile malicious
  oyab "Don't be too corky, Professor."
  show oyab normal
  oyab "Where are we going then?"

  hide oyab normal
  hide kanae_alt normal
  with dissolve

  scene bg hospital front
  with fade

  show oyab normal at right:
    xalign 0.8
  with dissolve

  oyab "That was quite easy, there were no cops no anythin"

  show kanae_alt normal at left:
    xalign 0.2
  with dissolve

  show kanae_alt speaking
  with dissolve

  show oyab surprised

  kanae_alt """
  Do not be too corky, Oyab.

  Professor, this is like the other times

  The police stoping the investigations, everyone leaving us free...

  Be careful.
  """

  show kanae_alt normal
  with dissolve

  show oyab speaking soft

  oyab "What's she talking about?"

  me "We need to know what the police have about us."

  """
  Kanae is right, the strings are moving for us
  """

  oyab """
  It's weird, we didn't saw any officers on our way here, but look at this thing

  It looks like an damn police station
  """
  
  hide oyab speaking soft
  with dissolve

  show kanae_alt normal at center
  with move 
  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Professor, you do know that this is crazy. We both know.

  He wants to prove us

  There are seven officers that I can see. They are covering all the ways to enter.
  """

  show kanae_alt normal
  with dissolve

  oyab "It'd be good if we could hear what they say, wouldn't be?"

  me "Yes.. where the hell did you went?"

  show kanae_alt normal:
    xalign 0.2
  with move

  show oyab normal at center
  with dissolve

  oyab "Shopping"

  "..." "{i}Main entrance is clear, {b}Wolf-4{/b} is returning{/i}"

  me "Did you stole a radio?"

  show oyab winking

  oyab "We had to know what they where saying didn't we?"

  show oyab normal

  me "I am not gonna ask how did you did it."

  show kanae_alt speaking
  with dissolve

  show oyab surprised

  kanae_alt """
  Even knowing what they say or know about us, is not going to help us enter the hospital

  There are to many cops.
  """

  show kanae_alt normal
  with dissolve

  show oyab speaking soft

  oyab "I have to do everything for you, isn't?"
  oyab "Hold the radio, if something goes wrong, run the hell out of here."

  hide oyab speaking soft
  with dissolve

  show kanae_alt normal at center
  with move

  "..." "{i}{b}Eagle-2{/b}, report{/i}"
  "..." "{i}Sector clear{/i}"
  "..." "{i}...Wait, we have something{/i}"

  oyab "Hey... fuckers!"
  oyab "I can bet your rifles smell like the tip of your asses haha"

  "..." "{i}Drunk guy at the entrance{/i}"
  "..." "{i}{b}Carlo-1{/b} care of him{/i}"

  """
  It seems they don't even know who he is.
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  He does not appear as a suspect, that is why the police is acting calm with him
  """

  show kanae_alt normal
  with dissolve

  "..." "{i}{b}Carlo-3{/b} we need back up, the guy is a pain in the ass{/i}"
  oyab "{i}Ya Carlo, your ass as well haha{/i}"

  me "This is our chance"

  stop music fadeout 4.0

  """
  We walk as if we were two more visitor
  """

  hide kanae_alt normal
  with dissolve

  scene bg hospital corridor
  with fade

  """
  There she is, My Kanae. Her doppelganger.
  """

  show kanae_alt normal at center
  with dissolve

  show kanae_alt surprised
  with dissolve

  me "You never saw another you. Another version of yourself"

  show kanae_alt speaking
  with dissolve

  kanae_alt "This was due to the accident?"

  show kanae_alt normal
  with dissolve

  play music main fadein 3.0 fadeout 1.0 loop

  """
  She ask, placing her hand on the glass
  """

  me """
  If I control the flow of time

  If I can focus on certain parts of her body, perhaps I can make heal the parts that are damage

  Perhaps that could help her to recover
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt "Those are a lot of {i}if{/i} and {i}perhaps{/i}"

  show kanae_alt normal
  with dissolve

  me "I know."

  show kanae_alt speaking
  with dissolve

  kanae_alt "It is risky"

  if day4_instinct:

    kanae_alt """
    The skill we used yesterday we did not even knew we had it, it was just luck that it ended like that.

    This may not give us the same opportunity. Are you sure you want to do it?
    """

  else:

    kanae_alt """
    You want to join the skill that I used in the dessert to try something you do not even know if we can do.
    """

    show kanae_alt normal
    with dissolve

    me "I know we can. I have the feeling inside me telling me that we can do this."

    show kanae_alt speaking
    with dissolve

    kanae_alt "It is really dangerous, Professor. I hope you know what we are doing."

  kanae_alt "Besides, we must find two other people to return the clock, if not, who could pay the price is my other self"

  show kanae_alt normal
  with dissolve

  hide kanae_alt normal
  with dissolve

  scene bg hospital room
  with fade

  """
  In front of me, while I take the hand of the version of my world, is the other Kanae
  """

  if day4_instinct:
    "As yesterday, I put my right hand on Kanae's forehead, while she is lying down with a respirator that runs down her esophagus."
  else:
    "I put my hand on her forehead, while I see the other Kanae do the same. Still undecided about whether to continue or not."

  show kanae_alt normal at center
  with dissolve

  show kanae_alt surprised
  with dissolve

  kanae_alt "It is madness. I do not know what might happen when she sees me."

  show kanae_alt normal
  with dissolve

  me "It's something we have to care later"

  show kanae_alt surprised
  with dissolve

  kanae_alt "I do not think I can do it, Professor. I feel tired."

  show kanae_alt normal
  with dissolve

  """
  Kanae is even paler than the other one, even though she is not in a coma.
  """

  show kanae_alt focus
  with dissolve

  show kanae_alt focus at left:
    xalign 0.2
  with move

  "..." "What are you two doing?"

  "Oh no."

  show kyoko alt speaking at right:
    xalign 0.8
  with dissolve

  kyoko "Professor, how did you appeared here?"

  show kyoko alt loud

  kyoko "That's Kanae? There are two of them?"

  if not day3_told_alan:
    show kyoko alt speaking
    kyoko "It's true... what you told me."

  me "Kyoko, please. Get out of here, is dangerous"

  stop music fadeout 3.0

  "As I said this, a very loud opaque sound flooded my ears"

  show kyoko alt shocked
  with dissolve

  """
  Seeing Kanae, she still is with her eyes closed. It must be her... the connection between them
  """
  with hpunch

  play sound earthquake fadein 1.0 fadeout 1.0 loop

  show kanae_alt focus at center
  with move

  """
  The entire room is shaking

  I approach little by little to hold again the version of Kanae version that was in a coma
  """

  kanae_alt "Do not touch her. She wants to live."
  with hpunch

  stop sound fadeout 3.0

  scene bg dark
  with Fade(2.0, 0.5, 0.3)

  """
  We are in the void

  I don't feel the pressure this time. He is not around

  If I focus enough, I can senses everything.

  I feel the next day. The morning.

  There are the three of us watching each other, but that always happens

  Why always her?

  She always dies.

  She dies.

  One version, then the other.

  She always dies.

  Death. Death.

  I…

  There's something? Is it the end of the line?

  I feel something.

  It is a figure that I can't define, I don't understand it, but it quickly approaches to me
  """

  show thing normal:
    xalign 0.5 yalign 0.5
  with Dissolve(0.2)

  """
  I see a big strange shadow among an indescribable light surrounding me
  """

  menu:
    " "

    "Fight back":
      call day5_fight from _call_day5_fight_1
    "Escape":
      "No, I am not going to fall in your tricks"

  if dead:
    return

  """
  I can't get lost in that darkness

  Kanae needs me

  This is not my time!
  """

  play sound glass_cracking

  scene bg hospital room
  with Fade(0.1,0.1,0.3)
  with hpunch

  play sound glass_breaking

  """
  When I manage to open my eyes, I see that the Kanae of the other dimension was also pushed strongly against the wall
  """

  me "Kanae!"

  show kanae_alt normal at left:
    xalign 0.2
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt "I am fine. Go help her. She has just returned"

  show kanae_alt normal
  with dissolve

  "She was standing in front of her bed without the devices connected, but with her eyes half-dreaming and the clothes she had when the accident"

  show my_kanae halfdream at center 
  with dissolve

  my_kanae "Professor, you came back...{w=0.4} you did not abandoned me."

  "Her voice is cracking while her eyes close again"

  me "Yes, I came back."

  play sound glass_breaking

  hide my_kanae halfdream
  with dissolve

  hide kanae_alt normal
  with dissolve

  "Oh no no no..."

  show kyoko alt hurt at center
  with dissolve

  me "No no no Kyoko no."

  "I can see the blood going from her throat throug her breast"

  if not day3_told_alan:
    kyoko "Time...{w=0.3} you... {w=0.4}t{w=0.1}i{w=0.1}m..."
  else:
    kyoko "Professor... he{w=0.1}l{w=0.1}p m{w=0.1}..."

  me "Kyoko, hold on, you'll be fine."

  show kyoko alt dead 
  with dissolve

  me "No! Kyoko!"

  show kanae_alt normal at left:
    xalign 0.2
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt "She died, Professor. We have to go."
  kanae_alt "They are coming"

  show kanae_alt normal
  with dissolve

  me "God damnit!"

  hide kyoko alt dead
  with dissolve
  hide kanae_alt normal
  with dissolve

  scene bg hospital corridor
  with fade

  play music dramatic fadein 3.0 fadeout 2.0 loop

  """
  Having the Kanae of my reality on my shoulders, we started running through the hospital
  """

  "..." "{i}The suspects are inside the hospital, repeat, the suspects are inside the hospital{/i}"
  "..." "{i}This is {b}Wolf-4{/b}, don't let them leave the hospital.{/i}"
  "..." "{i}They are really dangerous, they took down an entire patrol{/i}"

  "Fuck, it doesn't matter where we leave, they'll be there to catch us"

  show kanae_alt speaking
  with dissolve

  kanae_alt "The back door, Professor. Now!"
  kanae_alt "Oyab!"

  show kanae_alt normal
  with dissolve

  hide kanae_alt normal
  with dissolve

  "I go with Kanae without asking"

  scene bg hospital front
  with fade

  "We kept running, but a car parked in front of us. It was Oyab."

  scene bg car chase
  with fade

  show oyab mad at center
  with dissolve

  oyab "All of ya are a mess, what the fuck happened back there?"

  show oyab surprised at left:
    xalign 0.3
  with move

  show kanae_alt normal at right:
    xalign 0.8
  with dissolve

  show my_kanae halfdream at right:
    xalign 0.7
  with dissolve

  show oyab mad
  oyab "The hell? Two lunatics midgets? You're going to need a lot of help, dude"

  show oyab speaking soft

  me "We need to get ride of the police"
  oyab "No shit Sherlock."

  "..." "{i}(…) suspects left the hospital with a hostage. Extraction with a deceased civilian(…){/i}"
  "..." "{i}Don't shoot, they have a hostage. I repeat, don't shoot! They have a hostage{/i}"

  """
  Thats Alan's voice

  We are a target

  We've caused great damage

  I have to think about something, because Oyab will not be able to continue this chase for long

  Kanae is not in a position to make any jump and her doppelganger is unconscious
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Professor, I do not know how it will turn out

  I have never tried to make a jump being so exhausted and with a vehicle in motion. Anything could happen
  """

  show kanae_alt normal
  with dissolve

  """
  I must try. It's our only way out
  """
  with hpunch
  play sound gun
  $ renpy.pause(delay=0.3)
  with hpunch
  play sound gun

  show oyab surprised
  oyab "HEYY! What the fuck?"
  show oyab mad
  oyab "You are supposed to not shoot! You didn't hear your boss?"

  show oyab speaking soft

  "I am not going to be able to make the jump if they keep shooting"

  show oyab mad
  oyab "It's the biker behind us, if you can take care of him you can put our asses out of this"

  show oyab speaking soft

  """
  If I stop his bike, at this speed he probably will die

  If I try to break the concret, I could stop all the police
  """

  menu:
    "What should I do?"

    "Stop Bike":
      $ day5_break_concrete = False
    "Break Concret":
      $ day5_break_concrete = True


  if day5_break_concrete:
    call day5_break_concrete from _call_day5_break_concrete
  else:
    call day5_not_break_concrete from _call_day5_not_break_concrete


  scene bg flash
  with ImageDissolve(flash_img, 1.0)

  scene bg dark 
  with Fade(1.0, 0.3, 0.5)

  $ renpy.music.set_volume(0.0, delay=2.0, channel='music')

  "I can't see where we are"

  scene bg flash
  with ImageDissolve(flash_img, 0.3)

  scene bg road night
  with ImageDissolve(road_night, 1.0)

  "We are all desorented"

  show kanae_alt normal at left:
    xalign 0.2
  with dissolve

  show kanae_alt loud speaking
  with dissolve

  $ renpy.music.set_volume(1.0, delay=2.0, channel='music')

  kanae_alt "Professor, watch out!"

  "I see that Oyab and my version of Kanae are in the middle of a road and a car is fast approaching"
  "I try to take them to make a jump again, but Kanae holds me with her mutilated hand"

  show oyab surprised at right:
    xalign 0.8
  show my_kanae halfdream at right:
    xalign 0.7
  with Dissolve(0.2)

  me "I have to save them, Kanae!"

  """
  Without her letting go, I try to hold Oyab and Kanae, but I only manage to catch one of them
  """

  hide my_kanae halfdream
  hide kanae_alt loud speaking
  with dissolve

  """
  With the car right in front of us, I make the jump to a point which I don't even know where it is
  """

  show oyab mad
  with Dissolve(1.0)

  scene bg flash 
  with Dissolve(2.0)
  stop music fadeout 2.0

  scene bg dark
  with Fade(1.0, 0.5, 0.5)

  python:
    renpy.pause(delay=1.0)
  
  "What happened?"
  "Where am I?"

  scene bg alan_house normal
  with Fade(0.3, 0.1, 4.0)

  "This place?"

  show my_kanae worried soft at center
  with dissolve

  me "Kanae!"
  me "Are you ok?"

  play sound door_close

  show my_kanae worried soft:
    xalign 0.2
  with move

  show alan old smiling closed eyes at center
  with dissolve
  show alan old normal
  with dissolve
  show alan old normal:
    xalign 0.8
  with move

  show alan old speaking

  "..." "Welcome back, you pathetic scum."
  show alan old normal

  call day6 from _call_day6