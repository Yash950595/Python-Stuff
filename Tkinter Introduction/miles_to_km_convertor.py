from tkinter import *

def miles_to_km():
    miles=float(miles_input.get())
    km=int(miles*1.609)
    km_output.config(text=f"{km}")
    
my_windows=Tk()
my_windows.title("Miles to km Convertor")
my_windows.minsize(width=300,height=300)



miles_input=Entry(width=10)
miles_input.grid(column=1,row=0,padx=10,pady=10)

miles_label=Label(text="miles")
miles_label.grid(column=2,row=0,padx=10,pady=10)

equal_to_label=Label(text="is equal to")
equal_to_label.grid(column=0,row=1,padx=10,pady=10)

km_output=Label(text="0")
km_output.grid(column=1,row=1,padx=10,pady=10)

km_label=Label(text="km")
km_label.grid(column=2,row=1,padx=10,pady=10)

calculate_button=Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)
















my_windows.mainloop()