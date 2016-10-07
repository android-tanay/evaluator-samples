---
# Evaluator Samples

Interactive code evaluator application used to teach an introductory programming course to first year college students.

Consists of samples/examples to help the teaching assistants write tests which check for the correctness of the student's code and ensure they fulfill the lesson objectives. The purpose of the application is to check that submitted code actually meets criteria and lesson objectives.

---
# File structure

Code in `submission/template.py` is the initial structure shown to students, which is being overwritten with stutend's code depending on the lesson. Entire package is sent to code evaluator, which runs `make tests`. This generates an xml file with unit test report, which in turn is then sent back to the application for parsing and display.

`prog_question_test/tests` consists of tests used to detect whether specific criteria for different lesson is met.

---
