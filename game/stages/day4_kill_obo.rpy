label day4_kill_obo:

  show oyab surprised
  with dissolve

  python:
    renpy.pause(delay=0.4)

  show oyab speaking soft
  with dissolve

  hide oyab speaking soft
  with dissolve

  show kanae_alt normal at center
  with move

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  It is time, Professor.
  """

  show kanae_alt normal
  with dissolve

  """
  Damnit. I don't want to do it, but if I don't, I could kill someone else

  I took the last knife that was in the table
  """

  show kanae_alt normal:
    xalign 0.2
  with move

  show obo happy at center
  with dissolve

  show kanae_alt normal:
    xalign 0.3
  with move

  "She got close to him and grabbed one of his head."

  show obo normal
  with dissolve

  """
  I can see the wounds he has
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  It have to be at the same time, Professor.
  """

  show kanae_alt normal
  with dissolve

  me "There is no other option, Kanae?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  No.
  """

  show kanae_alt normal
  with dissolve

  show obo worried
  with dissolve

  "I... I don't know"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Now, Professor
  """

  show kanae_alt normal
  with dissolve

  $ renpy.music.set_volume(0.0, delay=0.5, channel='music')

  play sound stab
  $ renpy.pause(delay=0.2)
  play sound stab

  $achievement.grant("ACH_COLD_BLOOD")
  init:
    $achievement.register("ACH_COLD_BLOOD")
    $achievement.sync()

  $achievement.sync()

  scene bg dark
  with Fade(0.1, 0.5, 0.5)
  with hpunch

  scene bg dark
  with Fade(0.5, 1.0, 0.5)

  "Damnit... God Damnit"

  """
  The scar

  It hurt as hell
  """

  scene bg oyab house room evening
  with fade

  show kanae_alt normal at center
  with dissolve

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  It is done.
  """

  show kanae_alt normal
  with dissolve

  show kanae_alt normal:
    xalign 0.2
  with move

  show oyab normal at center
  with dissolve

  show oyab surprised
  with dissolve

  oyab """
  Your rings. They are burned now.
  """

  show oyab speaking soft

  oyab """
  Fuck.

  Let me take care of the body
  """

  $ renpy.music.set_volume(1.0, delay=3.0, channel='music')

  """
  Oyab puts a blanket on them and goes outside the room
  """

  show oyab normal at right
  with move

  hide oyab normal
  with dissolve

  show kanae_alt normal at center
  with move

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  I know it is not easy. The spaces burns harder everytime.
  """

  show kanae_alt normal
  with dissolve

  me "We killed them so we wouldn't hurt an innocent, didn't we?"

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Yes, Professor.
  """

  show kanae_alt normal
  with dissolve

  "I have to convince my mind of that."

  show kanae_alt normal:
    xalign 0.2
  with move