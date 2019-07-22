label day6_shoot:

  $ day6_shoot = True
  
  me "Kanae, I am not gonna let you hurt her. I am serious."

  "I raise the gun an pointed her"

  show kanae_alt surprised
  with dissolve

  $ renpy.pause(delay=0.5)

  show kanae_alt speaking
  with dissolve

  kanae_alt """
  Professor, do not you understand?

  I am not the enemy. I am not the one who destroyed our lives

  Is her!
  """

  show kanae_alt loud speaking
  with dissolve

  kanae_alt """
  Due to the being that is inside her now, all our lives went to hell
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt "She is the enemy, Professor. And we can end this now."

  show kanae_alt sad
  with dissolve

  kanae_alt """
  For all that we have went through, all what I have done.

  I know is her
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt "And I am not gonna let you set her free"

  show kanae_alt normal
  with dissolve

  play sound bones

  my_kanae "Professor, my neck... help"

  "I can feel how the power inside her is rising."
  "She's gonna kill her"


  menu:
    " "

    "Shoot Kanae":
      $ dead = True

    "Convince her":
      $ dead = False

  if not dead:

    me """
    Kanae, I know that it seems like that, but it can't be

    This Kanae, this version of Kanae can't be him. He would've escaped from you already.

    We have been through so many things as you say, but we have to keep going.
    """

    return

  me "Kanae, step back. Stay away from her."

  show kanae_alt speaking
  with dissolve

  kanae_alt "No, Professor. This ends now."

  show kanae_alt normal
  with dissolve

  me "No...!{nw}"

  play sound gun

  scene bg flash
  with Fade(0.1, 0.1, 0.1)
  with hpunch

  scene bg dark
  with Dissolve(0.1)
  with Fade(0.1, 0.1, 3.0)

  "I don't want to see what I did."
  "I' am an idiot"

  scene bg alan_house exploding
  with Fade(0.1, 0.1, 3.0)

  me "Kanae?"

  show kanae_alt sad at center
  with dissolve

  kanae_alt "It can not be, Professor... Why you?"

  """
  Kanae says to me with a totally disappointed look and with some small tears coming out of her eyes
  
  She wasn't hit by the shot

  The small bullet is suspended halfway between her and me
  """

  kanae_alt "I trusted in you"

  me "Kanae... I..."

  show my_kanae normal at left:
    xalign 0.2
  with dissolve
  show kanae_alt surprised
  with dissolve
  show kanae_alt surprised:
    xalign 0.8
  with move

  my_kanae """
  The disappointment, the damage you did to her
  """

  show my_kanae speaking

  my_kanae """
  She didn't expect it in the least. Precisely what I wanted to see up close.
  """

  show kanae_alt speaking
  with dissolve

  kanae_alt "You..."

  show kanae_alt sad
  with dissolve
  with hpunch

  play sound wind_crash
  show kanae_alt sad:
    xalign 0.6
  show my_kanae normal:
    xalign 0.4
  with move

  "Kanae... it can't be"

  """
  Who until moments ago was totally drowned by the pressure exerted by her double on her neck, now speaks without problems

  Now it makes me realize how great has been the mistake I've done.
  """

  my_kanae """
  This has been... fun.

  As funny as you wouldn't imagine.
  """

  show my_kanae worried soft
  my_kanae "Even though it could have been better."

  show my_kanae normal

  if not day4_instinct:
    my_kanae """
    You destroyed Kanae's heart, you destroyed Naila's heart.
    """
  else:
    my_kanae """
    You destroyed Kanae's heart.
    """
  
  show my_kanae speaking
  my_kanae "Also Kyoko. Do you remember her?"

  show my_kanae normal

  stop music fadeout 3.0

  my_kanae "We could've had so much fun still, but now it doesn't matter."

  show my_kanae speaking

  my_kanae "You were close though, better luck next time."

  show my_kanae normal:
    xalign 0.7
  with MoveTransition(0.4)

  show my_kanae normal:
    xalign 0.4
  with MoveTransition(0.1)

  play sound glass_breaking
  
  show kanae_alt sad at left
  with MoveTransition(0.1)
  with hpunch
  hide kanae_alt sad
  with Dissolve(0.1)

  show my_kanae normal at center
  with move

  scene bg flash
  with Fade(0.1, 0.1, 0.1)

  play sound thunder

  scene bg dark
  with Dissolve(0.1)
  with Fade(0.1, 0.1, 3.0)