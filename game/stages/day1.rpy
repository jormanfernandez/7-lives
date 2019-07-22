label day1:

  scene bg dark
  with dissolve

  """
  ...

  ....

  Warmth I feel warmth on my face. There is something that enlightens me and is heating my body and mood in a way that makes me wake up.
  """

  scene bg main_living
  with fade

  play music happy_loop fadein 1.0 fadeout 1.0 loop

  """
  While I open my eyes I feel surprised, I can't remember what happened yesterday. I only remember having visited Mrs. Itawa after leaving high school

  I feel the fatigue in every bone and muscle of my body, as if I had been punched close to dying, repeatedly.

  However, I get up to take a shower. As beaten as I am, I can't go to work without taking a bath.
  """

  #transition to a bath or something~

  scene bg main_living
  with fade

  """
  I feel demolished. I don't know how I'm going to give a class in this state.

  Wait... what's this?

  This is a scar in my hand...{w=1.0} Is like a scarred ring 
  """

  stop music fadeout 1.0

  #surprise bitch sound
  scene bg main_living
  with hpunch

  play music solo_music fadein 1.0 fadeout 1.0 loop

  """
  Oh crap!

  I remember everything that happened in Kanae's room.

  That wasn't a dream, it wasn't a bad thought, it really happened.

  I have to go with Mrs. Itawa to see if she is okay. Besides, she is the one who can explain to me what's all this...
  """

  scene bg itawa_house_front
  with fade

  """
  When arriving, the house of the old woman was very different from how it was the day before. 

  There were no lights that illuminated their flowers, and there were no flowers to be lighted

  Instead of the garden that took her years to create, there was a simple cement patio, with marks of the years that had passed
  """

  #scene with the concrete

  """
  One of these marks is the name of Kanae, with the date in which her family arrived in the neighborhood.

  I don't understand what's happening. I know that this garden existed, I saw it myself yesterday

  I saw the lights that illuminated it in the night, I felt the smell that its flowers gave off. What is happening? I'm going crazy? 
  """

  #scene with door in front
  play sound knock
  $ renpy.pause(delay=0.3)
  play sound knock

  "I knock on the door repeatedly, I needed answers."

  me "Mrs. Itawa? Kanae? Is someone here?"

  "I am so confused right now. What's happening here?"

  play sound knock
  $ renpy.pause(delay=0.2)
  play sound knock
  $ renpy.pause(delay=0.2)
  play sound knock

  me "Mrs. Itawa?..."

  """
  While I am knocking, I am still looking for something more that where constant

  Something more than Kanae's name and the date of her arrival in order to keep what I had left of sanity
  """

  play sound knock
  $ renpy.pause(delay=0.3)
  play sound knock

  """
  I insisted on the door for more time than it would be nice to admit, but no one answered

  If they aren't here, perhaps Kanae is in the school

  That should be a constant, since she lives here and arrived on the same date as I remember
  """

  scene bg school_morning
  with fade

  """
  She has to be here. This will be weird for her, but I have to know what happened yesterday.

  Going late helps. The majority of the students probably already arrived.
  """

  show supervisor smiling
  with dissolve

  supervisor "Hey! Colleague. How are you going?"

  """
  Tch...

  Really? Of course the Supervisor is expecting me
  """

  me "Hi, Supervisor. I am kinda late to the class, sorry for the rush!"

  show supervisor normal

  supervisor "Wait! You don't look to well, buddy. Are you okay?"

  "It's that obvious?"

  show supervisor speaking

  supervisor "I know that you like to give your class and all, but you are not in state to do it now."

  show supervisor normal

  """
  He's right. I must say that, although most of the supervisors that I've had during my career were assholes, He was one of the most pleasant and actually understand you.

  Even if he is that nice, he's not going to understand the madness that is in my head right now.
  """

  me "Yes, I know. But I have to..."

  show supervisor speaking

  supervisor """
  Sorry, but I can't let you do that this time.

  You should go home, take a bath and rest.
  """

  show supervisor normal

  "He is right. I can't even remember what was the class for today."

  me "Supervisor, could I ask you a favor instead?"

  show supervisor smiling

  supervisor "Sure! As the youngs says, {b}Shoot{/b}! Haha"

  show supervisor normal

  """
  He wouldn't understand, and if he did, he would surely ask me to visit a psychologist, which even I would recommend if it had not happened to me
  """

  me """
  Could you please bring Kanae here? She should be in the class room.

  I need to ask her something really quick.
  """

  show supervisor speaking

  supervisor "Are you sure? You don't look good."

  show supervisor normal

  me "It'll be fast. Don't worry."

  supervisor "Mmm..."

  show supervisor speaking

  supervisor "Okay, give me a minute."

  show supervisor normal

  hide supervisor normal
  with dissolve

  """
  I waited outside the school. It's better if a student doesn't sees me.

  When I saw her coming where I was, I couldn't hide my happiness.
  """

  show my_kanae speaking at left:
    xalign 0.2
  with dissolve

  show supervisor normal at right:
    xalign 0.8
  with dissolve

  my_kanae "Hello, Professor!"

  "She looked the same, as if nothing had changed. Her kindness always marks her presence"

  show my_kanae normal

  show supervisor smiling

  supervisor "Here she is, Colleague."

  show supervisor normal

  supervisor "I'll be inside if you need something. Have a good day both of you."

  hide supervisor normal
  with dissolve

  show my_kanae normal at center
  with MoveTransition(0.2)

  show my_kanae worried soft

  my_kanae "What's wrong, Professor? You look tired and scared"

  """
   I have so many answers to that question, the bad thing is that all those answers are more questions.

    I need to focus, I can't dump everything that happened instantly
  """

  menu:
    "Kanae..."

    "What happened to your mother's garden?":
      $ day1_asked_garden = True
    "Where is Makawa?":
      $ day1_asked_garden = False
  
  show my_kanae surprised

  if day1_asked_garden:

    my_kanae "What garden, Professor?"

    "What?! This has to be a joke."

    me "Your mother's garden, Kanae. The one she has been taking care since you arrived."

    show my_kanae sad

    my_kanae "Professor, why do you say that? You know what happened. I don't want to remember it."

    "Seeing tears in her big blue eyes makes me realizes that I screw it up"

    me "Kanae. I'm sorry... My memory isn't that good today"

    me "Sorry if I said something wrong"

    show my_kanae blushed

    my_kanae "It is okay, Professor"

    "I don't understand what's happening. She acts like Itawa's memories are the worst thing to have."

    show my_kanae worried soft

    my_kanae "Anyway, what happened to your memory, Professor?"

    me """
    I...{w=1.0} I don't know really.
    
    I just have this weirds memories... I don't know if it is a dream or what. It felt so real.
    """

    show my_kanae surprised

    me """
    It was a full life. Years that where put in my mind.

    I...{w=1.0} I remember Itawa. I saw her, I shared with her, with Makawa. With you.

    Not just from yesterday. The memories are since all of you came to this country.
    """

    show my_kanae worried soft

    my_kanae """
    Professor...

    How could you remember Mama? Remember that she died in Kyoto before we came here.
    """

    #nani the fuck
    show my_kanae worried soft
    with hpunch

    """
    What???

    It can't be. I clearly remember her.
    """

    show my_kanae normal

    my_kanae """
    Perhaps you created all in your head, Professor.

    You joined the photos that we have of Mama and created a full story with us in it, although it seems that your brain created a much bigger road. 

    You even hurt yourself in the finger. Look that scar
    """

    """
    It could be... My brain is shaking with this.
    """

  else:

    my_kanae "Makawa?..."

    show my_kanae blushed

    my_kanae """
    I think he is...

    He is at work...
    """

    show my_kanae surprised

    my_kanae "Why you ask about him? Something happened?"

    """
    Makawa is still with her. That's something at least
    """

    show my_kanae worried soft

    me """
    Kanae... well... I think I dreamed something. It was something about you, Makawa and your mother.

    It was so vivid. I still think it was real.
    """

    show my_kanae surprised

    my_kanae "You dreamed Mama?"

    show my_kanae normal

    my_kanae "I dream with her too...{w=1.0} Some nights she comes to my room."

    show my_kanae sad

    my_kanae "I...{w=1.0} I miss her."

    """
    Something is wrong. Itawa is not with them

    I have to handle this carefully
    """

    me "I bet you do, Kanae."

    show my_kanae normal

    my_kanae "You are hurt, Professor. Look the scar in your finger"

    "Yeah, I have forgotten the scar."

    show my_kanae surprised

    my_kanae "It was in your dream?"

    me "I think so... it doesn't matter. I will heal, haha"

    show my_kanae normal

    my_kanae "You are very tired, Professor. You should go to your house, rest and tomorrow give us the class that you owe to us for today."

    "I couldn't say that Kanae wasn't right. I needed to calm my mind while I know that this is the real thing, or it seems the most real at least."
  
  "While I was talking with Kanae, Makawa appeared from nowhere"


  show my_kanae surprised:
    xalign 0.8
  with MoveTransition(0.3)
  show makawa_old speaking normal at center
  with dissolve

  makawa_old "Kanae. Go."

  show makawa_old normal

  "It's true that I don't have the best friendship with Makawa, but still we greet eachother, or at least that's what I remembered."

  me "Hi, Makawa."

  show makawa_old speaking normal

  show my_kanae soft worried

  makawa_old "Leave..."

  show makawa_old normal

  "His eyes were dead. I've never seeing him like that"

  my_kanae "Professor. Thank you for speaking with me. I need to go with Makawa."

  "It doesn't seem she wants to go with him"

  me "Are you sure, Kanae? If you don' want to, you can..."

  show makawa_old speaking loud
  with hpunch

  makawa_old "Shut up!"

  show my_kanae sad

  "I felt that I shouldn't have said that, since the punch that came to my face was almost instantaneous."

  show makawa_old normal

  "Still so, I managed to dodge it, fortunately. I already feel the body beaten enough to receive another hit."
  
  show makawa_old normal:
    xalign 0.2
  with MoveTransition(0.3)

  show my_kanae mad talking at center
  with MoveTransition(0.3)

  my_kanae "Makawa! Stop! I will go with you."

  show makawa_old tsch

  show my_kanae sad

  my_kanae """
  Professor, please. Do not intervene.

  I do not want you to have the same fate as Mama.
  """

  "What does she mean by that?"

  show my_kanae sad at right
  with MoveTransition(0.3)
  hide my_kanae sad at right
  with dissolve

  show makawa_old tsch at right
  with MoveTransition(0.3)
  hide makawa_old tsch at right
  with dissolve

  """
  They leave before I can ask anything else.

  After that, it was that I understood what Kanae was warning me. 

  Why would she say that Makawa is capable of killing me? That's absurd! But instantly it resounds in my head what she said

  {i}\"I do not want you to have the same fate as Mama.\"{/i}
  
  I felt a chill all over my back escalating to my neck, making me hold my breath for a few seconds
  """

  #a tsch sound

  """
  I am completely paralyzed, I can't move, I can't do anything at all.

  She had just implied to me that Makawa had killed her mother

  Why would she make such a serious accusation? It can't be true... But if it wasn't, Makawa made no effort to defend himself.

  I have to clear my mind, so I decide to give a small walk by the park nearby the school
  """

  stop music fadeout 3.0

  scene bg park_morning
  with fade

  """
  While I am walking, I try to call Kanae again, but she doesn't answer.

  I can't go to the police to say that this boy with a pseudo-yakuza look had killed his mother and kidnapped his sister 

  Without knowing if this had already been discussed when they arrived here or before it could end in another disaster

  Besides, she told me that her mother died in Kyoto, not here

  No matter how much I want to do something, with the little information I have the police will not be able to do anything
  """

  menu:
    "I decide to"

    "Keep walking a little bit":
      $ day1_walking_forest = True

    "Return to my house":
      $ day1_walking_forest = False
  
  if day1_walking_forest:
    call day1_walking_forest from _call_day1_walking_forest
  else:
    call day1_returning_home from _call_day1_returning_home

  """
  While watching the sky,  I received a call, it was Kanae. I respond quickly, I was worried about how she was doing.

  When I take the call, between tears I hear:
  """

  play music dramatic fadein 1.0 fadeout 1.0 loop

  my_kanae """
  {i}Please help me, Makawa is crazy, he locked me in my room and he is with two people below{/i}

  {i}He hitted me very hard, dragged me to my room and closed it.{/i}

  {i}I can not go out and I do not have anyone else. Please, Professor, {b}Help me!{/b}{/i}
  """

  """
  As soon as she says that, the call ends. I try to call her back, but it doesn't work

  Withouth thinking in other things, I ran as fast as I can to her house.
  """

  scene bg itawa_house_front_evening
  with fade

  """
  I called the police on my way here

  They are going to be here in minutes, but I can't wait.

  When reaching the front of her house my hand begins to hurt just where I have the scarred ring.

  It begins to burn with great intensity that almost makes me kneel.
  """

  stop music fadeout 1.0

  scene bg dark
  with Fade(0.5, 1.5, 0.5)

  #change with weird house
  scene bg itawa_kyoto_house_normal
  with fade

  """
  While I am leaning in pain, I open my eyes to see around me and realize that I am no longer in front of Kanae's house. 

  In fact, I have no idea where I am.

  Everything starts to turn around in my head, the scar hurts even more to the point of burning.
  """

  scene bg dark
  with Fade(0.5, 1.5, 0.5)

  scene bg itawa_house_front_evening
  with fade

  """
  Itawa's House again...

  I still am hallucinating. My head is playing tricks... I can't stop to think about that, so I go to the door
  """

  #knocks
  me "Kanae...{w=1.0} it's me. Could you come, please?"

  show thug serious
  with dissolve

  show thug speaking
  thug "Mr. Makawa is waiting..."

  "This doesn't feel good... Something is wrong."
  "With my hands shaking, I enter the house"

  hide thug serious
  with dissolve

  scene bg itawa_inner_house
  with fade

  play music dramatic fadein 1.0 fadeout 1.0 loop

  show makawa_old normal at center
  with dissolve

  "There he was... his thug joined after I was in the room"

  show thug serious at left:
    xalign 0.2
  with dissolve

  """
  Makawa is there with a knife full of coagulated blood on the table.

  I can see a gun in the thug waist

  When I saw the knife I thought the worst...
  """

  show thug surprised

  me "Where's Kanae?!"

  "The guy at his side took the weapon quickly, but Makawa stopped him gesturing with his hand."

  show makawa_old speaking normal

  show thug serious

  makawa_old "This ends today, but I have to do it myself."

  show makawa_old normal

  """
  Makawa said, as he took the knife from the table. I had no escape

  I couldn't find the reason why he hated me so much

  At the same time that the scar on my finger hurt more and more, but seeing what I had in front of me could not distract
  """

  show makawa_old tsch

  me "Makawa, I am asking you. What the hell did you do with Kanae?"

  show makawa_old speaking normal

  makawa_old "Did you really think I would do something to my sister? I'm not a {b}monster{/b} like you."

  show makawa_old tsch 

  me "What the hell are you saying? I never did anything to you or your family"

  show makawa_old speaking loud

  makawa_old "This ends now!"

  show makawa_old speaking loud
  with hpunch

  "Makawa attacks me with the knife in his hand"

  show makawa_old tsch

  menu:
    "I..."

    "Try to avoid him":
      $ day1_stabbed = False

    "Try to punch him":
      $ day1_stabbed = True
  
  if not day1_stabbed:

    """
    I almost managed to avoid him, but he managed to make a wound on my face due how close he was
    """
  else:
    
    show makawa_old tsch
    with hpunch

    play sound punch

    show thug surprised

    """
    I can give him a hard punch on his stomach, but he scratch part of mine with the knife

    It's not dangerous, but it hurts as hell
    """

    show thug serious

    if restart:
      $ renpy.notify(":1")

  my_kanae "Makawa! Stop this, please! You still have time"

  """
  I can hear Kanae's screams down here

  Makawa is in front of me. I can't run. He wants to cut my throat.

  I try to stay as far away from him as I can, making time for the police to arrive. Now I think I should have waited them first
  """

  show makawa_old speaking loud

  makawa_old """
  Did you already forgot it, {b}monster{/b}?

  You never remembered my face, right? You don't remember what you did...

  How you destroyed my sister's life. Our lives!
  """

  show makawa_old tsch

  me "What the hell are you talking about? I haven't done anything"
  me "I am not responsible for your anger!"

  hide makawa_old tsch
  hide thug serious
  with dissolve

  scene bg flash
  with ImageDissolve(flash_img, 0.3)

  play sound thunder

  scene bg itawa_inner_house
  with ImageDissolve(itawa_inner_house, 0.3)
  with hpunch

  show makawa_old tsch at center
  show thug serious at left:
    xalign 0.2
  with dissolve

  """
  When saying this it sounds a great thunder and begins a heavy rain.

  Despite so many arguments that does not stop us from fighting
  """

  show makawa_old tsch
  with hpunch

  """
  With my hand burning for the scar I can give him a punch on the face that throws him on the ground hard enough so that the knife falls off.

  While he is on the ground, my mind begins to wobble again
  """

  scene bg dark
  with fade

  "Where am I? I can't see anything... wait"

  scene bg itawa_kyoto_house_normal
  with fade

  """
  I am again this house. I don't know what is happening
  """

  scene bg dark
  with Fade(0.5, 0.5, 0.5)

  scene bg itawa_inner_house
  with fade

  show makawa_old totally surprised at center
  with dissolve
  with hpunch

  makawa_old "{b}MONSTER!{/b}"

  """
  When I return to myself, I only see that Makawa rushes back to where I am only with his fist
  """

  show thug serious at left:
    xalign 0.2
  with dissolve

  show makawa_old tsch

  """
   I must say that his fists were so strong that they focused my mind for a moment and broke my nose.

   He returns to take the knife that was on the floor, while the guy that was with him is only dedicated to see
  """

  menu:
    "I try to"

    "Grab his hands":

      """
      But he throw several stabs straight at my liver, but with luck I manage to grab his hand

      I start to remove the knife again. At least it wouldn't kill me so easily
      """

      show makawa_old tsch
      with hpunch
      
      """
      I couldn't grab the knife, so I kicked him in one leg and steped back
      """

    "Punch his face":

      if restart:
        "..." "Control yourself."

        "There are voices in my head. I can't get distracted by them"


      """
      I throw a few punches to his face, but he avoid them, and punched me in the stomach.
      """

      show makawa_old tsch
      with hpunch

      play sound punch

      """
      Watching the knife, I block one of his fist and give him a really strong punch in the face.

      Maybe it was retribution for having broken my nose
      """
  
  """
  Both with our faces bathed in blood, are tired. We prepare to continue, but I start to feel a terrible headache again

  It can't be again. I'm hallucinating!
  """

  hide makawa_old tsch
  hide thug serious
  with dissolve

  scene bg itawa_kyoto_house_normal
  with fade

  """
  I see a lady in the kitchen... She is preparing something 

  She has a lighter... It can't be
  """

  show itawa_young surprised
  with dissolve

  itawa "Oh..."
  itawa "Who are you?"

  """
  It's Itawa! It's impossible...

  she's staring at me, but everything starts blinking

  In moments I see Itawa...
  """

  hide itawa_young surprised
  with dissolve
  scene bg itawa_inner_house
  show makawa_old tsch
  with Fade(0.1, 0.1, 0.1) 

  "In others Makawa"

  """
  With a headache impossible to bear, and a hand that was red hot, I hold strongly the knife that I took from Makawa in the middle of the struggle.

  Unable to react, Makawa tries to hit me again looking to remove the knife, I'm seeing his face, but in each blink he changes
  """

  scene bg itawa_kyoto_house_normal
  show itawa_young shocked
  with Fade(0.1, 0.1, 0.1) 

  "Itawa"

  scene bg itawa_inner_house
  show makawa_old totally surprised
  with Fade(0.1, 0.1, 0.1) 

  """
  Makawa...

  I just want this to stop!
  """

  stop music fadeout 3.0

  scene bg dark
  with fade

  """
  I hold the knife firmly in front of me with my eyes closed. There is no fight anymore, there is only silence

  I don't want to see what happened, what I did, but I must do it.
  """

  play sound stab fadein 0.3

  scene bg itawa_kyoto_house_normal
  with fade
  show itawa_young dead
  with dissolve

  """
  What the hell! What did I do?

  I can hardly feel her breathing...
  """

  itawa "Who...{w=1.0} are..{w=1.5} y.."

  """
  I feel her dropping the lighter that she had on the floor.

  While I hold her almost dying body, I see the blood on my hands...

  Was it me? Can't be.
  """

  #fire sounds




  show bg itawa_kyoto_house_fire
  with ImageDissolve(itawa_kyoto_house_fire, 3.0)




  """
  I feel the heat rising through the fire as it begin to burn everything around us

  When I turn my face I see a boy with a terrified look at the horrible scene... Oh, no
  """

  hide itawa_young dead
  with dissolve

  show makawa_kid fire surprised
  with dissolve

  """
  Makawa, Kanae... No! NO!...

  The headache returns, the ringshaped scar begins to burn so hard that it burns me completely one of the seven spaces.
  """

  #more fire

  hide makawa_kid fire surprised
  with dissolve
  
  scene bg dark 
  with fade

  """
  The pain in my hand is so great that I can almost handle it

  When the pain becomes more tolerable I open my eyes with the hope that it was not what happened
  """

  scene bg itawa_inner_house
  with fade

  show makawa_old dead at center
  with dissolve

  """
  God... No...
  """

  show my_kanae surprised at left:
    xalign 0.2
  with dissolve

  """
  No...{w=1.0} No.!
  """
  show my_kanae sad
  with dissolve

  """
  Sadness, amazement, shock. All in one look. Kanae was watching me hold the body of her brother, while I was bathed in my blood and his blood

   What the hell happened? How did I end up in this?
  """

  hide makawa_old dead
  with dissolve

  """
  Oh, hell... Makawa, Kanae...{w=1.0} I'm sorry.
  """

  scene bg dark
  with Fade(0.5, 1.0, 5)

  call day2 from _call_day2