def win_condition():
        blue_ball=0
        red_ball=0
        blue_var=0
        red_var=0
        Silos_State=[['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'x', ''], ['o', '', '']]
        for i in Silos_State:
            if i == ['o','o','o'] or i == ['o','x','o'] or i == ['x','o','o']:
                blue_var+=1
            elif i == ['x','x','x'] or i == ['x','o','x'] or i == ['o','x','x']:
                red_var+=1
            else:
                for i, ball in enumerate(Silos_State):
                    if ball == 'x':
                        red_ball+=1
                    elif ball == 'o':
                        blue_ball+=1

        if blue_var>=3:
            print("Blue Team won the match")
        elif red_var>=3:
            print("Red team won the match")
        else:
            print("No team won the match")
            print("Red Team Point : ",red_ball)
            print("Blue Team Point : ",blue_ball)
            print()
win_condition()