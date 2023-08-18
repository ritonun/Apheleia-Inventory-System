import tkinter as tk


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Apheleia Inventory System")
        self.geometry("700x500")
        icon = tk.PhotoImage(file="../assets/image.png")
        self.iconphoto(False, icon)


if __name__ == '__main__':
    app = App()
    app.mainloop()