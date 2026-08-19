import sounddevice as sd
from scipy.io.wavfile import write

SAMPLE_RATE = 16000
RECORDING_SECONDS = 5

print("Get ready...")
print("Speak for 5 seconds!")

audio = sd.rec(
    int(RECORDING_SECONDS * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1
)

sd.wait()

write("recording.wav", SAMPLE_RATE, audio)

print("Recording complete!")
print("Saved as recording.wav")