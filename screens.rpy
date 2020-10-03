    style default:
        color gui.text_color
        line_overlap_split 1
        line_spacing 1
        font gui.default_font
        outlines [(2, "#000000aa", 0, 0)]
        size gui.text_size

    style default_monika is normal:
        slow_cps 30

    style edited is default:
        xpos gui.text_xpos
        xanchor gui.text_xalign
        ypos gui.text_ypos
        text_align gui.text_xalign
        kerning 8
        xsize gui.text_width
        layout ("subtitle" if gui.text_xalign else "tex")
        font "gui/font/VerilySerifMono.otf"
        outlines [(10, "#000", 0, 0)]

    style normal is default:
        xpos gui.text_xpos
        xanchor gui.text_xalign
        ypos gui.text_ypos
        text_align gui.text_xalign
        xsize gui.text_width
        layout ("subtitle" if gui.text_xalign else "tex")


    style input:
        color gui.accent_color

    style hyperlink_text:
        color gui.accent_color
        hover_color gui.hover_color
        hover_underline True

    style splash_text:
        color "#000"
        size 24
        font gui.default_font
        text_align 0.5
        outlines []

    style poemgame_text:
        font "gui/font/Halogen.ttf"
        yalign 0.5
        color "#000"
        hover_xoffset -3
        outlines []
        hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]
        size 30


    style gui_text:
        color gui.interface_text_color
        font gui.interface_font
        size gui.interface_text_size


    style button:
        properties gui.button_properties("button")

    style button_text is gui_text:
        properties gui.button_text_properties("button")
        yalign 0.5


    style label_text is gui_text:
        color gui.accent_color
        size gui.label_text_size

    style prompt_text is gui_text:
        color gui.text_color
        size gui.interface_text_size







    style vbar:
        bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)
        top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
        xsize gui.bar_size

    style bar:
        ysize 18
        base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
        thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

    style scrollbar:
        bar_invert True
        ysize 18
        base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
        unscrollable "hide"
        thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)


    style vscrollbar:
        bar_invert True
        xsize 18
        base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
        unscrollable "hide"
        thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)






    style slider:
        ysize 18
        base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
        thumb "gui/slider/horizontal_hover_thumb.png"

    style vslider:
        base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
        xsize gui.slider_size
        thumb "gui/slider/vertical_[prefix_]thumb.png"


    style frame:
        padding gui.frame_borders.padding
        background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)





















screen say:
    style_prefix "say"
    window:
        id "window"
        text what:
            id "what"
        if who is not None:
            window:
                style "namebox"
                text who:
                    id "who"
    use quick_menu










    style window is default
    style say_label is default
    style say_dialogue is default
    style say_thought is say_dialogue

    style namebox is default
    style namebox_label is say_label


    style window:
        xalign 0.5
        xfill True
        ysize gui.textbox_height
        yalign gui.textbox_yalign
        background Image("gui/textbox.png", xalign=0.5, yalign=1.0)


    style window_monika is window:
        background Image("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

    style namebox:
        xpos gui.name_xpos
        xanchor gui.name_xalign
        background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
        ysize gui.namebox_height
        ypos gui.name_ypos
        padding gui.namebox_borders.padding
        xsize gui.namebox_width


    style say_label:
        xalign gui.name_xalign
        yalign 0.5
        color gui.accent_color
        font gui.name_font
        outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
        size gui.name_text_size

    style say_dialogue:
        xpos gui.text_xpos
        xanchor gui.text_xalign
        ypos gui.text_ypos
        text_align gui.text_xalign
        xsize gui.text_width
        layout ("subtitle" if gui.text_xalign else "tex")


    image ctc:
        xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True 
        "gui/ctc.png" 
        block:
            easeout 0.75 alpha 1.0 xoffset 0 
            easein 0.75 alpha 0.5 xoffset -5 
            repeat











    image input_caret:
        Solid("#b59") 
        size (2,25) subpixel True 
        block:
            linear 0.35 alpha 0 
            linear 0.35 alpha 1 
            repeat

screen input:
    style_prefix "input"
    window:
        vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos
            text prompt:
                style "input_prompt"
            input:
                id "input"



    style input_prompt is default

    style input_prompt:
        xalign gui.text_xalign
        xmaximum gui.text_width
        text_align gui.text_xalign

    style input:
        caret "input_caret"
        xalign 0.5
        xmaximum gui.text_width
        text_align 0.5










screen choice:
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption:
                action i.action




    define narrator_menu = True


    style choice_vbox is vbox
    style choice_button is button
    style choice_button_text is button_text

    style choice_vbox:
        xalign 0.5
        spacing gui.choice_spacing
        ypos 270
        yanchor 0.5


    style choice_button is default:
        hover_sound gui.hover_sound
        properties gui.button_properties("choice_button")
        activate_sound gui.activate_sound

    style choice_button_text is default:
        properties gui.button_text_properties("choice_button")
        outlines []


init -1 python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice:
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption:
                action i.action
    timer 1.0/30.0:
        repeat True
        action Function(RigMouse)



    define narrator_menu = True


    style choice_vbox is vbox
    style choice_button is button
    style choice_button_text is button_text

    style choice_vbox:
        xalign 0.5
        spacing gui.choice_spacing
        ypos 270
        yanchor 0.5


    style choice_button is default:
        hover_sound gui.hover_sound
        properties gui.button_properties("choice_button")
        activate_sound gui.activate_sound

    style choice_button_text is default:
        properties gui.button_text_properties("choice_button")
        outlines []







screen quick_menu:
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.995
            textbutton _("History"):
                action ShowMenu('history')
            textbutton _("Skip"):
                action Skip()
                alternate Skip(fast=True, confirm=True)
            textbutton _("Auto"):
                action Preference("auto-forward", "toggle")
            textbutton _("Save"):
                action ShowMenu('save')
            textbutton _("Load"):
                action ShowMenu('load')
            textbutton _("Settings"):
                action ShowMenu('preferences')
            if config.developer:
                textbutton "Devtools":
                    action ShowMenu('_developer')









    default quick_menu = True




    style quick_button:
        properties gui.button_properties("quick_button")
        activate_sound gui.activate_sound

    style quick_button_text:
        properties gui.button_text_properties("quick_button")
        outlines []











init -1 python:
    def FinishEnterName():
        if not player: return
        persistent.playername = player
        renpy.hide_screen("name_input")
        renpy.jump_out_of_context("start")

screen navigation:
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.8
        spacing gui.navigation_spacing
        if not persistent.autoload or not main_menu:
            if main_menu:
                if persistent.playthrough == 1:
                    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«"):
                        action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
                else:
                    textbutton _("New Game"):
                        action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName)))
            else:
                textbutton _("History"):
                    action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
                textbutton _("Save Game"):
                    action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)]
            textbutton _("Load Game"):
                action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)]
            if _in_replay:
                textbutton _("End Replay"):
                    action EndReplay(confirm=True)
            elif not main_menu:
                if persistent.playthrough != 3:
                    textbutton _("Main Menu"):
                        action MainMenu()
                else:
                    textbutton _("Main Menu"):
                        action NullAction()
            textbutton _("Settings"):
                action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
            if persistent.playthrough > 0:
                textbutton _("Characters"):
                    action [ShowMenu("characters"), SensitiveIf(renpy.get_screen("characters") == None)]
            if renpy.variant("pc"):
                textbutton _("Help"):
                    action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]
            textbutton _("Quit"):
                action Quit(confirm=not main_menu)
        else:
            timer 1.75:
                action Start("autoload_yurikill")











    style navigation_button is gui_button
    style navigation_button_text is gui_button_text

    style navigation_button:
        hover_sound gui.hover_sound
        properties gui.button_properties("navigation_button")
        activate_sound gui.activate_sound
        size_group "navigation"

    style navigation_button_text:
        color "#fff"
        outlines [(4, "#b59", 0, 0), (2, "#b59", 2, 2)]
        insensitive_outlines [(4, "#fce", 0, 0), (2, "#fce", 2, 2)]
        font "gui/font/RifficFree-Bold.ttf"
        properties gui.button_text_properties("navigation_button")
        hover_outlines [(4, "#fac", 0, 0), (2, "#fac", 2, 2)]








screen main_menu:
    tag menu
    style_prefix "main_menu"
    if persistent.ghost_menu:
        add "white"
        add "menu_art_y_ghost"
        add "menu_art_n_ghost"
    else:
        add "menu_bg"
        add "menu_art_y"
        add "menu_art_n"
        frame
        use navigation
    if gui.show_name:
        vbox:
            text "[config.name!t]":
                style "main_menu_title"
            text "[config.version]":
                style "main_menu_version"
    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"
    if persistent.ghost_menu:
        add "menu_art_s_ghost"
        add "menu_art_m_ghost"
    else:
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            add "menu_art_s_glitch"
        else:
            add "menu_art_s"
        add "menu_particles"
        if persistent.playthrough != 4:
            add "menu_art_m"
        add "menu_fade"
    key "K_ESCAPE":
        action Quit(confirm=False)













    style main_menu_frame is empty
    style main_menu_vbox is vbox
    style main_menu_text is gui_text
    style main_menu_title is main_menu_text
    style main_menu_version is main_menu_text:
        color "#000000"
        outlines []
        size 16

    style main_menu_frame:
        yfill True
        xsize 310
        background "menu_nav"


    style main_menu_vbox:
        xalign 1.0
        xmaximum 800
        xoffset -20
        yalign 1.0
        yoffset -20

    style main_menu_text:
        color gui.accent_color
        xalign 1.0
        layout "subtitle"
        text_align 1.0


    style main_menu_title:
        size gui.title_text_size











screen game_menu_m:
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3:
        action Hide("game_menu_m")
screen game_menu:
    style_prefix "game_menu"
    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3":
            action Return()
        add gui.game_menu_background
    frame:
        style "game_menu_outer_frame"
        hbox:
            frame:
                style "game_menu_navigation_frame"
            frame:
                style "game_menu_content_frame"
                if scroll == "viewport":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        yinitial 1.0
                        side_yfill True
                        vbox:
                            #TODO sl2 <renpy.sl2.slast.SLTransclude object at 0x05BA3150>
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial 1.0
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        side_yfill True
                        #TODO sl2 <renpy.sl2.slast.SLTransclude object at 0x05BA31F0>
                else:
                    #TODO sl2 <renpy.sl2.slast.SLTransclude object at 0x05BA3230>
    use navigation
    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0:
        on "show":
            action Show("game_menu_m")
    textbutton _("Return"):
        style "return_button"
        action Return()
    label title
    if main_menu:
        key "game_menu":
            action ShowMenu("main_menu")
























    style game_menu_outer_frame is empty
    style game_menu_navigation_frame is empty
    style game_menu_content_frame is empty
    style game_menu_viewport is gui_viewport
    style game_menu_side is gui_side
    style game_menu_scrollbar is gui_vscrollbar

    style game_menu_label is gui_label
    style game_menu_label_text is gui_label_text

    style return_button is navigation_button
    style return_button_text is navigation_button_text

    style game_menu_outer_frame:
        top_padding 120
        bottom_padding 30
        background "gui/overlay/game_menu.png"


    style game_menu_navigation_frame:
        yfill True
        xsize 280

    style game_menu_content_frame:
        left_margin 40
        top_margin 10
        right_margin 20

    style game_menu_viewport:
        xsize 920

    style game_menu_vscrollbar:
        unscrollable gui.unscrollable

    style game_menu_side:
        spacing 10

    style game_menu_label:
        xpos 50
        ysize 120

    style game_menu_label_text:
        color "#fff"
        font "gui/font/RifficFree-Bold.ttf"
        outlines [(6, "#b59", 0, 0), (3, "#b59", 2, 2)]
        yalign 0.5
        size gui.title_text_size

    style return_button:
        xpos gui.navigation_xpos
        yalign 1.0
        yoffset -30









screen about:
    tag menu
    use game_menu (_("About"), scroll="viewport")





















    define about = ""


    style about_label is gui_label
    style about_label_text is gui_label_text
    style about_text is gui_text

    style about_label_text:
        size gui.label_text_size











screen save:
    tag menu
    use file_slots (_("Save"))




screen load:
    tag menu
    use file_slots (_("Load"))



init -1 python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                    ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))
        else:
            return FileAction(name)


screen file_slots:
    default page_name_value = FilePageNameInputValue()
    use game_menu (title)








































































    style page_label is gui_label
    style page_label_text is gui_label_text
    style page_button is gui_button
    style page_button_text is gui_button_text

    style slot_button is gui_button
    style slot_button_text is gui_button_text
    style slot_time_text is slot_button_text
    style slot_name_text is slot_button_text

    style page_label:
        ypadding 3
        xpadding 50

    style page_label_text:
        color "#000"
        hover_color gui.hover_color
        layout "subtitle"
        outlines []
        text_align 0.5

    style page_button:
        properties gui.button_properties("page_button")

    style page_button_text:
        properties gui.button_text_properties("page_button")
        outlines []

    style slot_button:
        properties gui.button_properties("slot_button")

    style slot_button_text:
        color "#666"
        properties gui.button_text_properties("slot_button")
        outlines []


screen characters:
    tag menu
    use game_menu (_("Files"), scroll="viewport")








































screen preferences:
    tag menu
    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4
    use game_menu (_("Settings"), scroll="viewport")
    text "v[config.version]":
        xalign 1.0
        yalign 1.0
        xoffset -10
        yoffset -10
        style "main_menu_version"





















































































    style pref_label is gui_label
    style pref_label_text is gui_label_text
    style pref_vbox is vbox

    style radio_label is pref_label
    style radio_label_text is pref_label_text
    style radio_button is gui_button
    style radio_button_text is gui_button_text
    style radio_vbox is pref_vbox

    style check_label is pref_label
    style check_label_text is pref_label_text
    style check_button is gui_button
    style check_button_text is gui_button_text
    style check_vbox is pref_vbox

    style slider_label is pref_label
    style slider_label_text is pref_label_text
    style slider_slider is gui_slider
    style slider_button is gui_button
    style slider_button_text is gui_button_text
    style slider_pref_vbox is pref_vbox

    style mute_all_button is check_button
    style mute_all_button_text is check_button_text

    style pref_label:
        bottom_margin 2
        top_margin gui.pref_spacing

    style pref_label_text:
        color "#fff"
        font "gui/font/RifficFree-Bold.ttf"
        outlines [(3, "#b59", 0, 0), (1, "#b59", 1, 1)]
        yalign 1.0
        size 24

    style pref_vbox:
        xsize 225

    style radio_vbox:
        spacing gui.pref_button_spacing

    style radio_button:
        foreground "gui/button/check_[prefix_]foreground.png"
        properties gui.button_properties("radio_button")

    style radio_button_text:
        font "gui/font/Halogen.ttf"
        properties gui.button_text_properties("radio_button")
        outlines []

    style check_vbox:
        spacing gui.pref_button_spacing

    style check_button:
        foreground "gui/button/check_[prefix_]foreground.png"
        properties gui.button_properties("check_button")

    style check_button_text:
        font "gui/font/Halogen.ttf"
        properties gui.button_text_properties("check_button")
        outlines []

    style slider_slider:
        xsize 350

    style slider_button:
        properties gui.button_properties("slider_button")
        yalign 0.5
        left_margin 10

    style slider_button_text:
        properties gui.button_text_properties("slider_button")

    style slider_vbox:
        xsize 450










screen history:
    tag menu
    predict False
    use game_menu (_("History"), scroll=("vpgrid" if gui.history_height else "viewport"))































    style history_window is empty

    style history_name is gui_label
    style history_name_text is gui_label_text
    style history_text is gui_text

    style history_text is gui_text

    style history_label is gui_label
    style history_label_text is gui_label_text

    style history_window:
        ysize gui.history_height
        xfill True

    style history_name:
        xpos gui.history_name_xpos
        xanchor gui.history_name_xalign
        ypos gui.history_name_ypos
        xsize gui.history_name_width

    style history_name_text:
        min_width gui.history_name_width
        text_align gui.history_name_xalign

    style history_text:
        xpos gui.history_text_xpos
        xanchor gui.history_text_xalign
        ypos gui.history_text_ypos
        text_align gui.history_text_xalign
        xsize gui.history_text_width
        min_width gui.history_text_width
        layout ("subtitle" if gui.history_text_xalign else "tex")

    style history_label:
        xfill True

    style history_label_text:
        xalign 0.5












































































































































































screen name_input:
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    key "K_RETURN":
        action [Play("sound", gui.activate_sound), ok_action]
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            input:
                default ""
                value VariableInputValue("player")
                length 12
                allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK"):
                    action ok_action











screen dialog:
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            label _(message):
                style "confirm_prompt"
                xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("OK"):
                    action ok_action










    image confirm_glitch:
        "gui/overlay/confirm_glitch.png" 
        pause 0.02 
        "gui/overlay/confirm_glitch2.png" 
        pause 0.02 
        repeat

screen confirm:
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"
    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 30
            if in_sayori_kill and message == layout.QUIT:
                add "confirm_glitch":
                    xalign 0.5
            else:
                label _(message):
                    style "confirm_prompt"
                    xalign 0.5
            hbox:
                xalign 0.5
                spacing 100
                textbutton _("Yes"):
                    action yes_action
                textbutton _("No"):
                    action no_action













    style confirm_frame is gui_frame
    style confirm_prompt is gui_prompt
    style confirm_prompt_text is gui_prompt_text
    style confirm_button is gui_medium_button
    style confirm_button_text is gui_medium_button_text

    style confirm_frame:
        padding gui.confirm_frame_borders.padding
        xalign .5
        background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
        yalign .5

    style confirm_prompt_text:
        color "#000"
        layout "subtitle"
        outlines []
        text_align 0.5

    style confirm_button:
        hover_sound gui.hover_sound
        properties gui.button_properties("confirm_button")
        activate_sound gui.activate_sound

    style confirm_button_text is navigation_button_text:
        properties gui.button_text_properties("confirm_button")








screen fake_skip_indicator:
    use skip_indicator

screen skip_indicator:
    zorder 100
    style_prefix "skip"
    frame:
        hbox:
            spacing 6
            text _("Skipping")
            text "▸":
                at delayed_blink(0.0, 1.0)
                style "skip_triangle"
            text "▸":
                at delayed_blink(0.2, 1.0)
                style "skip_triangle"
            text "▸":
                at delayed_blink(0.4, 1.0)
                style "skip_triangle"


    transform delayed_blink (delay, cycle):
        alpha .5 
        pause delay 
        block:
            linear .2 alpha 1.0 
            pause .2 
            linear .2 alpha 0.5 
            pause (cycle - .4) 
            repeat




    style skip_frame is empty
    style skip_text is gui_text
    style skip_triangle is skip_text

    style skip_frame:
        padding gui.skip_frame_borders.padding
        ypos gui.skip_ypos
        background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)

    style skip_text:
        size gui.notify_text_size

    style skip_triangle:
        font "DejaVuSans.ttf"











screen notify:
    zorder 100
    style_prefix "notify"
    frame:
        at notify_appear
        text message
    timer 3.25:
        action Hide('notify')



    transform notify_appear:
        on hide:
            linear .5 alpha 0.0 
        on show:
            alpha 0 
            linear .25 alpha 1.0 


    style notify_frame is empty
    style notify_text is gui_text

    style notify_frame:
        padding gui.notify_frame_borders.padding
        ypos gui.notify_ypos
        background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)


    style notify_text:
        size gui.notify_text_size
