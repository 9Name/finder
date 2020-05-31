from tkinter import *
import tkinter as tk
from tkinter import messagebox
from bs4 import BeautifulSoup as bs
import requests as rq
from urllib.request import urlopen
from PIL import ImageTk, Image
from io import BytesIO
import io

root = tk.Tk()
root.geometry('600x400')
root.attributes("-zoomed",True)
root.resizable(True, True)
''' left frame'''
left = Frame(root,  relief="flat",bg ="mint cream")

left1 = tk.Canvas(left, width = 1000, height = 70, relief="flat",bg ="mint cream",highlightthickness=0)
left1.pack()



left1.create_text(500, 25, text='WELCOME TO USERNAME FINDER',anchor=N,font = "helvetica 20",fill="brown")

left2 = tk.Canvas(left, width = 400, height = 200, relief="flat",bg ="mint cream",highlightthickness=0)
left2.pack()

left2.create_text(200, 10, text='Search Codechef Username',anchor=N,font = "helvetica 20",fill="blue")

left2.create_text(200, 70, text='Type Username',anchor=N,font = "helvetica 15",fill = "green")

entry1 = tk.Entry (root,width="35")
left2.create_window(200, 120, window=entry1)


left3 = tk.Canvas(left, width = 1170, height = 55,  relief="flat",bg ="mint cream",highlightthickness=0)
left3.pack()
left4 = tk.Canvas(left, width = 1170, height = 55,  relief="flat",bg ="mint cream",highlightthickness=0)
left4.pack()
left5 = tk.Canvas(left, width = 1170, height = 55,  relief="flat",bg ="mint cream",highlightthickness=0)
left5.pack()
left6 = tk.Canvas(left, width = 1170, height = 55,  relief="flat",bg ="mint cream",highlightthickness=0)
left6.pack()
left7 = tk.Canvas(left, width = 1170, height = 55,  relief="flat",bg ="mint cream",highlightthickness=0)
left7.pack()
left8 = tk.Canvas(left, width = 1170, height = 55,  relief="flat",bg ="mint cream",highlightthickness=0)
left8.pack()

left9 = tk.Canvas(left, width = 1170, height = 55,  relief="flat",bg ="mint cream",highlightthickness=0)
left9.pack()

left10 = tk.Canvas(left, width = 1170, height = 55,  relief="flat",bg ="mint cream",highlightthickness=0)
left10.pack()

left11 = tk.Canvas(left, width = 1170, height = 55,  relief="flat",bg ="mint cream",highlightthickness=0)
left11.pack()



'''Right Frame'''
right = Frame(root,  relief="flat",bg ="mint cream",highlightthickness=0)

right1 = tk.Canvas(right, width = 300, height = 280, relief="flat",bg ="mint cream",highlightthickness=0)
right1.pack()

right10 = tk.Canvas(right, width = 400, height = 50, relief="flat",bg ="mint cream",highlightthickness=0)
right10.pack()

right2 = tk.Canvas(right, width = 400, height = 50,  relief="flat",bg ="mint cream",highlightthickness=0,)
right2.pack()

right3 = tk.Canvas(right, width = 400, height = 50,  relief="flat",bg ="mint cream",highlightthickness=0)
right3.pack()


right4 = tk.Canvas(right, width = 400, height = 50,  relief="flat",bg ="mint cream",highlightthickness=0)
right4.pack()

right5 = tk.Canvas(right, width = 400, height = 50,  relief="flat",bg ="mint cream",highlightthickness=0)
right5.pack()

right6 = tk.Canvas(right, width = 400, height = 50, relief="flat",bg ="mint cream",highlightthickness=0)
right6.pack()


right7 = tk.Canvas(right, width = 400, height = 50,  relief="flat",bg ="mint cream",highlightthickness=0)
right7.pack()

right8 = tk.Canvas(right, width = 400, height = 50,  relief="flat",bg ="mint cream",highlightthickness=0)
right8.pack()


right9 = tk.Canvas(right, width = 400, height = 50,  relief="flat",bg ="mint cream",highlightthickness=0)
right9.pack()

left.pack(side="left", expand=True, fill="both")
right.pack(side="right", expand=True, fill="both")

''' Working Start from here '''

def is_internet_available():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return True
    except:
        return False


def userdata():
    if is_internet_available()==True:
        try:

            x1 = entry1.get()
            url = "https://www.codechef.com/users/"+x1

            page = rq.get(url)
            soup = bs(page.content, 'html5lib')
            infoTag = soup.find('section', attrs = {'class':'user-details'})
            inf = soup.find('main', attrs = {'class':'content'})
            a = inf.contents[1].contents[1].contents[1]
            name = infoTag.contents[1].contents[1].text
            info = soup.find('ul', attrs = {'class':'side-nav'})
            rows = info.find_all('label')
            cols = info.find_all('li')
            k = []
            for y in rows:
                h = []
                if y.text!="Teams List:":
                    h.append(y.text)
                    k.append(h)
                    h = []

            for y in range(len(k)):
                k[y].insert(1,cols[y].span.text)
            for x in range(len(k)):
                k[x][1] = k[x][1].replace("\xa0","")
            #h = infoTag.contents[1].contents[15].text
            name = name.split(":")
            name[0] = name[0].strip()
            name[1] = name[1].strip()
            st = 0
            if name[1][0] == x1[0]:
                st = int(1)
            else:
                st = int(name[1][0])


            a = a.replace("»","")


            left3.delete("all")
            left3.create_text(20, 30, text="Name"+":",anchor=W,font = "Times 13 italic bold")
            left3.create_text(242, 30, text=a,anchor=W,font = "Times 13 italic bold")

            left4.delete("all")
            left4.create_text(20, 30, text=k[0][0],font = "Times 13 italic bold",anchor=W)
            left4.create_text(250, 30, text=k[0][1],font = "Times 13 italic bold",anchor=W)

            left5.delete("all")
            left5.create_text(20, 30, text=k[1][0],font = "Times 13 italic bold",anchor=W)
            left5.create_text(250, 30, text=k[1][1],font = "Times 13 italic bold",anchor=W)

            left6.delete("all")
            left6.create_text(20, 30, text=k[2][0],font = "Times 13 italic bold",anchor=W)
            left6.create_text(250, 30, text=k[2][1],font = "Times 13 italic bold",anchor=W)

            left7.delete("all")
            left7.create_text(20, 30, text=k[3][0],font = "Times 13 italic bold",anchor=W)
            left7.create_text(250, 30, text=k[3][1],font = "Times 13 italic bold",anchor=W)

            left8.delete("all")
            left8.create_text(20, 30, text=k[4][0],font = "Times 13 italic bold",anchor=W)
            left8.create_text(250, 30, text=k[4][1],font = "Times 13 italic bold",anchor=W)
            if len(k)>=6:

                left9.delete("all")
                left9.create_text(20, 30, text=k[5][0],font = "Times 13 italic bold",anchor=W)
                left9.create_text(250, 30, text=k[5][1],font = "Times 13 italic bold",anchor=W)
            else:
                left9.delete("all")
                left9.create_text(20, 30, text="",font = "Times 13 italic bold",anchor=W)
            if len(k)>=7:
                left10.delete("all")
                left10.create_text(20, 30, text=k[6][0],font = "Times 13 italic bold",anchor=W)
                left10.create_text(250, 30, text=k[6][1],font = "Times 13 italic bold",anchor=W)
            else:
                left10.delete("all")
                left10.create_text(20, 30, text="",font = "Times 13 italic bold",anchor=W)

            if len(k)>=8:
                left11.delete("all")
                left11.create_text(20, 30, text=k[7][0],font = "Times 13 italic bold",anchor=W)
                left11.create_text(250, 30, text=k[7][1],font = "Times 13 italic bold",anchor=W)
            else:
                left11.delete("all")
                left11.create_text(20, 30, text="",font = "Times 13 italic bold",anchor=W)


            ''' Working of right hand frame'''





            infoTagi = soup.find('div', attrs = {'class':'user-details-container plr10'})
            image1 = infoTagi.header.img.attrs["src"]
            if image1[0]=="/":
                image1 = "https://www.codechef.com"+image1



            # size of image display box you want
            w_box = 300
            h_box = 275






            # find yourself a picture on an internet web page you like
            # (right click on the picture, under properties copy the address)
            # a larger (1600 x 1200) picture from the internet

            image_bytes = rq.get(image1)
            # internal data file
            data_stream = io.BytesIO(image_bytes.content)
            # open as a PIL image object
            pil_image = Image.open(data_stream)
            w, h = pil_image.size
            f1 = 1.0*w_box/w  # 1.0 forces float division in Python2
            f2 = 1.0*h_box/h
            factor = min([f1, f2])
            #print(f1, f2, factor)  # test
            # use best down-sizing filter
            width = int(w*factor)
            height = int(h*factor)
            pil_image_resized = pil_image.resize((width, height), Image.ANTIALIAS)

            # optionally show resized image info ...
            # get the size of the resized image
            wr, hr = pil_image_resized.size
            tk_image = ImageTk.PhotoImage(pil_image_resized)
            # put the image on a widget the size of the specified display box
            label1 = tk.Label(right, image=tk_image, width=w_box, height=h_box,highlightthickness=0,bg = "mint cream")
            right1.create_window(158,152,window = label1)

            ''' right bottom work '''

            infoTag = soup.find('div', attrs = {'class':'user-details-container plr10'})
            infoTag1 = soup.find('aside', attrs = {'class':'sidebar small-4 columns pr0'})
            Rate = infoTag1.div.div.div.div.text
            star = infoTag1.div.span.text
            high = infoTag1.div.small.text
            glob = infoTag1.div.ul.li.strong.text
            infoTag1 = soup.find('div', attrs = {'class':'rating-ranks'})
            glob1 = infoTag1.text
            glob1 = glob1.split()
            country = glob1[-3]
            #h = infoTag.contents[1].contents[15].text

            infoTag3 = soup.find('section', attrs = {'class':'rating-data-section problems-solved'})
            Q = infoTag3.contents[3].contents[1].text
            q1 = Q.split()
            #h = infoTag.contents[1].contents[15].text

            q = q1[-1].replace("(","").replace(")","")
            high = high.replace("(","").replace(")","")
            high = high.split()

            st1 = st* star

            col = "seashell3"
            if st==2:
                col = "dark green"
            if st==3:
                col = "medium blue"
            if st==4:
                col = "Slate Blue2"

            if st==5:
                col = "yellow"
            if st==6:
                col = "orange"

            if st==7:
                col = "red"
            right10.delete("all")
            right10.create_text(200, 15, text=st1,anchor=N,font = "Times 25 italic bold",fill=col)



            right2.delete("all")
            right2.create_text(200,22,text = "Codechef Rating",font = "Times 13 italic bold",anchor=N)

            right3.delete("all")
            right3.create_text(200,22,text = Rate,font = "Times 13 italic bold",anchor = N)

            right4.delete("all")
            right4.create_text(200,22,text = "Heighest Rating",font = "Times 13 italic bold",anchor = N)

            right5.delete("all")
            right5.create_text(200,22,text = high[-1],font = "Times 13 italic bold",anchor = N)

            right6.delete("all")
            right6.create_text(200,22,text = "Country Rank"+"  "+"Global Rank",font = "Times 13 italic bold",anchor = N)


            right7.delete("all")
            right7.create_text(200,22,text = country+" "+"  "+glob,font = "Times 13 italic bold",anchor = N)



            right8.delete("all")
            right8.create_text(200,22,text = "Problems Solved",font = "Times 13 italic bold",anchor = N)

            right9.delete("all")
            right9.create_text(200,22,text = q ,font = "Times 13 italic bold",anchor = N)

            root.mainloop()
        except:
            messagebox.showinfo("USERNAME",x1+" "+ "Is Not Available")
    else:
        messagebox.showerror("Network problem","check your internet connection")

button1 = tk.Button(text='search',command=userdata ,bg='brown', fg='white', font=('helvetica', 9, 'bold'))
left2.create_window(200, 180, window=button1)
root.mainloop()
