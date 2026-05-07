from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

# Window setup
root = Tk()
root.title("CCSU Mobile App")
root.geometry("600x550")
root.resizable(0, 0)
root.configure(bg="#5f86a0")   # darker blue

# Show logo
img = Image.open("logo.png")

try:
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100, 100), Image.ANTIALIAS)

img = img.convert("RGBA")
data_img = img.getdata()
newData = []

for item in data_img:
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("transparent.png")

logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)

logoLabel = Label(root, image=logo, bg="#5f86a0")
logoLabel.place(x=10, y=10)

# Read CSV file
data = pd.read_csv("examfile.csv")

# Output label
lb = Label(root, text="", justify="left", bg="#5f86a0", anchor="w", fg="white")
lb.place(x=120, y=190)

# Functions
def calendar():
    df = pd.DataFrame(data, columns=["CalendarDate"])
    selected_rows = df[~df["CalendarDate"].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

def buildings():
    df = pd.DataFrame(data, columns=["Buildings"])
    selected_rows = df[~df["Buildings"].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

def faculty():
    df = pd.DataFrame(data, columns=["FacultyName"])
    selected_rows = df[~df["FacultyName"].isnull()]
    lb.config(text=selected_rows.to_string(index=False))

def school_business():
    lb.config(text="School of Business\n\nAccounting\nFinance\nManagement & Organization\nMarketing\nManagement Information Systems (MIS)\nBusiness Analytics")

def mis_department():
    lb.config(text="MIS Department\n\nIntro to MIS\nDatabases Management\nSystems Analysis & Design\nBusiness Analytics / Data Visualization\nNetwork and Information Security\nProject Management")

# Buttons (blue style, Mac-safe)
button1 = Button(root, text="Calendar", command=calendar, bg="#003366")
button1.place(x=30, y=120)

button2 = Button(root, text="Buildings", command=buildings, bg="#003366")
button2.place(x=130, y=120)

button3 = Button(root, text="Faculty", command=faculty, bg="#003366")
button3.place(x=240, y=120)

button4 = Button(root, text="School of Business", command=school_business, bg="#003366")
button4.place(x=40, y=155)

button5 = Button(root, text="MIS Department", command=mis_department, bg="#003366")
button5.place(x=230, y=155)

root.mainloop()
