label day0:
  
  stop music fadeout 1.0
  scene bg dark
  with Fade(0.5, 1.5, 0.5)
  
  scene bg school_evening
  with fade
  play ambient emptyness fadein 0.5 fadeout 0.5 loop

  play music happy_loop fadein 1.0 fadeout 1.0 loop

  """
  It was a pleasant afternoon, I was on my way home from work.

  Since I live close, I can walk. This helps me to relax. That way I can clear my mind. Being a high school teacher can be quite exhausting
  
  Dealing day after day with so many teenagers who believe that they manage their lives without help from anyone can exhaust you pretty quick.

  Seeing this sunset every day after leaving high school reassures me.

  Feeling the breeze that caresses my skin in such a soft and subtle way, that makes me rejoice for the view in front of my eyes with that orange sky on my way home.

  Crossing the block to get to my house, I managed to spot Mrs. Itawa's house. She is an old woman who moved to our urbanization a long time ago
  """

  scene bg itawa_house_front_before_evening
  with dissolve

  """
  She came from Kyoto accompanied by her two children. Makawa, the son, is a businessman. A guy who took seriously the issue of staying in shape

  Always wearing a nice suit with a rather peculiar mustache. He managed to found his own transport company. Half of the taxis that work in the city belong to him

  In the institute we had the incursion of a foreign student due to Mrs. Itawa's arrival. It was Kanae, her daughter.

  She is younger than Makawa by four years, so she has not finished high school yet. And yes, she's my student.

  She is a pretty applied girl, she has a snow-white skin and a hair as dark as ebony.

  I always take more time to return home because I keep checking student reports and planning the next day's class.

  I don't like to take work to my house, so if I can avoid it by doing it before I leave the institute, it's a win
  """

  show itawa_old normal speaking at center
  with dissolve

  itawa "Oh, hi Professor... it's nice to see you."

  show itawa_old normal
  
  "Mrs. Itawa was cleaning the front of her house on the way, we kindly greeted each other, but there was something different this afternoon."

  me "Hi, Mrs. Itawa... The garden looks more beautiful every day."

  me "You shouldn't put in so much effort. Rest a little, you look a bit tired."

  show itawa_old normal speaking

  itawa "An old woman like me sometimes finds it difficult to get the necessary rest, there are days when sleeping is not enough."
  itawa "Although, that is not what has me like that now"

  show itawa_old normal

  "I don't understand what Mrs. Itawa is saying"
  "Maybe she is saying it like a proverb like they do in her country..."

  me "Is there something I can do to help?"

  show itawa_old soft blushed

  "Yeah... you couldn't say other thing could you."

  show itawa_old blushed speaking

  itawa "Haha... you are a true gentleman."

  show itawa_old soft blushed

  """
  That was uncomfortable...  I can't deny that, besides her age, she is a really beautiful woman, but that wasn't what I wanted to ask.

  Itawa keeps watering her garden that she has been growing since she arrived to the country, while I see how the flowers are being showered by the old lady
  """

  show itawa_old normal speaking

  itawa "There is something that is happening in Kanae's room. It is so strong that I heard it in my room as well"

  show itawa_old serious 

  itawa """
  It is like there is a knock in the wall. A knock at a frequent rate, as if they were timed.

  Seven of them. One after another. Like sharp hits of knuckles on a table of fine wood.

  Kanae has heard them as well. She says that probably is a racoon that has entered in our house
  """

  show itawa_old normal speaking

  itawa "Probably it is nothing, haha..." 
  
  show itawa_old normal

  me "Well... it could be. But, if it doesn't mind you, I'd like to check just to make sure is not something else."

  show itawa_old soft blushed

  """
  Even with Makawa living with them, he is not always at home.

  This little town is really peacful, but there are some kids who likes to bother anyone they can
  """

  show itawa_old blushed speaking

  itawa "You are so nice, Professor... I shouldn't bother you with such a thing."

  show itawa_old soft blushed

  "I couldn't help by making this more awkward, could I?"

  show itawa_old normal speaking

  itawa "Okay, Professor. Thank you very much."

  hide itawa_old normal speaking
  with dissolve

  ### Itawa's house. Here we met Kanae

  scene bg itawa_inner_house
  with fade

  """
  It is true that Mrs. Itawa is very closed with her things, but I have manage to establish a good friendship with her and her daughter

  While entering in her house, I can see that there is someone in the room.

  It was Kanae, she was doing the homework that I had left for them at the institute

  I don't know why I stay watching her for a short period of time, until I hit the doorpost with my knuckles gently twice.
  """

  play sound knock
  $ renpy.pause(delay=0.2)
  play sound knock

  $ renpy.pause(delay=1.2)

  show my_kanae speaking at center
  with dissolve

  my_kanae "Oh! Hi, Professor"

  show my_kanae normal

  "She, shy as in class, greets with a warm smile and continues with her homework."

  hide my_kanae normal
  with dissolve

  """
  I wait for Mrs. Itawa to continue to Kanae's room and be able to corroborate what the old lady said previously

  Mrs. Itawa lost her husband five years after Kanae was born, that was one of the main causes of her leaving Kyoto.

  I was just studying pedagogy when the three of them arrived. So I've seen them both grow since they came

  When I get to Kanae's room, I stay at the side of the door without entering. I don't know why, I just didn't feel comfortable
  """

  show itawa_old normal speaking at center
  with dissolve

  itawa "It is okay, Professor. Don't worry."

  show itawa_old normal

  "I can't refuse... so, despite the discomfort, I entered..."

  hide itawa_old normal
  with dissolve

  scene bg kanae_room_evening
  with fade

  "While I was looking the room, I could see that there was a small table with portraits of Makawa and Kanae when they were children. Also from Itawa's husband."

  show itawa_old sad speaking at center
  with dissolve

  itawa "It comforts me to have his portrait there, along with Kanae and Makawa. It makes me feel that he still is taking care of them."

  show itawa_old serious

  "I can hear melancholy in her voice... she really loved him"

  show itawa_old normal speaking

  itawa "Well, Professor...{w=1.0} let's do what we came to."

  show itawa_old normal 

  "My face totally blushes. My mind is filled with totally unrelated thoughs about what we really came"

  show itawa_old normal speaking

  itawa "It is from that wall. Kanae hears the knocks from that wall."

  show itawa_old normal 

  "Sigh..."
  "She probably knew my thoughts before me. At least my face recovered it's color"

  me """
  Well... there's no sign of a real hole in the inside. And the wall is not attached to anything else.

  There are no pipes inside, nor did it seem that something had made a hole to sneak in. Perhaps is someone who just wants to disturb your sleep
  """

  hide itawa_old normal 
  with dissolve

  stop music fadeout 3.0

  "I touch the wall with the palm of my hand trying to feel something that could help me to understand this"

  play sound thunder
  scene bg kanae_room_evening
  with hpunch

  """
  I feel a small void in the facade of the wall, but in doing so, I hear a thundering thunder that even I cover my ears strongly.

  I didn't notice, but when I turned around I saw that the door room was closed, I am alone

  How could this be happening to me? Seriously...
  """

  scene bg kanae_room_raining
  with dissolve

  play sound wind fadein 1.0 fadeout 1.0 loop

  "I look out on the window and the only I can see is the sky turning gray, the rain droping its veil, quickly soaking everything under it."

  me "Mrs. Itawa? The door locked on the outside and I can't open it. Could you open?... please?"

  "It's useless...{w=1.5} where did she go?"

  me "Kanae? Can you hear me? The door is locked and I can't open it... hello?"

  """
  It's like there was no one in the house.

  I look up in the window again to see if there was a passerby who could help me communicate with someone in the house, but no one passed, the streets are desolate.

  Even my cellphone is dead. What's happening?

  I tried to open the window, but something was clogging it. I tried with all my strength 
  
  I felt the ardor in my hands of so much effort that I did, but it didn't give results.

  Everything was getting colder every second.

  I'd been locked in this room for less than ten minutes, but it seems like hours, and the rain doesn't make the situation any more pleasant
  """

  scene bg flash
  with ImageDissolve(flash_img, 0.3)

  scene bg kanae_room_raining
  with ImageDissolve(kanae_room_raining, 0.3)
  with hpunch

  stop sound fadeout 1.0
  play sound thunder fadein 1.0

  "The rain invoked thunders that resonated in my chest with lightnings that illuminated everything I could see"

  "The desperation consuming me faster than I could prevent."

  menu:
    "I try to..."

    "Break the window":
      $ day0_break_window = True

    "Break the door":
      $ day0_break_window = False

  if day0_break_window:

    "I grab Kanae's chair to hit with all my strength. If I break it, I could jump to the garden, even if we are in the second floor."

    stop sound fadeout 1.0
    play sound glass_breaking
    with hpunch

    """
    When I hit the window with the chair, all the wooden parts exploded as if they were extremely coold

    The window was intact, as if nothing happened. And the chair was a broken crystal in the ground.
    """

    play sound wind fadein 1.0 fadeout 1.0 loop

    me "What the hell is happening here? This is impossible."

  else:

    "I prepare myself. I know that Mrs. Itawa is gonna be mad at me, but I can't be here any longer."


  play sound knock
  $ renpy.pause(delay=1.0)
  play sound wind fadein 1.0 fadeout 1.0 loop

  """
  I give a few steps back. Then I hear a knock on the wall.

  It was a sharp blow, right where I had felt the emptiness.
  
  I don't know what to do, I keep looking at the place where I think the sound came from

  I hear a second blow seconds later wich is synchronized with a lightning bolt without thunder.
  """

  #lightning overhere
  scene bg flash
  with ImageDissolve(flash_img, 0.3)

  scene bg kanae_room_raining
  with ImageDissolve(kanae_room_raining, 0.3)

  """
  I counted how many seconds there are between each one, it was a total of seven seconds

  At the sixth blow, the rain stopped falling, but the cold intensified, I could feel it penetrating my skin, even my bones.
  """

  """
  In just a moment I felt the air come out of my lungs as if it were freezing in my trachea.

  Seven seconds after that, the last blow sounded
  """

  scene bg flash
  with ImageDissolve(flash_img, 0.3)

  play sound thunder

  scene bg kanae_room_raining
  with ImageDissolve(kanae_room_raining, 0.3)
  with hpunch

  $ renpy.pause(2.0)

  stop sound fadeout 1.0

  play sound wind fadein 1.0 fadeout 1.0 loop

  """
  A lightning blinded me and a thunder made me almost deaf.

  When I look up, I see that in front of me, on the middle of the air, there was a black hole.
  """

  show hollow small:
    xalign 0.5 yalign 0.5
  with dissolve

  "It did not lead anywhere, you couldn't see anything in it. It seemed as if it absorbed the reality in which we find ourselves to take it to it's own world"

  menu:
    "I..."

    "Step back":
      #wise man... ma'm
      $ day0_touch_my_hole = False

      """
      Giving a few steps back, I feel the wall in my back. I can't escape this room that has become a living nightmare.

      I am with my hands on the wall at my back, but sudenly I feel a strong force that attracts me to this hole.

      I put my hands in front of my, I can't escape from it.
      """

    "Raised my hand carefully":
      #why tho
      $ day0_touch_my_hole = True

      """
      I tried to see what is this. It has a thin edge.

      Even with the deformations, it doesn't produce any sounds, but I felt a small pressure in my chest.

      When I am going to put away my finger, I feel a force that attracts my hand in such a way that I can't fight it.
      """

  "I try to pull my hand out of this strange pulsing hole, but a superhuman impulse pushes me..." 

  hide hollow small
  show hollow half:
    xalign 0.5 yalign 0.5

  with dissolve

  stop sound fadeout 1.0
  play sound glass_breaking fadein 1.0

  with hpunch

  $ renpy.pause(1.5)

  stop sound fadeout 1.0

  play sound wind fadein 1.0 fadeout 1.0 loop

  """
  It makes me hit the wall with great force crashing my body against a small desk that was behind me

  Frozen by the cold in the room, sore from the shock and terror that this caused me

  I look at my finger and observe that I have a kind of scar in the shape of a ring, which has seven frames around it.
  """

  scene bg kanae_room_colder
  with dissolve

  stop sound fadeout 1.0
  play sound glass_cracking

  $ renpy.pause(delay=1.3)

  play sound wind fadein 1.0 fadeout 1.0 loop 

  """
  The glass of the window is completely marred with small pieces of ice by the cold, I lay on the floor, and this... thing.

  This ring-shaped scar makes me panic, so I start to bang on the door with all my strengh
  """

  hide hollow half
  show hollow big:
    xalign 0.5 yalign 0.5
  with dissolve

  """
  When I turned my eyes back to the wall, there was a problem. The one that at one time was a small hole, was growing. It was expanding so quickly.

  Is this my end? Am I a prisoner of a nightmare in a twisted illusion generated by my mind? Or is this real?

  I'm staring at it. If my end is like this, I'll take it.
  
  While I, petrified, see this strange thing, it stops. It doesn't grow anymore. It's like it wants to give me a chance to think.
  """

  scene bg dark
  hide hollow big
  with fade

  "I close my eyes and try to have something in mind for my end, but as pathetic as it seems, I don't visualize anyone. Not even myself."

  scene bg kanae_room_colder
  show hollow big
  with fade

  "So I open my eyes. There it is. I can't run from it. I can just be there."
  "In less than a second I see that the shadow rushes towards where I am"

  scene bg dark
  hide hollow big
  with hpunch
  with Fade(0.1, 0.1, 0.1)

  stop sound fadeout 1.0

  $ renpy.pause(delay=1.0)

  play sound bones fadein 0.4

  "I feel such a strong punch in my whole body that it breaks me, or at least it's as if I broke each bone."
  
  "Did I died? Why is everything black? Am I inside the shadow? Or is this simply what comes next? Darkness..."

  
  scene bg dark
  with Fade(0.5, 2.0, 0.5)

  call day1 from _call_day1

  call final_credits from _call_final_credits
  return