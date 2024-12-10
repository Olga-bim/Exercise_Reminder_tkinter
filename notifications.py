from plyer import notification
from exercises import exercises

# Сохраняем индексы для кнопки "Напомнить позже"
remind_later_index = None

def send_notification(index):
    global remind_later_index
    if 0 <= index < len(exercises):
        exercise = exercises[index]
        remind_later_index = index  # Сохраняем текущий индекс
        notification.notify(
            title="Time to Exercise!",
            message=f"Do: {exercise['name']}\nClick 'Remind Later' to set a new interval.",
            app_icon="assets/images/icon.png",
            timeout=10
        )
