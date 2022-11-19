import tkinter as tk  # Tkintet 를 이용해서 GUI를 만들어 냄
import PyPDF2 # pdf에서 데이터 불러오는 기능
from PIL import Image, ImageTk # 이미지 삽입
from tkinter.filedialog import askopenfile # 파일 열기
import test # 만든 모듈 불러오기

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to extract all its text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:test.open_file(browse_text, root), font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

#extract button
if test.open_file(browse_text, root):
    write_text = tk.StringVar()
    extract_btn = tk.Button(root, textvariable=write_text, command=lambda:test.open_file(write_text, root), font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
    fileSelect_btn = tk.Button(root, textvariable=write_text, command=lambda:test.open_file(browse_text, root), font="Raleway", bg="#20bebe", fg="black", height=2, width=15)
    write_text.set("Extracting")
    extract_btn.grid(column=1, row=4)
fileSelect_btn.grid(column=1, row=5)



root.mainloop()