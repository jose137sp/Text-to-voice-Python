from gtts import gTTS
import pygame

# Pide al usuario que introduzca el texto
text = input("Introduce el texto que deseas convertir en voz: ")

# Crea el objeto gTTS con el texto
tts = gTTS(text)

# Guarda el archivo de audio generado
tts.save("output.mp3")

# Reproduce el archivo de audio
pygame.mixer.init()
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue

