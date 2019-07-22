image thank_you es = "thank_you_es.png"
image thank_you en = "thank_you_en.png"

label final_credits:

  if _preferences.language == "spanish":

    show thank_you es at center:
      xalign 0.5 yalign 0.5
    with Dissolve(3.0)
  else:
    show thank_you en at center:
      xalign 0.5 yalign 0.5
    with Dissolve(3.0)


  $ renpy.pause(delay=4.0)

  hide thank_you
  with Dissolve(3.0)

  $ renpy.pause(delay=4.0)