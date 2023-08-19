import tkinter as tk
from tkinter import ttk
from settings import icon_path


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Apheleia Inventory System")
        self.geometry("700x500")
        icon = tk.PhotoImage(file=icon_path)
        self.iconphoto(False, icon)

        self.title_bar = TitleBar()


class TitleBar(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place(x=0, y=0, relwidth=1, relheight=0.2)

        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self, text="Apheleia").grid(row=0, column=0)


if __name__ == '__main__':
    app = App()
    app.mainloop()
