import json, pyaudio
from vosk import Model, KaldiRecognizer

def listen_en():
    model_en = Model('models/vosk_model_en_usa')
    rec = KaldiRecognizer(model_en, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()


    while True:

        data = stream.read(4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer = json.loads(rec.Result())
            if answer['text']:

                return answer['text']
