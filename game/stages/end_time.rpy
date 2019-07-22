label end_time:
  
  show thing normal:
    alpha 0.5
  with Dissolve(0.2)
  show thing normal:
    alpha 1.0
  with Dissolve(0.2)

  "..." """
  Wait, what are you doing?
  """

  scene bg time_madness animated
  with Dissolve(0.1)

  """
  My head starts to travel. I feel it out of here, I will not let you take me and do whatever you want with me
  """

  play music solo_music fadein 2.0 fadeout 2.0 loop

  scene bg flash
  with Fade(0.3, 0.1, 0.1)

  play sound thunder

  scene bg dark
  with Fade(1.0, 0.1, 0.1)

  $ renpy.pause(delay=2.0)

  """
  Where am I?

  I have to get out of this interdimensional vacuum

  I feel that my chest is going to burst while my limbs are pulled with superhuman strength
  """

  $ renpy.sound.set_volume(0.05, channel='sound')

  play sound beeep fadein 2.0 fadeout 2.0 loop

  show tree at center
  with dissolve

  """
  What's that?

  There are lines... they look like connectors.

  I feel... energy.

  I'm facing the everything and nothing

  Here I was born and died.

  Each of these lines is next to me

  My whole world is the tree of time that flows to take each of our steps from the beginning to the end

  I see everything and everyone. 
  """

  show thing normal at center:
    xalign 0.5 yalign 0.5
  with dissolve

  #cracks body

  """
  My whole body creaks and I begin to feel the tear of the pressure exerted by someone else

  You can't stop me now.
  """

  hide tree
  with dissolve

  """
  The center of the tree is nothing more and nothing less than yourself. 

  I know what I have contained since you gave me this strength, this ability.

  I know that this power is as big as you. That was your mistake
  """

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)
  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  $ renpy.sound.set_volume(0.15, delay=1.0, channel='sound')

  """
  The time to fix everything has arrived, your time has arrived
  """

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)
  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  """
  You've been dictating our ways since we opened our eyes for the first time, but today I refuse to continue being your little experiment
  """

  $ renpy.sound.set_volume(0.2, delay=1.0, channel='sound')

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)
  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  """
  Your mistake was to believe that we could not do this.
  """

  stop sound fadeout 1.0
  $ renpy.sound.set_volume(1.0, channel='sound')

  hide thing normal
  with Dissolve(0.1)
  with hpunch

  play sound thunder

  scene bg flash
  with Fade(0.3, 0.1, 2.0)
  with hpunch

  stop music fadeout 2.0


  """
  My whole body is torn, I feel how my limbs are detached one by one

  I'm in the center of everything, I'm the whole.

  It's time for each of us to have a new opportunity. We aren't your experiment.
  """

  $ renpy.pause(delay=2.0)

  scene bg kanae_room_morning
  with Fade(3.0, 0.1, 3.0)

  itawa "Kanae, hurry up!"

  show my_kanae normal at center
  with dissolve

  show my_kanae speaking
  with dissolve

  play music happy_loop fadein 2.0 fadeout 2.0 loop

  my_kanae "I am coming, Mama!"

  show my_kanae normal

  hide my_kanae normal
  with dissolve

  scene bg itawa_inner_house
  with fade

  show itawa_old normal at right:
    xalign 0.8
  with dissolve

  show itawa_old speaking

  itawa "Kanae, Makawa is waiting for you. You are gonna be late for school."

  show itawa_old normal 

  show my_kanae normal at left:
    xalign 0.2
  with dissolve

  show my_kanae speaking

  my_kanae """
  Yes, Mama.
  """

  show my_kanae normal

  my_kanae """
  I will be back at noon.
  """

  show itawa_old speaking
  itawa "I love you, my little girl."

  show itawa_old normal

  hide itawa_old normal
  with dissolve

  hide my_kanae normal
  with dissolve

  scene bg itawa_house_front_before

  show makawa_old normal at center
  with dissolve

  show makawa_old speaking normal

  makawa_old "Kanae, hurry up"

  show makawa_old normal:
    xalign 0.8
  with move

  show my_kanae normal at left:
    xalign 0.2
  with dissolve

  show makawa_old happy

  my_kanae "Do not be grumpy. I am already here."

  show makawa_old happy happy

  makawa_old "You will have to walk next time."

  show my_kanae speaking

  my_kanae "Nope, you will never leave me. You love me, haha."

  show makawa_old happy

  makawa_old "Cheater."

  show my_kanae normal

  """
  They are alive.

  She is alive.

  She laugh

  Laugh with the strength to continue one more day
  """

  scene bg flash 
  with Dissolve(4.0)

  $achievement.grant("ACH_END_OF_TIME")
  init:
    $achievement.register("ACH_END_OF_TIME")
    $achievement.sync()

  $achievement.sync()
  
  scene bg dark 
  with Fade(4.0, 2.0, 0.1)


  stop music fadeout 8.0