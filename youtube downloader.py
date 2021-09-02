from tkinter import *
page=Tk()
page.geometry("600x400")

a = Label(page,text="Enter URL").place(x=70,y=70)
c = Entry(page,width=80).place(x=160,y=80)
b = Button(page,text="Download").place(x=150,y=180)

page.mainloop()


# pip install pafy
#pip install youtube_dl
import pafy

from tkinter import *

def getMetaData(video):
    print("Video Details are ---")
    print("video title : ",video.title)  #print title
    # print view count
    # print(f"Total views : {video.viewcount}| video lenght : {video.lengh} secounds")
    print("channel name : ",video.author) #print author

def download_As_video(video):
    getMetaData(video) #get video details
    best= video.getbest()
    print(f"Video Resolution:{best.resolution}\n video extension:{best.extension}")
    best.download()#download the video
    print("Video is downloaded...")
#
# # if __name__ == "__main__":
# url = input("Enter video url : ")
# #create instance
# video = pafy.new(url)
# download_As_video(video)
def fn():
    url=textbox.get()
    video = pafy.new(url)
    download_As_video(video)
#     print(textbox.get())

frame=Tk()

frame.geometry("800x500")
textbox = Label(frame,text="Enter URL").place(x=70,y=80)
textbox = Entry(frame,width="80",textvariable="textbox")
textbox.place(x=150,y=80)

btn = Button(frame,text="submit",command=fn).place(x=160,y=150)
frame.mainloop()



