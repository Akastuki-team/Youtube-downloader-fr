from pytube import YouTube

#demander le lien à l'utilisateur
link = input("Entrez le lien de la vidéo YouTube que vous souhaitez télécharger:  ")
yt = YouTube(link)

#Showing details
print("Titre: ",yt.title)
print("Number de vues: ",yt.views)
print("Durée de la vidéo: ",yt.length)
print("Classement de la vidéo: ",yt.rating)
#Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

#démarrage du Telechargement
print("Telechargement...")
ys.download()
print("telechargement terminer, regarder dans vos fichier!!")