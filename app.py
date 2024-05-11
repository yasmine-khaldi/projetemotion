import cv2
from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

# Fonction pour accéder à la caméra et capturer les images en temps réel
def capture_camera():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break
        # Traitez le cadre ici si nécessaire
        # Par exemple, vous pouvez effectuer une détection faciale ou une analyse d'émotion
        # Ensuite, envoyez le cadre à la page HTML pour l'affichage dans le navigateur
        # (Vous devrez peut-être convertir le cadre en un format approprié pour l'affichage dans HTML)

# Route pour servir la page HTML
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # Lancer la capture d'images en parallèle
    camera_thread = Thread(target=capture_camera)
    camera_thread.start()

    # Démarrer l'application Flask
    app.run(debug=True)
