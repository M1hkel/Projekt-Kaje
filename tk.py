import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Make sure to install the Pillow library for working with images
import webbrowser
class myGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure(bg="deepskyblue4")
        self.root.title("Spotify esitusnimekirja generaator")
        img = tk.PhotoImage(file="spotify.png")
        self.root.iconphoto(False, img)

        row0 = tk.Frame(self.root, bg='deepskyblue4')
        row0.pack(side='top', fill='y')

        row1 = tk.Frame(self.root, bg='deepskyblue4')
        row1.pack(side='top', fill='y', anchor='nw')

        row2 = tk.Frame(self.root, bg='deepskyblue4')
        row2.pack(side='top', fill='y', anchor='nw')

        row3 = tk.Frame(self.root, bg='deepskyblue4')
        row3.pack(side='top', fill='y', anchor='nw')

        row4 = tk.Frame(self.root, bg='deepskyblue4')
        row4.pack(side='top', fill='y')

        row5 = tk.Frame(self.root, bg='deepskyblue4')
        row5.pack(side='top', fill='y')

        self.label= tk.Label(row0, text = "Parimad uued ja vanad hitid!", font = ("Arial", 16), bg="deepskyblue4", fg="white" )
        self.label.pack(padx = 10, pady = 10)

        self.label1= tk.Label(row1, text = "Palun sisesta oma USER_NAME:", font = ("Arial", 14), bg="deepskyblue4", fg="white")
        self.label1.pack(side="left", padx = 10, pady = 10)

        self.textbox1 = tk.Text(row1, height = 1, width = 30, font = ("Arial", 14))
        self.textbox1.pack(side="left", padx= 10, pady= 10)

        self.label2= tk.Label(row2, text = "Palun sisesta oma CLIENT_ID:", bg="deepskyblue4", fg="white", font = ("Arial", 14))
        self.label2.pack(side="left", padx = 10, pady = 10)

        self.textbox2 = tk.Text(row2, height = 1, width = 30, font = ("Arial", 14))
        self.textbox2.pack(side="left", padx= 10, pady= 10)

        self.label3= tk.Label(row3, text = "Palun sisesta oma CLIENT_SECRET:", bg="deepskyblue4", fg="white", font = ("Arial", 14))
        self.label3.pack(side="left", padx = 10, pady = 10)

        self.textbox3 = tk.Text(row3, height = 1, width = 30, font = ("Arial", 14))
        self.textbox3.pack(side="left", padx= 10, pady= 10)
       
        link_button_frame = tk.Frame(row4, bg="deepskyblue4")
        link_button_frame.pack(side='left', padx=10, pady=10)

        self.label4= tk.Label(link_button_frame, text = "Kas sa ei tea kust neid leida?", bg="deepskyblue4", fg="white", font = ("Arial", 14))
        self.label4.pack(side="left", padx = 10, pady = 10)

        self.button = tk.Button(row5, text = "Genereeri", font = ("Arial", 14), command = self.show_message)#ei kutsu funktsiooni vaid lihtsalt anname selle parameetri kui vajutame nuppu.
        self.button.pack(padx=10,pady=10)

        self.button1 = tk.Button(link_button_frame, text="Klikka siia!", font = ("Arial", 14), command=self.show_popup)
        self.button1.pack(padx=10, pady=10)

        self.link_button = tk.Button(link_button_frame, text="Link", font = ("Arial", 14), command=self.open_link)
        self.link_button.pack(side="left", padx=10, pady=10)

        self.link = "https://developer.spotify.com/"

        self.root.mainloop()

    def open_link(self):
        # Open the link in the default web browser
        webbrowser.open(self.link)

    def show_message(self):
         messagebox.showinfo(title = "Sõnum", message = "Su muusika ootab sind, mine otsi Spotify'st playlist nimega uus soovitus.")

    def show_popup(self):
        popup = tk.Toplevel(self.root)
        popup.title("Juhis")

        # Load your image (replace 'your_image.png' with the path to your image file)
        image = Image.open('juhis.png')
        photo = ImageTk.PhotoImage(image)

        # Display the image on the popup
        label = tk.Label(popup, image=photo)
        label.photo = photo  # To prevent image from being garbage collected
        label.pack(padx=10, pady=10)
myGui()

#Vaja kohta kuhu laul sisse kirjutada. Reference jaoks. Kui palju laule soovid ja väljundiks link selle
#CLIENT_ID = "61bd66e0447e4f2a9f867830a28f12fc"
#CLIENT_SECRET = "5b83f369f8624db79850410d9d845328"
#USER_NAME = "Markus Nurmik"
#REDIRECT_URI = "http://localhost:3000"

