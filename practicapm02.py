import tkinter as tk
import time

class MovingImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Moving Image Animation")

        # Создание Canvas
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        # Загрузка изображения и его отображение на Canvas
        self.photo = tk.PhotoImage(file="logo.png")
        self.image = self.canvas.create_image(200, 200, image=self.photo, anchor="center")

    def move_image(self):
        x, y = 200, 200
        for _ in range(100):
            x += 2
            self.canvas.move(self.image, 2, 0)  # Перемещение изображения по оси x
            self.root.update()  # Обновление окна для отображения перемещения
            time.sleep(0.05)  # Задержка для наблюдения анимации

root = tk.Tk()
app = MovingImageApp(root)
app.move_image()  # Запуск анимации передвижения изображения
root.mainloop()