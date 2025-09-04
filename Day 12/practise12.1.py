# # '''
# # Local Scope V/s Global Scope
# # '''

# # runs=10000   #### Here the variable has Global Scope and can be retrived from anywhere in the program

# # def Total_runs():
# #     runs=20000 ### Here the variable has local scope and its value remains changed only inside the function
# #                ### It cannot be accessed outside the function else name error is generated
# #     print(runs)


# # Total_runs()
# # print(runs)

# # runs=100
# # if runs > 50:
# #     runs=200
# #     print(runs)

# # print(runs)

# # '''
# # Variable created inside a function has local scope whereas if it is created inside a loop it has 

# # '''


# words_per_page= 0
# pages= int(input("Number of pages in the book: "))
# words_per_page= int(input("Number of words per page: "))
# total_words= words_per_page * pages
# print(total_words)

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])
            
fizz_buzz(15)