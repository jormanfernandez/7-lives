label day6_alan_kills_me(scenary=1):

  if scenary == 1:
    jump .death_by_shot
  elif scenary == 2:
    jump .knife_in_stomach
  else:
    jump .sacrifice

  label .death_by_shot:

    "We start forcing"

    show my_kanae sad at left:
      xalign 0.2
    with dissolve

    my_kanae "Please, stop!"

    show alan old speaking
    alan "You bastard, I'll end this"

    show my_kanae worried soft

    play sound gun
    with hpunch
    $ renpy.pause(delay=0.3)
    play sound gun
    with hpunch

    stop music fadeout 3.0

    show red_layer:
      xalign 0.5 yalign 0.5 alpha .2
    with Dissolve(3.0)

    "I...{w=1.0} I can't..."

    show my_kanae sad 
    with dissolve

    my_kanae "No, no, no... Professor"

    show my_kanae sad at center
    with move
    show alan old speaking at right 
    with move
    hide alan old speaking
    with dissolve

    my_kanae "Resist, please."
    my_kanae "You said you would not leave me"
    my_kanae "Professor..."

    scene bg dark
    with Fade(4.0, 0.1, 0.1)

    my_kanae "PROFESSOR!"

    scene bg dark
    with Fade(2.0, 0.1, 0.1)

    return


  label .knife_in_stomach:

    "He takes a knife he had in his belt"

    show alan old sigh
    with Dissolve(0.1)
    with hpunch

    play sound stab

    "I... I feel something in my stomach"

    show my_kanae sad at left:
      xalign 0.2
    with dissolve

    my_kanae "PROFESSOR!"

    "Everything begins to fade..."

    stop music fadeout 7.0

    scene bg dark
    with Fade(3.0,0.1, 0.1)

    "I feel as my legs weakens"

    scene bg alan_house normal
    show my_kanae sad at left:
      xalign 0.2
    show alan old sigh at center
    show red_layer:
      xalign 0.5 yalign 0.5 alpha .2
    with Fade(0.1, 0.1, 3.0)

    alan "Now everything will end."

    show alan old smiling speaking closed eyes
    with dissolve

    alan "This nightmare is over."

    scene bg dark
    with Fade(2.0, 0.1, 4.5)
    return

  label .sacrifice:

    stop music fadeout 4.0

    "I have done so many bad things"

    me "Kanae... both of you. I am sorry"

    show alan old speaking
    alan "Believe me, this is the best."

    show my_kanae worried soft at left:
      xalign 0.2
    with dissolve

    show my_kanae sad 
    with dissolve

    my_kanae "Professor... why?"

    me "Because it is what has to be done."
    me "Everything will be fine, Kanae. Just look in the window"

    me "Its time, Alan."

    show alan old sigh
    alan "I'm glad you understand."

    my_kanae "NOOOOO{nw}"
    with hpunch

    play sound gun

    scene bg flash
    with Fade(0.1, 0.1, 0.1)
    with hpunch

    $ renpy.pause(delay=2.0)

    $ renpy.notify("Such a shame")

    scene bg dark
    with Dissolve(0.1)

    $ renpy.pause(delay=2.0)
    return