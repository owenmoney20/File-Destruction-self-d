from Tkinter import *
import shutil
window = Tk()
window.title("Self destruct app:SELF-D")
window.geometry("320x320+550+200")
window.configure(background="black")
def e():
	exit()
def a(): 
	shutil.rmtree("selfd")
	win = Tk()
	win.title("File delete success")
	win.geometry("160x160+550+200")
	win.configure(background="black")
	Label(win, text="Files successfully deleted", fg="red", font="times 10 bold").pack()
	button = Button(win, text="exit", command=e, bg="black", fg="red").pack()
Label(window, text="SELF-D", fg="red", bg="black", font="none 40 bold").pack()
Label(window, text="We are not responsible for any harm you do with selfd!!!", fg="red", bg="black", font="none 7").pack()
button = Button(window, text="self destruct button", command=a, bg="black", fg=
"red").pack()
Label(window, text="!UPDATES COMING SOON!", fg="red", bg="black", font="none 10 bold").pack()
Label(window, text="Check github for updates", fg="red", bg="black", font="times 10 ").pack()
window.mainloop()
