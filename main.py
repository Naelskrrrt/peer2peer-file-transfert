from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

fontFamily = 'Acumin Variable Concept'

root=Tk()
root.title("Shareit")
root.geometry("450x560+500+200")
root.configure(bg="#f4fdfe")
root.resizable(False,False)

def Send():
    window=Toplevel(root)
    window.title("Send")
    window.geometry("450x560+500+200")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)
    
    def select_file():
        global filename
        filename=filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image File', filetype=(('file_type', '*.txt'),('all files', '*.*')))
        
    def sender():
        s=socket.socket()
        host=socket.gethostname()
        port=8080
        s.bind((host, port))
        s.listen(1)
        print(host)
        print('Waiting for any incoming connections...')
        conn, addr=s.accept()
        file=open(filename, "rb")
        file_data=file.read(1024)
        conn.send(file_data)
        print('Data has been transmited succesfully')  
              
    #icon
    image_icon1=PhotoImage(file="image/send.png")
    window.iconphoto(False, image_icon1)
    
    # Sbackground=PhotoImage(file="image/sender.png")
    # Label(window,image=Sbackground).place(x=-2, y=0)
    
    # Mbackground=PhotoImage(file="image/id.png")
    # Label(window, image=Mbackground, bg="#f4fdfe").place(x=100, y=260)
    
    host=socket.gethostname()
    
    Label(window, text=f'ID: {host}', bg='#fff', fg='#000').place(x=140, y=290)
    
    Button(window,text="+ select file", width=10, height=1, font='arial 14 bold', bg='#fff', fg='#000', command=select_file).place(x=160, y=150)
    Button(window, text='SEND', width=8, height=1, font='arial 14 bold', bg='#000', fg='#fff', command=sender).place(x=300, y=150)
    
    window.mainloop()
    
def Receive():
    main=Toplevel(root)
    main.title("Receive")
    main.geometry("450x560+500+200")
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)
    
    #icon
    image_icon2=PhotoImage(file="image/receive.png")
    main.iconphoto(False, image_icon2)
    
    main.mainloop()

#icon
image_icon=PhotoImage(file="image/icon.png")
root.iconphoto(False, image_icon)

Label(root, text="File Tranfert", font=(fontFamily, 20, 'bold'), bg="#f4fdfe").place(x=20, y=30)

Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

send_image=PhotoImage(file="image/send.png")
send=Button(root, image=send_image, bg="#f4fdfe", bd=0, command=Send)
send.place(x=50, y=100)

receive_image=PhotoImage(file="image/receive.png")
receive=Button(root, image=receive_image, bg="#f4fdfe", bd=0, command=Receive)
receive.place(x=300, y=100)

# label
Label(root, text="Send", font=(fontFamily, 17, 'bold'), bg='#f4fdfe').place(x=55, y=170)
Label(root, text="Receive", font=(fontFamily, 17, 'bold'), bg='#f4fdfe').place(x=290, y=170)


# background=PhotoImage(file="image/background.jpg")
# Label(root, image=background).place(x=-2, y=323)





root.mainloop()