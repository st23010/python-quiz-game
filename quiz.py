# Define the list of questions and answers using tuples
questions = [
    ("What colors is the flag of the United Nations?",
     "Blue and Red",
     "Purple and Blue",
     "Blue and White",
     "Green and Blue",
     3),
    ("What is the capital of Canada?",
     "Ottawa",
     "Toronto",
     "Vancouver",
     "Montreal",
     1),
    ("What country uses the Yen (¥) currency?",
     "China",
     "Japan",
     "Vietnam",
     "Russia",
     2),
    ("What is the name of the tallest mountain in the world?",
     "Mount Cook, New Zealand",
     "Mount Fuji, Japan",
     "Mount Everest, China",
     "Mount Kanchenjunga, India",
     3),
    ("Which country has the largest population in the world?",
     "Russia",
     "China",
     "India",
     "United States of America",
     2),
    ("What city in the USA is the Golden Gate Bridge located in?",
     "Orlando, Florida",
     "San Francisco, California",
     "Dallas, Texas",
     "Los Angeles, California",
     2),
    ("What is the largest country in the world?",
     "China",
     "United States of America",
     "Canada",
     "Russia",
     4),
    ("Where is the Eiffel Tower located?",
     "Italy",
     "Paris",
     "Finland",
     "Switzerland",
     2),
    ("What is the largest ocean in the world?",
     "Indian Ocean",
     "Pacific Ocean",
     "Atlantic Ocean",
     "Arctic Ocean",
     2),
    ("Mount Fuji is the highest point located in which Asian country?",
     "China",
     "Japan",
     "South Korea",
     "Thailand",
     2),
    ("What is the highest mountain in New Zealand?",
     "Mount Ruapehu, Waikato",
     "Aoraki / Mount Cook, Canterbury",
     "Mount Taranaki, Taranaki",
     "Tititea / Mount Aspiring, Otago",
     2),
    ("In which country is the Leaning Tower of Pisa located?",
     "France",
     "Italy",
     "Greece",
     "Finland",
     2),
    ("“The Lord of The Rings” film was produced in what country?",
     "New Zealand",
     "USA",
     "Australia",
     "Canada",
     1),
    ("Peking Duck is the national dish of what country?",
     "Russia",
     "China",
     "Italy",
     "Japan",
     2),
    ("What season does Australia experience in December?",
     "Summer",
     "Winter",
     "Autumn",
     "Spring",
     1)
]

def ask_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    answer = int(input("Enter your answer (1-4): "))  # Prompt user for answer
    return answer

def play_game():
    score = 0  # Initialize score to 0
    for question, option1, option2, option3, option4, correct_answer in questions:
        user_answer = ask_question(question, [option1, option2, option3, option4])  # Ask the question
        if user_answer == correct_answer:  # Check if user's answer matches the correct answer
            score += 1  # Increment the score if answer is correct

    percentage_score = (score / len(questions)) * 100  # Calculate percentage score
    print(f"\nYour score: {score}/{len(questions)}")
    print(f"Percentage score: {percentage_score}%")
