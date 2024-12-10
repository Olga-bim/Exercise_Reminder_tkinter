import tkinter as tk
from itertools import cycle
from exercises import exercises  # Импортируем список упражнений
from PIL import Image, ImageTk
from threading import Thread
from tkinter import simpledialog
from start_screen import StartScreen


class ExerciseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Exercise Reminder")
        
        # Получаем размеры экрана
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Устанавливаем размер окна
        window_size = f"{screen_width // 2}x{int(screen_height * 0.8)}"
        self.root.geometry(window_size)
        self.root.configure(bg="#2e2e2e")  # Темный фон
        
        # Переменные состояния
        self.is_paused = False
        self.current_exercise = None
        self.exercise_cycle = None
        self.countdown = 0
        self.time_left = 0
        self.timer_running = False
        self.repeat_count = 0
        self.reminder_timer = None  # Таймер для напоминания позже

        # Создаем стартовый экран
        self.start_screen = StartScreen(root, self.start_exercises)

    def start_exercises(self):
        """Запуск упражнений"""
        # Удаляем стартовый экран
        self.start_screen.destroy()

        # Виджеты для упражнений
        self.exercise_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#2e2e2e", fg="#ffffff")
        self.exercise_label.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#2e2e2e", fg="#ffffff")
        self.timer_label.pack(pady=10)

        self.image_label = tk.Label(self.root, bg="#2e2e2e")
        self.image_label.pack(pady=10)

        # Кнопки управления
        self.pause_button = tk.Button(self.root, text="Pause", font=("Arial", 16), fg="white", bg="#FF6347", command=self.pause_exercises, relief="flat", bd=0)
        self.pause_button.pack(side="left", padx=20, pady=10)

        self.resume_button = tk.Button(self.root, text="Continue", font=("Arial", 16), fg="white", bg="#4CAF50", command=self.resume_exercises, relief="flat", bd=0)
        self.resume_button.pack(side="left", padx=20, pady=10)

        self.remind_button = tk.Button(self.root, text="Remind me later", font=("Arial", 16), fg="white", bg="#FFD700", command=self.remind_later, relief="flat", bd=0)
        self.remind_button.pack(side="left", padx=20, pady=10)

        # Цикл упражнений
        self.exercise_cycle = cycle(exercises)
        self.show_next_exercise()

    def show_next_exercise(self):
        """Показываем следующее упражнение"""
        if self.is_paused:
            return

        exercise = next(self.exercise_cycle)
        self.current_exercise = exercise
        self.repeat_count = exercise.repeats

        self.exercise_label.config(text=f"{exercise.name}\nDuration: {exercise.duration}s\nrepeat for the other side: {self.repeat_count} раз")
        
        # Отображение изображения
        img = exercise.image
        try:
            image = Image.open(img)
            image.thumbnail((300, 300))
            self.start_image = ImageTk.PhotoImage(image)
            self.image_label.config(image=self.start_image)
            self.image_label.image = self.start_image
        except Exception as e:
            print(f"Error loading image: {e}")
        
        # Запуск таймера
        self.start_timer(exercise)

    def start_timer(self, exercise):
        """Запускает таймер для упражнения"""
        self.time_left = exercise.duration
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        """Обновляет таймер"""
        if self.timer_running:
            self.timer_label.config(text=f"There is time left: {self.time_left}s")
            if self.time_left > 0:
                self.time_left -= 1
                self.root.after(1000, self.update_timer)
            else:
                self.finish_exercise()

    def finish_exercise(self):
        """Обработка завершения упражнения"""
        self.repeat_count -= 1
        if self.repeat_count > 0:
            self.start_timer(self.current_exercise)
        else:
            self.show_next_exercise()

    def pause_exercises(self):
        """Ставит упражнения на паузу"""
        self.is_paused = True
        self.timer_running = False
        self.pause_button.config(state="disabled")
        self.resume_button.config(state="normal")

    def resume_exercises(self):
        """Возобновляет упражнения"""
        self.is_paused = False
        self.timer_running = True
        self.pause_button.config(state="normal")
        self.resume_button.config(state="disabled")
        self.update_timer()

    def remind_later(self):
        """Напомнить позже"""
        if self.timer_running:
            self.pause_exercises()

        # Пользователь вводит интервал для напоминания в минутах
        interval_minutes = simpledialog.askinteger("Remind me later", "Enter interval (in minutes):", minvalue=1, maxvalue=60)
    
        if interval_minutes:
            # Переводим интервал в секунды
            interval_seconds = interval_minutes * 60
        
            # Устанавливаем таймер на выбранное время
            if self.reminder_timer:
                self.root.after_cancel(self.reminder_timer)  # Отменяем предыдущий таймер, если он был
            self.reminder_timer = self.root.after(interval_seconds * 1000, self.resume_exercises)


def main():
    # Запуск Tkinter
    root = tk.Tk()
    app = ExerciseApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
