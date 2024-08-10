import tkinter 
import customtkinter as Tk
from pytube import YouTube



def startDownload():
  try:
    ytLink = link.get()
    ytObject = YouTube(ytLink, on_progress_callback=on_progress)
    title.configure(text=ytObject.title,text_color='white')
    video = ytObject.streams.get_highest_resolution()
    ytObject.streams
    vido.download()

  except:
    finish_label.configure(text='Download Error⛔',text_color="red")
  finish_label.configure(text="Dowloaded✅",text_color='white')


def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per=str(int(percentage_of_completion))
    progress_percentage.configure(text=per + '%')
    progress_percentage.update()

    progress_bar.set(float(percentage_of_completion/100))


# app theme/config
Tk.set_appearance_mode('system')
Tk.set_default_color_theme('blue')






# app dimensions/title config
app = Tk.CTk()
app.geometry('720x480')
app.iconbitmap('Top-Secret-Projects/Youtube-Downloader/youzen_icon.ico')
app.title('Youzen')


title = Tk.CTkLabel(app, text='insert a youtube link ☺️',font=('Helvetica',20))
title.pack(padx=10, pady=10)

url_var = tkinter.StringVar()
link = Tk.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()



finish_label = Tk.CTkLabel(app, text='')
finish_label.pack()

download = Tk.CTkButton(app, text='download',command=startDownload,font=('Helvetica',14))
download.pack(pady=10,padx=10)

progress_percentage = Tk.CTkLabel(app,text='0%')
progress_percentage.pack()

progress_bar = Tk.CTkProgressBar(app, width=400)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)




startDownload()

app.mainloop()
