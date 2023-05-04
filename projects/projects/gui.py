import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name


from downloader import download as download_video


def download():
    download_video(link.get(), path_label.cget("text"))


def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)


screen = Tk()
title = screen.title('Youtube Video Downloader')

canvas = Canvas(screen, width=500, height=500)

canvas.pack()
# logo
logo = PhotoImage(file='C:\VIT Projesi\projects\projects\youtube.png')
# resize
logo = logo.subsample(2, 2)
# place the image
canvas.create_image(250, 70, image=logo)

# Link
link = Entry(screen, text='Link', font=('Arial', 15))
link_label = Label(screen, text='Enter the link: ', font=('Arial', 15))

# Place to the canvas
canvas.create_window(250, 170, window=link_label)
canvas.create_window(250, 220, window=link)

# Select Path for saving the file
path_label = Label(screen, text="Select Path For Download", font=('Arial', 15))
select_btn = Button(screen, text="Select Path", bg='red', padx='22',
                    pady='5', font=('Arial', 15), fg='#fff', command=select_path)
# Add to window
canvas.create_window(250, 280, window=path_label)
canvas.create_window(250, 330, window=select_btn)

# download btn
download_btn = Button(screen, text='Download', font=('Arial', 15),
                      command=download)

canvas.create_window(250, 400, window=download_btn)


screen.mainloop()
