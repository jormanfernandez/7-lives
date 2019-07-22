label day1_walking_forest:

  "I kept walking a little bit longer in the park"

  if day1_asked_garden:
   """
   Kanae's tears couldn't be faked. This is not a joke. I trust in here more than my self.
   """
  else:
   """
   Makawa's action were just weird. I know we weren't the best friends, but we never tried to punch each other.
   """

  """
  My mind has been playing tricks with me all along. I need to focus.
  """

  play music happy_loop fadein 1.0 fadeout 1.0 loop

  """
  While I am walking in the park, I see a teenager walking by along the way.

  I stayed back a little bit, watching where this girl was going
  """
  
  "..." "..."

  "..." "Can I help you?"

  "What? She is talking to me"

  "..." "I can see you..."

  "How?"

  show keeper soft serious
  with dissolve

  "..." "You are too obvious. Why are you following me?"

  "Actually, I don't even know."

  me "I was just walking by..."

  show keeper serious

  "..." "You are just a creep, aren't you?"

  me "I...{w=1.0} wait. No... I am not"

  show keeper cheerful

  "..." "Haha, don't worry. I saw you before you even knew I was here."

  show keeper soft cheerful
  "..." "I saw that you were just walking by"

  show keeper normal

  me "Well... then you are the creep."

  show keeper soft cheerful

  "..." "Yup!"

  """
  Who's this girl? She came from nowhere
  """

  show keeper normal

  me """
  I just need to clear my mind a little bit.

  Sometimes thoughs can overwelm you and you need to just dump everything and breath.
  """

  show keeper soft serious

  "..." "Yes. I understand how's that."

  show keeper soft cheerful

  "..." """
  I live far from here, but when I have the chance, I came here just to see this park.

  Sitting here just to leave all behind... Feeling the air around me.

  Nothing more matters. Just this place, this moment. As if it is frozen in time and it last forever.
  """

  show keeper normal

  """
  She is right... it feels so peaceful

  We sit on the road, just seeing all the trees around us.
  
  I put my head on the grass, feeling it in all my neck.
  """

  play sound wind fadein 1.0 fadeout 1.0 loop

  "..." "Do you feel it? It's like everything is frozen."

  """
  It seems like... it would be nice just to froze time, just for a little moment once in a while

  While layed on the grass, my eyes close on their own will
  """

  hide keeper normal
  with dissolve

  scene bg dark
  with Fade(0.5, 1.5, 0.5)

  """
  Everything that has happened its so weird

  All the memories that I have with Itawa and Makawa being a Dream.

  This ring shaped scar in my finger...

  What's all this?
  """

  stop music fadeout 4.0

  scene bg dark
  with Fade(0.5, 0.5, 0.5)

  "..." "Time passes so we can live"
  $achievement.grant("ACH_RIVER_OF_TIME")
  init:
    $achievement.register("ACH_RIVER_OF_TIME")
    $achievement.sync()

  $achievement.sync()

  stop sound fadeout 1.0

  scene bg dark
  with Fade(0.5, 3.0, 0.5)

  "... what? What happened?"
 
  scene bg park_evening
  with fade

  """
  It seems that I felt asleep... the girl isn't here anymore.

  I don't know how much time has passed.

  I put on my feets, streching after the nap. Actually it did helped me to calm my mind a little bit.
  """