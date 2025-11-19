# translator.py — Universal Text & Voice Translator (Python 3.13 Compatible)

import os
from deep_translator import GoogleTranslator
from gtts import gTTS
import pygame
import speech_recognition as sr


# 🎵 AUDIO PLAYER FUNCTION
def play_audio(filename):
    """Play an MP3 file using pygame"""
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.quit()


# 1️⃣ TEXT TO SPEECH
def text_to_speech():
    text = input("\nEnter text to convert to speech: ")
    lang = input("Enter language code (e.g., en, hi, te, ta, fr, es): ")

    tts = gTTS(text=text, lang=lang)
    filename = "speech.mp3"
    tts.save(filename)
    print("🔊 Playing speech...")
    play_audio(filename)
    os.remove(filename)


# 2️⃣ TEXT TRANSLATION + SPEECH OUTPUT
def text_translate():
    print("\n🌐 TEXT TRANSLATION MODE 🌐")
    source_lang = input("Enter source language code (e.g., en, hi, te, ta, fr, es): ")
    target_lang = input("Enter target language code (e.g., en, hi, te, ta, fr, es): ")
    text = input("Enter text to translate: ")

    translated = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
    print(f"\n✅ Translated Text ({target_lang}): {translated}")

    tts = gTTS(text=translated, lang=target_lang)
    filename = "translated_speech.mp3"
    tts.save(filename)
    print("🔊 Playing translated speech...")
    play_audio(filename)
    os.remove(filename)


# 3️⃣ VOICE TRANSLATION
def voice_translation():
    print("\n🎤 VOICE TRANSLATION MODE 🎤")
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("🎙️ Speak now... (recording will auto-stop when you stop talking)")
        audio = recognizer.listen(source)

    try:
        print("⏳ Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"🗣️ You said: {text}")

        target_lang = input("Enter target language code (e.g., en, hi, te, ta, fr, es): ")
        translated = GoogleTranslator(source='auto', target=target_lang).translate(text)
        print(f"\n✅ Translated Text ({target_lang}): {translated}")

        tts = gTTS(text=translated, lang=target_lang)
        filename = "voice_translation.mp3"
        tts.save(filename)
        print("🔊 Playing translated speech...")
        play_audio(filename)
        os.remove(filename)

    except Exception as e:
        print(f"❌ Error: {e}")


# 4️⃣ SPEECH-TO-TEXT (Stops Automatically on Silence)
def speech_to_text():
    print("\n🎧 SPEECH-TO-TEXT MODE 🎧")
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("🎙️ Speak now... (Recording will stop automatically when you’re silent)")
        audio = recognizer.listen(source, phrase_time_limit=None)

    try:
        print("⏳ Recognizing speech...")
        text = recognizer.recognize_google(audio)
        print(f"📝 Transcribed text: {text}")

        save_choice = input("Save transcript to file? (y/N): ")
        if save_choice.strip().lower() == 'y':
            filename = input("Enter filename (e.g., transcript.txt): ")
            if filename:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"💾 Saved transcript to {filename}")

    except sr.UnknownValueError:
        print("⚠️ Could not understand the audio.")
    except sr.RequestError:
        print("⚠️ Could not reach the speech recognition service.")
    except Exception as e:
        print(f"❌ Error: {e}")


# MAIN MENU
def main():
    while True:
        print("\n========== 🌍 UNIVERSAL TRANSLATOR ==========")
        print("1️⃣  Text to Speech")
        print("2️⃣  Text Translate ")
        print("3️⃣  Voice Translation ")
        print("4️⃣  Speech-to-Text ")
        print("5️⃣  Exit")
        print("===============================================")

        choice = input("Select an option (1-5): ")

        if choice == '1':
            text_to_speech()
        elif choice == '2':
            text_translate()
        elif choice == '3':
            voice_translation()
        elif choice == '4':
            speech_to_text()
        elif choice == '5':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please select again.")


if __name__ == "__main__":
    main()
n