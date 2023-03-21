from moviepy.editor import ImageSequenceClip, AudioFileClip, VideoFileClip, concatenate_videoclips
import random


def images_to_video():
    forest = ["D:\\Final\\src\\input\\Images\\forest\\1.jpg", "D:\\Final\\src\\input\\Images\\forest\\2.jpg","D:\\Final\\src\\input\\Images\\forest\\3.jpg","D:\\Final\\src\\input\\Images\\forest\\4.jpg","D:\\Final\\src\\input\\Images\\forest\\5.jpg","D:\\Final\\src\\input\\Images\\forest\\6.jpg","D:\\Final\\src\\input\\Images\\forest\\7.jpg","D:\\Final\\src\\input\\Images\\forest\\8.jpg","D:\\Final\\src\\input\\Images\\forest\\9.jpg","D:\\Final\\src\\input\\Images\\forest\\10.jpg","D:\\Final\\src\\input\\Images\\forest\\11.jpg","D:\\Final\\src\\input\\Images\\forest\\12.jpg","D:\\Final\\src\\input\\Images\\forest\\13.jpg","D:\\Final\\src\\input\\Images\\forest\\14.jpg","D:\\Final\\src\\input\\Images\\forest\\15.jpg","D:\\Final\\src\\input\\Images\\forest\\16.jpg","D:\\Final\\src\\input\\Images\\forest\\17.jpg","D:\\Final\\src\\input\\Images\\forest\\18.jpg","D:\\Final\\src\\input\\Images\\forest\\19.jpg","D:\\Final\\src\\input\\Images\\forest\\20.jpg","D:\\Final\\src\\input\\Images\\forest\\21.jpg","D:\\Final\\src\\input\\Images\\forest\\22.jpg","D:\\Final\\src\\input\\Images\\forest\\23.jpg","D:\\Final\\src\\input\\Images\\forest\\24.jpg","D:\\Final\\src\\input\\Images\\forest\\25.jpg","D:\\Final\\src\\input\\Images\\forest\\27.jpg","D:\\Final\\src\\input\\Images\\forest\\28.jpg","D:\\Final\\src\\input\\Images\\forest\\29.jpg","D:\\Final\\src\\input\\Images\\forest\\30.jpg","D:\\Final\\src\\input\\Images\\forest\\31.jpg","D:\\Final\\src\\input\\Images\\forest\\32.jpg","D:\\Final\\src\\input\\Images\\forest\\33.jpg","D:\\Final\\src\\input\\Images\\forest\\34.jpg","D:\\Final\\src\\input\\Images\\forest\\35.jpg","D:\\Final\\src\\input\\Images\\forest\\36.jpg","D:\\Final\\src\\input\\Images\\forest\\37.jpg","D:\\Final\\src\\input\\Images\\forest\\38.jpg","D:\\Final\\src\\input\\Images\\forest\\39.jpg","D:\\Final\\src\\input\\Images\\forest\\40.jpg","D:\\Final\\src\\input\\Images\\forest\\41.jpg","D:\\Final\\src\\input\\Images\\forest\\42.jpg","D:\\Final\\src\\input\\Images\\forest\\43.jpg","D:\\Final\\src\\input\\Images\\forest\\44.jpg","D:\\Final\\src\\input\\Images\\forest\\45.jpg","D:\\Final\\src\\input\\Images\\forest\\46.jpg","D:\\Final\\src\\input\\Images\\forest\\47.jpg","D:\\Final\\src\\input\\Images\\forest\\48.jpg","D:\\Final\\src\\input\\Images\\forest\\49.jpg","D:\\Final\\src\\input\\Images\\forest\\50.jpg"]

    color = ["D:\\Final\\src\\input\\Images\\color\\1.jpg", "D:\\Final\\src\\input\\Images\\color\\2.jpg","D:\\Final\\src\\input\\Images\\color\\3.jpg","D:\\Final\\src\\input\\Images\\color\\4.jpg","D:\\Final\\src\\input\\Images\\color\\5.jpg","D:\\Final\\src\\input\\Images\\color\\6.jpg","D:\\Final\\src\\input\\Images\\color\\7.jpg","D:\\Final\\src\\input\\Images\\color\\8.jpg","D:\\Final\\src\\input\\Images\\color\\9.jpg","D:\\Final\\src\\input\\Images\\color\\10.jpg","D:\\Final\\src\\input\\Images\\color\\11.jpg","D:\\Final\\src\\input\\Images\\color\\12.jpg","D:\\Final\\src\\input\\Images\\color\\13.jpg","D:\\Final\\src\\input\\Images\\color\\14.jpg","D:\\Final\\src\\input\\Images\\color\\21.jpg","D:\\Final\\src\\input\\Images\\color\\16.jpg","D:\\Final\\src\\input\\Images\\color\\17.jpg","D:\\Final\\src\\input\\Images\\color\\18.jpg","D:\\Final\\src\\input\\Images\\color\\19.jpg","D:\\Final\\src\\input\\Images\\color\\22.jpg","D:\\Final\\src\\input\\Images\\color\\21.jpg","D:\\Final\\src\\input\\Images\\color\\24.jpg","D:\\Final\\src\\input\\Images\\color\\25.jpg","D:\\Final\\src\\input\\Images\\color\\26.jpg","D:\\Final\\src\\input\\Images\\color\\27.jpg","D:\\Final\\src\\input\\Images\\color\\29.jpg","D:\\Final\\src\\input\\Images\\color\\30.jpg","D:\\Final\\src\\input\\Images\\color\\31.jpg","D:\\Final\\src\\input\\Images\\color\\32.jpg","D:\\Final\\src\\input\\Images\\color\\33.jpg","D:\\Final\\src\\input\\Images\\color\\34.jpg","D:\\Final\\src\\input\\Images\\color\\35.jpg","D:\\Final\\src\\input\\Images\\color\\36.jpg","D:\\Final\\src\\input\\Images\\color\\37.jpg","D:\\Final\\src\\input\\Images\\color\\38.jpg","D:\\Final\\src\\input\\Images\\color\\39.jpg","D:\\Final\\src\\input\\Images\\color\\40.jpg","D:\\Final\\src\\input\\Images\\color\\41.jpg","D:\\Final\\src\\input\\Images\\color\\42.jpg","D:\\Final\\src\\input\\Images\\color\\43.jpg","D:\\Final\\src\\input\\Images\\color\\44.jpg","D:\\Final\\src\\input\\Images\\color\\45.jpg","D:\\Final\\src\\input\\Images\\color\\46.jpg","D:\\Final\\src\\input\\Images\\color\\47.jpg","D:\\Final\\src\\input\\Images\\color\\48.jpg","D:\\Final\\src\\input\\Images\\color\\49.jpg","D:\\Final\\src\\input\\Images\\color\\50.jpg"]

    space = ["D:\\Final\\src\\input\\Images\\space\\1.jpg", "D:\\Final\\src\\input\\Images\\space\\8.jpg", "D:\\Final\\src\\input\\Images\\space\\9.jpg", "D:\\Final\\src\\input\\Images\\space\\4.jpg", "D:\\Final\\src\\input\\Images\\space\\5.jpg", "D:\\Final\\src\\input\\Images\\space\\6.jpg", "D:\\Final\\src\\input\\Images\\space\\7.jpg", "D:\\Final\\src\\input\\Images\\space\\8.jpg", "D:\\Final\\src\\input\\Images\\space\\9.jpg", "D:\\Final\\src\\input\\Images\\space\\10.jpg", "D:\\Final\\src\\input\\Images\\space\\16.jpg", "D:\\Final\\src\\input\\Images\\space\\12.jpg", "D:\\Final\\src\\input\\Images\\space\\13.jpg", "D:\\Final\\src\\input\\Images\\space\\14.jpg", "D:\\Final\\src\\input\\Images\\space\\15.jpg", "D:\\Final\\src\\input\\Images\\space\\16.jpg", "D:\\Final\\src\\input\\Images\\space\\17.jpg", "D:\\Final\\src\\input\\Images\\space\\18.jpg", "D:\\Final\\src\\input\\Images\\space\\19.jpg", "D:\\Final\\src\\input\\Images\\space\\20.jpg", "D:\\Final\\src\\input\\Images\\space\\21.jpg", "D:\\Final\\src\\input\\Images\\space\\22.jpg", "D:\\Final\\src\\input\\Images\\space\\23.jpg", "D:\\Final\\src\\input\\Images\\space\\24.jpg", "D:\\Final\\src\\input\\Images\\space\\5.jpg", "D:\\Final\\src\\input\\Images\\space\\26.jpg", "D:\\Final\\src\\input\\Images\\space\\27.jpg", "D:\\Final\\src\\input\\Images\\space\\28.jpg", "D:\\Final\\src\\input\\Images\\space\\29.jpg", "D:\\Final\\src\\input\\Images\\space\\1.jpg", "D:\\Final\\src\\input\\Images\\space\\31.jpg", "D:\\Final\\src\\input\\Images\\space\\32.jpg", "D:\\Final\\src\\input\\Images\\space\\33.jpg", "D:\\Final\\src\\input\\Images\\space\\34.jpg", "D:\\Final\\src\\input\\Images\\space\\35.jpg", "D:\\Final\\src\\input\\Images\\space\\36.jpg", "D:\\Final\\src\\input\\Images\\space\\37.jpg", "D:\\Final\\src\\input\\Images\\space\\38.jpg", "D:\\Final\\src\\input\\Images\\space\\39.jpg", "D:\\Final\\src\\input\\Images\\space\\40.jpg", "D:\\Final\\src\\input\\Images\\space\\41.jpg", ]

    files = [forest, color, space]
    num = random.randint(0, 2)

    clip = ImageSequenceClip(files[num], fps = 0.25) 
    clip.write_videofile("src\\output\\images.mp4", fps = 24)
    clipa = AudioFileClip("static\\simple_audio.mp4")
    duration = clipa.duration  
    clip_duration = clip.duration
    num_repeats = int(duration / clip_duration) + 1
    repeated_clip = concatenate_videoclips([clip] * num_repeats)
    repeated_clip.duration = duration   
    clipm = repeated_clip.set_audio(clipa)
    clipm.write_videofile('D:\\Final\\static\\images_to_video.mp4')