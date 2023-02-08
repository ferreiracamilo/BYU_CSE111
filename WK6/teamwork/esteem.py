def calculate_question_score (reply,question_type):
    question_score = -1
    positive_score_dictionary = {
                "D": 0,
                "d": 1,
                "a": 2,
                "A": 3
                }

    negative_score_dictionary = {
                "D": 3,
                "d": 2,
                "a": 1,
                "A": 0
                }
    
    if question_type == "positive":
        question_score = positive_score_dictionary[reply]
    else:
        question_score = negative_score_dictionary[reply]
    return question_score

def self_esteem_result(total_points):
    message = ""
    if total_points < 15:
        message = "A score below 15 may indicate problematic low self-esteem."
    else:
        message = "A score equal or above 15 may indicate there're no apparent self esteem issues."
    return message

def main():
    question_list = {
                "I feel that I am a person of worth, at least on an equal plane with others": "positive",
                "I feel that I have a number of good qualities.": "positive",
                "All in all, I am inclined to feel that I am a failure.": "negative",
                "I am able to do things as well as most other people.": "positive",
                "I feel I do not have much to be proud of.": "negative",
                "I take a positive attitude toward myself.": "positive",
                "On the whole, I am satisfied with myself.": "positive",
                "I wish I could have more respect for myself.": "negative",
                "I certainly feel useless at times.": "negative",
                "At times I think I am no good at all.": "negative"
                }
    i = 1
    total_score = 0

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
        one_reply = input("Enter D, d, a, or A: ")
        question_type = question_list[question]
        question_score = calculate_question_score(one_reply,question_type)
        total_score += question_score
        i += 1

    print(f"\nYour score is {total_score}.")
    print(f"\n{self_esteem_result(total_score)}")

# Start this program by
# calling the main function.
if __name__ == "__main__":
    main()