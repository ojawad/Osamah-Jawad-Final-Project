#name Osamah Jawad
##class Sdev 140
#profname Nick LaPlante
##date December 18 2022
#PIZZA GUI APP
#using PIL for the pictures

from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image


#creating tkinter window
def print_selected_items():

    for i in Pizza_List.curselection():
        print(Pizza_List.get(i))
    print(drinks.get())
Pizza = Tk()

def call_back_add_pizza():
    print("*********Def add Pizza")
    print_selected_items()

Pizza.geometry("700x600")
Pizza.title("MY Pizza App")
# Create the textboxes
# the purpose here is to add the customers info to the system
name_Label = Label(Pizza, text="Type your name? ")
name_Label.grid(row=0, column=0)

name_entry = Entry(Pizza, width=25)
name_entry.grid(row=0, column=1)
# the purpose for this box to adding the custome address
address_Label = Label(Pizza, text="Type your address? ")
address_Label.grid(row=1, column=0)

address_entry = Entry(Pizza, width=25)
address_entry.grid(row=1, column=1)
# the purpose for this box to adding the custome phone number
phone_Label = Label(Pizza, text="Enter your phone number? ")
phone_Label.grid(row=2, column=0)

phone_entry = Entry(Pizza, width=25)
phone_entry.grid(row=2, column=1)

#Our Pizza list
# the purpose for this box to let the customers pick the topping of thr pizza
my_Pizza_List = ["Cheese", "Veggie", "Pepperoni", "Mushroom", "Chicken", "Beef", "Olive", "Steak"]



Pizza_List = Listbox(Pizza, selectmode=MULTIPLE, bg="white", fg="black")
Pizza_List.grid(row=4, column=1)

for item in my_Pizza_List:
    Pizza_List.insert(0, item)
#Create button
# the purpose for this buttom to adding the pizza to the order list
add_button = Button(Pizza, text="Add pizza",command = call_back_add_pizza)
add_button.grid(row=5,column=0)

# the purpose for this buttom to shows the the customers info
def check():
    text1 = name_entry.get()
    new_lbl = Label(Pizza, text="Name: " + text1)
    new_lbl.grid(row=5,column=2)

    text2 = address_entry.get()
    new_lbl2 = Label(Pizza, text="Address" + text2)
    new_lbl2.grid(row=6,column=2)

    text3 = phone_entry.get()
    new_lbl3 = Label(Pizza, text="Phone Number" + text3)
    new_lbl3.grid(row=7,column=2)
    

    
Pizza_Options = StringVar()
Pizza_Options.set("Choose a Pizza")

#the drink mune (coca,Fanta,Root Beer,Sprite,Lemaonade)    
# the purpose for this buttom to shows the the customers all the drinks option that i offer to them
menu = OptionMenu(Pizza, Pizza_Options, "coca", "Fanta", "Root Beer", "Sprite", "Lemaonade",)

drinks = StringVar()
drinks.set("Choose a drink")


# the drinks list    
drink = OptionMenu(Pizza, drinks, "coca", "Fanta", "Root Beer", "Sprite", "Lemaonade",)
    
##this buttom will appear all the customers information such as name, email, phone number
check_button = Button(Pizza, text="Checkout", command=check)
check_button.grid(row=6,column=0)
#this bottom allow the customers to delete the pizza if want to change the topping
def deleteme():
    Pizza_List.delete(0,7)

del_button = Button(Pizza, text="Delete Pizza", command=deleteme)
del_button.grid(row=7,column=0)
#this bottom allow the customers to pick the type of the drink
drinks = StringVar()
drinks.set("Choose a drink")

drink = OptionMenu(Pizza, drinks, "coca", "Fanta", "Root Beer", "Sprite", "Lemaonade",) # add a command here to print the value to the screen
drink.grid(row=8,column=0)
#here adding picture number1 using PIL
img = Image.open("pizza.png.jpg")
img = img.resize((180, 180))
pizza_pic = ImageTk.PhotoImage(img)
label = Label(Pizza, image=pizza_pic)
label.image = pizza_pic

label.place(x=450, y=20)
##here adding picture number2 using PIL
img = Image.open("Pizza23.png")
img = img.resize((180, 180))
pizza_pic = ImageTk.PhotoImage(img)
label = Label(Pizza, image=pizza_pic)
label.image = pizza_pic

label.place(x=450, y=400)

#exit buttom
# the purpose of the buttom to let the customers exit the app if the y done with the order
def exitout():
    answer = messagebox.askyesno("Exit", "Are you sure, you want to exit?")
    if answer == 1:
        Pizza.destroy()
    else:
        return

exit_button = Button(Pizza, text="Exit out", command=exitout)
exit_button.grid(row=1, column=7)



Pizza.mainloop()
