import tkinter as tk
import webbrowser as wb

root = tk.Tk()
root.title("Instagram Enquiry Form")


l1 = tk.Label(root,text = "Name: ",font = ("Times New Roman",20),width = 10)
l1.grid()
l2 = tk.Label(root,text = "Email: ",font = ("Times New Roman",20))
l2.grid()
l3 = tk.Label(root,text = "Enquiry: ",font = ("Times New Roman",20))
l3.grid()

e1 = tk.Entry(root,font = ("Times New Roman",19))
e1.grid(row=0,column=3)
e2 = tk.Entry(root,font = ("Times New Roman",19))
e2.grid(row=1,column=3)
e3 = tk.Entry(root,font = ("Times New Roman",19))
e3.grid(row=2,column=3)


def getDetails():
    name = e1.get()
    email = e2.get()
    enq = e3.get()

    f = open("enquiries.txt","a")
    f.writelines(["Name: ",name,"\nEmail: ",email,"\nEnquiry: ",enq,"\n-------------\n"])
    url = "https://help.instagram.com/"
    wb.open(url)
    

b1 = tk.Button(root,text = "Submit",command = getDetails,activebackground = "cyan")
b1.grid(row=5,column=3)


root.mainloop()