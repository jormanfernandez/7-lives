label dayx_go_back:
  
  me "I... I want to go back."

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)

  $ renpy.pause(delay=1.0)

  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  "..." """
  I see...

  Your simulation will be restored. Everything will be as if nothing happened.

  I will not shut it down. Even if you don't know it, I just want to be clear.
  """

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)

  "..." """
  Why not chose to change something, though?

  Perhaps I was wrong with you and all this was pure... how do you name it? Luck
  """

  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  "..." """
  Good bye, Professor. Go back to your dispensable life.
  """

  hide thing normal
  with dissolve

  me "Should I have chosen that?"
  me "It matters now?"
  me "I don't know."

  scene bg flash
  with Fade(0.1, 0.1, 3.0)

  play sound thunder

  scene bg school_morning
  with Fade(1.5, 0.1, 1.5)

  play music happy_loop fadein 2.0 fadeout 2.0 loop

  me "This is the school."

  show my_kanae normal at center
  with dissolve

  show my_kanae speaking
  my_kanae "Professor! Hi!"

  me "Kanae!"

  show my_kanae normal
  my_kanae "I am ready for class! haha"

  show my_kanae normal at left:
    xalign 0.2
  with move

  show itawa_old normal at right:
    xalign 0.8
  with dissolve

  show itawa_old speaking

  itawa "Hi, Professor. Good morning"

  show itawa_old normal

  me "Mrs. Itawa... you are okay"

  itawa "Yes. Thanks, I guess haha."

  show itawa_old speaking

  itawa "Makawa sends his regards. He wants to prepare a dinner tomorrow, you are invited directly by him."

  me "I see..."

  show itawa_old normal
  with None
  show my_kanae surprised
  with dissolve

  my_kanae "Are you okay, Professor?"

  me "I...{w=0.5} yes, Kanae. I am fine."
  me "Everything will be fine now."

  "Everything will be fine..."

  scene bg flash 
  with Dissolve(4.0)
  scene bg dark 
  with Fade(4.0, 2.0, 0.1)
  
  $achievement.grant("ACH_KNOWING_NOTHING")
  init:
    $achievement.register("ACH_KNOWING_NOTHING")
    $achievement.sync()

  $achievement.sync()

  stop music fadeout 8.0