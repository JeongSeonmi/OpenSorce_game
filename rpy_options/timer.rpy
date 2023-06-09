style text_timer_ok:
    size 100
    color "#FFF"
    outlines [(2, "#000", 0, 0)]

style text_timer_near:
    size 100
    color "#F22"
    outlines [(2, "#000", 0, 0)]

init python:
    
    def text_countdown( st, at, 
                        duration = 15.0,  
                        screen = 'text_timer',
                        ok_style = 'text_timer_ok',
                        near_style = 'text_timer_near',
                        style_swap = 5.0,
                        text_format = "{minutes:02d}:{seconds:02d}" ):
        remaining = duration - st

        parts_dict = {
            'minutes' : int( remaining // 60 ),
            'seconds' : int( remaining % 60 ),
        }
        if remaining <= 0.0 :
            renpy.hide_screen("text_timer")
            if myP == "hospital" :
                renpy.jump ("hospital")
            elif myP == "company" :
                renpy.jump("company")
            elif myP == "villa" :
                renpy.jump("villa")
    
        return Text( text_format.format(**parts_dict), 
                    style = ok_style if remaining > style_swap else near_style), .1

    
screen text_timer :
    zorder 100
    vbox:
        add DynamicDisplayable(text_countdown)
        xalign 0.99
        