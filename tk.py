import tkinter as tk
from tkinter import messagebox

class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="black")
        self.root.title("Spotify esitusnimekirja generaator")
        img = tk.PhotoImage(file="spotify.png")
        self.root.iconphoto(False, img)

        row0 = tk.Frame(self.root, bg='black')
        row0.pack(side='top', fill='y')

        row1 = tk.Frame(self.root, bg='black')
        row1.pack(side='top', fill='y', anchor='nw')

        row2 = tk.Frame(self.root, bg='black')
        row2.pack(side='top', fill='y', anchor='nw')

        row3 = tk.Frame(self.root, bg='black')
        row3.pack(side='top', fill='y')

        self.label= tk.Label(row0, text = "Parimad uued ja vanad hitid!", font = ("Arial", 16), bg="black", fg="white" )
        self.label.pack(padx = 10, pady = 10)

        self.label1= tk.Label(row1, text = "Palun sisesta oma lemmiklugu:", font = ("Arial", 14), bg="black", fg="white")
        self.label1.pack(side="left", padx = 10, pady = 10)

        self.textbox1 = tk.Text(row1, height = 1, width = 30, font = ("Arial", 14))
        self.textbox1.pack(side="left", padx= 10, pady= 10)

        self.label2= tk.Label(row2, text = "Soovitud lugude arv playlistis:  ", bg="black", fg="white", font = ("Arial", 14))
        self.label2.pack(side="left", padx = 10, pady = 10)

        self.textbox2 = tk.Text(row2, height = 1, width = 30, font = ("Arial", 14))
        self.textbox2.pack(side="left", padx= 10, pady= 10)
        #checkbuttoni muutuja, mis omandab vastava väärtuse.
        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text  = "Näita uut akent", font = ("Arial", 14), bg="black", fg="white", variable= self.check_state)#omistab vastava väärtuse
        self.check.pack(padx= 10, pady= 10)

        self.button = tk.Button(row3, text = "Genereeri", font = ("Arial", 14), command = self.show_message)#ei kutsu funktsiooni vaid lihtsalt anname selle parameetri kui vajutame nuppu.
        self.button.pack(padx=10,pady=10)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:#0 kui ei ole klikitud
            print(self.textbox1.get("1.0", tk.END))#string 1.0 alguseks kuni lõpuni, kui tahad kogu sisu.
        else:#kui on klikitud
            messagebox.showinfo(title = "Sõnum", message=self.textbox1.get("1.0", tk.END))
myGui()

#Vaja kohta kuhu laul sisse kirjutada. Reference jaoks. Kui palju laule soovid ja väljundiks link selle
"""
#esialgne variant
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
"""

