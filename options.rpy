


python early:
    def widget__info():
        import os
        def editoverlay():
            fullfn, line = renpy.get_filename_line()
            ui.button(clicked=None, xpos=1.0, xanchor=1.0, ypos=2, xpadding=0, xminimum=200)
            ui.text(u"%s:%d" % (os.path.basename(fullfn), line), size=16)
            if renpy.current_screen() is None:
                return
            ui.button(clicked=None, xpos=0.75, xanchor=1.0, ypos=2, xpadding=0, xminimum=200)
            ui.text(u"%s, %s" % (renpy.current_screen(), str(renpy.current_screen()._location)), size=16)
            out_str = "scr %s (%s), fl %s:%d" % (renpy.current_screen(), str(renpy.current_screen()._location), os.path.basename(fullfn), line)
            print out_str.encode('utf-8')
        config.overlay_functions.append(editoverlay)
init 9000 python:
    if config.developer:
        widget__info()












    define name = "Doki Doki Literature Club!"





    define show_name = False




    define version = "1.1.0"





    define about = _("")






    define name = "DDLC"






    define has_sound = True
    define has_music = True
    define has_voice = False













    define main_menu_music = audio.t1










    define enter_transition = Dissolve(.2)
    define exit_transition = Dissolve(.2)




    define after_load_transition = None




    define end_game_transition = Dissolve(.5)
















    define window = "auto"




    define window_show_transition = Dissolve(.2)
    define window_hide_transition = Dissolve(.2)







    default text_cps = 50
    default fullscreen = True





    default afm_time = 15

    default music_volume = 0.75
    default sfx_volume = 0.75
















    define save_directory = "DDLC-1454445547"







    define window_icon = "gui/window_icon.png"



    define allow_skipping = True

    define autosave_slots = 8
    define layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
    define image_cache_size = 64
    define predict_statements = 50
    define rollback_enabled = config.developer
    define menu_clear_layers = ["front"]
    define gl_test_image = "white"

init 65533 python:
    config.has_autosave = True  
    config.autosave_on_quit = True
    config.autosave_frequency = 10  
    config.save_on_mobile_background = True
    config.quit_on_mobile_background = False

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014')
        s = s.replace(' - ', u'\u2014')
        return s
    config.replace_text = replace_text
    
    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')
    
    config.game_menu_action = game_menu_check
    
    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)






init python:
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    build.archive("scripts", "all")
    build.archive("images", "all")
    build.archive("audio", "all")
    build.archive("fonts", "all")
    
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")
    
    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.txt", "scripts")
    build.classify("game/**.chr", "scripts")
    build.classify("game/**.wav", "audio")
    build.classify("game/**.mp3", "audio")
    build.classify("game/**.ogg", "audio")
    build.classify("game/**.ttf", "fonts")
    build.classify("game/**.otf", "audio")
    
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    
    
    
    
    
    
    
    
    
    build.documentation('*.html')
    build.documentation('*.txt')
    
    build.include_old_themes = False











    define itch_project = "teamsalvato/ddlc"
