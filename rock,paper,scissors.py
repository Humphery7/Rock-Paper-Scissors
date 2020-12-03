import random
print("Welcome to Rock, Paper, Scissors  Game")
nums = ['rock', 'paper','scissors']
print(nums)


def fun():
    #computer chooses and player picks from nums
    computer = random.choice(nums)
    player = input("pick one from nums : ")

    def inside():
        #function to determine winner
        if player == 'rock':
            if computer == 'rock':
                print(computer)
                print("Draw")
                print("do you want to play again")
                ans = input("enter yes or no ")
                if ans == 'yes':
                    fun()
            elif computer == 'paper':
                    print(computer)
                    print("you loose")
                    print("do you want to play again")
                    ans = input("enter yes or no ")
                    if ans == 'yes':
                        fun()
            elif computer == 'scissors':
                    print(computer)
                    print("you win")
                    print("do you want to play again")
                    ans = input("enter yes or no ")
                    if ans == 'yes':
                        fun()

        elif player == 'paper':
            if computer == 'rock':
                print(computer)
                print("you win")
                print("do you want to play again")
                ans = input("enter yes or no ")
                if ans == 'yes':
                    fun()
            elif computer == 'paper':
                    print(computer)
                    print("Draw")
                    print("do you want to play again")
                    ans = input("enter yes or no ")
                    if ans == 'yes':
                        fun()
            elif computer == 'scissors':
                    print(computer)
                    print("you loose")
                    print("do you want to play again")
                    ans = input("enter yes or no ")
                    if ans == 'yes':
                        fun()

        elif player == 'scissors':
            if computer == 'rock':
                print(computer)
                print("you loose")
                print("do you want to play again")
                ans = input("enter yes or no ")
                if ans == 'yes':
                    fun()
            elif computer == 'paper':
                    print(computer)
                    print("you win")
                    print("do you want to play again")
                    ans = input("enter yes or no ")
                    if ans == 'yes':
                        fun()
            elif computer == 'scissors':
                    print(computer)
                    print("draw")
                    print("do you want to play again")
                    ans = input("enter yes or no ")
                    if ans == 'yes':
                        fun()
        else:
            print("wrong input, pick one from nums")
            exit()
    inside()

fun()