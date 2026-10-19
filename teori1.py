import tkinter as tk
import tkinter.messagebox as msg

top=tk.Tk()
def helloCallback():
    msg.showinfo("Belajar GUI", "assalamualaikum")
Check
w1=tk.Button(top, text="Klik Saya", command=helloCallback)
w1.pack()
w2=tk.Button(top, text="Tekan Saya Lagi", command=helloCallback)
w2.pack()
top.mainloop()

