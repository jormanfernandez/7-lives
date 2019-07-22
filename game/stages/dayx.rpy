label dayx:
  
  play sound laugh_child

  """
  Laugh

  I hear children laughing.
  """

  play sound laugh_s
  $ renpy.pause(delay=10)
  stop sound fadeout 8
  
  """
  I don't know if I have my eyelids open or closed, but I keep hearing these laughs

  No, not anymore. They stopped.

  Now there is silence.

  Darkness and silence that keep me in an unknown room.

  I don't know if I'm breathing. Am I breathing? I don't think I am.

  What was the last thing that happened?

  I don't remember what happened.

  How did I got here?

  Questions and more questions. Always questions. Why no one answers?

  Nobody speaks, only me.

  And the laughs? They're gone, they're silent. Now there is silence.
  """

  "..." "{i}It's weird that you ask me, Kanae should talk of this more with you than with someone else. She sees you as a father.{/i}"

  "..." "{i}Ey... hello?{/i}"

  """
  Where am I?

  I can feel warmth on my face

  Can I open my eyes? 
  """

  play music happy_loop fadein 1.0 fadeout 1.0 loop

  scene bg main_living
  with Fade(0.1, 0.1, 3.0)

  show phone normal:
    xalign 0.5 yalign 0.5
  with dissolve

  supervisor "{i}Colleague? Are you ok?{/i}"

  """
  Wait. I've seen this, you're not going to fool me
  """

  stop music fadeout 0.5
  play sound wind fadein 2.0 fadeout 1.0 loop

  supervisor "{i}...{/i}"
  supervisor "{i}I see...{/i}"
  supervisor "{i}I see.....{/i}"
  supervisor """
  {i}Kanae knew everything that was going to happen. She was a smart girl.{/i}

  {i}I liked her, it's pity that you left both of her versions in that explosion{/i}

  {i}Because you killed them too, you know? Both two, you also killed them{/i}
  """

  me "No, I didn't left them. You took me"

  supervisor """
  {i}Are you sure? I told you the renderization was over, but here you are.{/i}

  {i}You aren't with them. You just saved your ass.{/i}

  {i}Still, I don't know how you did it. You should be dead.{/i}
  """

  "No, I am not dead. I am here. I hear you. I can handle this."

  supervisor "{i}Can you?{/i}"

  me "Shut up!"

  stop sound fadeout 1.0

  show phone normal at left
  with MoveTransition(0.1)

  play sound glass_breaking

  hide phone normal
  with Dissolve(0.1)
  with hpunch

  "No. I know that this isn't everything."

  "..." "Since that day everything has been put on stage, but you have always had the final choice"

  "That voice, I recognize it."

  scene bg itawa_house_front
  with dissolve

  play sound wind fadein 2.0 fadeout 1.0 loop
  play music dramatic fadein 1.0 fadeout 1.0 loop

  show itawa_old serious at center
  with dissolve

  itawa """
  You know. Don't try to blame anyone else for your mistakes, because this is the cause of your actions. I am your fault.
  """

  me """
  Mrs. Itawa...

  No... No. You are not my fault. I never wanted to kill you.

  I didn't wanted to kill you or Makawa.

  He pushed me into that situation and Kan...{nw}
  """

  show itawa_old mad screaming
  itawa "LIES!"

  show itawa_old mad serious
  itawa """
  You know you wanted to face Makawa
  """

  show itawa_old mad screaming

  itawa """
  {b}FACE YOUR ACTS!{/b}
  """

  show itawa_old mad serious

  itawa """
  Don't shield yourself on my girl. Look what you did to her.

  Look what you did to me. My blood is your fault
  """

  hide itawa_old mad serious
  with Dissolve(1.0)

  """
  Itawa's voice grew louder with each scream she made, while I find myself immobile in front of this woman who makes me see the result of her spilled blood
  """

  "..." "Are you a {b}monster{/b}?"

  """
  That voice... is a childish voice, but I feel that I recognize it
  """

  show makawa_kid sad at center
  with dissolve

  "..." """
  Long ago a monster attacked my house. I fled.

  His face is in my memory.
  """

  show makawa_kid surprised
  show bg itawa_kyoto_house_fire
  with ImageDissolve(itawa_kyoto_house_fire, 3.0)

  "..." """
  You look like him. 

  Are you that {b}monster{/b}?
  """

  me "Makawa?"

  hide makawa_kid surprised
  with dissolve
  show makawa_old normal at center
  with dissolve

  show bg itawa_inner_house
  with ImageDissolve(itawa_inner_house, 1.0)


  show makawa_old speaking normal
  makawa_old """
  You had the opportunity to leave

  You had the opportunity to come back and, perhaps, to make the things differently, but you wanted to end with me.

  You wanted Kanae for you, didn't you?
  """

  show makawa_old normal

  me """
  That's not true

  I just wanted her to be safe, that's what I always tried.

  I never asked to be in this sick game, I never asked for this.

  I never asked for it.
  """

  hide makawa_old normal
  with dissolve

  """
  I can't control my emotions, I feel my mind creak. I just tried to help her.
  """

  stop music fadeout 4.0
  stop sound fadeout 4.0

  scene bg dark
  with Fade(3.0, 0.1, 1.0)

  my_kanae """
  You wanted to be with me, right, professor?
  """

  show white:
    xalign 0.5 yalign 0.5 alpha .1
  show my_kanae blushed at center
  with dissolve

  my_kanae """
  You got rid of Makawa, also from Itawa, because you wanted to be with me. So I was only yours.
  """

  menu:
    " "
    "Yes":
      $ dayx_for_kanae = True
    "No":
      $ dayx_for_kanae = False

  if dayx_for_kanae:
    "I... I don't..."
    play sound laugh_child
  else:
    my_kanae "Don't lie, Professor."

  show my_kanae face_destroyed
  with Dissolve(1.5)

  my_kanae "You wanted me to be only yours."

  menu:
    " "
    "Yes":
      $ dead = False
    "Yes":
      $ dead = False
    "Yes":
      $ dead = False

  my_kanae "Entirely yours"

  menu:
    " "
    "Yes":
      $ dead = False
    "Yes":
      $ dead = False
    "Yes":
      $ dead = False

  hide my_kanae face_destroyed
  hide white
  with dissolve

  $ renpy.sound.set_volume(0.3, channel='sound')

  play sound beeep fadein 2.0 fadeout 2.0 loop

  show makawa_old speaking normal at left:
    xalign 0.2
  with dissolve

  makawa_old "You took our lives one by one. We are your responsibility."

  show kyoko speaking serious at right:
    xalign 0.8
  with dissolve

  if not day3_told_alan:
    kyoko "I wanted to help you. You escaped without warnings"
  else:
    kyoko "You only cared for yourself"

  kyoko "You killed me"

  show itawa_old mad serious at center
  with dissolve

  itawa "You separated me from my family"
  itawa "You took away everything from me"

  hide itawa_old mad serious
  hide kyoko speaking serious
  hide makawa_old speaking normal
  with dissolve

  """
  There are all of them. Those who have lose their lives on this road talking one after another 
  """

  show my_kanae sad at center
  show white:
    xalign 0.5 yalign 0.5 alpha .1
  with dissolve

  my_kanae "You cheated on me, Professor. You said you would always protect me"

  "No... Kanae.."

  hide my_kanae sad
  hide white
  with dissolve

  show my_kanae sad at left:
    xalign 0.2
  show kanae_alt sad at right:
    xalign 0.8
  show white:
    xalign 0.5 yalign 0.5 alpha .1
  with dissolve

  kanae_alt "I believed in you, Professor. Why did you decide to leave us?"

  """
  I am kneeling in front of both Kanae's

  I know that I am guilty of this, I want to redeem what I have done.

  My tears fall when I see the faces of those who because of me have died, including the two little innocents I swore to protect.
  """

  hide my_kanae sad
  hide kanae_alt sad
  hide white
  with dissolve

  stop sound fadeout 3.0

  "..." """
  Interesting...

  How do they keep appearing? They shouldn't exist anymore.
  """

  $ renpy.pause(delay=1.5)

  "..." """
  Oh... I see.
  """

  me "I want to reverse this."

  "..." "Really?"

  me "They shouldn't have died."

  "..." "Give up on that idea."

  me """
  I have sacrificed so much

  Kanae sacrificed so much

  I want to reverse this.
  """

  show thing normal:
    xalign 0.5 yalign 0.5
  with Dissolve(3.0)

  "..." """
  You have survived because I have wanted

  You have reached this point because I have wanted

  You speak to me because I allow it.

  I must admit that this game has been interesting. I didn't though it would come here, I didn't though you would get here.

  I have to admit it. I didn't want you to die in that desolate house as Alan.

  I couldn't allow such a pathetic end to something so... entertaining.

  Since you were born, I've been here. Since you died, I've been here.

  This creation has been very entertaining to watch, it has given me great moments, but it is {b}time{/b} for it to end its journey.
  """

  me "Time?"

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)
  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  "..." """
  {b}Time{/b}. Ironic.

  All this time you have tried to understand how to use time in your favor.

  You have been able to control it, stop it at your whim. It feels good, isn't it?

  You see, when time stops, you should not be able to move at all, or move anything around you because, you know, everything is stopped.

  But it wouldn't have been so interesting if things had happened like this
  """

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)
  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  me "Why us?"

  "..." """
  This renderization was my experiment. You were my test.

  I tried other races, but nothing was as entertaining as with you.

  Sometimes I tried to give you a hand, only that you attacked what you didn't understood.

  I liked to leave it as a myth thinking that perhaps that would create something, but nothing. You destroyed what seemed strange to you.

  And after an infinity of repetitions, something new appeared.

  I came back to you to make you more like me
  """

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)
  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  "..." """
  Your only purpose was to investigate evolution of magnified neural networks on extra dimensions

  Everytime I setted a limit for you, you broke it. So I thought on giving you a really big jump in your evolution.

  What if you were me, but with your conscience?
  """

  me "You played with all of us"

  show thing normal:
    alpha 0.5
  with Dissolve(0.2)
  show thing normal:
    alpha 1.0
  with Dissolve(0.2)

  "..." """
  Kinda. Still, you didn't disappoint

  You, above all. You made me feel for the first time that I didn't knew everything about this renderization

  You made me feel... ignorant.

  The proof is that you are here, where nothing is written. Where everything starts. Convenient, isn't it?
  """

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)
  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  me "Why I can't see anything here?"

  "..." """
  You are radiation of energy around the void. You don't understand what is around you, but I can see you.

  The truth is... I don't know how you ended up here, and why all the other ones didn't got deleted. That's the biggest surprise of all.

  So, I am gonna make something for you.
  """

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)

  "..." """
  Imagine that you can start over again all the steps you have taken so far

  Do you think your path would be different from the one you have taken?
  """

  if _preferences.language != "spanish":
    $ renpy.notify("Choose that option Choose it.")
  else:
    $ renpy.notify("Elige esa opción. Elígela.")

  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  "..." """
  Of course, if you take this option, what guarantees that you have not done it yet?

  If you decide to return the steps, how can you know that you have not taken it before?
  """

  if _preferences.language != "spanish":
    $ renpy.notify("You haven’t done it, choose it")
  else:
    $ renpy.notify("No lo has hecho, elígela")

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)

  "..." """
  You can also go back to your timeline. Knowing that you are an experiment, knowing everything that happened, but you can't do anything else

  I'll make sure that Kanae, your version of Kanae, is there with Itawa and Makawa.

  What you fought, what you wanted, but knowing why it was taken away from you, and at least an idea of who did it.
  """

  if _preferences.language != "spanish":
    $ renpy.notify("Yes. Choose that. It is our option. Choose it")
  else:
    $ renpy.notify("Sí. Elige esa. Es nuestra opción. Eligela")

  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  "..." """
  As always, dear Professor. I only give the stage, you choose.
  """

  menu:
    " "

    "Go back":
      call dayx_go_back from _call_dayx_go_back

    "Start Again":
      call dayx_start_again from _call_dayx_start_again

    "My time" if day3_clear_mind and not day2_say_dream and day4_instinct:
      call end_time from _call_end_time