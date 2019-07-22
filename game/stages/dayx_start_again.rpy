label dayx_start_again:

  $ restart = True

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)
  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  "..." """
  Haha... So you think you can change something.

  Fair enough, I admire that.

  I just want you to know, if you mess up, everything will end.
  """

  me "Everything?"

  "..." """
  And all you know will be deleted
  """

  show thing normal:
    alpha 0.5
  with Dissolve(0.5)
  show thing normal:
    alpha 1.0
  with Dissolve(0.5)

  me "What? Wait, you can't do that"

  "..." "I can. And that's how'll be done."

  me "No, wait!"

  play sound wind_crash

  hide thing normal
  with Dissolve(0.1)

  if day0_touch_my_hole:
    "I see an extrange figure with the form of a hand appears on the darkness"

  play sound bones

  "My bones... everything starts to crumble"
  "I feel that I am ripped apart"

  scene bg dark
  with Fade(0.1, 0.1, 3.0)

  python:
    day1_walking_forest = False
    day1_stabbed = False

    day2_talk_kanae_police = False
    day2_say_dream = False
    day2_open_door = False
    day2_break_window = False

    day3_clear_mind = False
    day3_told_alan = False
    day3_ask_help = False

    day4_opened_eyes = False
    day4_instinct = False
    day4_they_suffered = False

    day5_iteration = 0
    day5_break_concrete = False

    day6_rancor = False
    day6_shoot = False

    dayx_for_kanae = False

  call day1 from _call_day1_1