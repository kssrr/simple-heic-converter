import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory

from converter import HeicConverter

# TODO:
# * Format-button (png oder jpeg) ?

class HeicConverterApp():

    def __init__(self, geom="800x400") -> None:
        self.geom = geom
        self.converter = HeicConverter(path=askdirectory())
        self.outdir = self.converter.dir_path
        self.__window_setup()
        self.__frame_setup(label=f"Ausgewählter Ordner: {self.converter.dir_path}\nGefundene Bilder: {len(self.converter.images)}")
        self.__button_setup()

    def __window_setup(self) -> None:
        self.window = tk.Tk()
        self.window.title("HEIC-Bilder konvertieren")
        self.window.geometry(self.geom)

    def __frame_setup(self, label: str, initial=False) -> None:
        self.content = tk.Frame()
        self.label = tk.Label(self.window, text=label, wraplength=400)
        self.label.pack()

    def __button_setup(self) -> None:
        self.button_outdir = tk.Button(
            self.window,
            text="Speichern unter...",
            command=self.__select_outdir
        )
        self.button_convert = tk.Button(
            self.window,
            text="Konvertieren",
            command=self.__convert
        )
        [button.pack() for button in [self.button_outdir, self.button_convert]]

    def __select_outdir(self) -> None:
        self.converter.out_path = askdirectory()

    def __convert(self) -> None:
        n_files = len(self.converter.images)
        if n_files > 0:
            progress_update = self.__show_progress_bar(n_files)
            self.converter.convert_all(
                progress_callback=lambda current,
                total: progress_update(current)
            )
        else:
            tk.messagebox.showinfo("Information", "Keine HEIC-Dateien zum Konvertieren gefunden.")

    def __show_progress_bar(self, n: int) -> None:
        popup = tk.Toplevel(self.window)
        popup.title("Konvertierung läuft...")
        tk.Label(popup, text="Konvertierung...").pack(pady=10)
        progress_bar = ttk.Progressbar(
            popup,
            orient="horizontal",
            length=300,
            mode="determinate",
            maximum=n
        )
        progress_bar.pack(pady=10)

        def progress_fun(num):
            progress_bar['value'] = num
            popup.update_idletasks()

        return progress_fun

    def start(self) -> None:
        self.window.mainloop()

