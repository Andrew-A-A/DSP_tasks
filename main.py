import tkinter as tk
from Task_12 import Task_12
from Task_3 import Task_3
from Task_45 import Task_45
from Task_6 import Task_6
from Task_7 import Task_7
from Task_8 import Task_8
from Task_9 import Task_9

# region GUI
main_window = tk.Tk()
main_window.title("Digital Signal Processing")
# Place he windows in he centres of the screen
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()
x_position = (screen_width - 250) // 2
y_position = (screen_height - 250) // 2
# Set the window's geometry to be centered
main_window.geometry(f"{250}x{250}+{x_position}+{y_position}")

# prepare each window for each Task
task_12 = Task_12(main_window, "Task 1&2")
task_3 = Task_3(main_window, "Task 3")
task_45 = Task_45(main_window, "Task 4&5")
task_6 = Task_6(main_window, "Task 6")
task_7 = Task_7(main_window, "Task 7")
task_8 = Task_8(main_window, "Task 8")
task_9 = Task_9(main_window, "Task 9")

# Creates a list of button labels
button_data = [task_12, task_3, task_45, task_6, task_7, task_8, task_9]
# Create and center the buttons for each task
for win in button_data:
    button = tk.Button(main_window, text=win.title, command=win.open_window)
    button.pack(fill="x", pady=5)

main_window.mainloop()
# endregion
