from tkinter import *
import speedtest  # pip install speedtest-cli
import threading

root = Tk()  # main Window is called 'root'
root.title("Internet Speed Test")  # Giving Title to window 'root'
root.resizable(False, False)  # can't rescale the window
root.configure(bg="#141527")  # set dark background color

# Dimensions for the Window
w = 450
h = 700

# Code to get coordinates to place window at center
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

root.geometry("%dx%d+%d+%d" % (w, h, x, y))  # place the window 'root'


def Test():
    def run_speed_test():

        Download.config(text="Loading")

        test = speedtest.Speedtest()
        servernames = []
        test.get_servers(servernames)
        data = test.get_config()

        service_data = data["client"]["isp"]
        ip_data = data["client"]["ip"]

        uploading = round(test.upload() / (1024 * 1024), 2)
        downloading = round(test.download() / (1024 * 1024), 2)

        # Update the labels with the test results
        ping.config(text=test.results.ping)
        upload.config(text=uploading)
        download.config(text=downloading)
        Download.config(text=downloading)
        service.config(text=service_data)
        ip.config(text=ip_data)
        root.update()

    # Start the speed test in a separate thread
    threading.Thread(target=run_speed_test).start()


def Check():
    # Loading.config(text = "Loading...")
    Test()


# #Set all data to 00
def Reset():
    ping.config(text="--")
    upload.config(text="--")
    download.config(text="--")

    Download.config(text="--")

    service.config(text="- - -")
    ip.config(text="- - - - - - - -")


# icon for window
image_icon = PhotoImage(file="./images/logo.png")
root.iconphoto(False, image_icon)

# Images for UI and buttons
Top = PhotoImage(file="./images/background.png")
Label(root, image=Top, bg="#141527").place(x=0, y=0)


Test_Image = PhotoImage(file="./images/button.png")
Test_Button = Button(
    root,
    image=Test_Image,
    bg="#141527",
    bd=0,
    activebackground="#141527",
    cursor="hand2",
    command=Check,
)
Test_Button.place(x=125, y=510)

Reset_Image = PhotoImage(file="./images/reset.png")
Reset_Button = Button(
    root,
    image=Reset_Image,
    bg="#141527",
    bd=0,
    activebackground="#141527",
    cursor="hand2",
    command=Reset,
)
Reset_Button.place(x=190, y=600)


# Labels to show values
ping = Label(root, text="--", font="arial 20", bg="#141527", fg="#e9b342")
ping.place(x=100, y=215, anchor="center")

download = Label(root, text="--", font="arial 20", bg="#141527", fg="#0cf107")
download.place(x=225, y=215, anchor="center")

upload = Label(root, text="--", font="arial 20", bg="#141527", fg="#e61c25")
upload.place(x=350, y=215, anchor="center")

Download = Label(root, text="--", font="arial 30", bg="#141527", fg="#00FFFF")
Download.place(x=225, y=430, anchor="center")

service = Label(root, text="- - -", font="arial 12", bg="#141527", fg="white")
service.place(x=55, y=590, anchor="center")

ip = Label(root, text="- - - - - - - -",
           font="arial 12", bg="#141527", fg="white")
ip.place(x=380, y=590, anchor="center")


root.mainloop()
