import tkinter as tk
import webbrowser as wb

root=tk.Tk()
root.title("GitHub User Search")

def navigate():
    s=e1.get()
    wb.open(f"https://github.com/search?q={s}&type=users")
    print("Navigating to:",s)
    
l1=tk.Label(root,text="Enter name of the GitHub user:",font=("Times New Roman",20),width=30)   
l1.grid()

e1=tk.Entry(root,font=("Times New Roman",25),bg="#b3d4ff",width=30)
e1.grid()

b1=tk.Button(root,text="Search", bg="yellow",activebackground="white",command=navigate)
b1.grid()

root.mainloop()
