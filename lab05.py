# ---------- DO NOT EDIT ------------
import random 
random.seed(256)
# ------------------------------------

def generate_problem(operation: str, difficulty: int) -> int:
    """
    Generates a random math problem (+, -, *, /) based on the given operation and difficulty. The operation is a string that says what operation the problem will be performing.
    The difficulty is from 1-infinity. The more difficult the problem, the bigger the numbers are in the equation.

    Args:
        operation: The type of operation that the problem will generate (addition, subtraction, multiplication, division)
        difficulty: The difficulty for the problem from 1-infinity that determines how big the numbers are.
    
    Returns:
        Prints out a random math problem difficulty
    """
    
    # This will generate a random first and second number for you to use
    first_num = random.randint(1, (10 ** difficulty))
    second_num = random.randint(1, (10 ** difficulty))

    # IF the problem is division, use this code to make the first number the higher one
    first_num = max([first_num, second_num])
    second_num = min([first_num, second_num])

    # eval() returns the solution to your problem.

    if operation == "addition":
        sign = "+"
    elif  operation == "subtraction":
        sign = "-"
    elif operation ==  "multiplication":
        sign = "*" 
    else:
        sign = "/"
    print(f"{first_num} {sign} {second_num}")  # This is the equation that will be aksed to the user.
    answer = int(eval(f"{first_num} {sign} {second_num}"))
    return answer

def get_operation():
"""This function prompts the user to pick an operation until they enter a valid one"
then returns the operation as a string""" 
    print("Would you like to practice addition, subtraction, multiplication, or division?")
    operation = input().strip()
     
    while operation != "addition" and operation != "subtraction" and operation != "multiplication" and operation != "division":
        print("Please select either addition, subtraction, multiplication, or division")
        operation = input().strip() # This code above prompts the user to enter an operation and repeats until they do so.
    return operation
def get_num_problems(operation):
""" This function asks the user to input how many problems they want of the"
operation they chose and repeats until the user chooses a number greater than 0"
then the function returns the number of problems as an integer."""
    print(f"How many types of {operation} problems would you like to solve?")
    num_problems = int(input())

    while num_problems <= 0:               # This code asks the user to enter a number and will continue to until they enter a number greater than 0.
        print("Enter a number greater than 0.")
        num_problems = int(input())
    return num_problems

    #TODO: Print the operation and return the solution.

    

# ---------START CODING HERE----------

print("Welcome to Math Quest! Here you will be challenged by answering increasingly difficult math problems until you decide you have had enough.")
print('You will be presented with n number math problems at a time. If you get more than half right, we will increase the difficulty. Otherwise, we will lower the difficulty, if possible.')
difficulty = 1
final_score = 0
questions = 0
play = True
while play:          # While the user wants to play this code below will continue to run.

    
    operation = get_operation()
    num_problems = get_num_problems(operation)
    print(f"Here are your {num_problems} {operation} problems:")
    score = 0
    for i in range (num_problems):            # This code will walk through each question one by one and track which ones the users got right and wrong.
        answer = generate_problem(operation, difficulty)
        user_answer = int(input())
        if user_answer == answer:
            print("Correct! Next problem...")    #The code will tell them when they got the question right and add one to their score.
            score = score + 1
            questions = questions + 1
        else:
            print("(loud incorrect noise) Wrong! Next problem...") # The code will alert the user when wrong as well.
            questions = questions + 1
   
    if score > num_problems / 2: # This code is checking if the user got more than 50% of the questions right and will increase difficulty if so.
            print(f"Your score was {score}/{num_problems}. We will be increasing the difficulty for next time!")
            difficulty = difficulty + 1
    else: 
        if difficulty > 1: # If the user has already increased their difficulty and scores less than 50% the code will lower the difficulty.
            print(f"Your score was {score}/{num_problems}. We will be lowering the difficulty for next time.")
            difficulty = difficulty - 1
        else:
            print("You are already at the lowest difficulty!") # If user was already at the lowest difficulty it will remain the same.

    print("Continue? (enter 'quit' to exit)") # Allows the user to exit the game if they wish.
    choice = input().strip()

    if choice == "quit":
        play = False


print(f"Congrats! Your final score was {score} out of {questions}.") # Tells user their final score.







