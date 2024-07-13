import customtkinter as ctk
from random import choices

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("+700+400")
        self.title("Счётчик цифр")

        self.label = ctk.CTkLabel(self, text="0", font=("Roboto", 70))
        self.label.pack(padx=20, pady=40)

        self.button1 = ctk.CTkButton(self, text="Увеличение", width=220, height=50, corner_radius=25, border_width=2,
                                     font=("Roboto", 17), fg_color="#4169E1", hover_color='#6495ED',
                                     command=self.counter_digits)
        self.button1.pack(padx=20, pady=20)

        self.button2: ctk.CTkButton | None

    def random_color(self):
        return "#" + "".join(choices("0123456789ABCDEF", k=6))

    def counter_digits(self):
        self.label.configure(text=str(int(self.label.cget("text")) + 1), text_color=self.random_color())
        if self.label.cget("text") == "1":
            self.button2 = ctk.CTkButton(self, text="Перезагрузить", width=220, height=50, corner_radius=25,
                                         border_width=2, command=self.label_close,
                                         font=("Roboto", 17), fg_color="#800000", hover_color='#A52A2A')
            self.button2.pack(padx=20, pady=(0, 20))

    def label_close(self):
        self.label.configure(text="0", text_color="white")
        self.button2.destroy()


if __name__ == '__main__':
    app = App()
    app.mainloop()
