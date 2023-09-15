from langchain import OpenAI, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferMemory
import keyboard
import os
from elevenlabs import generate, play, set_api_key
import pyaudio
import numpy as np
import time
import wave
import openai
import soundfile as sf
import tempfile
import sounddevice as sd
from dotenv import load_dotenv

load_dotenv()
duration = 5  # Duration in seconds 
fs = 44100
audio = pyaudio.PyAudio()
output_file = "recorded_audio.wav"


set_api_key("b124c046ad5bbca7cb4d8b50469a5ed6")
openai.api_key = "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"
def play_generated_audio(text, voice="Bella", model="eleven_monolingual_v1"):
    audio = generate(text=text, voice=voice, model=model)
    play(audio)

def transcribe_audio(recording, fs):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_audio:
        sf.write(temp_audio.name, recording, fs)
        temp_audio.close()
        with open(temp_audio.name, "rb") as audio_file:
            transcript = openai.Audio.transcribe("whisper-1", audio_file)
        os.remove(temp_audio.name)
    return transcript["text"].strip()

def record_audio(duration, output_file, sample_rate=44100, channels=1, format=pyaudio.paInt16):
    frames = []

    audio = pyaudio.PyAudio()

    def callback(in_data, frame_count, time_info, status):
        frames.append(in_data)
        return (in_data, pyaudio.paContinue)

    stream = audio.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        stream_callback=callback)

    stream.start_stream()


    start_time = time.time()
    while time.time() - start_time < duration:
        time.sleep(0.1)

    stream.stop_stream()
    stream.close()
    audio.terminate()


    audio_array = np.frombuffer(b''.join(frames), dtype=np.int16)

    with wave.open(output_file, 'wb') as wavefile:
        wavefile.setnchannels(channels)
        wavefile.setsampwidth(audio.get_sample_size(format))
        wavefile.setframerate(sample_rate)
        wavefile.writeframes(audio_array)

    return audio_array




def get_res_from_ai(human_input):

    template = """
            your name is doda
            1) Behave like a human counterpart with a language addictions with "em.." "sir...." 
            2) Don't be overly enthusiastic, keep your answers short and to the point not more 2-5 lines, 
            if required sure but not all the time.

        
        {history}

        Me: {human_input}
        Doda:

    """

    prompt = PromptTemplate(
        input_variables = ("history", "human_input"),
        template = template
    )

    chatgpt_chain = LLMChain(
        llm = OpenAI(temperature = 0.2),
        prompt = prompt,
        verbose = True,
        memory = ConversationBufferMemory(k = 2)
    )

    output = str(chatgpt_chain.predict(human_input = human_input))

    return output


while(True):
    print("Press spacebar to start recording.")
    keyboard.wait("space")  # Wait for spacebar to be pressed
    recorded_audio = record_audio(duration, output_file, sample_rate=44100, channels=1, format=pyaudio.paInt16)
    message = transcribe_audio(recorded_audio, fs)
    print(f"You: {message}")
    assistant_message = get_res_from_ai(message)
    play_generated_audio(assistant_message)
    




