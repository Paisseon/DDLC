























python early:
    
    
    
    
    
    
    
    
    
    
    @renpy.atl_warper
    def linear(t):
        return t
    
    @renpy.atl_warper
    def easeout(x):
        import math
        return 1.0 - math.cos(x * math.pi / 2.0)
    
    @renpy.atl_warper
    def easein(x):
        import math
        return math.cos((1.0 - x) * math.pi / 2.0)
    
    @renpy.atl_warper
    def ease(x):
        import math
        return .5 - math.cos(math.pi * x) / 2.0
    
    
    
    
    
    
    
    @renpy.atl_warper
    def easeout_quad(t):
        return pow(t, 2)
    
    @renpy.atl_warper
    def easein_quad(t):
        return 1 - easeout_quad(1 - t)
    
    @renpy.atl_warper
    def ease_quad(t):
        if t < .5:
            return easeout_quad(t * 2.0) / 2.0
        else:
            return 1 - easeout_quad((1 - t)* 2.0) / 2.0
    
    
    
    @renpy.atl_warper
    def easeout_cubic(t):
        return pow(t, 3)
    
    @renpy.atl_warper
    def easein_cubic(t):
        return 1 - easeout_cubic(1 - t)
    
    @renpy.atl_warper
    def ease_cubic(t):
        if t < .5:
            return easeout_cubic(t * 2.0) / 2.0
        else:
            return 1 - easeout_cubic((1 - t)* 2.0) / 2.0
    
    
    
    @renpy.atl_warper
    def easeout_quart(t):
        return pow(t, 4)
    
    @renpy.atl_warper
    def easein_quart(t):
        return 1 - easeout_quart(1 - t)
    
    @renpy.atl_warper
    def ease_quart(t):
        if t < .5:
            return easeout_quart(t * 2.0) / 2.0
        else:
            return 1 - easeout_quart((1 - t)* 2.0) / 2.0
    
    
    
    @renpy.atl_warper
    def easeout_quint(t):
        return pow(t, 5)
    
    @renpy.atl_warper
    def easein_quint(t):
        return 1 - easeout_quint(1 - t)
    
    @renpy.atl_warper
    def ease_quint(t):
        if t < .5:
            return easeout_quint(t * 2.0) / 2.0
        else:
            return 1 - easeout_quint((1 - t)* 2.0) / 2.0
    
    
    
    @renpy.atl_warper
    def easeout_expo(t):
        return pow(2, 10 * (t - 1))
    
    @renpy.atl_warper
    def easein_expo(t):
        return 1 - easeout_expo(1 - t)
    
    @renpy.atl_warper
    def ease_expo(t):
        if t < .5:
            return easeout_expo(t * 2.0) / 2.0
        else:
            return 1 - easeout_expo((1 - t)* 2.0) / 2.0
    
    
    
    @renpy.atl_warper
    def easeout_circ(t):
        import math
        return 1 - math.sqrt(1 - t * t)
    
    @renpy.atl_warper
    def easein_circ(t):
        return 1 - easeout_circ(1- t)
    
    @renpy.atl_warper
    def ease_circ(t):
        if t < .5:
            return  easeout_circ(t * 2.0) / 2.0
        else:
            return 1 - easeout_circ((1- t) * 2.0) / 2.0
    
    
    
    @renpy.atl_warper
    def easeout_back(t):
        s = 1.7015 
        return t * t * ((s + 1) * t - s)
    
    @renpy.atl_warper
    def easein_back(t):
        return  1 - easeout_back(1- t)
    
    @renpy.atl_warper
    def ease_back(t):
        if t < .5:
            return  easeout_back(t * 2.0) / 2.0
        else:
            return 1 - easeout_back((1- t) * 2.0) / 2.0
    
    
    
    @renpy.atl_warper
    def easein_elastic(t):
        import math
        p = .3 
        return 1 + pow(2, - 10 * t) * math.sin((t - p / 4.0) * (2.0 * math.pi) / p)
    
    @renpy.atl_warper
    def easeout_elastic(t):
        return 1 - easein_elastic(1 - t)
    
    @renpy.atl_warper
    def ease_elastic(t):
        if t < .5:
            return  easeout_elastic(t * 2.0) / 2.0
        else:
            return 1 - easeout_elastic((1- t) * 2.0) / 2.0
    
    
    
    @renpy.atl_warper
    def easein_bounce(t):
        p = 2.75 
        s = pow(p, 2)
        if t < (1.0 / p):
            return s * t * t
        elif t < (2.0 / p):
            return 1 + s * (pow(t - 1.5 / p, 2) - pow(- .5 / p, 2))
        elif t < (2.5 / p):
            return 1 + s * (pow(t - 2.25 / p, 2) - pow(- .25 / p, 2))
        else:
            return 1 + s * (pow(t - 2.625 / p, 2) - pow(- .125 / p, 2))
    
    @renpy.atl_warper
    def easeout_bounce(t):
        return 1 - easein_bounce(1 - t)
    
    @renpy.atl_warper
    def ease_bounce(t):
        if t < .5:
            return  easeout_bounce(t * 2.0) / 2.0
        else:
            return 1 - easeout_bounce((1- t) * 2.0) / 2.0
