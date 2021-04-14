import pytube

url = input("Link: ")

try:
    youtube = pytube.YouTube(url)
    print(youtube)
    print(f"O download do video '{youtube.title}', está iniciando")
    video = youtube.streams.first().get_highest_resolution()
    video.download()
    print("O Video foi gravado com sucesso!")

except:
    print("O video não foi baixado, verifique sua conexão ou URL e tente novamente.")