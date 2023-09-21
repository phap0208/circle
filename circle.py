import tkinter as tk


root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000, bg="white")
radius = 50
x = 250
y = 250
circle = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="yellow")
radius2 = 30
x2 = 500
y2 = 500
circle2 = canvas.create_oval(x2 - radius2, y2 - radius2, x2 + radius2, y2 + radius2, fill="green")
text = canvas.create_text(x, y - radius - 20, text="phap", fill="red", font=("Arial", 20))
text2 = canvas.create_text(x2, y2 - radius2 - 20, text="boss", fill="red", font=("Arial", 20))

def check_collision():
    global x, y, radius, x2, y2, radius2
    distance = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
    if distance <= radius + radius2:
        return True
    else:
        return False

def show_message():
    if check_collision():
        message = canvas.create_text(
            canvas_width + 500,  # Xác định x-coordinate
            canvas_height + 50,  # Xác định y-coordinate
            text="stop!",  # Văn bản cần hiển thị
            fill="red",
            font=("Arial", 30)
        )
        canvas.after(3000, lambda: canvas.delete(message))

def remove_message():
    canvas.delete("message")

pressed_keys = set()  # Sử dụng để theo dõi các phím đang được nhấn

def key_pressed(event):
    global pressed_keys
    key = event.keysym
    pressed_keys.add(key)
    move_circle()  # Gọi hàm move_circle() khi một phím được nhấn

def key_released(event):
    global pressed_keys
    key = event.keysym
    pressed_keys.discard(key)

def move_circle():
    global circle, circle2
    global x, y, radius, x2, y2, radius2
    global text, text2

    step = 10
    delta = 1

    # Calculate the canvas boundaries
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    if "Left" in pressed_keys:
        if x2 - radius2 > 0:
            x2 -= step
    elif "Up" in pressed_keys:
        if y2 - radius2 > 0:
            y2 -= step
    elif "Right" in pressed_keys:
        if x2 + radius2 < canvas_width:
            x2 += step
    elif "Down" in pressed_keys:
        if y2 + radius2 < canvas_height:
            y2 += step
    elif "a" in pressed_keys:
        if x - radius > 0:
            x -= step
    elif "w" in pressed_keys:
        if y - radius > 0:
            y -= step
    elif "d" in pressed_keys:
        if x + radius < canvas_width:
            x += step
    elif "s" in pressed_keys:
        if y + radius < canvas_height:
            y += step
    elif "k" in pressed_keys:
        radius += delta
    elif "m" in pressed_keys:
        if radius > 0:
            radius -= delta
    elif "y" in pressed_keys:
        radius2 += delta
    elif "h" in pressed_keys:
        if radius2 > 0:
            radius2 -= delta

    canvas.delete(circle)
    circle = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="yellow")
    canvas.delete(circle2)
    circle2 = canvas.create_oval(x2 - radius2, y2 - radius2, x2 + radius2, y2 + radius2, fill="green")

    canvas.delete(text)
    text = canvas.create_text(x, y - radius - 20, text="phap", fill="red", font=("Arial", 20))
    canvas.delete(text2)
    text2 = canvas.create_text(x2, y2 - radius2 - 20, text="boss", fill="red", font=("Arial", 20))

    show_message()  # Hiển thị thông báo

root.bind("<KeyPress>", key_pressed)
root.bind("<KeyRelease>", key_released)
canvas.pack()

# Calculate the canvas boundaries
canvas_width = canvas.winfo_width()
canvas_height = canvas.winfo_height()

root.mainloop()
