label day6_easy_way_out:

  me """
  Kanae... I can't

  I can't keep doing this.
  """

  show kanae_alt surprised
  with dissolve

  """
  I point the gun at my head
  """

  me """
  If he wants to play with us, I am not gonna give him the chance

  I am not his toy.
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Professor, this is not the way. You said it yourself

  We can not let him win.
  """
  show kanae_alt surprised
  with dissolve

  me """
  Win?

  Win what?

  Everything is already lost, Kanae.

  Makawa and Itawa died, the timeline is lost. I can't make the jump and an explosion is surrounding us.
  """

  show kanae_alt sad
  with dissolve

  stop music fadeout 4.0

  me "My hands are full of blood... all because of me."

  kanae_alt "Professor... Please..."

  $ renpy.pause(delay=0.5)

  me "You wanted a surprise, isn't it?"
  me "What about this?"

  kanae_alt "NOOOOO{nw}"

  play sound gun
  with hpunch

  scene bg flash
  with Fade(0.1, 0.1, 0.1)
  with hpunch

  $ renpy.notify("... Pathetic")

  scene bg dark
  with Dissolve(0.1)

  $ renpy.pause(delay=2.0)