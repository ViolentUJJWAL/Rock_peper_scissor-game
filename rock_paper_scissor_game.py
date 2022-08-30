import random,time

def speak(str):
      from win32com.client import Dispatch
      speak=Dispatch('SAPI.SpVoice')
      speak.Speak(str)

while True:
    s=int(input('''
1.Start GAME
2.EXIT
:-'''))
    if s==1:
        print("START GAME")
        us=0
        cs=0
        x=int(input('Number of Round: '))
        while x>0:
            print(f'            Round {x}')
            l=["rock","paper","scissor"]
            c=random.choice(l)
            fu={1:"rock",2:"paper",3:"scissor"}
            ul=["            1. for ROCK","            2. for PAPER","            3. for SCISSOR"]
            for ula in range(0,len(ul)):
                print(ul[ula])
                time.sleep(0.5)
            speak('Rock paper scissor')
            uc=int(input('''            you choose :-'''))
            if 0<uc<4:
                x = x-1
                u = fu[uc]
                time.sleep(0.5)
                print("computer choice :",c)
                time.sleep(0.5)
                print("you choice :",u)
                if u==c:
                    us=us+1
                    cs=cs+1
                    if u=="rock":
                        print('Rock Boxing')
                        speak('Rock Boxing')
                    elif u=="paper":
                        print('Paper Smackdown')
                        speak('Paper Smackdown')
                    elif u=="scissor":
                        print('Scissor Fight')
                        speak('Scissor Fight')
                    time.sleep(0.5)
                    print("both are same")
                elif (c=="rock" and u=="paper") or (c=="paper" and u=="scissor") or (c=="scissor" and u=="rock"):
                    if c=="rock" and u=="paper":
                        print("Paper Covers Rock")
                        speak("Paper Covers Rock")
                    elif c=="paper" and u=="scissor":
                        print("Scissor Cuts paper")
                        speak("Scissor Cuts paper")
                    elif c=="scissor" and u=="rock":
                        print('Rock Breaks Scissor')
                        speak('Rock Breaks Scissor')
                    us=us+1
                    time.sleep(0.5)
                    print("YOU WIN")
                    speak('you win')
                else:
                    if u=="rock" and c=="paper":
                        print("Paper Covers Rock")
                        speak("Paper Covers Rock")
                    elif u=="paper" and c=="scissor":
                        print("Scissor Cuts paper")
                        speak("Scissor Cuts paper")
                    elif u=="scissor" and c=="rock":
                        print('Rock Breaks Scissor')
                        speak('Rock Breaks Scissor')
                    cs=cs+1
                    time.sleep(0.5)
                    print("YOU LOSE")
                    speak("YOU LOSE")
            else:
                print("Wrong choice")
                speak('Wrong choice')
        print(f"\nSCORE")
        speak('score')
        time.sleep(0.5)
        print("computer score-", cs)
        speak(f'Computer score {cs}')
        time.sleep(0.5)
        print("your score-", us)
        speak(f'Your score {us}')
        time.sleep(0.5)
        if cs==us:
            print("          GAME DRAW")
            speak('GAME DRAW')
        elif cs > us :
            print("         Computer WIN ")
            speak("computer WIN")
        else:
            print("           You WIN")
            speak('you win')

    elif s==2:
        yn=int(input('''
        1. YES
        2. NO.
        -'''))
        if yn==1:
            break
        elif yn == 2:
            pass
        else:
            print("enter only 1 or 2")
    else:
        print('''enter 1 or 2
1 for start
2 for exit''')