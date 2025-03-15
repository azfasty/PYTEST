import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import pygame
import threading
import time


pygame.mixer.init()

def jouer_son():
    pygame.mixer.music.load("son.mp3")
    pygame.mixer.music.set_volume(1.0)  # Volume au maximum
    pygame.mixer.music.play()

def creer_fenetre(duree=1000):
    """Crée une nouvelle fenêtre et réduit progressivement l'intervalle d'apparition."""
    fenetre = tk.Toplevel()
    fenetre.title("Image Infinie")

    image = Image.open("image.jpg").resize((600, 600))
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(fenetre, image=photo)
    label.image = photo
    label.pack()

    
    nouveau_delai = max(100, duree - 100)
    fenetre.after(nouveau_delai, lambda: creer_fenetre(nouveau_delai))

def lancer_images_infinies():
    """Lance les fenêtres infinies après 5 secondes."""
    time.sleep(5)
    creer_fenetre(1000)  

def afficher_image_inverse():
    """Affiche l’image en plein écran avec couleurs inversées après 15 secondes."""
    time.sleep(15)

    root_inverse = tk.Tk()
    root_inverse.attributes("-fullscreen", True)
    root_inverse.configure(bg="black")

    image = Image.open("image.jpg").convert("RGB")
    image = ImageOps.invert(image)  
    image = image.resize((root_inverse.winfo_screenwidth(), root_inverse.winfo_screenheight()))

    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root_inverse, image=photo)
    label.image = photo
    label.pack()

    root_inverse.mainloop()


jouer_son()


threading.Thread(target=lancer_images_infinies, daemon=True).start()


threading.Thread(target=afficher_image_inverse, daemon=True).start()


root = tk.Tk()
root.title("Alex Novia le Staffer")

image = Image.open("image.jpg").resize((600, 600))
photo = ImageTk.PhotoImage(image)

label_image = tk.Label(root, image=photo)
label_image.image = photo
label_image.pack()

root.mainloop()
