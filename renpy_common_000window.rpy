























init -1200 python:
    
    config.window_show_transition = None
    config.window_hide_transition = None
    config.window = None
    
    
    config.window_auto_show = [ "say", "menu-with-caption" ]
    
    
    config.window_auto_hide = [ "scene", "call screen", "menu" ]
    
    _window_auto = False
    
    def _window_show(trans=False):
        """
            :doc: window
    
            The Python equivalent of the "window show" statement.
    
            `trans`
                If False, the default window show transition is used. If None,
                no transition is used. Otherwise, the specified transition is
                used.
            """
        
        if store._window:
            return
        
        if trans is False:
            trans = config.window_show_transition
        
        if _preferences.show_empty_window and (not renpy.game.after_rollback):
            renpy.with_statement(None)
            store._window = True
            renpy.with_statement(trans)
        else:
            store._window = True
    
    def _window_hide(trans=False):
        """
            :doc: window
    
            The Python equivalent of the "window hide" statement.
    
            `trans`
                If False, the default window hide transition is used. If None,
                no transition is used. Otherwise, the specified transition is
                used.
            """
        
        if not store._window:
            return
        
        if trans is False:
            trans = config.window_hide_transition
        
        if _preferences.show_empty_window and (not renpy.game.after_rollback):
            renpy.with_statement(None)
            store._window = False
            renpy.with_statement(trans)
        else:
            store._window = False
    
    def _window_auto_callback(statement):
        
        if not store._window_auto:
            return
        
        if statement in config.window_auto_hide:
            _window_hide()
        
        if statement in config.window_auto_show:
            _window_show()
    
    config.statement_callbacks.append(_window_auto_callback)
    
    def _init_window():
        
        global _window
        global _window_auto
        
        if config.window == "auto":
            _window_auto = True
            _window = False
        
        elif config.window == "show":
            _window_auto = False
            _window = True
        
        elif config.window == "hide":
            _window_auto = False
            _window = False


python early hide:
    
    
    
    def parse_window(l):
        p = l.simple_expression()
        if not l.eol():
            renpy.error('expected end of line')
        
        return p
    
    def lint_window(p):
        if p is not None:
            _try_eval(p, 'window transition')
    
    def execute_window_show(p):
        store._window_auto = False
        
        if p is not None:
            trans = eval(p)
        else:
            trans = False
        
        _window_show(trans)
    
    def execute_window_hide(p):
        store._window_auto = False
        
        if p is not None:
            trans = eval(p)
        else:
            trans = False
        
        _window_hide(trans)
    
    def parse_window_auto(l):
        
        rv = { }
        
        if l.keyword('hide'):
            hide = l.simple_expression() or "False"
            rv["hide"] = hide
        
        elif l.keyword('show'):
            show = l.simple_expression() or "False"
            rv["show"] = show
        
        if not l.eol():
            renpy.error('expected end of line')
        
        return rv
    
    def execute_window_auto(p):
        store._window_auto = True
        
        if "hide" in p:
            trans = eval(p["hide"])
            _window_hide(trans)
        
        if "show" in p:
            trans = eval(p["show"])
            _window_show(trans)
    
    
    renpy.register_statement('window show',
                                  parse=parse_window,
                                  execute=execute_window_show,
                                  lint=lint_window,
                                  warp=lambda : True)
    
    renpy.register_statement('window hide',
                                  parse=parse_window,
                                  execute=execute_window_hide,
                                  lint=lint_window,
                                  warp=lambda : True)
    
    renpy.register_statement('window auto',
                                 parse=parse_window_auto,
                                 execute=execute_window_auto,
                                 warp=lambda : True)
