import sys

score = int(sys.stdin.readline())
grade = "A"

if score < 90:
    grade = "B"
if score < 80:
    grade = "C"
if score < 70:
    grade = "D"
if score < 60:
    grade = "F"

print(grade)