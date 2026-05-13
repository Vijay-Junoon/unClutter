from PIL import Image
import extractData
import ast
import customtkinter as Tk
from tkinter import filedialog
from pathlib import Path


app = Tk.CTk()
# app.iconphoto(True, Tk.PhotoImage(file="icon.png"))
app.title("Unclutter")
app.geometry("1280x800")
app.configure(fg_color="#030303")
app.minsize(1200, 800)

# Center layout system (3 columns: left spacer, main, right spacer)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=2)
app.grid_columnconfigure(2, weight=1)


def simulateVectorization(lab, btn, parentFolder):
    btn.destroy()
    lab.destroy()

    answer = extractData.vectorize()
    data = answer[0]
    folder_titles = ast.literal_eval(answer[1])

    n = len(data.keys())
    frames = []

    # 👉 Results container frame (keeps everything centered)
    result_container = Tk.CTkFrame(app, fg_color="transparent")
    result_container.grid(row=7, column=1, pady=30)

    result_container.grid_columnconfigure(tuple(range(n)), weight=1)

    # Frames in one horizontal row
    for i in range(n):
        frame = Tk.CTkFrame(
            result_container,
            width=300,
            height=220,
            corner_radius=15,
            fg_color="#111111"
        )
        frame.grid(row=0, column=i, padx=15, pady=10, sticky="n")
        frames.append(frame)

    # Folder titles aligned above frames
    for i in range(len(frames)):
        lab = Tk.CTkLabel(
            result_container,
            text=folder_titles[i],
            text_color="#ffffff",
            font=("Inter", 16, "bold")
        )
        lab.grid(row=1, column=i, pady=(5, 15))

    # Data inside frames
    for i in data:
        for j in range(len(data[i])):
            label = Tk.CTkLabel(
                frames[int(i)],
                text=data[i][j],
                text_color="#9ca3af",
                font=("Inter", 13)
            )
            label.grid(row=j, column=0, padx=10, pady=5)

    proceedBtn = Tk.CTkButton(
        app,
        fg_color="#ffffff",
        text_color="#030303",
        hover_color="#9ca3af",
        text="Proceed!",
        font=("Inter", 16),
        corner_radius=30,
        width=120,
        height=40,
        command=lambda: extractData.createDir(data, folder_titles, parentFolder)
    )
    proceedBtn.grid(row=8, column=1, pady=30)


def getAllFiles(parentFolder):
    parentFolder = Path(parentFolder)
    extractData.parent = parentFolder
    x = extractData.extractCorpus()

    label = Tk.CTkLabel(
        app,
        text=f"{x} files selected. Proceed?",
        font=("Inter", 16),
        text_color="#ffffff"
    )
    label.grid(row=5, column=1, pady=15)

    proceedButton = Tk.CTkButton(
        app,
        fg_color="#ffffff",
        text_color="#030303",
        hover_color="#9ca3af",
        text="Proceed",
        font=("Inter", 16),
        corner_radius=30,
        width=120,
        height=40,
        command=lambda: simulateVectorization(label, proceedButton, parentFolder)
    )
    proceedButton.grid(row=6, column=1, pady=15)


def open_windows():
    parentFolder = filedialog.askdirectory()
    getAllFiles(parentFolder)


# ===== HEADER SECTION (centered + spaced) =====
heading = Tk.CTkLabel(
    app,
    text="Your Files.",
    font=("Inter", 60, "bold"),
    text_color="#ffffff"
)
heading.grid(row=0, column=1, pady=(40, 0))

heading1 = Tk.CTkLabel(
    app,
    text="Finally Organized.",
    font=("Inter", 52, "bold"),
    text_color="#9ca3af"
)
heading1.grid(row=1, column=1, pady=(5, 0))

subtext = Tk.CTkLabel(
    app,
    justify="center",
    text="unClutter automatically groups and organizes messy PDFs using AI — no manual sorting required.",
    font=("Inter", 18),
    text_color="#9ca3af"
)
subtext.grid(row=2, column=1, pady=(10, 20))

btn = Tk.CTkButton(
    app,
    fg_color="#ffffff",
    text_color="#030303",
    hover_color="#9ca3af",
    text="Select Folder!",
    font=("Inter", 16),
    corner_radius=30,
    width=160,
    height=45,
    command=open_windows
)
btn.grid(row=3, column=1, pady=10)

label = Tk.CTkLabel(
    app,
    text="Select a folder to continue",
    text_color="#9ca3af",
    font=("Inter", 14)
)
label.grid(row=4, column=1, pady=10)

app.mainloop()