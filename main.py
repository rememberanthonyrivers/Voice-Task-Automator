import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
RECORDING_SECONDS = 5

print("Loading Whisper...")

model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8"
)

print("Whisper loaded!")
print("Speak for 5 seconds...")

audio = sd.rec(
    int(RECORDING_SECONDS * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1
)

sd.wait()

write("recording.wav", SAMPLE_RATE, audio)

print("Recording complete!")
print("Transcribing...")

segments, info = model.transcribe(
    "recording.wav"
)

transcription = ""

for segment in segments:
    transcription += segment.text

print()
print("You said:")
print(transcription)


def process_command(command):
    command = command.lower().strip()

    # CREATE FILE
    if "create" in command and "file" in command:
        print("I detected a file creation command!")

        words = command.split()

        if "called" in words:
            called_index = words.index("called")

            if called_index + 1 < len(words):
                filename = words[called_index + 1]

                if not filename.endswith(".txt"):
                    filename += ".txt"

                with open(filename, "w") as file:
                    file.write("Created by Voice Task Automator.")

                print(f"Created file: {filename}")

            else:
                print("I couldn't determine the filename.")

        else:
            print("Please say the filename using 'called'.")

    # CREATE FOLDER
    elif "create" in command and "folder" in command:
        print("I detected a folder creation command!")

        words = command.split()

        if "called" in words:
            called_index = words.index("called")

            if called_index + 1 < len(words):
                folder_name = words[called_index + 1]

                import os

                os.makedirs(folder_name, exist_ok=True)

                print(f"Created folder: {folder_name}")

            else:
                print("I couldn't determine the folder name.")

        else:
            print("Please say the folder name using 'called'.")

    else:
        print("I don't recognize that command yet.")