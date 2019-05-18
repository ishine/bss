import pyaudio
import wave
import numpy as np
from scipy.io import wavfile

CHUNK = 1024
FORMAT = pyaudio.paInt16
<<<<<<< HEAD
CHANNELS = 5
RATE = 44100
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "output.wav"
=======
CHANNELS = 3
RATE = 44100
RECORD_SECONDS = 10
group_number = '5'
WAVE_OUTPUT_FILENAME = "./samples/group{}/output.wav".format(group_number)
>>>>>>> c7880457e08370f2d3e78a6fc889bd032841045f

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
<<<<<<< HEAD
                input_device_index=13,
=======
                input_device_index=14,
>>>>>>> c7880457e08370f2d3e78a6fc889bd032841045f
                frames_per_buffer=CHUNK
                )

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

<<<<<<< HEAD

#Not really sure what b'' means in BYTE STRING but numpy needs it
#just like wave did...
framesAll = b''.join(frames)

#Use numpy to format data and reshape.
#PyAudio output from stream.read() is interlaced.
result = np.fromstring(framesAll, dtype=np.int16)
chunk_length = len(result) // CHANNELS
result = np.reshape(result, (chunk_length, CHANNELS))

#Write multi-channel .wav file with SciPy
wavfile.write(WAVE_OUTPUT_FILENAME,RATE,result)
=======
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
>>>>>>> c7880457e08370f2d3e78a6fc889bd032841045f
