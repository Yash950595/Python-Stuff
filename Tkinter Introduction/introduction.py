from tkinter import *
'''We can write it as "from tkinter import *" where * denotes/tells 
 the import function to import all the functions that are possible'''
 
window=Tk()
window.title("Intro")
window.minsize(width=600,height=800)


#Label 
label=Label(text="Hello There",font=("Papyrus",25,"bold"))
label.pack(side="left")

#Button Creation
def button_click():
    write=Box.get()
    label.config(text=write)
    print(write)


button=Button(text="click me",command=button_click)
button.pack()

#Box Creation
Box=Entry(width=200)
Box.pack


'''
so it means we use box as a variable to store the entry attribute and then this box is method is called inside the button click that updates the label text according to user input 


ChatGPT said:
Yes — you're exactly right! Let’s break it down clearly to reinforce your understanding:

✅ Step-by-Step Explanation
1. Box = Entry(...)
You create a Tkinter Entry widget (a text input box) and store it in a variable named Box.


Box = Entry(width=30)
Now, Box represents that text entry field in your program.

2. Box.get()
This is a method call that retrieves the text currently typed into the Entry box.

So inside your function:

write = Box.get()
You're storing the user's input from the Entry widget into the write variable.

3. label.config(text=write)
This line updates the label’s text to whatever the user typed in.

So the full function:

def button_click():
    write = Box.get()
    label.config(text=write)
Means:

When the button is clicked,

Fetch the current text from the Entry box,

And change the label’s text to match it.

🎯 Key Concept:
You're using Box as a reference to the Entry widget, and then .get() is a method of that widget to retrieve the input.

🧠 In Simple Terms:
Box = Entry(...) → create the input field.

Box.get() → get what the user typed.

label.config(...) → change the label based on that input.

Let me know if you'd like to add features like:

Automatically clearing the box after clicking

Using default placeholder text

Adding validation (e.g., only numbers)

Happy to help!
'''



window.mainloop()