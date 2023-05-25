import socket

serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind(('localhost', 0))
port = serveur.getsockname()[1]
ip_locale = socket.gethostbyname(socket.gethostname())
serveur.listen(1)

print('Serveur démarré sur', ip_locale + ':' + str(port))

while True:
    connexion, adresse = serveur.accept()
    print('Connexion entrante de', adresse)

    donnees_ent = connexion.recv(1024)
    if donnees_ent:
        print('Données entrantes :', donnees_ent)

        if donnees_ent.startswith(b'PING'):
            reponse = b'PONG'
            connexion.sendall(reponse)
            print('Ping entrant détecté et répondu')
        else:
            reponse = b'HTTP/1.1 200 OK\n\nHello, World!'
            connexion.sendall(reponse)
            print('Requête HTTP entrante détectée et réponse envoyée')

    connexion.close()
