# Класс для описания упражнений
class Exercise:
    def __init__(self, name, image, duration, repeats=1):
        self.name = name  # Название упражнения
        self.image = image  # Путь к изображению
        self.duration = duration  # Длительность выполнения (в секундах)
        self.repeats = repeats  # Количество повторений

    def __repr__(self):
        return f"{self.name} - {self.duration}s - {self.repeats} times"


# Список упражнений
exercises = [
    Exercise("1. Stretch for 15 seconds", "../img/1.jpg", 15),
    Exercise("2. Stretch for 15 seconds", "../img/2.jpg", 15),
    Exercise("3. Stretch to each side for 10 seconds", "../img/3.jpg", 10, 2),
    Exercise("4. Stretch for 15 seconds", "../img/4.jpg", 15),
    Exercise("5. Lifting and lowering shoulders x 5", "../img/5.jpg", 10),
    Exercise("6. Neck stretch for 5 seconds on each side", "../img/6.jpg", 5, 2),
    Exercise("7. Wrist stretch 10 seconds", "../img/7.jpg", 10),
    Exercise("8. Turning palms down", "../img/8.jpg", 10),
    Exercise("9. Stretching arms to each side for 5 seconds", "../img/9.jpg", 5, 2),
    Exercise("10. Rotation to both sides", "../img/10.jpg", 5, 2),
    Exercise("11. Shrug back 10 seconds", "../img/11.jpg", 10),
    Exercise("12. Hand movement 10 seconds", "../img/12.jpg", 10),
]

# Функция для получения упражнения по индексу
def get_exercise(index):
    """Возвращает упражнение по индексу или None, если индекс некорректен."""
    return exercises[index] if 0 <= index < len(exercises) else None
