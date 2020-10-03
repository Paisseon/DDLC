









init -2 python:
    gui.init(1280, 720)







    define hover_sound = "gui/sfx/hover.ogg"
    define activate_sound = "gui/sfx/select.ogg"
    define activate_sound_glitch = "gui/sfx/select_glitch.ogg"






    define accent_color = '#ffffff'


    define idle_color = '#aaaaaa'



    define idle_small_color = '#333'


    define hover_color = '#cc6699'



    define selected_color = '#bb5588'


    define insensitive_color = '#aaaaaa7f'



    define muted_color = '#6666a3'
    define hover_muted_color = '#9999c1'


    define text_color = '#ffffff'
    define interface_text_color = '#ffffff'





    define default_font = "gui/font/Aller_Rg.ttf"


    define name_font = "gui/font/RifficFree-Bold.ttf"


    define interface_font = "gui/font/Aller_Rg.ttf"


    define text_size = 26


    define name_text_size = 26


    define interface_text_size = 26


    define label_text_size = 30


    define notify_text_size = 16


    define title_text_size = 40





    define main_menu_background = "menu_bg"
    define game_menu_background = "game_menu_bg"


    define show_name = False








    define textbox_height = 182



    define textbox_yalign = 0.99




    define name_xpos = 350
    define name_ypos = -3



    define name_xalign = 0.5



    define namebox_width = 168
    define namebox_height = 39



    define namebox_borders = Borders(5, 5, 5, 2)



    define namebox_tile = False





    define text_xpos = 240
    define text_ypos = 43


    define text_width = 804



    define text_xalign = 0.0








    define button_width = None
    define button_height = 36


    define button_borders = Borders(4, 4, 4, 4)



    define button_tile = False


    define button_text_font = gui.interface_font


    define button_text_size = gui.interface_text_size


    define button_text_idle_color = gui.idle_color
    define button_text_hover_color = gui.hover_color
    define button_text_selected_color = gui.selected_color
    define button_text_insensitive_color = gui.insensitive_color



    define button_text_xalign = 0.0








    define radio_button_borders = Borders(28, 4, 4, 4)

    define check_button_borders = Borders(28, 4, 4, 4)

    define confirm_button_text_xalign = 0.5

    define page_button_borders = Borders(10, 4, 10, 4)


    define quick_button_text_size = 19
    define quick_button_text_idle_color = "#522"
    define quick_button_text_hover_color = "#fcc"
    define quick_button_text_selected_color = gui.accent_color
    define quick_button_text_insensitive_color = "#a66"












    define choice_button_width = 420
    define choice_button_height = None
    define choice_button_tile = False
    define choice_button_borders = Borders(100, 5, 100, 5)
    define choice_button_text_font = gui.default_font
    define choice_button_text_size = gui.text_size
    define choice_button_text_xalign = 0.5
    define choice_button_text_idle_color = "#000"
    define choice_button_text_hover_color = "#fa9"









    define slot_button_width = 276
    define slot_button_height = 206
    define slot_button_borders = Borders(10, 10, 10, 10)
    define slot_button_text_size = 14
    define slot_button_text_xalign = 0.5
    define slot_button_text_idle_color = gui.idle_small_color
    define slot_button_text_hover_color = gui.hover_color


    define thumbnail_width = 256
    define thumbnail_height = 144


    define file_slot_cols = 3
    define file_slot_rows = 2









    define navigation_xpos = 80


    define skip_ypos = 10


    define notify_ypos = 45


    define choice_spacing = 22


    define navigation_spacing = 6


    define pref_spacing = 10


    define pref_button_spacing = 0


    define page_spacing = 0


    define slot_spacing = 10








    define frame_borders = Borders(4, 4, 4, 4)


    define confirm_frame_borders = Borders(40, 40, 40, 40)


    define skip_frame_borders = Borders(16, 5, 50, 5)


    define notify_frame_borders = Borders(16, 5, 40, 5)


    define frame_tile = False











    define bar_size = 36
    define scrollbar_size = 12
    define slider_size = 30


    define bar_tile = False
    define scrollbar_tile = False
    define slider_tile = False


    define bar_borders = Borders(4, 4, 4, 4)
    define scrollbar_borders = Borders(4, 4, 4, 4)
    define slider_borders = Borders(4, 4, 4, 4)


    define vbar_borders = Borders(4, 4, 4, 4)
    define vscrollbar_borders = Borders(4, 4, 4, 4)
    define vslider_borders = Borders(4, 4, 4, 4)



    define unscrollable = "hide"







    define history_length = 50



    define history_height = None



    define history_name_xpos = 150
    define history_name_ypos = 0
    define history_name_width = 150
    define history_name_xalign = 1.0


    define history_text_xpos = 170
    define history_text_ypos = 5
    define history_text_width = 740
    define history_text_xalign = 0.0







    define nvl_borders = Borders(0, 10, 0, 20)



    define nvl_height = 115



    define nvl_spacing = 10



    define nvl_name_xpos = 430
    define nvl_name_ypos = 0
    define nvl_name_width = 150
    define nvl_name_xalign = 1.0


    define nvl_text_xpos = 450
    define nvl_text_ypos = 8
    define nvl_text_width = 590
    define nvl_text_xalign = 0.0



    define nvl_thought_xpos = 240
    define nvl_thought_ypos = 0
    define nvl_thought_width = 780
    define nvl_thought_xalign = 0.0


    define nvl_button_xpos = 450
    define nvl_button_xalign = 0.0







init -2 python:
    
    
    
    if renpy.variant("touch"): 
        
        gui.quick_button_borders = Borders(18, 7, 20, 0)
    
    
    
    if False:  
        
        
        gui.text_size = 30
        gui.name_text_size = 36
        gui.notify_text_size = 25
        gui.interface_text_size = 36
        gui.button_text_size = 34
        gui.label_text_size = 36
        
        
        gui.textbox_height = 240
        gui.name_xpos = 80
        gui.text_xpos = 90
        gui.text_width = 1100
        
        
        gui.choice_button_width = 1240
        
        gui.navigation_spacing = 20
        gui.pref_button_spacing = 10
        
        gui.history_height = 190
        gui.history_text_width = 690
        
        
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2
        
        
        gui.nvl_height = 170
        
        gui.nvl_name_width = 305
        gui.nvl_name_xpos = 325
        
        gui.nvl_text_width = 915
        gui.nvl_text_xpos = 345
        gui.nvl_text_ypos = 5
        
        gui.nvl_thought_width = 1240
        gui.nvl_thought_xpos = 20
        
        gui.nvl_button_width = 1240
        gui.nvl_button_xpos = 20
        
        
        gui.quick_button_text_size = 20
