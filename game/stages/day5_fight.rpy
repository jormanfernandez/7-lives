label day5_fight:

  if day5_iteration < 1:
    "I feel the pressure increasing"
  elif day5_iteration == 1:
    "When I am"
  elif day5_iteration == 2:
    "My head is going to explode"
  elif day5_iteration == 3:
    itawa "You are doing it great, Professor"
  elif day5_iteration == 4:
    "I am a hrerors?"
  elif day5_iteration == 5:
    "Ahhhh!"
  elif day5_iteration == 6:
    my_kanae "Professor, help me!"
  else:
    
    $ dead = True

    "..." """
    I though you would be more interesting, and you were just an obstinated bag of meat.

    It's a pity.
    """

    "I... everything hurts"

    play sound bones

    "..." """
    Your bones will be cracking forever. Perhaps that way you will learn to not be that obstinated.

    This is not the end you though, didn't you?

    Such a shame. The other Kanaes should be more... interesting.
    """

    play sound bones

    "..." "Clean up before you leave... thanks."

    scene bg dark
    with Fade(0.5, 3.0, 0.5)
    return

  menu:
    " "

    "Fight back":
      $ day5_iteration = day5_iteration + 1
      call day5_fight from _call_day5_fight

    "Escape":
      "This is not going to work with me anymore."
      if day5_iteration == 5:
        $achievement.grant("ACH_PATIENCE")
        init:
          $achievement.register("ACH_PATIENCE")
          $achievement.sync()

        $achievement.sync()