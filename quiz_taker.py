from string import ascii_lowercase
import random
import pathlib
from config import config
import sys

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib

NUM_QUESTIONS_PER_QUIZ = 5
QUESTIONS_PATH = pathlib.Path(__file__).parent / "questions.toml"

def prepare_questions(path, num_questions):
    topic_info = tomllib.loads(path.read_text())
    topics = {
        topic["label"]: topic["questions"] for topic in topic_info.values()
    }
    topic_label = get_answers(
        question="Which topic you want to take quiz about",
        alternatives=sorted(topics),
    )[0]
    questions= topics[topic_label]
    num_questions = min(num_questions, len(questions))
    return random.sample(questions, k=num_questions)

def get_answers(question, alternatives, num_choices=1, hint=None):
    exit_conditions = [':q', "quit", 'exit']
    print(f"{question}")
    labeled_alternatives = dict(zip(ascii_lowercase,alternatives))
    if hint:
        labeled_alternatives["?"] = "Hint"
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while True:
        plurals = "" if num_choices == 1 else f"s"
        answer = input(f"\nChoice{plurals}? ")
        if answer in exit_conditions:
            sys.exit(0)
        answers = set(answer.replace(",", " ").split())

        if hint and "?" in answers:
            print(f"\nHINT: {hint}")
            continue

        if len(answers) != num_choices:
            plurals = "" if num_choices==1 else f"s , separated by comma"
            print(f"Please answer {num_choices} alternative{plurals}")
            continue

        if any(
            (invalid := answer) not in labeled_alternatives
            for answer in answers
        ):
            print(f"{invalid!r} is not a valid choice. "
                  f"Please use {', '.join(labeled_alternatives)}"
                  )
            continue

        return [labeled_alternatives[answer] for answer in answers]

def ask_question(question):
    correct_answer = question['answer']
    alternatives = question['answer'] + question['alternatives']
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answers = get_answers(question['question'], ordered_alternatives, num_choices=len(correct_answer), hint=question.get('hint'))
    if correct := set(answers) == set(correct_answer):
        print("⭐Correct⭐")
    else:
        is_are = " is" if len(correct_answer) == 1 else "s are"
        print(f"No, The answer{is_are}: " + "\n ".join(correct_answer))

    if "explanation" in question:
        print(f"\nEXPLANATION:\n{question['explanation']}")

    return 1 if correct else 0

def run_quiz():
    questions = prepare_questions(
        QUESTIONS_PATH, num_questions=config['NUM_QUESTIONS_PER_QUIZ']
    )

    num_correct = 0
    for num, question in enumerate(questions, start=1):
        print(f"\nQuestion {num}:")
        num_correct += ask_question(question)

    if config['SHOW_MARKS_IN_OUTPUT']:
        print(f"You got {num_correct}*10 out of {num}*10 marks")
    else:
        print(f"\nYou got {num_correct} correct out of {num} questions")


if __name__ == '__main__':
    run_quiz()