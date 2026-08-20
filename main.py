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