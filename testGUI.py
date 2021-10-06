from tkinter import *
from tkinter import font
from tkinter import filedialog

class GUI():
  def __init__(self):
    #create a window
    window = Tk()
    window.withdraw()

    login = Toplevel()
    login.title("Login chatroom")
    #Create login label
    loginLbl = Label(login, text="Enter your name to login",font=("Arial",20))
    loginLbl.grid(column=0, row=0)
    
    
    #Tao input cho ten user
    nameInp = Entry(login,width=50)
    nameInp.grid(column=0,row=2,padx=20)

    nameInp.focus()
    def enterChatroom():
      name = nameInp.get()
      layout(name)
    def layout(name):
      login.destroy()
      window.deiconify()
      window.title("Chatroom application")

      #Hien thi ten user
      labelHead = Label(window,
                               bg="#17202A",
                               fg="#EAECEE",
                               text=name,
                               font="Helvetica 13 bold",
                               pady=5)
      #Chieu rong co gia tri trong khoang 0.0 -> 1.0
      labelHead.place(relwidth=1)
      
      textCons = Text(window,
                      width=20,
                      height=2,
                      bg="#17202A",
                      fg="#EAECEE",
                      font="Helvetica 14",
                      padx=5,
                      pady=5)

      textCons.place(relheight=0.745,
                            relwidth=0.75,
                            rely=0.08)
      usersOnl = Label(window,
                      width=20,
                      height=2,
                      bg="#17202A",
                      fg="#EAECEE",
                      font="Helvetica 14",
                      padx=5,
                      pady=5)

      usersOnl.place(relheight=0.745,
                            relwidth=0.25,
                            rely=0.08,relx=0.75)
      usersOnl.configure(text="Online users\nUser1\nUser2\nUser3\nUser4")
      labelBottom = Label(window,
                                 bg="#ABB2B9",
                                 height=80)

      labelBottom.place(relwidth=1,
                               rely=0.825)

      self.entryMsg = Entry(labelBottom,
                              bg="#2C3E50",
                              fg="#EAECEE",
                              font="Helvetica 13")

        # place the given widget
        # into the gui window
      self.entryMsg.place(relwidth=0.75,
                            relheight=0.12,
                            rely=0.008,
                            relx=0)

      self.entryMsg.focus()
      # create a Send Button
      self.buttonMsg = Button(labelBottom,
                              text="Send",
                              font="Helvetica 10 bold",
                              width=20,
                              bg="#ABB2B9",
                              command=lambda: self.sendButton(self.entryMsg.get()))

      self.buttonMsg.place(relx=0.77,
                            rely=0.008,
                            relheight=0.06,
                            relwidth=0.22)
      # create a file Button
      self.fileBtn = Button(labelBottom,
                              text="File",
                              font="Helvetica 10 bold",
                              width=20,
                              bg="#cccccc",
                              command=UploadAction)

      self.fileBtn.place(relx=0.77,
                            rely=0.075,
                            relheight=0.06,
                            relwidth=0.22)


      textCons.config(cursor="arrow")
      

        # create a scroll bar
      scrollbar = Scrollbar(textCons)
    def UploadAction(event=None):
      filename = filedialog.askopenfilename()
      print('Selected:', filename)
    #Create button
    btnHello = Button(login, text="Enter chatroom", command=enterChatroom)
    btnHello.grid(row=4,column=0,padx=20, pady=20)

    window.mainloop()
g = GUI()