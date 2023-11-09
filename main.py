import tkinter as tk
from Task_12 import Task_12
from Task_3 import Task_3
from Task_4 import Task_4

# region GUI
main_window = tk.Tk()
# Place he windows in he centres of the screen
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
x_position = (screen_width - 200) // 2
y_position = (screen_height - 200) // 2
# Set the window's geometry to be centered
main_window.geometry(f"{200}x{200}+{x_position}+{y_position}")

main_window.title("Signal Processing")
# prepare each window for each Task
task_12 = Task_12(main_window)
task_3 = Task_3(main_window)
task_4 = Task_4(main_window)

# Creates a list of button labels
button_data = [("Task 1&2", task_12), ("Task 3", task_3), ("Task 4", task_4)]
# Create and center the buttons for each task
for label, win in button_data:
    button = tk.Button(main_window, text=label, command=win.open_window)
    button.pack(fill="x", pady=5)

main_window.mainloop()
# endregion
