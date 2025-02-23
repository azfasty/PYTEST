import webbrowser
import time

# Liste des URLs à ouvrir
urls = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.github.com",
    "https://www.wikipedia.org",
    "https://www.reddit.com"
]

# Ouvrir chaque URL dans un nouvel onglet
for url in urls:
    webbrowser.open(url)  # Ouvre l'URL dans le navigateur par défaut
    time.sleep(0.5)  # Attendre un peu entre chaque ouverture
