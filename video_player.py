import tkinter as tk
from tkinter import filedialog, ttk
import vlc

class VideoPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        self.root.geometry("800x600")

        # VLC Player instance
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # Create a frame for video
        self.video_frame = tk.Frame(self.root, bg="black")
        self.video_frame.pack(fill=tk.BOTH, expand=True)

        # Get the handle for embedding video
        self.player.set_hwnd(self.video_frame.winfo_id())

        # Add control buttons
        controls = tk.Frame(self.root)
        controls.pack(fill=tk.X)

        play_button = ttk.Button(controls, text="Play", command=self.play_video)
        play_button.pack(side=tk.LEFT, padx=5)

        pause_button = ttk.Button(controls, text="Pause", command=self.pause_video)
        pause_button.pack(side=tk.LEFT, padx=5)

        stop_button = ttk.Button(controls, text="Stop", command=self.stop_video)
        stop_button.pack(side=tk.LEFT, padx=5)

        open_button = ttk.Button(controls, text="Open", command=self.open_file)
        open_button.pack(side=tk.LEFT, padx=5)

        self.volume_slider = ttk.Scale(controls, from_=0, to=100, orient=tk.HORIZONTAL, command=self.set_volume)
        self.volume_slider.set(50)  # Default volume
        self.volume_slider.pack(side=tk.RIGHT, padx=5)

        self.current_file = None

    def open_file(self):
        # Open a file dialog to select a video file
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv *.mov")])
        if file_path:
            self.current_file = file_path
            self.load_video(file_path)

    def load_video(self, file_path):
        # Load the video into the player
        media = self.instance.media_new(file_path)
        self.player.set_media(media)
        self.play_video()

    def play_video(self):
        if self.current_file:
            self.player.play()

    def pause_video(self):
        self.player.pause()

    def stop_video(self):
        self.player.stop()

    def set_volume(self, value):
        volume = int(float(value))
        self.player.audio_set_volume(volume)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = VideoPlayerApp(root)
    root.mainloop()
