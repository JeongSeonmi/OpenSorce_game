label talk_suspecter1:
    nvl clear
    "\n\n 이곳에서는 용의자에게 질문을 할 수 있습니다"
    "\n'뒤로가기'를 입력하면 돌아갈 수 있습니다"
    nvl clear
    while True:

        $ user_input = ""  
        $ user_input= renpy.input('하고싶은 말이 뭔가요...')

        $ mmm = plz.person('펜션에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 친한 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자의 담당 간호사이다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 피 묻은 칼과 침대 옆 선반에 수면제 가루가 발견되었다.' ,'김민석',user_input)
        
        ch_men1 "[mmm]"

        $ if user_input == "뒤로가기" : renpy.jump(myP)


label talk_suspecter2:
    nvl clear
    "\n\n 이곳에서는 용의자에게 질문을 할 수 있습니다"
    "\n'뒤로가기'를 입력하면 돌아갈 수 있습니다"
    nvl clear
    while True:

        $ user_input = ""  
        $ user_input= renpy.input('하고싶은 말이 뭔가요...')

        $ mmm = plz.person('펜션에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 친한 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자의 담당 간호사이다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 피 묻은 칼과 침대 옆 선반에 수면제 가루가 발견되었다.' ,'김민석',user_input)
        
        ch_men1 "[mmm]"

        $ if user_input == "뒤로가기" : renpy.jump(myP)

label talk_suspecter3:
    nvl clear
    "\n\n 이곳에서는 용의자에게 질문을 할 수 있습니다"
    "\n'뒤로가기'를 입력하면 돌아갈 수 있습니다"
    nvl clear
    while True:

        $ user_input = ""  
        $ user_input= renpy.input('하고싶은 말이 뭔가요...')

        $ mmm = plz.person('펜션에서 살인 사건이 일어났다. 용의자 김민석, 유승환, 최가은, 정선미, 신재혁 중 범인이 있다고 한다. 김민석은 평소 피해자와 친한 사이였으며 사건 추정시간에는 유승환과 함께 급하게 밖으로 나가는 모습이 CCTV에 포착되었다. 최가은은 피해자와 채무 관계가 있다. 정선미는 피해자의 담당 간호사이다. 신재혁은 사건 당시 화장실에 있다고 진술했다. 살해 추정 시간은 새벽 1시이며 침대 밑에서 피 묻은 칼과 침대 옆 선반에 수면제 가루가 발견되었다.' ,'김민석',user_input)
        
        ch_men1 "[mmm]"

        $ if user_input == "뒤로가기" : renpy.jump(myP)
