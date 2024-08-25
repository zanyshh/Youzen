import tkinter 
import customtkinter as Tk
from pytube import YouTube


# function to start download
def startDownload():
  try:
    ytLink = link.get()
    ytObject = YouTube(ytLink, on_progress_callback=on_progress)
    title.configure(text=ytObject.title,text_color='white')
    video = ytObject.streams.get_highest_resolution()
    ytObject.streams
    vido.download()

  except:
    finish_label.configure(text='Download Error',text_color="red")
  finish_label.configure(text="Dowloaded",text_color='blue')




# app theme/config
Tk.set_appearance_mode('system')
Tk.set_default_color_theme('blue')




# app dimensions/title config
app = Tk.CTk()
app.geometry('400x300')
app.title('Youzen')
app.iconbitmap('youzen/resources/youzen_icon.ico')




# window frame config
frame = Tk.CTkFrame(app)
frame.pack(pady=20,padx=20)


url_var = tkinter.StringVar()

# link entry label
link = Tk.CTkEntry(frame,
                  width=300, height=30,
                  textvariable=url_var,
                  placeholder_text='Enter Link Here>>')
link.pack()

# finish label
finish_label = Tk.CTkLabel(frame, 
                          text='')
finish_label.pack()



# download button
download = Tk.CTkButton(frame,
                       text='download',
                       command=startDownload,
                       font=('Helvetica',14),
                        width=60,height=40,
                        fg_color='#c1121f',
                        hover_color='#780000')
download.pack(pady=10,padx=10)


# loop to show window
app.mainloop()
