from pytube import YouTube
import tkinter
import customtkinter

def startDownload():
    try:
        ytLink=link.get()
        yt = YouTube(ytLink,on_progress_callback=on_progress)
        yd = yt.streams.get_highest_resolution()
        title.configure(text=yt.title,text_color="white")
        finishLabel.configure(text="")
        yd.download('/home/nick/Downloads')
        finishLabel.configure(text="Downloaded")
    except:
        finishLabel.configure(text="YouTube link invalid",text_color="red")
    
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size-bytes_remaining
    percentage_of_competion = bytes_downloaded/total_size*100
    per = str(int(percentage_of_competion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

    progressBar.set(float(percentage_of_competion)/100)

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

title = customtkinter.CTkLabel(app,text="Insert YouTube Link")
title.pack(padx=10, pady=10)

url_var=tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=500, height=40,textvariable=url_var)
link.pack()

finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

pPercentage = customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()
progressBar=customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

app.mainloop()
