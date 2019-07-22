label day3_not_told_alan:

  me "It's really complicated. You will think I lost my mind."

  show kyoko normal speaking

  kyoko "With that preview and everything that has happened, what makes you think I already don't think that?"

  show kyoko normal

  "Sigh..."

  show kyoko normal speaking

  kyoko """
  Look. I am in your side. At least I try to

  But if youn don't tell me everything, I am not going to be able to defend you.

  Alan will cut your head an eat it for breakfast if you don't let me do my job.
  """

  show kyoko speaking
  me "I think I control time."

  show kyoko normal serious

  me "I know how it sounds... but I think I can."

  show kyoko speaking serious
  kyoko """
  You want to plead insanity?

  That's how you plead insanity
  """

  show kyoko normal

  me "I know. But I am not joking"

  show kyoko normal serious
  with dissolve

  python:
    renpy.pause(delay=1.0)

  show kyoko normal speaking
  with dissolve

  kyoko "How it started?"

  show kyoko normal

  me """
  It started in Kanae's house.

  I have in my mind all the memories of years that I shared with Makawa, Kanae and their mother

  I remember her clearly. All the time we spent
  """

  show kyoko speaking serious

  kyoko "But she died years ago. Makawa took care of that."

  show kyoko normal

  me "That's what seems like, but it wasn't him"

  show kyoko normal speaking

  kyoko "What do you mean by that?"

  show kyoko normal

  me "I...{w=1.0} I think it was me"

  "How she still is listening to all this?"

  show kyoko speaking serious

  kyoko "So... you killed Itawa"
  kyoko "How Makawa mix up in all this?"

  show kyoko normal

  if day2_talk_kanae_police:
    me """
    I don't know. When that happened I saw him

    He was a kid... I saw his terrified eyes
    """
  else:
    me """
    Alan told me that after the accident, the police in Japan covered up everything.

    They sended them here, and the rest you know it.
    """

  show kyoko speaking serious
  kyoko "And how do you control this... power?"

  show kyoko normal
  me "I don't know."

  show kyoko speaking serious
  kyoko """
  Yesterday happened that as well?

  You got lost in that and when you came, those people were there
  """

  show kyoko normal

  me """
  Yes...

  I don't know where they came from, but I think I recognized something in the body of that guy
  """

  show kyoko speaking serious
  kyoko "Besides your vomit?"
  show kyoko normal

  "...{w=0.3} Yeah, I forgot that"

  me "If I can see him again, I know..."

  show kyoko normal speaking
  kyoko "Hold on a sec"

  show kyoko speaking serious

  kyoko """
  You can't leave this room. Alan will hunt your ass down.

  I am not saying that I am into this story, but lets say that is real

  How do you pretend to put everything where it belongs?
  """

  show kyoko normal

  me """
  I don't know yet.

  Previously I've been able to move through time. That happened when I confronted Makawa

  It was totally unintentionally

  I entered in this empty space without intention and things happened
  """

  show kyoko normal serious
  with dissolve

  python:
    renpy.pause(delay=0.4)

  show kyoko speaking serious
  with dissolve

  kyoko "What about meditation?"

  show kyoko normal

  me "Meditation?"

  """
  She comes closer to the beth
  """

  show kyoko normal speaking
  kyoko """
  Concentrate, Professor.

  Focus on nothing more than my voice

  Now, close your eyes
  """

  scene bg dark 
  with fade

  kyoko "You are nowhere, Professor."