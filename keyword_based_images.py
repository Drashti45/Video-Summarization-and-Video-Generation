from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
from IPython.display import YouTubeVideo
import pyttsx3
from textblob import TextBlob
from summa import keywords
from huggingsound import SpeechRecognitionModel
import librosa
import soundfile as sf
import torch
import subprocess
import os
import random
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, ImageSequenceClip
import glob

from diffusers import StableDiffusionPipeline
import torch


voice_list = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_RaviM", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enIN_HeeraM", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enUS_MarkM", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0" ]

random1 = random.randint(0, 4)

def file_remover():
    if os.path.exists ("static\\audio1.mp4") :
        os.remove ("static\\audio1.mp4")

def converted(summarized_text):
    str = ""
    for i in range(len(summarized_text)):
        for j in summarized_text[i]:
            str+=j
    return str

def vid_id(url):
    video_id = url.split("=")[1]
    return video_id

def enter_url_images(url):
    if os.path.exists ("ytaudio.mp4") :
        os.remove ("ytaudio.mp4")
    if os.path.exists ("ytaudio.wav") :
        os.remove ("ytaudio.wav")
    yt = YouTube(url)
    video_id = url.split("=")[1]
    YouTubeVideo(video_id)
    try: 
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript1 = ""
        for tx in transcript:
            transcript1 += " " + tx['text']
    except:
        yt.streams \
        .filter(only_audio = True, file_extension = 'mp4') \
        .first() \
        .download(filename = 'ytaudio.mp4') 

        subprocess.call(['ffmpeg', '-i', 'ytaudio.mp4','-acodec','pcm_s16le','-ar','16000',
                        'ytaudio.wav'])

        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-english", device = device)
        input_file = 'ytaudio.wav'
        stream = librosa.stream(input_file, block_length=30, frame_length=16000, hop_length=16000)
        for i,speech in enumerate(stream):
            sf.write(f'{i}.wav', speech, 16000)
        audio_path =[]
        for a in range(i+1):
            audio_path.append(f'{a}.wav')
        transcriptions = model.transcribe(audio_path)
        os.remove("ytaudio.wav")
        os.remove("ytaudio.mp4")
        transcript1 = ' '
        for item in transcriptions:
            transcript1 += ''.join(item['transcription'])
        for a in range(i+1):
            os.remove(f"{a}.wav")
           
    summarizer = pipeline('summarization')
    if len(transcript1)<=300:
        summarized_text = summarizer(transcript1, max_length = 100, min_length =  30)
    else:
        num_iters = int(len(transcript1)/1000)
        summarized_text = []
        for i in range(0, num_iters + 1):
                start = 0
                start = i*1000
                end = (i+1)*1000
                out = summarizer(transcript1[start:end], max_length = 45, min_length =  5)
                out = out[0]
                out = out['summary_text']
                summarized_text.append(out)

    sum_text = converted(summarized_text)
    engine = pyttsx3.init('sapi5')
    engine.setProperty('voice', voice_list[random1])
    engine.save_to_file(sum_text,'static/simple_audio.mp4')
    engine.runAndWait()

    files = glob.glob('src\\input\\generated')
    for f in files:
        os.remove(f)
    
    # model_id = "dreamlike-art/dreamlike-photoreal-2.0"
    # pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    # pipe = pipe.to("cuda")

    # list = sum_text.split(" . ")
    # length = len(list)
    # for i in range(len(list)):
    #     prompt = list[i]
    #     image = pipe(prompt).images[0]
    #     image.save(f"./generated/{i}.jpg")
    # print(length)
    # images = []
    # for i in range(len(list)):
    #     images.append(f"D:\\Final\\src\\input\\generated\\{i}.jpg")

    # clip = ImageSequenceClip(images, fps = 0.25) 
    # clip.write_videofile("src\\output\\generated.mp4", fps = 24)
    # clipa = AudioFileClip("static\\simple_audio.mp4")
    # duration = clipa.duration  
    # clip_duration = clip.duration
    # num_repeats = int(duration / clip_duration) + 1
    # repeated_clip = concatenate_videoclips([clip] * num_repeats)
    # repeated_clip.duration = duration   
    # clipm = repeated_clip.set_audio(clipa)
    # clipm.write_videofile('D:\\Final\\static\\generated_images.mp4')
    return sum_text

def keywords_images(sum_text):
    keywords1 = keywords.keywords(sum_text, scores=True)
    list_keywords = []
    for i in range(7):
        list_keywords.append(keywords1[i][0])
    return list_keywords
    return keyw[1][0]

def audio_generator_images(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voices[1].id)
        engine.save_to_file(text,'audio.wav')
    engine.runAndWait()

def sentiment_analysis_images(text):
    analysis = TextBlob(text)
    return analysis.polarity

def senti_analysis_images(text):
    analysis = TextBlob(text)
    polarity =  analysis.polarity
    if polarity > 0:
        ans = "Positive"
    elif polarity < 0:
        ans = "Negative"
    else:
        ans = "Neutral"
    return ans

# print(enter_url_images("https://www.youtube.com/watch?v=t5iO4LzVeLU&t=215s"))
# print(keywords_images(sum_text))