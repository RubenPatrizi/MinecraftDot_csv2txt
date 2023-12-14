from sys import exit
import tkinter
import tkinter.filedialog
import customtkinter as c
from conversion import *

c.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
c.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class dimWindow(c.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.grab_set()
        self._lan: str

        default_font = c.CTkFont(family="arial", size=15, weight="bold")
        self.geometry("280x170")
        self.resizable(False, False)
        self.title(" ")
        self.frame = c.CTkFrame(self, width=170, corner_radius=20)
        self.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)

        self.lan_label = c.CTkLabel(self, text="Language", font=default_font)
        self.lan_label.place(relx=0.345, rely=0.06)
        self.lan = c.CTkOptionMenu(self,values=["EN","IT"],width=80,height=30)
        self.lan.place(relx=0.33, rely=0.25)

        self.confirm_button = c.CTkButton(self, height=30, width=100, text="Confirm",font=default_font, fg_color="green",hover_color="dark green", command=self.save_info)
        self.confirm_button.place(relx=0.3, rely=0.6)

        self.info = c.CTkLabel(self, text="Choose output language")
        self.info.grid(row=7, columnspan=8)

    def save_info(self):
        self._lan = self.lan.get()
        self.destroy()

    def get_info(self):
        self.master.wait_window(self)
        return self._lan


class App(c.CTk):
    def __init__(self):
        super().__init__()

        self._path: str
        self._lan: int
        self._text: str
        self._text = ""
        default_font = c.CTkFont(family="arial", size=15, weight="bold")

        # configure window
        self.title("MinecraftDot to text")
        self.geometry("500x600")
        self.resizable(False, False)

        # configure grid layout
        self.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5), weight=0)

# -----------------------------------------------          MAIN WINDOW        ------------------------------------------------------------

        self.text_preview = c.CTkTextbox(self,width=350,height=500,corner_radius=20,font=c.CTkFont(family="arial", size=14, weight="bold"))
        self.text_preview.grid(row=1,column=1,columnspan=4,pady=15)

        self.open_button = c.CTkButton(self, height=40, text="Open csv", font=default_font, command=self.file_browse_and_write)
        self.open_button.grid(row=4, column=1, columnspan=1, padx=30, pady=10)
        self.convert_button = c.CTkButton(self, height=40, text="Save to txt", font=default_font, command=self.write_on_file)
        self.convert_button.grid(row=4, column=3, columnspan=1, padx=0, pady=10)

    def error_window(self,msg):
        error_window = c.CTkToplevel(self)
        error_window.geometry("250x100")
        error_window.resizable(False, False)
        error_window.grab_set()
        error_window.title("Error")
        error_window.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=0)
        error_window.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=0)
        if msg:
            error_window.label = c.CTkLabel(error_window, text=msg, height=10)
        else:
            error_window.label = c.CTkLabel(error_window, text="Something went wrong!", height=10)
        error_window.label.grid(row=0, column=0, padx=(20, 0), pady=(25, 0))
        error_window.button = c.CTkButton(error_window, text="OK", fg_color="red", command=error_window.destroy)
        error_window.button.grid(row=1, column=0, padx=(50, 0), pady=(20, 0))

    def success_window(self):
        success_window = c.CTkToplevel(self)
        success_window.geometry("220x100")
        success_window.resizable(False, False)
        success_window.grab_set()
        success_window.title("Done")
        success_window.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=0)
        success_window.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=0)
        success_window.label = c.CTkLabel(success_window, text="File converted successfully!", height=10)
        success_window.label.grid(row=0, column=0, padx=(20, 0), pady=(25, 0))
        success_window.button = c.CTkButton(success_window, text="OK", fg_color="green", command=success_window.destroy)
        success_window.button.grid(row=1, column=0, padx=(40, 0), pady=(20, 0))

    def file_browse_and_write(self):
        self._path = tkinter.filedialog.askopenfilename(title="Select csv", filetypes=(("", ""), ("", ".csv")))
        self._lan = dimWindow().get_info()
        self.text_preview.configure(state="normal")
        if self._text != "":
            self.text_preview.delete("0.0","end")
        self._text = convert_to_text(read_file(self._path),self._lan)
        self.text_preview.insert("0.0",self._text)
        self.text_preview.configure(state="disabled")

    def exit_event(self):
        exit()

    def write_on_file(self):
        if self._text == "":
            self.error_window("You must select a csv first!")
            return
        self._path = tkinter.filedialog.askdirectory(title="Select folder")
        output = open(f"{self._path}/instructions.txt","w")
        output.write(self._text)
        output.close()
        self.success_window()


if __name__ == "__main__":
    App().mainloop()
