# TikTok Video Script: Why Messi is Way Ahead of CR7

# Step 1: Import necessary libraries (for video editing)
# You can use libraries like moviepy or external tools like CapCut, Final Cut Pro, or Adobe Premiere.

from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip

# Step 2: Define the script for the TikTok video
script = [
    {"text": "Why Messi is WAY ahead of CR7 🐐", "duration": 2},
    {"text": "1. Natural Talent 🎨", "duration": 2},
    {"text": "Messi's dribbling is pure magic. CR7 relies more on athleticism.", "duration": 3},
    {"text": "2. Playmaking Ability 🧠", "duration": 2},
    {"text": "Messi has more assists than any player EVER. He creates chances like no other.", "duration": 4},
    {"text": "3. Consistency Over Time ⏳", "duration": 2},
    {"text": "Messi has been world-class for 15+ years. CR7 peaked later and declined earlier.", "duration": 4},
    {"text": "4. Trophies & Awards 🏆", "duration": 2},
    {"text": "Messi has more Ballon d'Ors (8) and a World Cup. Enough said.", "duration": 4},
    {"text": "5. Impact on the Game 🌍", "duration": 2},
    {"text": "Messi changed how we see football. CR7 is a legend, but Messi is a once-in-a-lifetime player.", "duration": 5},
    {"text": "Agree? Drop a 🐐 in the comments!", "duration": 3}
]

# Step 3: Add background music
background_music = "path_to_epic_music.mp3"  # Replace with your music file

# Step 4: Create text overlays and compile the video
clips = []
for i, scene in enumerate(script):
    text_clip = TextClip(
        scene["text"],
        fontsize=50,
        color="white",
        font="Arial-Bold",
        size=(1080, 1920),  # TikTok vertical video size
        bg_color="black"
    ).set_duration(scene["duration"]).set_position("center")
    clips.append(text_clip)

# Combine all clips into one video
final_clip = CompositeVideoClip(clips)

# Add background music
audio = AudioFileClip(background_music)
final_clip = final_clip.set_audio(audio)

# Step 5: Export the video
final_clip.write_videofile("messi_vs_cr7_tiktok.mp4", fps=24)

print("TikTok video created successfully! Upload it and watch it go viral! 🚀")
