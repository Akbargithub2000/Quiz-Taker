# Quiz-Taker

Install the tomli package
//pip install tomli

## How to add a question
/This changes has to made in questions.toml file
First enter the topic and give a label.
Syntax:
[Topic]   //[java]
label = 'Name_of_topic'  //label = 'Java'

Enter the question in toml format
Format:
[[Topic.questions]] //[[java.questions]]
question = "Enter the question"
answer = Enter the answer as a list  //["answers"]
/Answers can be multiple separated by comma.
alternatives = Enter the alternative option as list  //["opt1", "opt2", "opt3"]
hint = "Enter the hint  //optional
explanation = "Enter the explanation" //optional
/Large and multiple explanations can be entered as a docstring inside triple quotes //"""docstring"""

## Running the main file
/Open the command line.
/Go to directory containing the file.
/Run the file as python3 quiz_taker.py or python3 -m quiz_taker

## Configuration Changes
/this changes has to be done in confug.py file
/You can change the maximum number of questions by changing the value for 'NUM_QUESTIONS_PER_QUIZ' variable.
/You can check your marks at last by changing the value of 'SHOW_MARKS_IN_OUTPUT' as True.

## Other Changes
/If you want to use it regularly, you can run the file by using your specified alias
/Go to ~/.bashrc
/Make the changes as alias __varname/words__ = 'python3 quiz_taker.py' and save it in bash(linux).
