# define the list of questions and answers using tuples
questions = [
    ("What colors is the flag of the United Nations?", 
     ("Blue and Red", "Purple and Blue", "Blue and White", "Green and Blue"), 
     3),
    ("What is the capital of Canada?", 
     ("Ottawa", "Toronto", "Vancouver", "Montreal"), 
     1),
    ("What country uses the Yen (¥) currency?",
     ("China", "Japan", "Vietnam", "Russia"),
     2),
    ("What is the name of the tallest mountain in the world?",
     ("Mount Cook, New Zealand", "Mount Fuji, Japan", "Mount Everest, China", "Mount Kanchenjunga, India"),
     3),
    ("Which country has the largest population in the world?",
     ("Russia", "China", "India", "United States of America"),
     2),
    ("What city in the USA is the Golden Gate Bridge located in?",
     ("Orlando, Florida", "San Francisco, California", "Dallas, Texas", "Los Angeles, California"),
     2),
    ("What is the largest country in the world?",
     ("China", "United States of America", "Canada", "Russia"),
     4),
    ("Where is the Eiffel Tower located?",
     ("Italy", "Paris", "Finland", "Switzerland"),
     2),
    ("What is the largest ocean in the world?",
     ("Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean"),
     2),
    ("Mount Fuji is the highest point located in which Asian country?",
     ("China", "Japan", "South Korea", "Thailand"),
     2),
    ("What is the highest mountain in New Zealand?",
     ("Mount Ruapehu, Waikato", "‘Aoraki’ Mount Cook, Canterbury", "Mount Taranaki, Taranaki", "‘Tititea’ Mount Aspiring, Otago"),
     2),
    ("In which country is the Leaning Tower of Pisa located?",
     ("France", "Italy", "Greece", "Finland"),
     2),
    ("“The Lord of The Rings” film was produced in what country?",
     ("New Zealand", "USA", "Australia", "Canada"),
     1),
    ("Peking Duck is the national dish of what country?",
     ("Russia", "China", "Italy", "Japan"),
     2),
    ("What season does Australia experience in December?",
     ("Summer", "Winter", "Autumn", "Spring"),
     1)
]

def play_game():
    score = 0
    for question, options, correct_answer in questions:
        user_answer = ask_question(question, options)
        if user_answer == correct_answer:
            score += 1

    percentage_score = (score / len(questions)) * 100 # calculate % score

    print(f"\nYour score: {score}/{len(questions)}") # print the final score
    print(f"Percentage score: {percentage_score}%")

def ask_question(question, options):
    print(question)  # prints the question and answer options
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    
    # get user's answer
    while True:
        try:
            answer = int(input("Enter your answer (1-4): "))
            if 1 <= answer <= 4:
                return answer
            else:
                print("Please enter a valid answer (1-4).")
        except ValueError:
            print("Please enter a valid answer (1-4).")

# satart the game
play_game()

# ask if the user wants to play again
while True:
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        play_game()
    elif play_again.lower() == "no":
        print("Thanks for playing!")
        break
    else:
        print("Please enter either yes or no.")
