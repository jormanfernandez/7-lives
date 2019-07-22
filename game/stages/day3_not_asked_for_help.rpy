label day3_not_asked_for_help:

  me "I need to leave. We'll talk later."

  show supervisor speaking
  supervisor "Are you sure?"

  show supervisor normal

  me "You are with your car? Please, let me borrow it for now. I'll give it to you later"

  show supervisor speaking
  supervisor "Buddy, you don't look good. Sorry but.."

  show supervisor normal

  """
  I see cops on the street in front of us
  """

  me "Now!"

  """
  The cops start coming where we are
  """

  show supervisor speaking
  supervisor "Sorry, but I am not going to do that"
  show supervisor normal

  """
  I know I can reverse all this, I am sure of it

  I see his car close to us
  """

  play sound wapash

  show supervisor speaking
  with hpunch

  """
  I punched him and took his keys. I have to leave before the police catch me
  """

  hide supervisor speaking
  with dissolve

  """
  The police man took his gun and pointed at me, while I started running torwards the car
  """

  supervisor "Stop!"
  supervisor "Professor, stop!"

  "Police" "Don't move!"

  """
  I got in the car and did a turn at full speed
  """

  supervisor "My car!"
  supervisor "Stop!"

  """
  He's still coming for the car
  """

  hide supervisor speaking
  with hpunch
  play sound gun
  $ renpy.pause(delay=0.4)
  play sound gun

  """
  The Police started shooting at me
  """

  play sound gun
  $ renpy.pause(delay=0.4)
  play sound glass_breaking

  """
  What the fuck?
  """

  hide supervisor speaking
  with hpunch
  play sound gun
  $ renpy.pause(delay=0.4)
  play sound gun

  "Police" "Stop right there!"

  """
  I pull the accelerator at max
  """

  supervisor "Stop! St..."

  hide supervisor speaking
  with hpunch
  play sound gun

  #scream

  """
  The supervisor is on the ground

  There's blood in his shoulder... God damnit. It can't be

  I can reverse all this. I know I can...

  I know I can. I have to.
  """