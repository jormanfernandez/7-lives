label day4:


  itawa """
  You are safe, Professor.

  Remember, you are a hero
  """

  """
  I am not that sure

  I feel... lost.
  """

  play music happy_loop fadein 1.0 fadeout 1.0 loop

  scene bg itawa_house_front
  with fade

  show itawa_old normal
  with dissolve

  show itawa_old normal speaking
  with dissolve

  itawa "You are a hero. You are doing it great."

  show itawa_old normal

  me "Mrs. Itawa, I don't know. I think I lost my mind"

  show itawa_old serious
  with dissolve

  me """
  All the things that I've done

  Kanae...
  """

  show itawa_old sad speaking

  itawa "You are not lost"

  show itawa_old normal speaking
  with dissolve

  itawa "My child found you"

  show itawa_old normal

  me "She is Kanae?"

  show itawa_old normal speaking
  itawa "She is"
  itawa "Trust in her, Professor"

  show itawa_old normal

  hide itawa_old normal
  with dissolve

  scene bg dark
  with fade

  "Trust in her"
  "Why?"

  stop music fadeout 4.0

  scene bg shadow_tree
  with Fade(1.5, 1.0, 0.5)

  me "Where are we?"

  kanae_alt "Now we are far from the town, Professor."

  show kanae_alt normal
  with dissolve

  me "Kanae..."

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Professor, I know you are confused

  I know it is hard to understand this whole situation

  Even though I am Kanae, I am not the Kanae you saw in the hospital

  I am not your Kanae
  """

  show kanae_alt normal
  with dissolve

  "They are identical, but her voice"
  "Her voice sounds much more colder than the little girl I knew"

  play music main fadein 3.0 fadeout 3.0 loop

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I can see your ring

  You have gone through several circumstances. I am sorry for that.

  Although I myself witnessed one of them, it is still regrettable
  """

  show kanae_alt normal
  with dissolve

  me """
  You where the other one back in the road

  You appeared from nowhere... how?
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  The accident you had when you came back from seeing Oyab was entirely my fault

  The one you murdered was Oyab, but not the one of this reality. It was mine
  """

  show kanae_alt normal
  with dissolve

  if not day2_say_dream:
    me """
    You are from a different slice of time
    """

    show kanae_alt speaking
    with dissolve

    kanae_alt """
    You could say that.
    """

    show kanae_alt normal
    with dissolve
  else:
    me "How did you ended up there?"

    show kanae_alt speaking
    with dissolve

    kanae_alt "It is a long story"

    show kanae_alt normal
    with dissolve

    me "Well, I have plenty of time now."

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I know you have many questions, Professor

  I have the same charge as you. I have it for a little longer
  """

  show kanae_alt normal
  with dissolve

  """
  She, taking off a white glove that she had in her right hand, shows me that three of her fingers are marked with these rings of death

  Two of them with the seven places completely marked and the third with only two spaces.
  """

  if day3_clear_mind:
    me """
    You also has gone through a few things

    Those consumed spaces means that a life has been taken, isn't it?
    """

    show kanae_alt speaking
    with dissolve

    kanae_alt "Indeed, Professor."

    show kanae_alt normal
    with dissolve

    me "But, how?"

  else:

    me """
    You have this for more days than me. More than two weeks?
    """

    show kanae_alt speaking
    with dissolve

    kanae_alt "Yes, but the spaces not only mean days"

    show kanae_alt normal
    with dissolve

    "What?"

    show kanae_alt speaking
    with dissolve

    kanae_alt """
    Each space means the life of someone

    Have not you noticed that when a space is marked in your ring, someone die?

    Someone who was in contact with you before his death
    """

    show kanae_alt normal
    with dissolve

    me "But yesterday's space was marked without me killing someone"

    show kanae_alt speaking
    with dissolve

    kanae_alt "Are you sure?"

    show kanae_alt normal
    with dissolve

    "The Supervisor"
    with hpunch

    show kanae_alt speaking
    with dissolve

    kanae_alt "Every day, someone will die because of you"

    show kanae_alt normal
    with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  You do not have to kill them directly

  You do not have to put a knife in their stomach for the space to be filled.

  Your last action with them can conduce them to their death.
  """

  show kanae_alt normal
  with dissolve

  if day3_clear_mind:
    show kanae_alt speaking
    with dissolve

    kanae_alt "Every day, someone will die because of you"

    show kanae_alt normal
    with dissolve
  else:
    "It can't be. Then anyone can die because of me"

  me "That means... you"

  show kanae_alt speaking
  with dissolve

  kanae_alt "Yes."

  show kanae_alt normal
  with dissolve

  """
  I manage to visualize that her hand has less than five fingers
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I...{w=0.5} I tried to stop it

  I could not keep seeing that every day in some way or another

  In some way I...{w=1.0} he took a life
  """

  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=0.4)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I cut one of my fingers when only two spaces where left

  It did not worked
  """

  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=0.3)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  It jumped to another finger with all the spaces empty and everything started again
  """

  show kanae_alt normal
  with dissolve

  """
  These few days have seemed like an eternity, but they become nothing compared to what she must've lived
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  There is something else, Professor

  This is a kind of Machiavellian game. I have felt it. 
  """
  show kanae_alt normal
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Someone or something gave us the power to travel between these alternate realities

  And at the same time, with a sadistic and twisted purpose, made this curse that for each day that passes, a space is consumed

  Consumed, and with it, a life is taken
  """

  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=0.6)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Many things came to my mind

  If I ended my life maybe it would stop
  """

  show kanae_alt normal
  with dissolve

  "Wait what?"

  me "Are you serious? I am sure that's not the answer"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Yes, me neither.

  Probably will follow the trend of my hand

  Perhaps instead of going from one finger to another, it would pass from one person to another 

  I do not want to take that risk
  """

  show kanae_alt normal
  with dissolve

  "She really though about killing herself"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  This curse is mine and I must finish it
  """

  show kanae_alt normal
  with dissolve

  """
  Maybe that's why I have this curse now?

  Someone dared to take his own life, and as a way to find a guest, this curse jumped on me that afternoon in Itawa's house
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  One day I simply woke up and already had this mark on my hand

  I did not know what or why it had come out and I did not give it importance

  Unlike you, Professor, I was not changed from reality. 
  """

  show kanae_alt normal
  with dissolve

  me "How you do know that I changed from reality?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  We can sense it
  
  You still can not do it. But it is perceptible for us to detect someone who does not belong to this place. 
  """

  show kanae_alt normal
  with dissolve

  me "What? This is like a muscle? I need training or what?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  You could say, Professor.

  It is really difficult to learn how to use this

  More if we have to see with who we are, remembering that someone could die if they are close to us.
  """

  show kanae_alt normal
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  When the first life was taken I felt that everything was my fault

  I had never seen anyone die. At least until that moment
  """

  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=0.6)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  There were many investigations, but they all stopped very irregularly.

  Like if the police themselves wanted me to be free to continue this martyrdom

  At that time, the second event came

  With that person was when my first temporary jump happened

  I moved only a few hours back in time and returned, but keeping myself in my reality
  """

  show kanae_alt normal
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  You know what that feels like

  The uncertainty and maybe the thoughts of madness that comes to our mind
  """

  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=0.3)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  The being behind this I imagine that observes us in a twisted way with the simple aim of seeing us suffer in this perverse environment

  Almost a week later, on the sixth day, I met Oyab

  He told me that something had prompted him to leave the place where he was and look for someone with a tattooed hand in the shape of a ring. It was me
  """

  show kanae_alt normal
  with dissolve

  """
  This looks like a game

  Explore, discover or die.
  """

  me """
  You've pass through a lot of things, but why you were alone all the time?
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I know what you want to ask, Professor

  You are not in the story, not because you did not wanted to help me, Professor
  """

  kanae_alt """
  You were the first person who die for my scar
  """ with hpunch

  show kanae_alt normal
  with dissolve

  "What? I died?"

  me "How it happened?"

  show kanae_alt speaking
  with dissolve

  kanae_alt "You do not need to know."

  show kanae_alt normal
  with dissolve

  """
  It's hard to accept

  Even though I know it's possible that in hundreds of realities there may be some where maybe I wasn't born

  Although, that someone confessed to me that murdered me, generates a great unrest, even more so when it was Kanae herself who did it.
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  When having the second ring, I went through a lot of places to look for information to change this

  No one ever answered until one day, in the middle of the road that led to nothing, I told Oyab to stop the car.

  I needed to scream. I needed to get rid of that frustration I felt
  """

  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=0.3)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Just that the scream was so loud that everything around me turned black and I felt as if I had been moved to nothing.

  From there everything took a dizzying direction where Oyab was the one who helped me to understand even more this
  """

  show kanae_alt normal
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  The lives that I took from then on were the ones that Oyab was looking for

  Mostly they were people who were going to die very soon and I simply went to shorten their waiting periods. 

  This gave me a window to investigate with more conscience and tranquility
  """

  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=0.7)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I trained in the desert. Oyab helped me canalize everything.

  I could enter in those voids for a short period of time to make my research
  """

  show kanae_alt normal
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  That reasearch led me to conclude that the darkness that we witness when we are in those temporary voids is a place where space and time are interconnected

  When we are there, we can decide where to go.

  From there we can travel to different realities as well

  Places where I did not have an accident, places where I did not kill you because of this ring
  """

  show kanae_alt normal
  with dissolve

  me """
  You've felt it, haven't you, Kanae?

  When we are in that emptiness, you've felt his presence

  That pressure in our chest when darkness surrounds us. It's him, isn't it?
  """

# ############################
#  python:
#    renpy.notify(":P")
# ############################

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Yes, Professor

  That presence makes you feel that it is omnipotent.

  I feel and I think he is the one who gave us this curse.
  """

  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=1.5)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Think about time as the branches of the tree that is giving us its shadow

  Only that each of the branches is a timeline where circumstances can be very different. Those would be our realities
  """

  show kanae_alt normal
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  We humans are beings that live in four dimensions

  Our dimensions of height, width and volume, as well as in the dimension of time to which we all belong.

  Only that we see the time always going in one direction, we had never seen it go backwards

  We are not beings prepared for that.
  """

  show kanae_alt normal
  with dissolve

  me """
  Are you suggesting that the one who gave us this curse is from another dimension?
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  That is what it seems like.

  For him, our time must be just as irrelevant as a simple though.
  """

  show kanae_alt normal
  with dissolve

  """
  A dimension where time is so insignificant that it can be manipulated at will
  """

  me """
  The nothingness where we move when we travel in these temporary spaces must be a kind of passage or capsule

  It allows us to travel in other dimensions beyond our own, only that is incomprehensible to our thinking capacity.
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt "Yes, that is what I had in my mind."

  show kanae_alt normal
  with dissolve

  me """
  If you know what will happen at all times, under all circumstances, there'll be a point where you want something to be different

  An abnormality. Something he can't foresee. Maybe that's why we are gathered here
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  This being wants something that he has not been able to visualize before

  A god for us who wants to be more like us, but with totally torturous methods to get it.
  """

  show kanae_alt normal
  with dissolve

  me "How did we ended up here?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  The fact that we escaped from that road last night exhausted me completely.

  We jumped from a space to another, but stayed in the same reality and time.
  """

  show kanae_alt normal
  with dissolve

  me "We can do that?"

  show kanae_alt speaking
  with dissolve

  kanae_alt "Yes, you have done it as well..."

  show kanae_alt normal
  with dissolve

  "Itawa and Makawa. Of course."

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Perhaps you have noticed that performing these temporary jumps destroys our minds

  You should be careful, because if you try too hard, you may have a temporary collapse and your mind will be lost in time
  """

  show kanae_alt normal
  with dissolve

  "Lost in time?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  The truth is, I do not know if that is possible

  If I am honest, it is just a theory
  """

  show kanae_alt normal
  with dissolve

  me """
  I'll have it in mind

  On the other side, we need to go somewhere else. I have no idea where we are
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Me neither, I just jumped without visualizing where we would end
  """

  show kanae_alt normal
  with dissolve

  me "So we could have ended inside a building or something like that?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Probably, but it did not happened.
  """

  show kanae_alt normal
  with dissolve

  "Sigh..."

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  We have to go to find Oyab. Your Oyab. 

  He may have a better guide than the two of us

  It is a pity that you killed the one that came with me.
  """

  show kanae_alt normal
  with dissolve

  me "I didn't wanted to do it"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I know.
  """

  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=1.5)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  You must prepare yourself for the jump.

  I can not do it now, if I do, who knows where we would end up, or if we would even get somewhere or in a moment.

  Before I had control, now I am unstable.
  """

  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=0.5)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  It is very similar to meditate

  You have done it before, only that you have not controlled it. You have the strength to do it
  """

  show kanae_alt normal
  with dissolve

  show kanae_alt at right
  with move

  hide kanae_alt
  with dissolve

  $ renpy.music.set_volume(0.4, delay=2.0, channel='music')

  """
  Kanae approaches to me and grabs my shoulders by my back.

  Her voice, although it is quite dry, makes me calm down while closing my eyes
  """

  scene bg dark
  with Fade(1.0, 1.0, 0.5)

  kanae_alt """
  You are nowhere

  There is nothing around you

  You have been there before.

  You knows how it is. You are nowhere.
  """

  stop music fadeout 1.0

  scene bg dark
  with Fade(1.0, 1.0, 0.5)

  $ renpy.music.set_volume(1.0, delay=2.0, channel='music')

  """
  I am not listening anything

  My surroundings begin to fade
  """

  menu:
    " "

    "Open my eyes":
      $ day4_opened_eyes = True
      call day4_opened_eyes from _call_day4_opened_eyes

    "Keep my focus":
      $ day4_opened_eyes = True
      call day4_closed_eyes from _call_day4_closed_eyes

  kanae_alt """
  You are in the everything and nothing, Professor

  You can go to any point at any time.

  Do not try to go far behind

  The further you go, the more effort you must make and if you are not strong enough you could destroy yourself
  """

  play sound wind fadein 1.0 fadeout 1.0 loop

  """
  I know. I am no strong enough yet

  If I practice enough maybe in a moment I can go far enough back to...
  """

  kanae_alt """
  Professor, you must choose where to go faster

  You should not stay in that vacuum for so long. Your memories can be mixed having so much in your mind
  """

  """
  Maybe I can go back to that point, but now I can't lose myself in time without having solved all this
  """

  scene bg oyab motorhome eyelids
  with Fade(1.0, 1.5, 1.0)

  """
  According to Kanae, Oyab is the one who could give those answers that Kanae's Oyab knew

  I can see his house

  I feel Kanae's arms on my shoulders and her forehead on my back
  """

  kanae_alt """
  Now you must feel that you are there, Professor

  You are in that place.

  Feel it and now, make it true
  """

  stop sound fadeout 0.5

  scene bg dark
  with Fade(1.0, 1.0, 0.5)

  "I know I can"

  kanae_alt "Do it"

  scene bg flash
  with ImageDissolve(flash_img, 0.3)

  play sound thunder

  scene bg oyab motorhome
  with ImageDissolve(oyab_motorhome, 0.5)
  with hpunch

  "..."

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Congratulations, Professor.

  I know it is not easy, you must be exhausted.
  """

  show kanae_alt normal
  with dissolve

  me """
  I am

  I feel like I've just ran a marathon
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  It will pass.
  """

  play music solo_music fadein 3.0 fadeout 1.0 loop

  show kanae_alt normal
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Is this Oyab's house?

  It is different from the one I remember. This may be a problem.
  """

  show kanae_alt normal
  with dissolve

  me "Why do yo say?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  My Oyab wasn't living in a dumpster like this.

  This one is broken
  """

  show kanae_alt normal
  with dissolve

  "She knows everything just like that?"

  hide kanae_alt normal
  with dissolve

  "I need to know how to handle this"

  show oyab surprised
  with dissolve

  show oyab speaking soft
  with dissolve

  oyab "You came back, didn't ya? Fuckers, you are insistent"

  show oyab surprised

  me """
  Listen, I know you don't want to be part of this, but two days ago the girl with who I came here saw something in you, something more

  Today she is in a coma
  """

  show oyab mad

  oyab "Do you think I'm retard? I can be in a dumpster, but I can see that the girl is still with you and is on the other side of the trailer"

  show oyab surprised

  show kanae_alt normal at left:
    xalign 0.2
  with dissolve

  show oyab surprised at right:
    xalign 0.8
  with move

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I see...
  """

  show kanae_alt normal
  with dissolve

  show oyab speaking soft

  oyab """
  Leave me alone

  I don't want to play these childese games. I've had enough of things like that
  """

  show oyab surprised

  me "You have much more for us than this crap. I know it"

  show oyab speaking soft
  oyab """
  I don't care what you know. You just have to leave, that's it.
  """

  show kanae_alt speaking
  with dissolve

  show oyab surprised

  kanae_alt """
  We need someone to kill. You know people who need to die
  """

  show kanae_alt normal
  with dissolve

  """
  No, she can't be Kanae

  Who is this person?
  """

  show oyab speaking soft

  oyab """
  Who the fuck are you?

  You aren't the same girl who came a few days ago. What the hell happened?

  The one that came a few days ago had a broken spirit, but still wanted to put together the parts to build it and continue

  But you... you're just a motherfucking robot
  """

  show oyab mad
  oyab """
  What the hell did you do to this girl, dude?
  """

  show oyab surprised
  oyab """
  If I hadn't seen you how you behaved that day, I'd say you're another person...

  Wait... you are her twin or somethin?
  """

  """
  He clearly have no idea what he is talking about, although he looks more sober than before.
  """

  show oyab speaking soft

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Can you get those people who need to die or not?
  """

  show kanae_alt normal
  with dissolve

  """
  If we kill someone before the curse does, with could save an innocent

  However, the way in which she seeks to do it makes me rethink if all this okay 

  Would it be wrong to help someone die, even when is assured that they'll die in a few days anyway?

  Or should I hope that fate, that is totally out of our hands, do what it has to do and take the life of this person, who is not involved in any of this?
  """

  show oyab surprised
  oyab """
  You're serious about it, girl...
  """

  show oyab speaking soft

  oyab """
  I know some people who can please your weird fetishes

  Yours too, lizard
  """

  "What?"

  oyab """
  I only have great curiosity

  Why?
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  We have... something.

  This something causes a person to die around us if we have not taken someone else life before.

  It happens every day. We have tried to stop it, but it is impossible

  If you help us, you will give us one more day to investigate without worrying
  """

  show kanae_alt normal
  with dissolve

  show oyab mad

  oyab """
  You are both crazy

  I'll be in all the shit you want, but at least I don't have an idea as sick as that
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Wait!
  """
  show kanae_alt normal
  with dissolve

  show oyab surprised

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Do you recognize this?
  """
  show kanae_alt normal
  with dissolve

  """
  She, taking off the glove from her mutilated hand, shows the rings to Oyab
  """

  show oyab mad

  oyab """
  OUT! I DON'T WANT YOU HERE!

  You shouldn't be here

  I've seen what happens if I help ya and it isn't something that I'll like
  """

  show oyab surprised
  oyab """
  I have seen it... I don't want it.

  Out... get out.
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I know you have seen us.

  Just like you, we can also see more than normal. Beyond what everyone else sees

  It is a curse that we carry and that is why these rings are in our fingers.

  The big difference is that you do not have them, right?...
  """
  show kanae_alt normal
  with dissolve

  show oyab speaking soft

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  You are right, I am not the Kanae that came in the first instance with him and you are not the Oyab that I met.

  You do not approach him in anything, but I know you can try.
  """
  show kanae_alt normal
  with dissolve

  """
  She comments to him with a totally dehumanized voice, while the discomfort of the silence makes see Oyab's insecurity

  Kanae has been through a lot, I'm sure

  I just can't imagine what those situations were like to transform that innocent and happy girl that I've known so much into this machine that is determined to go over anybody to end this. 

  Maybe I could be one of her obstacles if the moment comes, but should I oppose to her?

  I've done nothing but destroy lives and she has gone much further than I ever thought
  """

  show oyab surprised

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  You do not feel that you have to prove anything to anyone, not even to yourself

  Maybe you are right to believe it, but at least you could do it to calm your mind of all those events

  Those ones that have been recordered without even having lived them
  """
  show kanae_alt normal
  with dissolve

  stop music fadeout 4.0

  """
  Oyab's face doesn't show any other expression
  """

  show oyab speaking soft

  oyab """
  I can take ya with someone. They're pretty close.

  You'll need two people, don't ya? I'll take you to them.
  """

  show oyab speaking soft at right
  with move
  hide oyab speaking soft
  with dissolve

  """
  Without mentioning anything else, he begins to walk to a town that looked far away his home. 

  I wasn't in a hurry to end someone else's life, but if I don't do it this way I'd surely end up causing an accident

  I could kill someone totally innocent again. Maybe even Kanae
  """

  show kanae_alt normal at center
  with move

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Now is not the time, but I would like to know what he saw about us, Professor

  When my Oyab found me, he never mentioned anything about having seen me, he just said he felt he should look for me
  """
  show kanae_alt normal
  with dissolve

  me "How did you knew this Oyab saw us then?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I did not.

  If he knew the ring, probably he felt the same things that my Oyab did.

  I just joined things and said to him what he needed to hear.
  """
  show kanae_alt normal
  with dissolve

  "She just manipulated Oyab to find those persons."

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  If something bad is going to happen to him, it will be for us, Professor.
  """
  show kanae_alt normal
  with dissolve

  me "Why you say that?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  He had visions about us.

  Probably time merged in his mind makind him see altern futures.

  He is one of the chosen ones by this being, just with a different purpuse.
  """
  show kanae_alt normal
  with dissolve

  hide kanae_alt normal
  with dissolve

  scene bg oyab house
  with fade

  play music happy_loop fadein 1.0 fadeout 1.0

  """
  After a long time walking marked by silence among all, we arrived at the urbanization where are the people Oyab commented

  He leads us to a fairly simple house where the dirt covered the entire entrance and the dust sprang from wherever it touched
  """

  #some knocks

  "..." "Coming!"

  show oyab speaking soft
  with dissolve

  show oyab speaking soft at right:
    xalign 0.8
  with move

  show keeper normal
  with dissolve
  show keeper big smile
  with dissolve

  "..." "Hi!"

  if day1_walking_forest:
    call day4_already_met from _call_day4_already_met
  else:
    call day4_not_met from _call_day4_not_met

  oyab "Naila, Where are they?"

  show keeper normal

  keeper """
  They wanted to rest

  They were very grateful for what you did to them last week. They were greatly relieved
  """

  """
  It seems that Oyab has taken care of some people for a while. 
  """

  oyab "Let me see them"

  show keeper soft worried
  with dissolve

  show keeper soft serious
  with dissolve

  keeper "They are inside. Upstairs. Come"

  hide keeper soft serious
  with dissolve

  hide oyab speaking soft
  with dissolve

  stop music fadeout 4.0

  show kanae_alt speaking at center
  with move

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I do not know her, Professor

  This is the first time I have seen her. My Oyab never told me about them
  """
  show kanae_alt normal
  with dissolve

  oyab "Hey! What are you two waiting? Come."

  """
  The whole house looked quite abandoned, in fact if I had not seen Naila, I'd be able to say that nobody lives here

  The sound produced by the staircase with each step we take leaves great evidence of the years that this house have
  """

  hide kanae_alt normal
  with dissolve

  scene bg dark
  with Fade(1.0, 1.0, 0.5)

  #staircase sounds

  scene bg oyab house room evening
  with fade

  "Oh, god..."

  show kanae_alt normal at left:
    xalign 0.2
  with dissolve

  show kanae_alt surprised
  with dissolve

  kanae_alt """
  I...

  I never knew about this.
  """
  show kanae_alt normal
  with dissolve

  play music dramatic fadein 2.0 fadeout 2.0 loop

  show oyab normal at right:
    xalign 0.8
  with dissolve

  show oyab speaking soft
  with dissolve

  oyab "You didn't knew your Oyab that much then."

  show oyab normal

  """
  I have never seen someone like that
  """

  show obo happy at center
  with dissolve

  """
  They are two bodies in one.

  Certainly they appeared to be quite young, I would estimate that they would be between fifteen and seventeen years old.

  In some areas they had open wounds and others with several bandages to protect them from dust and flies
  """

  show obo normal
  with dissolve

  show oyab speaking soft
  oyab """
  I've taken care of them since they were born

  Nobody else would, but I can't anymore. I can't see them like that
  """

  show oyab normal
  with None

  show obo happy
  with dissolve

  """
  These people have a nice and gentle behavior

  I can hear that they don't have the capacity to speak coherently
  """

  show oyab speaking soft
  with None

  show obo normal
  with dissolve

  oyab """
  The've been here for years. Before, I could handle with all they need

  Now I...
  """

  show obo happy
  with dissolve

  oyab """
  How you'd do it?

  Do you have a trick up your sleeve or will it be in cold blood?
  """

  """
  I haven't though about it
  """

  hide obo happy 
  hide oyab speaking soft
  with dissolve

  show kanae_alt normal at center
  with move

  me "How we are supossed to do it?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  It is complicated.

  Perhaps if one dies, the other does it instantly as well, that would be bad for one of us
  """
  show kanae_alt normal
  with dissolve

  """
  Take the life of a being that has never had one and has been confined all his existence by the deformities that he has
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I never knew about him... them, Professor.

  I had no idea that Oyab was going through this

  When I met him he did not mentioned these people, even when he helped me finish the grief of the dying
  """
  show kanae_alt normal
  with dissolve

  python:
    renpy.pause(delay=2.0)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I do not know if we can do it.

  It is very complicated because we do not know how each one will react to the death of the other.
  """
  show kanae_alt normal
  with dissolve

  """
  Kanae comments with her cold, fixed gaze, but even so, I feel the consternation of the whole situation in front of us
  """

  me "How did you though you will do it?"
  me "A knife in the neck? A pillow in his nose?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Yes. But is different in this ocassion.
  """
  show kanae_alt normal
  with dissolve

  "That's how Kanae has done it before."

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  It will be your first time doing it voluntarily, is not it?
  """

  show kanae_alt normal
  with dissolve

  me "Yes"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I have verified that we must be the cause of the death with the last action we have with that person. 

  That's why the Supervisor counted as a death done by you. 

  You pushed him in the direction of the policeman, but in this instance, we can not do that.

  We do not have pills to sedate them deeply, we have no alternatives.
  """
  show kanae_alt normal
  with dissolve

  """
  Seeing Kanae with that determined look makes me reconsider all options

  I certainly don't want to put a knife in the neck of these innocents
  """

  show kanae_alt normal:
    xalign 0.2
  with move

  show oyab normal at center
  with dissolve
  show oyab mad
  with dissolve

  oyab "What the hell are you talking that much?"

  show oyab speaking soft
  oyab """
  You'll do it or what? Why do you think so much?

  Don't tell me you are a fraud
  """

  """
  I see how Kanae tooks a knife that was in a table close to us
  """

  menu:
    " "

    "Knife in the neck":
      $ day4_instinct = False

    "Instinct":
      $ day4_instinct = True

  if day4_instinct:
    call day4_vanish_obo from _call_day4_vanish_obo
  else:
    call day4_kill_obo from _call_day4_kill_obo

  show oyab speaking soft at right:
    xalign 0.8
  with dissolve

  oyab """
  This is more than I thought

  Listen
  """

  stop music fadeout 2.0
  play music main fadein 2.0 fadeout 2.0 loop

  if day4_instinct:

    show oyab surprised
    oyab """
    Seeing how this happened is something that I never though possible.
    """
    show oyab speaking soft
  else:

    oyab """
    If I wouldn't've seen that ring being burned out of nothing I'd be killing you right now

    But know I can see that this is beyon us.
    """

  oyab """
  I have no idea what happened to you or how you have this... thing.

  I also don't know how I fell into this

  How those visions of both of you came to my mind
  """

  show oyab surprised

  oyab """
  It's clear that these goes beyond yourself

  What you have goes beyond anything that has happened in this world in all its history. I am sure of it.
  """

  show oyab speaking soft

  oyab "I... I couldn't do it myself"

  show oyab surprised
  me "What about Naila?"

  show oyab speaking soft
  oyab "She'll understand"

  show oyab surprised
  oyab """
  I can tell you've had a fucking day.

  You'd better rest today, and tomorrow I'll see who else will give you time
  """

  show oyab speaking soft
  oyab """
  Use this room. After all, it's already free and is the only one available

  I'll come in the morning.
  """

  hide oyab speaking soft
  with dissolve

  """
  Oyab starts down the stairs and leaves Kanae and me in the room
  """

  show kanae_alt normal at center
  with move

  show kanae_alt speaking
  with dissolve

  if day4_instinct:
    kanae_alt """
    This was different to all the other times
    """

    show kanae_alt sad
    with dissolve

    kanae_alt """
    I... I have done so many things.
    """

    me "Its okay, Kanae. This curse made us do things we regret."

  else:

    kanae_alt """
    It will be okay, Professor.

    Now we have to focus on stoping this madness.
    """

    show kanae_alt normal
    with dissolve

    me "I hope so"

    show kanae_alt speaking
    with dissolve

    kanae_alt "Oyab helped us more than I though, now is up to us."

  show kanae_alt normal
  with dissolve

  show kanae_alt normal:
    xalign 0.2
  with move

  show keeper normal at center
  with dissolve

  keeper "Hi... Oyab is already leaving"

  show keeper soft worried

  keeper "He told me what happened"

  show keeper soft serious
  with dissolve

  keeper """
  I... I have taked care of them for a few years

  They had a really hard life

  Please, tell me. Did they suffered?
  """

  menu:
    " "

    "Yes":
      $ day4_they_suffered = True

    "No":
      $ day4_they_suffered = False

  show keeper soft worried

  keeper "I see..."

  if not day4_they_suffered and day4_instinct:

    show keeper normal

    keeper """
    I'm glad

    Thank you, both of you.
    """

    show keeper soft cheerful
    keeper "You probably are hungry. I made this, hope you like it."

    """
    She brings enough food for Kanae and me. Rice, salad, juice.
    """

    show kanae_alt surprised
    with dissolve

    kanae_alt """
    Thank you, Naila

    I know that you care about him. Now he is happier.
    """
    show kanae_alt normal
    with dissolve

    show keeper normal
    keeper "Yes. I know. Thanks, Kanae."

    show keeper soft cheerful
    keeper "Eat. It will be good for you. I'll see you in the morning"

    hide keeper soft cheerful
    with dissolve

  else:

    show keeper soft serious

    keeper """
    I am sorry, I have to go.

    There's dinner. Bye.
    """

    hide keeper soft serious
    with dissolve

    play sound door_close

  show kanae_alt normal at center
  with move

  """
  The room becomes smaller than it was while Kanae and I settled down to rest

  I choose to sleep in a small chair that was close to Kanae, while she's sitting on the bed
  """

  hide kanae_alt normal
  with dissolve

  """
  In my thoughts there is only one person hanging around, I need to find her, to know how she is.

  I can't leave her, my Kanae, in that hospital
  """

  if day4_instinct:
    """
    If I made that these persons ended their time like that, maybe I can help her heal in a similar way

    What will be the limit? The more I learn of this curse, the more I realize the full potential.
    """

    show kanae_alt normal at center
    with dissolve

    show kanae_alt speaking
    with dissolve

    kanae_alt """
    It is dangerous, Professor.

    Do not get carried away by the euphoria that we have experienced with this new skill.

    Believe that you can... that we can control this is pure naivety

    Something granted by a bored and possibly almighty being will not be in our total control. Never
    """

    show kanae_alt normal
    with dissolve

    """
    Kanae is right, but I can't let that make me stop looking at her other version, the one of my reality

    Now I am more than determined to solve this.

    The moment has come to put the {b}time{/b} in our favor
    """
  else:
    """
    We have to see another way of doing this

    We can't keep stabbing persons to gain another day.

    Without Kanae's Oyab, we have to seek for answers ourselfs.
    """

    show kanae_alt normal at center
    with dissolve

    show kanae_alt speaking
    with dissolve

    kanae_alt """
    You are thinking on her, aren't you?

    Your Kanae.
    """

    show kanae_alt normal
    with dissolve

    me "Yes... maybe I can help her to recover"

    show kanae_alt speaking
    with dissolve

    kanae_alt """
    How?
    """

    show kanae_alt normal
    with dissolve

    me """
    I don't know. I just feel that I can. And I have to look for her.
    """

    show kanae_alt speaking
    with dissolve

    kanae_alt """
    Be careful, Professor. Having this curse can make you think a lot of things

    Some of them are things that have been put on your mind by that... being
    """

    show kanae_alt normal
    with dissolve

    """
    Perhaps she is right, but I can't shake this out of my mind.

    I know I can do it.
    """

  hide kanae_alt normal
  with dissolve

  stop music fadeout 4.0

  scene bg dark
  with Fade(1.0, 1.0, 1.0)

  call day5 from _call_day5