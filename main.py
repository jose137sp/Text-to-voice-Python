from gtts import gTTS
import pygame

def convert_text_to_speech(text):
    """
    Convierte un texto en voz y reproduce el audio generado.

    Parámetros:
    - text: El texto a convertir en voz.
    """

    try:
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

    except Exception as e:
        print("Ocurrió un error al convertir el texto en voz:", str(e))

def main():
    """
    Función principal que solicita al usuario el texto a convertir en voz.
    """

    try:
        # Pide al usuario que introduzca el texto
        text = input("Introduce el texto que deseas convertir en voz: ")

        convert_text_to_speech(text)

    except KeyboardInterrupt:
        print("La ejecución del programa fue interrumpida.")

if __name__ == '__main__':
    main()
