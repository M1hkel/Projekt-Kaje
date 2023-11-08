import tkinter as tk
from tkinter import messagebox
"""
root = tk.Tk()

#määra suurus
root.geometry("700x700")

root.title("Spotify API")

label = tk.Label(root, text= "laulusoovitus", font = ("Arial", 18))
label.pack(padx= 20, pady = 20)

textbox = tk.Text(root, height = 1, font = ("Arial", 16))
textbox.pack(padx = 10, pady = 10)

#button = tk.Button(root, text = "Click me!", font =("Arial", 18))
#button.pack(padx = 10, pady = 10)

#myentry  = tk.Entry(root)
#myentry.pack()
"""
"""
buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight = 1)
buttonframe.columnconfigure(1, weight = 1)
buttonframe.columnconfigure(2, weight = 1)

btn1 = tk.Button(buttonframe, text = 1, font = ("Arial", 18))
btn1.grid(row = 0, column = 0, sticky = tk.W + tk.E)

btn2 = tk.Button(buttonframe, text = 2, font = ("Arial", 18))
btn2.grid(row = 0, column = 1, sticky = tk.W + tk.E)

btn3 = tk.Button(buttonframe, text = 3, font = ("Arial", 18))
btn3.grid(row = 0, column = 2, sticky = tk.W + tk.E)

btn4 = tk.Button(buttonframe, text = 4, font = ("Arial", 18))
btn4.grid(row = 1, column = 0, sticky = tk.W + tk.E)

btn5 = tk.Button(buttonframe, text = 5, font = ("Arial", 18))
btn5.grid(row = 1, column = 1, sticky = tk.W + tk.E)

btn6 = tk.Button(buttonframe, text = 6, font = ("Arial", 18))
btn6.grid(row = 1, column = 2, sticky = tk.W + tk.E)

buttonframe.pack(fill = "x")

anotherbtn = tk.Button(root, text = "TEST")
anotherbtn.place(x = 200, y = 200, height= 100, width = 100)
root.mainloop()
"""
"""
class myGui:
    def __init__(self):
        self.root = tk.Tk()

        self.label= tk.Label(self.root, text = "Write here", font = ("Arial", 16))
        self.label.pack(padx = 10, pady = 10)

        self.textbox = tk.Text(self.root, height = 1, font = ("Arial", 16))
        self.textbox.pack(padx= 10, pady= 10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text  = "Show messagebox", font = ("Arial", 16), variable= self.check_state)
        self.check.pack(padx= 10, pady= 10)

        self.button = tk.Button(self.root, text = "Show message", font = ("Arial", 16), command = self.show_message)
        self.button.pack(padx=10,pady=10)



        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title = "Message", message=self.textbox.get("1.0", tk.END))
            

myGui()
"""
#Markuse Öpe
"""
root = tk.Tk()

root.geometry("500x500")
root.title("Minu esimene GUI")

label = tk.Label(root, text= "Sisesta oma lemmiklugu!", font = ("Arial", 18))
label.pack(padx= 10, pady = 10)

textbox = tk.Text(root, height = 2, font = ("Arial", 16))
textbox.pack(padx = 10, pady = 10)

button = tk.Button(root, text = "Vajuta siia!", font =("Arial", 18))
button.pack(padx = 10, pady = 10)

root.mainloop()
"""
class myGui:
    def __init__(self):
        self.root = tk.Tk()
        #self.root.configure(bg="lightblue")

        self.label= tk.Label(self.root, text = "Parimad uued ja vanad hitid!", font = ("Arial", 16))
        self.label.pack(padx = 10, pady = 10)

        self.label1= tk.Label(self.root, text = "Palun sisesta oma lemmiklugu:", font = ("Arial", 14), anchor="w", justify="left", width=70)
        self.label1.pack(padx = 10, pady = 10)

        self.textbox1 = tk.Text(self.root, height = 1, font = ("Arial", 14))
        self.textbox1.pack(padx= 10, pady= 10)

        self.label2= tk.Label(self.root, text = "Palun sisesta mitu lugu sa oma playlisti soovid:", font = ("Arial", 14), anchor="w", justify="left", width=70)
        self.label2.pack(padx = 10, pady = 10)

        self.textbox2 = tk.Text(self.root, height = 1, font = ("Arial", 14))
        self.textbox2.pack(padx= 10, pady= 10)
        #checkbuttoni muutuja, mis omandab vastava väärtuse.
        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text  = "Näita uut akent", font = ("Arial", 14), variable= self.check_state)#omistab vastava väärtuse
        self.check.pack(padx= 10, pady= 10)

        self.button = tk.Button(self.root, text = "Genereeri", font = ("Arial", 14), command = self.show_message)#ei kutsu funktsiooni vaid lihtsalt anname selle parameetri kui vajutame nuppu.
        self.button.pack(padx=10,pady=10)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:#0 kui ei ole klikitud
            print(self.textbox1.get("1.0", tk.END))#string 1.0 alguseks kuni lõpuni, kui tahad kogu sisu.
        else:#kui on klikitud
            messagebox.showinfo(title = "Sõnum", message=self.textbox1.get("1.0", tk.END))
myGui()

#Vaja kohta kuhu laul sisse kirjutada. Reference jaoks. Kui palju laule soovid ja väljundiks link selle

