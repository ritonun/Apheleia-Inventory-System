import tkinter as tk
from settings import icon_path, COLORS


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Apheleia Inventory System")
        self.geometry("700x500")
        icon = tk.PhotoImage(file=icon_path)
        self.iconphoto(False, icon)

        self.title_bar = TitleBar(bg=COLORS["bg"])


class TitleBar(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place(x=0, y=0, relwidth=1, relheight=0.1)

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure((0, 1, 2), weight=1)
        label = tk.Label(self, text="APHELEIA", fg="white", bg="black", font=72)
        label.grid(row=0, column=1)


if __name__ == '__main__':
    app = App()
    app.mainloop()
