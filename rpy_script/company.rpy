label company : 
    #증거 찾기 이미지맵이랑, 라벨만 CP붙힘/ search : 이미지맵, find : 라벨
    $ myP = "company"
    $ myR = ""  
    $ visit_company = 1
        
init python:
    #추리점수&방 탐색
    visited = set()
    hint = set()
    Talk = set()

## 게임에서 사용할 이미지(배경, 캐릭터 등) ##   
init :
    #방 이미지
    image bg_CP = "BG/CP.png"   
    image bg_CP_office1 = "BG/CP_office1.png"
    image bg_CP_office2 = "BG/CP_office2.png"
    image bg_CP_room = "BG/CP_room.png"
    image CP_map = im.FactorScale("BG/CP_map.png", 1.3)
   

    ## 사무실 201호 증거찾기   // 위치만 설정 완료, 변수명 바꿔야함
    screen search_CP1 : 
        zorder 99
        imagemap :
            ground "BG/CP_office1.png"
            hotspot(383, 746, 121, 246) action Return("hint1") #왼쪽기준 서랍1
            hotspot(774, 680, 106, 200) action Return("hint2") #서랍2
            hotspot(1009, 521, 52, 124) action Return("hint3") #서랍3
            hotspot(528, 535, 142, 134) action Return("hint4") #컴퓨터
            hotspot(1127, 564, 72, 184) action Return("hint5") #서랍4
            hotspot(1424, 323, 27, 45) action Return("hint6") #왼쪽기준 1번째 창문 유리
            hotspot(178, 199, 667, 300) action Return("hint7") #3번째 창문 유리
            hotspot(1601, 457, 125, 307) action Return("hint8") #오른쪽 책상 위
            
            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("company_office1")]

    ## 사무실 202호 증거찾기
    screen search_CP2 : 
        zorder 99
        imagemap :
            ground "BG/CP_office2.png"
            hotspot(326, 620, 93, 201) action Return("hint1") #서랍
            hotspot(919, 733, 69, 177) action Return("hint2") #서랍
            hotspot(1275, 428, 109, 190) action Return("hint3") #빨간 꽃 화분
            hotspot(1601, 457, 125, 307) action Return("hint4") #오른쪽 화분 밑 큰 서랍
            hotspot(165, 348, 79, 142) action Return("hint5") #화분
            hotspot(342, 523, 111, 62) action Return("hint6") #책상 위 하얀 종이
            hotspot(854, 704, 45, 74) action Return("hint7") #서랍위 하얀종이
            hotspot(978, 549, 29, 44) action Return("hint8") #책상 위 파란색

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("company_office2")]

    ## 휴게실 증거찾기
    screen search_CP3 : 
        zorder 99
        imagemap :
            ground "BG/CP_room.png"
            hotspot(1318, 368, 121, 142) action Return("hint1") #벽에 큰 게시판
            hotspot(229, 356, 126, 254) action Return("hint2") #책장
            hotspot(0, 605, 111, 177) action Return("hint3") #컴퓨터
            hotspot(569, 572, 236, 17) action Return("hint4") #책상 위
            hotspot(1026, 325, 62, 231) action Return("hint5") #오른쪽 커튼
            hotspot(360, 238, 77, 349) action Return("hint6") #왼쪽 커튼
            hotspot(547, 868, 130, 139) action Return("hint7") #그냥 바닥
            hotspot(1820, 544, 45, 82) action Return("hint8") #전등 스위치

            imagebutton idle "return_btn" :
                xalign 0.01
                yalign 0.96
                action [Hide("text_timer"), Jump("company_room")]

    ## 지도
    screen company_map :
        zorder 100
        imagemap :
                xalign 0.25
                yalign 0.45
                ground "CP_map"
                hotspot(192, 192, 223, 143) action Jump("company_office1")
                hotspot(210, 363, 207, 89) action Jump("company_office2")
                hotspot(212, 26, 207, 124) action Jump("company_room")
                
                imagebutton idle "gui/button/icon_exit.png" action Hide("company_map")

    screen company_btn:
        imagebutton idle "find_idle_btn" hover "find_hover_btn":
                xpos 927
                ypos 350
                action [
                    If(myR == "office1",
                        If("find_CP1" not in visited, Jump("find_CP1"))
                    ),
                    If(myR == "office2",
                        If("find_CP2" not in visited, Jump("find_CP2"))
                    ),
                    If(myR == "room",
                        If("find_CP3" not in visited, Jump("find_CP3"))
                    ),
                    Jump("error")
                ]

        imagebutton idle "talk_idle_btn" hover "talk_hover_btn" :
                xpos 927
                ypos 498
                action [
                    If(myR == "office1",
                        If("talk_suspecter1" not in visited, Jump("talk_suspecter1"))
                    ),
                    If(myR == "office2",
                        If("talk_suspecter2" not in visited, Jump("talk_suspecter2"))
                    ),
                    If(myR == "room",
                        If("talk_suspecter3" not in visited, Jump("talk_suspecter3"))
                    ),
                    Jump("error")
                ]
        
        imagebutton idle "gui/button/btn_return.png" :
                activate_sound "audio/sound/select.mp3"
                xalign 0.01
                yalign 0.96
                action Jump("company")

#############################################################################
## 본 스크립트 ##
hide screen company_map
scene bg_CP
show cr_Detective at right with dissolve
$ quick_menu = False

if "company_main" not in visited : 
    
    nvl clear
    DT "어디부터 살펴볼까"
    
$ visited.add("company_main")
menu : 
    "사무실 201호" :
        DT "그래 사무실 201호부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump company_office1

    "사무실 202호" :
        DT "그래 진료실 202호부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump company_office2

    "휴게실" :
        DT "그래 휴게실부터 살펴보자"
        play sound "audio/sound/open.mp3"
        jump company_room

    "그만 살펴본다" :
        $ myP = "company"
        show cr_Detective at left
        DT "이 사건의 수수께끼는 모두 풀렸어"
        show cr_police at right
        ch_police "역시 자네야! 사건의 진상을 알려주게!"
                
        $ killer_name = renpy.input('범인은 ...')
        $ last_inventory=True
        DT "범인은 [killer_name]이야!"
        
        hide cr_Detective
        hide cr_police
        
        if (killer_name == killer):
            $ ending_point += 100
        else :
            $ ending_point += 10   
        
        DT "범행 도구는..."
        jump inventory

##########################################################################
## office1 ##

label company_office1 :
    hide screen company_map
    show screen notify("사무실 201호")
    $ myR = "office1"
    $ quick_menu = False
    if "company_office1" not in visited:
        $ visited.add("company_office1")
        scene bg_CP_office1 with fade
        show cr_Detective at right

        DT "이 사무실에 평소와 같이 출근 했다고 들었는데.."

        hide cr_Detective

    scene bg_CP_office1
    show cr_CP_man1 :
        xpos 368
        ypos 100 
    
    if "man1" not in Talk:
        $ Talk.add("man1")
        ch_CP_man1 "안녕하세요 탐정님. 조사가 빨리 끝났으면 좋겠네요."
    call screen company_btn 

label find_CP1 :
    $ visited.add("find_CP1")
    $ quick_menu = True
    hide cr_CP_man1

    hide company_map
    show screen text_timer
    call screen search_CP1

    if "office1_hint1" not in hint : #왼쪽기준 서랍1
        if _return is "hint1":
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_company_hotsix).pickup(1)
            show item_company_hotsix with dissolve :
            DT idle "누가 마시던 음료군.\n 야근을 한걸까.."
            $ hint.add("office1_hint1")
            hide item_company_hotsix
            
    
    if "office1_hint2" not in hint : #서랍2
        if _return is "hint2" :
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_company_knife).pickup(1)
            show item_company_knife with dissolve :
            DT idle "(커터칼이 널브러져 있다)\n칼 끝에 무언가 묻어있어."
            $ hint.add("office1_hint2")
            hide item_company_knife

    if "office1_hint3" not in hint : #서랍3
        if _return is "hint3" :
            DT idle "(서랍 속에는 잡다한 물건뿐이다.)"
            $ hint.add("office1_hint3")
    
    if "office1_hint4" not in hint : #컴퓨터
        if _return is "hint4":
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_company_computer).pickup(1)
            show item_company_computer with dissolve :
            DT idle "컴퓨터도 끄지않은채 그대로라니...\n한창 무언가를 작업하던 중이었나보네"
            $ hint.add("office1_hint4")
            hide item_company_computer

    if "office1_hint5" not in hint : #서랍4
        if _return is "hint5":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_company_nameteg).pickup(1)
            
            show item_company_nameteg with dissolve :
            DT idle "사원증이네.\n 이걸 특별히 사용할 곳이 있을까?"
            $ hint.add("office1_hint5")
            hide item_company_nameteg

    if "office1_hint6" not in hint : #3번째 창문 유리
        if _return is "hint6":
            #play sound "audio/sound/save.mp3"
            DT idle "(무언가 빨간 색의 액체가 묻어있다.)"
            $ hint.add("office1_hint6")

    if "office1_hint7" not in hint : #왼쪽기준 1번째 창문 유리
        if _return is "hint7":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_company_view).pickup(1)
        
            show item_company_view with dissolve :
            DT idle "이 창문에서는 이러한 풍경이 보이네.\n 혹시 단서가 될까?"
            $ hint.add("office1_hint7")
            hide item_company_view
    
    if "office1_hint8" not in hint : #오른쪽 책상 위
        if _return is "hint8":
            # play sound "audio/sound/save.mp3"
            # $ item_post.pickup(1)
            # show item_hint1 with dissolve :
            DT idle "(책상 위는 깔끔하게 정리되어있다.)"
            $ hint.add("office1_hint8")
            #hide item_hint1
    
    jump find_CP1
    return

##########################################################################
## office2 ##

label company_office2 :
    hide screen company_map
    show screen notify("사무실 202호")
    $ myR = "office2"
    $ quick_menu = False

    if "company_office2" not in visited:
        $ visited.add("company_office2")
        scene bg_CP_office2 with fade
        show cr_Detective at right

        DT "어젯밤에 이 방에서 살인사건이 일어났어."

        nvl clear
        hide cr_Detective

    scene bg_CP_office2
    show cr_CP_man2 :
        xpos 368
        ypos 200
    ##npc 추가할경우 상호작용##
    if "man2" not in Talk:
        $ Talk.add("man2")
        ch_CP_man2 "하아.. 할 일이 산더미인데.."
    call screen company_btn 

label find_CP2 :
    $ visited.add("find_CP2")
    $ quick_menu = True
    hide company_map
    hide cr_CP_man2

    show screen text_timer
    call screen search_CP2 

    if "office1_hint1" not in hint : #서랍
        if _return is "hint1":
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_company_hotsix).pickup(1)
            
            show item_company_hotsix with dissolve :
            DT idle "(누군가가 마시던 음료이다)"
            $ hint.add("office2_hint1")
            hide item_company_hotsix
            
    
    if "office2_hint2" not in hint : #서랍
        if _return is "hint2" :
            play sound "audio/sound/save.mp3"
            #$ item_company_nameteg.pickup(1)
            show item_company_nameteg with dissolve :
            DT idle "(사원증이다. 이걸 특별히 사용할 곳이 있을까?)"
            $ hint.add("office2_hint2")
            hide item_company_nameteg

    if "office2_hint3" not in hint : #빨간 꽃 화분
        if _return is "hint3" :
            play sound "audio/sound/save.mp3"
            $ InvItem(*item_company_stapler).pickup(1)
            
            show item_company_stapler with dissolve :
            DT idle "스테이플러다. 증거가 될 수도 있겠군."
            $ hint.add("office2_hint3")
            hide item_company_stapler
    
    if "office2_hint4" not in hint : #오른쪽 화분 밑 큰 서랍
        if _return is "hint4":
            play sound "audio/sound/save.mp3"
           
            $ InvItem(*item_company_coffee).pickup(1)
            show item_company_coffee with dissolve :
            DT idle "(흔히 볼 수 있는 커피다.)"
            DT idle "아무리 그래도 여기있으면 안되지"
            $ hint.add("office2_hint4")
            hide item_company_coffee

    if "office2_hint5" not in hint : #화분
        if _return is "hint5":
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_company_thirsty).pickup(1)
            show item_company_thirsty with dissolve :
            DT idle "오랫동안 관리되지 않았나본데,\n무슨 일이 있었을까?"
            $ hint.add("office2_hint5")
            hide item_company_thirsty

    if "office2_hint6" not in hint : #책상 위 하얀 종이
        if _return is "hint6":
            #play sound "audio/sound/save.mp3"
            #$ InvItem(*item_post).pickup(1)
            #show item_hint1 with dissolve :
            DT idle "(업무 관련된 중요한 내용이 적혀있다.)\n함부로 읽으면 안될 것 같아."
            $ hint.add("office2_hint6")
            #hide item_hint1

    if "office2_hint7" not in hint : #서랍 위 하얀 종이
        if _return is "hint7":
            #play sound "audio/sound/save.mp3"
            #$ InvItem(*item_post).pickup(1)
            #show item_hint1 with dissolve :
            DT idle "낙서한 종이가 여기 굴러다니네.. 일하기 싫었던걸까?"
            $ hint.add("office2_hint7")
            #hide item_hint1
    
    if "office2_hint8" not in hint : #책상 위 파란색
        if _return is "hint8":
            #play sound "audio/sound/save.mp3"
            #$ InvItem(*item_post).pickup(1)
            #show item_hint1 with dissolve :
            DT idle "이 사무실은 화분이 이상할 정도로 많아.."
            DT idle "무언가 숨겨져 있어도 이상하지 않아."
            $ hint.add("office2_hint8")
            #hide item_hint1
    
    jump find_CP2
    return

##############################################################################
## room ##

label company_room :
    hide screen company_map
    show screen notify("회사 휴게실")
    $ myR = "room"
    $ quick_menu = False

    if "company_room" not in visited:
            $ visited.add("company_room")
            scene bg_CP_room with fade
            show cr_Detective at right

            DT "어젯밤에 이 방에서 살인사건이 일어났어."

            nvl clear
            hide cr_Detective

    scene bg_CP_room
    show cr_CP_woman :
        xpos 407
        ypos 170 
    ##npc 추가할경우 상호작용##
    if "woman" not in Talk:
        $ Talk.add("woman")
        ch_CP_woman "도시 한복판에서 살인사건이라니.. 너무 무서워요.."
    call screen company_btn 
 
label find_CP3 :
    $ visited.add("find_CP3")
    $ quick_menu = True
    hide company_map
    hide cr_CP_woman

    show screen text_timer
    call screen search_CP3
    
    ##증거
    if "room_hint1" not in hint : #벽에 큰 게시판
        if _return is "hint1":
            DT idle "회의한 중요한 내용을 여기에 모아둔 것 같아.\n내가 봐도 되는걸까?"
            $ hint.add("room_hint1")
            
    if "room_hint2" not in hint : #책장
        if _return is "hint2" :
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_company_port).pickup(1)
            show item_company_port with dissolve :
            DT idle "커피포트이다."
            $ hint.add("room_hint2")
            hide item_company_port

    if "room_hint3" not in hint : #컴퓨터
        if _return is "hint3" :
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_company_cctv).pickup(1)
            show item_company_cctv with dissolve :
            DT idle "CCTV가 있다. 무언가 찍혔을까?\n시간이 되면 확인해보자."
            $ hint.add("room_hint3")
            hide item_company_cctv
    
    if "room_hint4" not in hint : #책상 위
        if _return is "hint4":
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_company_coffee).pickup(1)
            show item_company_coffee with dissolve :
            DT idle "흔히 볼 수 있는 커피다."
            $ hint.add("room_hint4")
            hide item_company_coffee

    if "room_hint5" not in hint : #오른쪽 커튼
        if _return is "hint5":
            DT idle "(당연히 아무것도 없다.)"
            $ hint.add("room_hint5")


    if "room_hint6" not in hint : #왼쪽 커튼
        if _return is "hint6":
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_company_wire).pickup(1)
            show item_company_wire with dissolve :
            DT idle "전선이 왜 여기에 있지? 범행에 쓰였을지도 모르겠군."
            $ hint.add("room_hint6")
            hide item_company_wire

    if "room_hint7" not in hint : #그냥 바닥
        if _return is "hint7":
            play sound "audio/sound/save.mp3"
            
            $ InvItem(*item_company_electricshocker).pickup(1)
            show item_company_electricshocker with dissolve :
            DT idle "(전기충격기이다.)\n이게 왜 여기에 있지?"
            DT idle "누가 호신용으로 가지고 다닌건가."
            $ hint.add("room_hint7")
            hide item_company_electricshocker
    
    if "room_hint8" not in hint : #전등 스위치
        if _return is "hint8":
            DT idle "불은 끄지 말자."
            $ hint.add("room_hint8")


    jump find_CP3
    return