import sounddevice as sd
import numpy as np
THRESHOLD = 20  # Adjust this threshold based on your environment
CLAP_DURATION = 5  # Minimum duration of a clap (in seconds)

def detect_claps(audio_data, sample_rate):
    energy = np.sum(audio_data**2)
    if energy > THRESHOLD:
        print("Clap detected!")
def audio_callback(indata, frames, time, status):
    if status:
        print("Error:", status)
        return
    detect_claps(indata[:, 0], sample_rate)

sample_rate = 44100  # Adjust as needed 44100 def
duration =  86400
with sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate):
    sd.sleep(int(duration * 1000))