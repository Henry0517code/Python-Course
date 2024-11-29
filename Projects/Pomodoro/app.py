import tkinter as tk
from tkinter import ttk, messagebox
import threading
import webbrowser

class PomodoroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Meow")
        self.root.geometry("600x250")
        self.root.resizable(False, False)

        # Timer variables
        self.work_duration = 45 * 60  # 45 minutes (customized from 25 minutes)
        self.short_break = 5 * 60  # 5 minutes
        self.long_break = 15 * 60  # 15 minutes
        self.reps = 0
        self.timer_running = False
        self.is_paused = False
        self.remaining_time = 0

        # Styling
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 14))
        style.configure("TLabel", font=("Helvetica", 18))

        # Header label
        self.label = ttk.Label(root, text="Flow", font=("Helvetica", 24), foreground="black")
        self.label.pack(pady=20)

        # Timer display
        self.time_display = ttk.Label(root, text="45:00", font=("Helvetica", 48))
        self.time_display.pack(pady=10)

        # Button controls
        self.button_frame = ttk.Frame(root)
        self.button_frame.pack(pady=20)

        self.start_button = ttk.Button(self.button_frame, text="Start", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=10)

        self.pause_button = ttk.Button(self.button_frame, text="Pause", command=self.pause_timer, state="disabled")
        self.pause_button.grid(row=0, column=1, padx=10)

        self.reset_button = ttk.Button(self.button_frame, text="Reset", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=10)

        self.timer = None

    def reset_timer(self):
        if self.timer:
            self.root.after_cancel(self.timer)
        self.timer_running = False
        self.is_paused = False
        self.reps = 0
        self.remaining_time = 0
        self.time_display.config(text="45:00")
        self.label.config(text="Flow", foreground="black")
        self.pause_button.config(state="disabled")
        self.start_button.config(state="normal")

        # Open Rick Roll video
        threading.Thread(target=self.open_rickroll).start()

    def open_rickroll(self):
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.pause_button.config(state="normal")
            self.start_button.config(state="disabled")

            if self.remaining_time == 0:
                self.reps += 1
                if self.reps % 8 == 0:
                    # Long break
                    self.countdown(self.long_break)
                    self.label.config(text="Long Break", foreground="blue")
                elif self.reps % 2 == 0:
                    # Short break
                    self.countdown(self.short_break)
                    self.label.config(text="Short Break", foreground="orange")
                else:
                    # Work session
                    self.countdown(self.work_duration)
                    self.label.config(text="Work", foreground="green")
            else:
                self.countdown(self.remaining_time)

    def pause_timer(self):
        if self.timer_running:
            if not self.is_paused:
                self.root.after_cancel(self.timer)
                self.is_paused = True
                self.pause_button.config(text="Resume")
            else:
                self.is_paused = False
                self.pause_button.config(text="Pause")
                self.countdown(self.remaining_time)

    def countdown(self, count):
        self.remaining_time = count
        mins = count // 60
        secs = count % 60
        self.time_display.config(text=f"{mins:02d}:{secs:02d}")

        if count > 0 and not self.is_paused:
            self.timer = self.root.after(1000, self.countdown, count - 1)
        elif count == 0:
            self.timer_running = False
            self.remaining_time = 0
            self.start_timer()  # Automatically start the next session
            messagebox.showinfo("Pomodoro Timer", "Time's up!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroApp(root)
    root.mainloop()