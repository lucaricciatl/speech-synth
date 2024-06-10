
from IPython.display import Audio, display
import torch
from TTS.api import TTS
import io 
import soundfile as sf
from scipy.io.wavfile import write

class SpeechSynthesizer:
    def __init__(self):
        self.gpt_cond_len = 3
        self.temperature = 0.8
        self.audio_input = None
        self.stream = False
        self.language = "en"
        self.tts = None
        self.output_wav = "out.wav"
        self.input_wav = "samples\glados.wav"
        self.sample_rate = 22050
        self.emotion = "neutral"

        self.InitModel()

    def InitModel(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        self.tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

    def SetSampleRate(self,sr = 22050):
        self.sample_rate = sr

    def SetConditions(self,conditions):
        self.gpt_cond_len = conditions

    def SetTemperature(self,temperature):
        self.temperature = temperature

    def SetStream(self,stream):
        self.stream = stream

    def SetInputWav(self,audio_input):
        self.input_wav = audio_input

    def SetOutputWaf(self,output_wav):
        self.output_wav = output_wav

    def SetLanguge(self,lan="en"):
        self.language = lan

    def SetEmotion(self,emotion="neutral"):
        self.emotion = emotion

    def synthesize_speech(self, text, streamOverride=False):
        audio_bytes = io.BytesIO()

        self.tts.tts_to_file(text,
                file_path=audio_bytes,
                speaker_wav=self.input_wav,
                language=self.language,
                temperature=self.temperature,
                gpt_cond_len= self.gpt_cond_len,
                emotion= self.emotion
                )
        
        return audio_bytes

    # Example usage
#synthesizer = SpeechSynthesizer()

# Here, you would process the file to generate audio data
# For demonstration, let's assume you just echo the content
#speech_wav = synthesizer.synthesize_speech(
#    "It took me quite a long time to develop a voice and now that I have it I am not going to be silent.",
#    speaker_wav="D:\\Development\\vci\\samples\\glados.wav",
#    gpt_cond_len=3,  # Set the context length for GPT conditioning
#    language="en",  # Set the language to English
#    temperature=0.9,  # Set the temperature for speech generation
#    out="D:\\Development\\vci\\outputs\\out.wav"  # Output file path for the synthesized speech
#)
## You can return the audio data as a response
#with open("D:\\Development\\vci\\outputs\\out.wav", "rb") as audio_file:  # Open the synthesized audio file
#    audio_data = audio_file.read()  # Read the audio data


# Example usage:
#synthesizer = SpeechSynthesizer()
#audio = synthesizer.synthesize_speech("Hello, world!",  streamOverride=True)
