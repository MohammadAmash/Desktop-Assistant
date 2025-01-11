import customtkinter as ctk
import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import wikipedia
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def about():
    hour = int(datetime.datetime.now().hour)
    if hour >= 5 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Mark 1 Desktop Assistant, How may I help you?")

def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open gmail" in c.lower():
        webbrowser.open("https://gmail.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif 'tell me time' in c.lower():
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is: {str_time}")
        output_label.configure(text=f"The time is: {str_time}")
    elif 'wikipedia' in c.lower():
        speak('Searching Wikipedia...')
        search = c.replace("wikipedia", "")
        results = wikipedia.summary(search, sentences=2)
        speak("According to Wikipedia")
        output_label.configure(text=results)
        speak(results)
    elif 'open vs code' in c.lower():
        path = "C:\\Users\\moham\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(path)
    else:
        speak("Sorry, I did not understand that command.")
        output_label.configure(text="Command not recognized.")

def activate_assistant():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            output_label.configure(text="Listening for wake word 'Mark 1'...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)
            word = recognizer.recognize_google(audio)

            if word.lower() == "mark 1":
                speak("Yes")
                output_label.configure(text="Assistant Activated! Listening for command...")
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)
                process_command(command)
            else:
                output_label.configure(text="Wake word not detected.")
    except Exception as e:
        output_label.configure(text=f"Error: {e}")
        ctk.CTkMessagebox.show_error("Error", f"An error occurred: {e}")

# GUI Setup
ctk.set_appearance_mode("System")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

root = ctk.CTk()
root.title("Mark 1 Desktop Assistant")
root.geometry("500x300")

header_label = ctk.CTkLabel(root, text="Mark 1 Desktop Assistant", font=("Helvetica", 16, "bold"))
header_label.pack(pady=10)

activate_button = ctk.CTkButton(root, text="Activate Assistant", font=("Helvetica", 14), command=activate_assistant)
activate_button.pack(pady=20)

output_label = ctk.CTkLabel(root, text="", font=("Helvetica", 12), wraplength=400, justify="center")
output_label.pack(pady=20)

about_button = ctk.CTkButton(root, text="About Assistant", font=("Helvetica", 12), command=about)
about_button.pack(pady=10)

exit_button = ctk.CTkButton(root, text="Exit", font=("Helvetica", 12), command=root.quit)
exit_button.pack(pady=10)

root.mainloop()
