import random
def user_input():
    n=int(input("Enter the number of times you want to play the game:"))
    user_mark=0
    computer_mark=0
    choicelist=["stone","paper","scissors"]
    while(n>0):
        U=input("User(stone/paper/scissors):")
        C=random.choice(choicelist)
        print("Computer(stone/paper/scissors):",C)
        if(U=="stone" and C=="stone"):
            print("Tie..!No points")
        elif(U=="stone" and C=="paper"):
            computer_mark=computer_mark+1
        elif(U=="stone" and C=="scissors"):
            user_mark=user_mark+1
        elif(U=="paper" and C=="stone"):
            user_mark=user_mark+1
        elif(U=="paper" and C=="paper"):
            print("Tie..!No points")
        elif(U=="paper" and C=="scissors"):
            computer_mark=computer_mark+1
        elif(U=="scissors" and C=="stone"):
            computer_mark=computer_mark+1
        elif(U=="scissors" and C=="paper"):
            user_mark=user_mark+1
        elif(U=="scissors" and C=="scissors"):
            print("Tie..!No points")
        else:
            print("Invalid user input,please check..!")
        n=n-1

    print("Score of the user: ",user_mark)
    print("Score of the computer:",computer_mark)
    def compare_result():
        if(user_mark==computer_mark):
            print("Tie..!Both have equal score")
        elif(user_mark>computer_mark):
            print("User is the WINNER....!")
        elif(user_mark<computer_mark):
            print("Computer is the WINNER.....!")
        else:
            print("Something went wrong...!")
    compare_result()
user_input()


            
            
            
        
    

     
