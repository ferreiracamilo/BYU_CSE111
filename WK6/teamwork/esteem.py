def calculate_positive_questions(question_list):
    positive_score = 0
    positive_score_dictionary = {
                "D": 0,
                "d": 1,
                "a": 2,
                "A": 3
                }
    
    for question in question_list:
        #thisdict["brand"]
        question_value = positive_score_dictionary[question]
        positive_score += question_value
    
    return positive_score

def calculate_negative_questions(question_list):
    negative_score = 0
    negative_score_dictionary = {
                "D": 3,
                "d": 2,
                "a": 1,
                "A": 0
                }
    
    for question in question_list:
        #thisdict["brand"]
        question_value = negative_score_dictionary[question]
        negative_score += question_value
    
    return negative_score

def self_esteem_result(total_points):
    message = ""
    if total_points < 15:
        message = "A score below 15 may indicate problematic low self-esteem."
    else:
        message = "A score equal or above 15 may indicate there're no apparent self esteem issues."

def main():
    question_list = ["I feel that I am a person of worth, at least on an equal plane with others.", "I feel that I have a number of good qualities.", "All in all, I am inclined to feel that I am a failure.",
                    "I am able to do things as well as most other people.", "I feel I do not have much to be proud of.", "I take a positive attitude toward myself.", "On the whole, I am satisfied with myself.",
                    "I wish I could have more respect for myself.", "I certainly feel useless at times.", "At times I think I am no good at all."]
    i = 1
    positive_replies = []
    negative_replies = []
    peson_score = -1

    print("This program is an implementation of the Rosenberg")
    print("Self-Esteem Scale. This program will show you ten")
    print("statements that you could possibly apply to yourself.")
    print("Please rate how much you agree with each of the")
    print("statements by responding with one of these four letters:\n")

    print("D means you strongly disagree with the statement.")
    print("d means you disagree with the statement.")
    print("a means you agree with the statement.")
    print("A means you strongly agree with the statement.\n")

    for question in question_list:
        print(f"{i}. {question}")
        one_reply = ("Enter D, d, a, or A: ")
        if(i <= 5):
            positive_replies.append(one_reply)
        else:
            negative_replies.append(one_reply)
        i += 1

    total_score = calculate_negative_questions(negative_replies) + calculate_positive_questions(positive_replies)
    print(f"\nYour score is {total_score}.")
    print(f"\n+{self_esteem_result(total_score)}")

# Start this program by
# calling the main function.
if __name__ == "__main__":
    main()