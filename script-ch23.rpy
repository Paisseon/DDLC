    image noface1:
        topleft 
        xtile 10 ytile 10 
        block:
            block:
                choice:
                    "images/sayori/noface1.png" 
                choice:
                    "images/sayori/noface1b.png" 
            block:
                choice:
                    0.075 
                choice:
                    0.3 
                choice:
                    0.4 
                choice:
                    0.5 
                choice:
                    0.6 
            repeat
    image noface2:
        "images/sayori/noface2.png" 
        xalign 0.95 yalign 0.47 

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white 
        show noface1 
        show noface2 
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        pause 7
        $ quick_menu = True
        scene bg club_day2 
        show yuri 2 at i11 zorder 2 
    else:
        scene bg club_day2 
        with dissolve_scene_half

    play music t6
    show yuri 2y5 at t11 zorder 2 
    y "Hi, [player]!"
    y "I've been waiting for you."
    y "Are you ready to continue reading?"
    y "I brought my best tea today--"
    show yuri 2f 
    show natsuki 4w at f33 zorder 3 
    n "Monika!"
    n "I told you not to--"
    n "Ugh..."
    n "Is she really late again?"
    show natsuki at t33 zorder 2 
    show yuri at f32 zorder 3 
    y "Inconsiderate as usual, Natsuki."
    show yuri at t32 zorder 2 
    show natsuki at f33 zorder 3 
    n "Excuse me?"
    show natsuki at t33 zorder 2 
    show yuri at f32 zorder 3 
    y "Must you always interrupt my conversations with your incessant yelling?"
    show yuri at t32 zorder 2 
    show natsuki at f33 zorder 3 
    n "What are you talking about?!"
    n "You say that like I do it on a regular basis or something."
    n "I just wasn't paying attention, okay? I'm sorry."
    n "Seriously... What's gotten into you lately?"
    if n_appeal >= 2:
        n "Look..."
        n "I did some thinking about yesterday."
        n "I was a little more hostile than I meant to be..."
        n "I guess I really felt threatened or something."
        n "But I know this is something we're doing together."
        n "Another new member wouldn't hurt, as long as they're cool..."
        n "And I guess another girl would be nice this time..."
        n "So..."
        show natsuki at t33 zorder 2 
        show yuri at f32 zorder 3 
        $ style.say_dialogue = style.normal
        y "Natsuki..."
        $ style.say_dialogue = style.edited
        y "Nobody cares."
        y "Why don't you go look for some coins under the vending machines or something?"
        $ style.say_dialogue = style.normal
        show yuri at t32 zorder 2 
        show natsuki at f33 zorder 3 
        n "--!"
        n "..."
        n "..."
        show natsuki at thide 
        hide natsuki 
        pause 1.0
        show monika 1g at l31 
        m "Aw, man..."
        m "I'm the last one here again!"
        show yuri at f32 zorder 3 
        y "Were you practicing piano again?"
        show yuri at t32 zorder 2 
        show monika at f31 zorder 3 
        m "Yeah..."
        m "Ahaha..."
        show monika at t31 zorder 2 
        show yuri at f32 zorder 3 
        y "You must have a lot of determination."
        y "Starting this club, and still trying to make time for piano..."
        show yuri 1a at t32 zorder 2 
        show monika at f31 zorder 3 
        m "Well, maybe not determination..."
        m "But I guess passion."
        m "It motivates me to work hard for the festival, too."
    else:
        show natsuki at t33 zorder 2 
        show yuri at f32 zorder 3 
        y "Me?"
        y "N-Nothing..."
        show yuri at t32 zorder 2 
        show natsuki at f33 zorder 3 
        n "..."
        show natsuki at t33 zorder 2 
        show yuri at f32 zorder 3 
        y "Is it really that bad...?"
        show yuri at t32 zorder 2 
        show natsuki at f33 zorder 3 
        n "See, it {i}is{/i} something."
        show natsuki at t33 zorder 2 
        show yuri at f32 zorder 3 
        y "I'll get over it!"
        y "It's not even anything noteworthy..."
        y "I've just been feeling a little on edge lately..."
        y "A-Anyway, we don't need to talk about it!"
        show yuri at t32 zorder 2 
        show natsuki at f33 zorder 3 
        n "Well, I just felt like I needed to bring it up."
        n "It's not like I really care or anything..."
        show natsuki at t33 zorder 2 
        show yuri 3e 
        show monika 1g at l31 
        m "Aw, man..."
        m "I'm the last one here again!"
        show natsuki at f33 zorder 3 
        n "Well, [player] just walked in too."
        show natsuki at t33 zorder 2 
        show yuri at f32 zorder 3 
        y "Were you practicing piano again?"
        show yuri at t32 zorder 2 
        show monika at f31 zorder 3 
        m "Yeah..."
        m "Ahaha..."
        show monika at t31 zorder 2 
        show yuri at f32 zorder 3 
        y "You must have a lot of determination."
        y "Starting this club, and still trying to make time for piano..."
        show yuri 1a at t32 zorder 2 
        show monika at f31 zorder 3 
        m "Well, maybe not determination..."
        m "But I guess passion."
        m "It motivates me to work hard for the festival and..."
        m "Um..."
        show monika at t31 zorder 2 
        show natsuki at f33 zorder 3 
        n "..."
        show natsuki at t33 zorder 2 
        show monika at f31 zorder 3 
        m "Right..."
        m "I-I forgot..."
        show monika at thide zorder 1 
        hide monika 
        show yuri at f32 zorder 3 
        y "Um, about that, Natsuki..."
        y "We were all talking yesterday, and..."
        y "Well...we decided that we would like to support the festival as well."
        y "However...!"
        y "I understand how you feel about not wanting the club to change."
        y "I think we all kind of feel that way."
        y "So as long as we're all working together, this club will never become something we don't want."
        show yuri at t32 zorder 2 
        show natsuki at f33 zorder 3 
        n "..."
        show natsuki at t33 zorder 2 
        show yuri at f32 zorder 3 
        y "Um, also..."
        y "If you help us out with the festival..."
        y "...Then I'll buy you a new manga!"
        show yuri 3t at t32 zorder 2 
        show natsuki at f33 zorder 3 
        n "..."
        n "Ahahaha!"
        n "Sorry, that last part was really funny."
        n "Look..."
        n "I did some thinking about yesterday."
        n "I was a little more hostile than I meant to be..."
        n "I guess I really felt threatened or something."
        n "But I know this is something we're doing together."
        n "Another new member wouldn't hurt, as long as they're cool..."
        n "And I guess another girl would be nice this time..."
        n "...But more importantly, I would hate to see the event suck just because I chose to back out!"
        n "I'm a pro, you know!"
        n "So I'm gonna help too, and we'll make sure it's done right."
        show natsuki at t33 zorder 2 
        show yuri at f32 zorder 3 
        y "Thank goodness..."
        y "Isn't that great, Monika?"
        show yuri at t32 zorder 2 
        show natsuki at f33 zorder 3 
        n "...Monika?"
        show natsuki at t33 zorder 2 
        show monika 1o at f31 zorder 3 
        m "Ah--"
        m "Yeah, that's wonderful!"
        m "It wouldn't be the same without you, Natsuki."
    m "Anyway, [player]..."
    m "What do you want to do today?"
    m "I was thinking we could--"
    show monika at t31 zorder 2 
    show yuri at f32 zorder 3 
    y "We already have plans today."
    show yuri at t32 zorder 2 
    show monika at f31 zorder 3 
    m "Ah..."
    m "Is that so, Yuri?"
    show monika at t31 zorder 2 
    show yuri at f32 zorder 3 
    y "That's correct."
    y "[player] is already engaged in a novel that we're reading together."
    y "Aren't you glad I've already gotten him into literature, Monika?"
    show yuri 1a at t32 zorder 2 
    show monika at f31 zorder 3 
    m "I..."
    m "I suppose..."
    m "I was just--"
    m "Actually, it doesn't matter."
    m "It really doesn't."
    m "You guys can do whatever you want."
    show monika at t31 zorder 2 
    show yuri at hf32 zorder 3 
    y "{i}(Yes!){/i}{w=0.5}{nw}"
    y "Um... Thank you for understanding, Monika."
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    scene bg club_day2 
    show yuri 3 at t11 zorder 2 
    with wipeleft_scene
    call yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene black 
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2])
        scene black  with Dissolve(1.0)
    else:
        pass
    scene bg club_day2 
    show monika 4b at t32 zorder 2 
    with wipeleft_scene
    play music t3
    m "Okay, everyone!"
    m "It's time to figure out the festival preparations."
    m "Let's hurry and get this over with."
    if n_appeal >= 2:
        show natsuki 4q at f31 zorder 3 
        n "..."
    else:
        show natsuki 4q at f31 zorder 3 
        n "Jeez..."
        n "Why is the mood so weird today?"
        n "Look, even Yuri isn't immune to it."
    show natsuki at t31 zorder 2 
    show yuri 4b at f33 zorder 3 
    y "Uu..."
    y "Stagnating air is common foreshadowing that something terrible is about to happen..."
    show yuri at t33 zorder 2 
    show monika at f32 zorder 3 
    m "Look, can we just get this done?"
    m "I'm going to be printing and assembling all the poetry pamphlets."
    if n_appeal >= 2:
        m "Natsuki, you can make cupcakes."
        m "I know you're at least good at that."
        show monika at t32 zorder 2 
        show natsuki at f31 zorder 3 
        n "..."
        show natsuki at t31 zorder 2 
        show monika at f32 zorder 3 
    else:
        m "Natsuki, I was thinking--"
        show monika at t32 zorder 2 
        show natsuki at f31 zorder 3 
        n "I want to make cupcakes!"
        show natsuki 2a at t31 zorder 2 
        show monika at f32 zorder 3 
        m "...Yeah, that."
        m "Glad we're on the same page."
    m "Yuri, you can..."
    m "...Well, it doesn't matter."
    m "Do whatever you want, as long as you think it'll help."
    show monika at t32 zorder 2 
    show yuri at f33 zorder 3 
    y "Monika..."
    y "I'm not useless, you know!"
    show yuri at t33 zorder 2 
    show monika at f32 zorder 3 
    m "I-I know that!"
    show monika at t32 zorder 2 
    show yuri at f33 zorder 3 
    y "I already know what I'd like to do."
    y "We can't run a successful poetry event without having the right atmosphere for the occasion."
    y "So I'm going to make decorations and set up some nice mood lighting."
    show yuri at t33 zorder 2 
    show monika at f32 zorder 3 
    m "There, see?"
    m "That's a great idea!"
    m "And that gives us all something to do."
    show monika at t32 zorder 2 
    show yuri at f33 zorder 3 
    y "Eh?"
    y "What about [player]?"
    show yuri at t33 zorder 2 
    show monika at f32 zorder 3 
    m "[player] is going to help me."
    show monika 2a at t32 zorder 2 
    show natsuki at f31 zorder 3 
    n "Wait, you?"
    n "You have the easiest job, Monika!"
    show natsuki at t31 zorder 2 
    show monika at f32 zorder 3 
    m "Sorry, but that's just how it is."
    show monika at t32 zorder 2 
    show natsuki at f31 zorder 3 
    n "Like hell it is!"
    n "What are you trying to pull?"
    show natsuki at t31 zorder 2 
    show yuri at f33 zorder 3 
    y "I-I agree with Natsuki!"
    y "Not only is your work already most suitable for one person..."
    y "But my task is laborious enough to benefit from an extra pair of hands."
    show yuri at t33 zorder 2 
    show natsuki at f31 zorder 3 
    n "Mine too!"
    show natsuki at t31 zorder 2 
    show yuri at f33 zorder 3 
    y "What, your cupcakes?"
    y "Please."
    show yuri at t33 zorder 2 
    show natsuki at f31 zorder 3 
    n "Like {i}you{/i} would fucking know!"
    n "All you care about now is dragging [player] around with you and your stupid books."
    n "You {i}and{/i} Monika!"
    show natsuki at t31 zorder 2 
    show monika at f32 zorder 3 
    m "Hey!"
    m "I didn't even do anything!"
    show monika at t32 zorder 2 
    show natsuki at f31 zorder 3 
    n "Okay, then why not let [player] decide who to help instead of abusing your power?"
    show natsuki at t31 zorder 2 
    show monika at f32 zorder 3 
    m "I'm not...abusing my power."
    show monika at t32 zorder 2 
    show yuri at f33 zorder 3 
    y "Yes you are, Monika."
    y "Just let [player] make the choice, okay?"
    show yuri at t33 zorder 2 
    show monika at f32 zorder 3 
    m "Okay, fine!"
    m "Fine."
    show monika 1h at t32 zorder 2 
    show natsuki at f31 zorder 3 
    n "Jeez..."
    n "[player], I know how fed up you are with these two by now."
    n "We can just--"
    show natsuki at t31 zorder 2 
    show yuri at f33 zorder 3 
    y "Natsuki, shut your fucking mouth and let him decide for himself."
    show yuri at t33 zorder 2 
    show natsuki at f31 zorder 3 
    n "{i}You{/i} shut your mouth!"
    show natsuki at t31 zorder 2 
    show monika at f32 zorder 3 
    m "Jesus christ..."
    m "This is never going to end. Just make the choice, okay?"
    show monika at t32 zorder 2 
    $ madechoice = renpy.display_menu([("Natsuki.", "natsuki"), ("Yuri.", "yuri"), ("Monika.", "monika")], screen="rigged_choice")


    if madechoice != "monika":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white 
        show yuripupils zorder 10 
        pause 3.0
        show bg club_day:
            alpha 0.05 
            yoffset 0 ytile 2 
            linear 5.25 yoffset -720 
            repeat
        show noise:
            alpha 0.1 
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
            "Monika":
                pass
        scene bg club_day 
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11 
    else:
        show natsuki at thide zorder 1 
        show yuri at thide zorder 1 
        hide natsuki 
        hide yuri 

    m "Yay, you picked me!"
    m "We can meet at your house this weekend."
    m "I promise it'll be fun."
    m "Is Sunday okay with you?"
    show natsuki 1e at f31 zorder 3 
    n "Are you fucking kidding me?"
    n "This isn't fair at all!"
    show natsuki at t31 zorder 2 
    show monika at f32 zorder 3 
    m "It is fair, Natsuki."
    m "It's what he chose."
    show monika at t32 zorder 2 
    show yuri 3r at f33 zorder 3 
    y "No, it's not fair!"
    y "Giving us all this work and then taking [player] for yourself."
    y "What a shameful thing to do!"
    show yuri at t33 zorder 2 
    show monika at f32 zorder 3 
    m "Yuri, I didn't even give you any work."
    m "You decided it for yourself."
    m "You're being a little unreasonable here."
    stop music
    show monika at t32 zorder 2 
    show yuri at f33 zorder 3 
    y "I'm being unreasonable?"
    y "Ahahaha!"
    y "Monika, I can't believe how delusional and self-important you are!"
    y "Pulling [player] away from me every single time you're not included in something."
    y "Are you jealous?"
    y "Crazy?"
    y "Or maybe you just hate yourself so much that you take it out on others?"
    y "Here's a suggestion. Have you considered killing yourself?"
    y "It would be beneficial to your mental health."
    show yuri at t33 zorder 2 
    show natsuki at f31 zorder 3 
    n "Yuri, you're scaring me a little..."
    show natsuki at t31 zorder 2 
    show monika at f32 zorder 3 
    m "Natsuki, let's just go."
    m "I don't think she wants us around right now."
    show monika at t32 zorder 2 
    show yuri at f33 zorder 3 
    y "See, that wasn't very hard."
    y "All I want is to spend a little time with him."
    y "Is that so much to ask?"
    hide natsuki 
    hide monika 
    hide yuri 
    with wipeleft
    "Yuri follows Monika and Natsuki to the door."
    show monika 5a at t11 zorder 2 
    m "Hey, [player]..."
    m "Yuri is really something, isn't she?"
    show monika at thide zorder 1 
    hide monika 
    "Monika giggles as Yuri pushes her out the door."
    python:
        
        
        
        
        
        
        
        
        if persistent.have_a_nice_weekend is None:
            persistent.have_a_nice_weekend = "G2pilVJccjJiQZ1poiM3iYZhj3I0IRbvj3wxomnoeOatVHUxZ2ozGKJgjXMzj2LgoOitBOM1dSDzHMatdRpmQZpidNehG29mkTxwmDJbGJxsjnVeQT9mTPSwSAOwnuWhSE50ByMpcuJoqGstJOCxqHCtdvG3HJV0TOGuwOIyoOGhwOHgm2GhlZpyISJik3J/"
        persistent.hxppy = None
        persistent.can_you_hear_me = None
        persistent.iii = None

    play music t10y
    show yuri 2m at t11 zorder 2 
    y "Finally."
    y "Finally!"
    y "This is really all I wanted."
    y "[player], there's no need to spend the weekend with Monika."
    y "Don't listen to her."
    y "Just come to my house instead."
    y "The whole day, with just the two of us..."
    y "Doesn't that sound wonderful?"
    y "Ahahaha!"
    y "Wow... There's really something wrong with me, isn't there?"
    y "But you know what?"
    y "I don't care anymore."
    y "I've never felt this good my whole life."
    y "Just being with you is a far greater pleasure than anything I could imagine."
    y "I'm addicted to you."
    y "It feels like I'm going to die if I'm not breathing the same air as you."
    y "Doesn't it feel nice to have someone care about you so much?"
    y "To have someone who wants to revolve their entire life around you?"
    y "But if it feels so good..."
    y "Then why does it feel more and more like something horrible is going to happen?"
    y "Maybe that's why I tried stopping myself at first..."
    y "But the feeling is too strong now."
    y "I don't care anymore, [player]!"
    y "I have to tell you!"
    y "I'm...I'm madly in love with you!"
    y "It feels like every inch of my body...every drop of blood in me...is screaming your name."
    y "I don't care what the consequences are anymore!"
    y "I don't care if Monika is listening!"
    y "Please, [player], just know how much I love you."
    y "I love you so much that I even touch myself with the pen I stole from you."
    y "I just want to pull your skin open and crawl inside of you."
    y "I want you all to myself."
    y "And I will be only yours."
    y "Doesn't that sound perfect?"
    y "Tell me, [player]."
    y "Tell me you want to be my lover."
    y "Do you accept my confession?"

    menu:
        "Yes.":
            jump yuri_kill
        "No.":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    pause 1.0


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = "yuri_kill_1"
    $ quick_menu = False
    stop music
    scene bg club_day 
    show yuri 3d at i11 
    y "...Ahahaha."
    y "Ahahahahahaha!"
    $ style.say_dialogue = style.normal
    y "Ahahahahahahahaha!"
    $ style.say_dialogue = style.edited
    y "AHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    pause 1.43
    show yuri stab_1 
    pause 0.75
    show yuri stab_2 
    show blood:
        pos (610,485) 
    pause 1.25
    show yuri stab_3 
    pause 0.75
    show yuri stab_2 
    show blood:
        pos (610,485) 
    show yuri stab_4  with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5 
    pause 0.70
    show yuri stab_6:
        2.55 
        easeout_cubic 0.5 yoffset 300 
    show blood as blood2:
        pos (635,335) 
    pause 2.55
    hide blood 
    hide blood2 
    pause 0.25
    play sound fall
    pause 0.25
    scene black 
    pause 2.0

    scene black 
    show y_kill 
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = "yuri_kill_2"
    python:
        _history_list = []
        m.add_history(None, "", """Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!Every day is full of chit-chat and fun activities with all of my adorable and unique club members:Sayori, the youthful bundle of sunshine who values happiness the most;Natsuki, the deceivingly cute girl who packs an assertive punch;Yuri, the timid and mysterious one who finds comfort in the world of books;...And, of course, Monika, the leader of the club! That's me!I'm super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you're a sweetheart—will you promise to spend the most time with me?Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!Every day is full of chit-chat and fun activities with all of my adorable and unique club members:Sayori, the youthful bundle of sunshine who values happiness the most;Natsuki, the deceivingly cute girl who packs an assertive punch;Yuri, the timid and mysterious one who finds comfort in the world of books;...And, of course, Monika, the leader of the club! That's me!I'm super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you're a sweetheart—will you promise to spend the most time with me?Welcome to the Literature Club! It's always been a dream of mine to make something special out of the things I love. Now that you're a club member, you can help me make that dream come true in this cute game!Every day is full of chit-chat and fun activities with all of my adorable and unique club members:Sayori, the youthful bundle of sunshine who values happiness the most;Natsuki, the deceivingly cute girl who packs an assertive punch;Yuri, the timid and mysterious one who finds comfort in the world of books;...And, of course, Monika, the leader of the club! That's me!I'm super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you're a sweetheart—will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with me?will you promise to spend the most time with""")

    $ style.say_dialogue = style.edited
    scene black 
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show y_kill 
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    $ persistent.have_a_nice_weekend = None



    $ persistent.autoload = "yuri_kill_3"
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day 
    "[gtext]"
    window auto
    n "Alright, it's festival time!"
    show natsuki 4k at t11 zorder 2 
    n "Wow, you got here before me?"
    n "I thought I was pretty ea--{nw}"
    show natsuki scream at h11 
    n "EYAH!"
    n "AAAAAAAAAAAAAAAHHHH!!!"
    pause 1.0
    show natsuki scream at h11 
    pause 0.75
    show natsuki vomit at h11 
    pause 1.25
    show natsuki at lhide 
    hide natsuki 
    "Natsuki runs away."
    m "..."
    show monika 2b at t11 zorder 2 
    m "I'm here!"
    m "[player], did something happen?"
    m "Natsuki just ran past me..."
    m "...Oh..."
    m "...Oh."
    m "..."
    m "Ahahaha!"
    m "Well, that's a shame."
    m "Wait, were you here the entire weekend, [player]?"
    m "Oh, jeez..."
    m "I didn't realize the script was broken that badly."
    m "I'm super sorry!"
    m "It must have been pretty boring..."
    m "I'll make it up to you, okay?"
    m "Just gimme a sec..."
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr deleted successfully.")
    $ delete_character("yuri")
    pause 1.0
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr deleted successfully.")
    $ delete_character("natsuki")
    pause 1.0
    m "I'm almost done."
    m "I just want to have a cupcake real quick!"
    $ gtext = glitchtext(10)
    "Monika lifts the foil from [gtext]'s tray and takes a cupcake."
    m "Seriously, these are the best!"
    m "I really just had to have one, since it's the last time I'll ever get the chance to."
    m "You know, before they stop existing and everything."
    m "...But anyway, I really shouldn't be making you wait any longer."
    m "Just bear with me, okay?"
    m "This should only take a second."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.full_restart(transition=None, label="splashscreen")

    return
