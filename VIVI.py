import speech_recognition as sr
import pyttsx3 as pyt
import webbrowser
import subprocess
import pyautogui
import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

engine = pyt.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def perintah():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Silakan mulai berbicara...")
        recognizer.pause_threshold = 0.9
        while True:
            audio_data = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio_data)
                print("Anda mengatakan:", text)
                
                history_text.insert(tk.END, "Anda mengatakan: " + text + "\n")
                history_text.see(tk.END)

                if "enough" in text.lower():
                    engine.say("Happy to have served you.")
                    engine.runAndWait()
                    return  # Keluar dari fungsi perintah() dan akhiri program
                
                elif "open google" in text.lower() or "google" in text.lower():
                    while True:
                        engine.say("What do you want to search for on Google?")
                        engine.runAndWait()
                        audio_data = recognizer.listen(source)
                        search_query = recognizer.recognize_google(audio_data)
                        print("search on google:", search_query)
                        url = f"https://www.google.com/search?q={search_query}"
                        webbrowser.open(url)
                        while True:
                            engine.say("Do you want to search for something else on Google? Say 'yes' to continue or 'no' to open other else.")
                            engine.runAndWait()
                            audio_data = recognizer.listen(source)
                            user_response = recognizer.recognize_google(audio_data)
                            if "no" in user_response.lower():
                                continue_search = False
                                break
                            elif "yes" in user_response.lower():
                                continue_search = True
                                break
                        if not continue_search:
                            break
                    engine.say("What do you want to do?")
                    engine.runAndWait()
                
                elif "open youtube" in text.lower() or "youtube" in text.lower():
                    while True:
                        engine.say("What do you want to search for on Youtube?")
                        engine.runAndWait()
                        audio_data = recognizer.listen(source)
                        search_query = recognizer.recognize_google(audio_data)
                        print("search on Youtube:", search_query)
                        url = f"https://www.youtube.com/results?search_query={search_query}"
                        webbrowser.open(url)
                        while True:
                            engine.say("Do you want to search for something else on Youtube? Say 'yes' to continue or 'no' to open other else.")
                            engine.runAndWait()
                            audio_data = recognizer.listen(source)
                            user_response = recognizer.recognize_google(audio_data)
                            if "no" in user_response.lower():
                                continue_search = False
                                break
                            elif "yes" in user_response.lower():
                                continue_search = True
                                break
                        if not continue_search:
                            break
                    engine.say("What do you want to do?")
                    engine.runAndWait()
                    
                elif any(keyword in text.lower() for keyword in ["instagram", "github", "stackoverflow", "tiktok", "facebook"]):
                    site = next(keyword for keyword in ["instagram", "github", "stackoverflow", "tiktok", "facebook"] if keyword in text.lower())
                    webbrowser.open(f"https://{site}.com")
                    engine.say(f"Opening {site}.")
                    engine.runAndWait()
                    engine.say("What do you want to do now?")
                    engine.runAndWait()
                
                elif "open notepad" in text.lower():
                    engine.say("Opening Notepad.")
                    engine.runAndWait()
                    buka_notepad()
                    engine.say("What do you want to do now?")
                    engine.runAndWait()
                
                elif "type" in text.lower() or "write" in text.lower():
                    engine.say("What do you want to write in Notepad?")
                    engine.runAndWait()
                    audio_data = recognizer.listen(source)
                    text_to_write = recognizer.recognize_google(audio_data)
                    engine.say("Writing in Notepad.")
                    engine.runAndWait()
                    tulis_di_notepad(text_to_write)
                    engine.say("What do you want to do now?")
                    engine.runAndWait()   
                
                elif "open application" in text.lower():
                    engine.say("What application do you want to open?")
                    engine.runAndWait()
                    audio_data = recognizer.listen(source)
                    aplikasi = recognizer.recognize_google(audio_data)
                    engine.say(f"Opening {aplikasi}.")
                    engine.runAndWait()
                    buka_aplikasi(aplikasi)
                    engine.say("What do you want to do now?")
                    engine.runAndWait()
                    
                else:
                    engine.say("Sorry, I can't do what you told me to do.")
                    engine.runAndWait()
                    engine.say("What do you want to do now?")
                    engine.runAndWait()
                    continue
                
            except sr.UnknownValueError:
                engine.say("Sorry, your voice is not clear, can you repeat your command?")
                engine.runAndWait()
                print("Sorry, your voice is not clear, can you repeat your command?")
            except sr.RequestError as e:
                print("request error; {0}".format(e))
                return "request error"

def buka_notepad():
    try:
        subprocess.Popen(['notepad.exe'])
    except OSError as e:
        print("Failed to open Notepad:", e)

# Fungsi untuk menulis teks di Notepad
def tulis_di_notepad(text):
    # Fokus ke Notepad
    pyautogui.click(x=100, y=100)  # Ganti koordinat x dan y sesuai dengan posisi Notepad di layar
    time.sleep(1)  # Tunggu 1 detik untuk memastikan Notepad terfokus

    # Ketik teks
    pyautogui.write(text)

def buka_aplikasi(aplikasi):
    try:
        subprocess.Popen([aplikasi])  # Ganti 'aplikasi' dengan jalur atau nama file eksekutif aplikasi yang ingin Anda buka
    except OSError as e:
        print(f"Gagal membuka aplikasi {aplikasi}: {e}")

def run_vivi():
    engine.say("Hai, I'm VIVI your voice assistant. How can I help you today?")
    engine.runAndWait()
    perintah()
    
def start_vivi():
    # Mulai asisten VIVI
    run_vivi()

# Membuat jendela utama
root = tk.Tk()
root.title("VIVI Assistant")

# Membuat area teks untuk menampilkan riwayat percakapan
history_text = ScrolledText(root, width=50, height=20)
history_text.pack(padx=10, pady=10)

# Membuat tombol untuk memulai asisten VIVI
start_button = tk.Button(root, text="Start VIVI", command=start_vivi)
start_button.pack(pady=5)

# Menjalankan jendela utama
root.mainloop()