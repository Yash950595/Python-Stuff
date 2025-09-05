'''
numbers=[1,2,3]
print(numbers)
new_list=[]
for n in numbers:
    add_1=n+1
    new_list.append(add_1)

print(new_list)
'''


'''
Syntax for list comprehension
new_list=[new_item for item in list] where,

    list --> the one that we ant to iterate through.In above example we used "numbers"
    item --> the temperory variable taken in the loop.In above case we have taken "n"
    new_item --> 
'''
'''
numbers=[1,2,3]
print(numbers)
new_list=[n+1 for n in numbers] #here n+1 is the operation that we perform, n is the temp variable
                                #numbers is the list we iterate through
print(new_list)

double_num=[n*2 for n in range(1,5)]
print(double_num)
'''
import random

### CONDITIONAL LIST COMPREHENSION ###
names=["caroline","eleanor","freddie","alex","albon","hulkenburg"]
new_list=[n.upper() for n in names if len(n)>5] #we faced error here because len function measured
                                                #length of names list rather than each item inside it
print(new_list)

### DICTIONARY COMPREHENSION ###
    # Here we create a new dictionary from an existing list 
scores={student:random.randint(1,100) for student in names}

new_dict={student:score for (student,score) in scores.items() if score>=60 }
print(scores)

'''
What the line does:
It creates a new dictionary called new_dict that includes only students who scored 60 or more.

🔍 Step-by-step explanation:
for (student, score) in scores.items()
→ This loops through each key-value pair in the scores dictionary.
→ Example: First iteration: student = "Alice", score = 85.

if score >= 60
→ This is a condition that filters out students who scored less than 60.

{student: score ...}
→ This creates a new dictionary entry only for students who pass the condition.
'''