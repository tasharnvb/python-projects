# Trivia Challenge (Edit)
# Trivia game that reads a plain text file

# Pg 216, Challenge No. 2
# Improve the Trivia Challenge so that it maintain a 
# of high-scores in a file.

import sys
import pickle

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)
    
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
        
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
        
    explanation = next_line(the_file)

    value = next_line(the_file)
    try:
        value = int(value)
    except ValueError as e:
        # if category is not empty, then it is not the end of the game yet
        # meaning that the point value has not been set correctly.
        if category:
            print("The point value must be an integer (a whole number)!")
            print("Defaulting point value to 1 for this question")
            value = 1

    return category, question, answers, correct, explanation, value

def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title, "\n")
 
def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0

    # get first block
    category, question, answers, correct, explanation, value = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += value
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, explanation, value = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("You're final score is", score)

    try:
        scores_file = open("scores.dat", "rb")
    except IOError:
        print("Could not find high scores file. Creating new high scores file.")
        # the high_scores file doesn't exist yet so create it
        scores_file = open("scores.dat", "wb")
        default_scores = [(10, "aaa"),
                          (6, "bbb"),
                          (3, "ccc"),
                          (1, "ddd"),
                          (0, "eee")]
        pickle.dump(default_scores, scores_file)
        scores_file.close()
        scores_file = open("scores.dat", "rb")
        
    high_scores = pickle.load(scores_file)
    # code adapted from pg 137
    for entry in high_scores:
        curr_score, curr_name = entry
        if curr_score < score:
            scores_file.close()
            scores_file = open("scores.dat", "wb")
            print("\nNew high-score!")
            name = input("Please enter your name: ")
            new_entry = (score, name)
            high_scores.append(new_entry)
            high_scores.sort(reverse=True)
            high_scores = high_scores[:5]
            pickle.dump(high_scores, scores_file)
            scores_file.close()
            print("High scores updated")
            break

    # display scores
    scores_file = open("scores.dat", "rb")
    print("\n\n\tHigh Scores\n")
    for entry in high_scores:
        curr_score, curr_name = entry
        print("\t", curr_name, "\t\t", curr_score)

    scores_file.close()
            
 
main()  
input("\n\nPress the enter key to exit.")
