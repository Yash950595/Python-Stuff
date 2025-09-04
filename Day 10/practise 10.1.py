#Method 1:
'''
def format_name(f_name,l_name,):
    return f_name,l_name.title()
    

print(format_name("YaSh","PaTiL"))
'''

#Method 2:
'''
def format_name(f_name,l_name,):
    a=f_name.title()
    b=l_name.title()

    print(f"{a} {b}")

format_name(f_name="YasH", l_name="PatiL")
'''

#Method 3:
def format_name(f_name,l_name,):
    a=f_name.title()
    b=l_name.title()

    return f"{a} {b}"

print(format_name(f_name="YasH", l_name="PatiL"))

