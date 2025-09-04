#Using multiple return statements in a function 
'''
def format_name(f_name,l_name):
    return "Nothing to do further"  # Function ends here. No further execution takes place

    if f_name=="" or l_name=="":
        a=f_name.title()
        b=l_name.title()
        return f"Result: {a} {b}"
    
print(format_name)
print(format_name(input("Your name pls:"), input("Your last name pls:")))
'''

def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    if year%4==0:
        return True
    else:
        return False
        
print(is_leap_year(2400))
print(is_leap_year(1989))
