import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Make sure to install the Pillow library for working with images

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
        row3.pack(side='top', fill='y', anchor='nw')

        row4 = tk.Frame(self.root, bg='black')
        row4.pack(side='top', fill='y')

        row5 = tk.Frame(self.root, bg='black')
        row5.pack(side='top', fill='y')

        self.label= tk.Label(row0, text = "Parimad uued ja vanad hitid!", font = ("Arial", 16), bg="black", fg="white" )
        self.label.pack(padx = 10, pady = 10)

        self.label1= tk.Label(row1, text = "Palun sisesta oma USER_NAME", font = ("Arial", 14), bg="black", fg="white")
        self.label1.pack(side="left", padx = 10, pady = 10)

        self.textbox1 = tk.Text(row1, height = 1, width = 30, font = ("Arial", 14))
        self.textbox1.pack(side="left", padx= 10, pady= 10)

        self.label2= tk.Label(row2, text = "Palun sisesta oma CLIENT_ID", bg="black", fg="white", font = ("Arial", 14))
        self.label2.pack(side="left", padx = 10, pady = 10)

        self.textbox2 = tk.Text(row2, height = 1, width = 30, font = ("Arial", 14))
        self.textbox2.pack(side="left", padx= 10, pady= 10)

        self.label3= tk.Label(row3, text = "Palun sisesta oma CLIENT_SECRET", bg="black", fg="white", font = ("Arial", 14))
        self.label3.pack(side="left", padx = 10, pady = 10)

        self.textbox3 = tk.Text(row3, height = 1, width = 30, font = ("Arial", 14))
        self.textbox3.pack(side="left", padx= 10, pady= 10)

        #checkbuttoni muutuja, mis omandab vastava väärtuse.
        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text  = "Näita uut akent", font = ("Arial", 14), bg="black", fg="white", variable= self.check_state)#omistab vastava väärtuse
        self.check.pack(padx= 10, pady= 10)

        self.button = tk.Button(row4, text = "Genereeri", font = ("Arial", 14), command = self.show_message)#ei kutsu funktsiooni vaid lihtsalt anname selle parameetri kui vajutame nuppu.
        self.button.pack(padx=10,pady=10)

        self.button1 = tk.Button(row5, text="Juhised", font = ("Arial", 14), command=self.show_popup)
        self.button1.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:#0 kui ei ole klikitud
            print(self.textbox1.get("1.0", tk.END))#string 1.0 alguseks kuni lõpuni, kui tahad kogu sisu.
        else:#kui on klikitud
            messagebox.showinfo(title = "Sõnum", message=self.textbox1.get("1.0", tk.END))
    def show_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Juhis")

        # Load your image (replace 'your_image.png' with the path to your image file)
        image = Image.open('juhis.png')
        photo = ImageTk.PhotoImage(image)

        # Display the image on the popup
        label = ttk.Label(popup, image=photo)
        label.photo = photo  # To prevent image from being garbage collected
        label.pack(padx=10, pady=10)
myGui()

#Vaja kohta kuhu laul sisse kirjutada. Reference jaoks. Kui palju laule soovid ja väljundiks link selle
#CLIENT_ID = "61bd66e0447e4f2a9f867830a28f12fc"
#CLIENT_SECRET = "5b83f369f8624db79850410d9d845328"
#USER_NAME = "Markus Nurmik"
#REDIRECT_URI = "http://localhost:3000"
"""
def show_popup():
    popup = tk.Toplevel(root)
    popup.title("Image Popup")

    # Load your image (replace 'your_image.png' with the path to your image file)
    image = Image.open('your_image.png')
    photo = ImageTk.PhotoImage(image)

    # Display the image on the popup
    label = ttk.Label(popup, image=photo)
    label.photo = photo  # To prevent image from being garbage collected
    label.pack(padx=10, pady=10)

# Create the main window
root = tk.Tk()
root.title("Tkinter Image Popup")

# Create a button to show the popup
button = ttk.Button(root, text="Show Image Popup", command=show_popup)
button.pack(padx=20, pady=20)

# Run the Tkinter event loop
root.mainloop()

"""
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

