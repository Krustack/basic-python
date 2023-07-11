while True :
    name = str(input("please insert your name:"))
    score = int(input("please enter your scores:"))
    if score >=80:
        print(f"{name} score: {score} grade : A")
    elif score >=70 :
        print(f"{name} score: {score} grade : B")
    elif score >=60 :
        print(f"{name} score: {score} grade : C")
    elif score >=50 :
        print(f"{name} score: {score} grade : D")
    else :
        print(f"{name} score: {score} grade : F")
