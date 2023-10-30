import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from ArethmaticOperations import *
from SignalProcessor import SignalProcessor
from testing import SignalSamplesAreEqual

class Task_3:
    def __init__(self, main_window):
        self.main_window = main_window
        self.app = None  # Initialize app as None

    def open_window(self):
        if self.app is not None:
            return
        
        self.app = tk.Toplevel(self.main_window)
        self.app.title("Task 3")
