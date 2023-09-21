import tkinter as tk
import tkinter.messagebox as mb
import time  # Add the time module

root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=1000, bg="white")
radius = 50
x = 250
y = 250
circle = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")
radius2 = 30
x2 = 500
y2 = 500
circle2 = canvas.create_oval(x2 - radius2, y2 - radius2, x2 + radius2, y2 + radius2, fill="blue")
text = canvas.create_text(x, y - radius - 20, text="Red", fill="red", font=("Arial", 20))
text2 = canvas.create_text(x2, y2 - radius2 - 20, text="Blue", fill="blue", font=("Arial", 20))

def check_collision():
    global x, y, radius, x2, y2, radius2
    distance = ((x - x2) ** 2 + (y - y2) ** 2) ** 0.5
    if distance <= radius + radius2:
        return True
    else:
        return False

# Define a function to move the circles based on key press
def move_circle(event):
    global circle, circle2  # Declare circles as global
    global x, y, radius, x2, y2, radius2
    global text, text2 # Declare texts as global
    # Get the key code
    key = event.keycode
    # Define the step size for moving
    step = 10
    # Define the change in radius for resizing
    delta = 1

    # Calculate the canvas boundaries
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Check which key is pressed and update the position and radius accordingly
    if key == 37:  # Left arrow key
        if x2 - radius2 > 0:
            x2 -= step
    elif key == 38:  # Up arrow key
        if y2 - radius2 > 0:
            y2 -= step
    elif key == 39:  # Right arrow key
        if x2 + radius2 < canvas_width:
            x2 += step
    elif key == 40:  # Down arrow key
        if y2 + radius2 < canvas_height:
            y2 += step
    elif key == 65:  # A key
        if x - radius > 0:
            x -= step
    elif key == 87:  # W key
        if y - radius > 0:
            y -= step
    elif key == 68:  # D key
        if x + radius < canvas_width:
            x += step
    elif key == 83:  # S key
        if y + radius < canvas_height:
            y += step
    elif key == 75:  # K key for red circle
        radius += delta
    elif key == 77:  # M key for red circle
        if radius > 0:
            radius -= delta
    elif key == 89:  # Y key for blue circle
        radius2 += delta
    elif key == 72:  # H key for blue circle
        if radius2 > 0:
            radius2 -= delta

    # Delete the old circles and draw new ones with the updated position and radius
    canvas.delete(circle)
    circle = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="red")
    canvas.delete(circle2)
    circle2 = canvas.create_oval(x2 - radius2, y2 - radius2, x2 + radius2, y2 + radius2, fill="blue")

    # Delete the old texts and draw new ones with the updated position and content
    canvas.delete(text)
    text = canvas.create_text(x, y - radius - 20, text="Red", fill="red", font=("Arial", 20))
    canvas.delete(text2)
    text2 = canvas.create_text(x2, y2 - radius2 - 20, text="Blue", fill="blue", font=("Arial", 20))

    # Check if the circles are colliding and show a message box if they are
    if check_collision():
        mb.showinfo("Collision", "The circles are colliding!")

# Bind the function to the root window's key press event
root.bind("<Key>", move_circle)

# Pack the canvas widget to the root window
canvas.pack()

# Start the main loop of the root window
root.mainloop()

