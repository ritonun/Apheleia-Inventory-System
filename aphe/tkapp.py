import tkinter as tk
from settings import icon_path, COLORS, db_path
from database import DatabaseInterface


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Apheleia Inventory System")
        self.geometry("700x500")
        icon = tk.PhotoImage(file=icon_path)
        self.iconphoto(False, icon)

        self.db = DatabaseInterface(path=db_path)

        self.title_bar = TitleBar(bg=COLORS["bg"])
        self.title_bar.place(x=0, y=0, relwidth=1, relheight=0.1)
        # self.title_bar.grid(row=0, column=0)

        self.database_display = DatabaseDisplay(self.db)
        self.database_display.place(x=0, rely=0.5)


class TitleBar(tk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.create_widgets()

    def create_widgets(self):
        self.columnconfigure((0, 1, 2), weight=1)
        label = tk.Label(self, text="APHELEIA", fg="white", bg=COLORS["bg"], font=72)
        label.grid(row=0, column=1)


class DatabaseDisplay(tk.Frame):
    def __init__(self, db, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.db = db
        self.table = self.db.fetch_all_table()
        self.create_widgets()
        self.db.quit()

    def update_table(self):
        table = self.db.fetch_all_table()
        self.table = None
        self.table = (table[0], table[2])
        self.create_widgets()

    def create_widgets(self):
        self.create_listbox()
        button = tk.Button(self, text="Update", command=self.update_table).grid(row=0, column=0)

    def create_listbox(self):
        for column in range(len(self.table[0])):
            lb = tk.Listbox(self)
            for index, comp in enumerate(self.table):
                lb.insert(index, str(comp[column]))
            lb.grid(row=1, column=column)


if __name__ == '__main__':
    app = App()
    app.mainloop()
