from pytube import YouTube


print("--------------------------------- |descargador de videos de youtube en calidad 720p| -----------------------------------\n\n\ningresa la url del video que quieres descargar: \n")
yt = input()
xd = "http" in yt

if xd == True:
    print("descargando video...\n\n")
    yt = YouTube(yt)
    stream = yt.streams.get_by_itag(22)
    stream.download()
    print("\ndescarga completa\n\n")

else:
    print("vuelva a ejecutar el programa eh ingrese la url\n]n")

print("recuerde que este es un programa amateur y tiene fallas\n")
