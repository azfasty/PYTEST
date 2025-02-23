import webbrowser
import time

# Liste des URLs à ouvrir
urls = [
    "https://cdn.discordapp.com/attachments/1339570046338596966/1343259645585784903/IMG_1568.png?ex=67bc9f88&is=67bb4e08&hm=0948002f851ce1ebb74dfa8eda85d867700ce8f4be9b6c9d29ae48fc8ccb9b2f&",
    "https://cdn.discordapp.com/attachments/1341471594761027659/1343338805603598458/IMG_1961.png?ex=67bce941&is=67bb97c1&hm=658528c1fc0b713d4c5fd699ba23fd57876647d0af42d18a7281a0b27123753d&"
]

# Ouvrir chaque URL dans un nouvel onglet
for url in urls:
    webbrowser.open(url)  # Ouvre l'URL dans le navigateur par défaut
    time.sleep(0.5)  # Attendre un peu entre chaque ouverture
