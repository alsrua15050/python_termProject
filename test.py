import tkinter as tk  # Tkintet 를 이용해서 GUI를 만들어 냄
import PyPDF2 # pdf에서 데이터 불러오는 기능
from PIL import Image, ImageTk # 이미지 삽입
from tkinter.filedialog import askopenfile # 파일 열기

#파일 입출력 설정
class Interface:
    def __init__(self, file_name, text):
        self.file_name = file_name
        self.text = text
    def write_file(self):
        with open(self.file_name, "w") as file:
            contents = file.write(self.text)
        print(file)

def open_file(browse_text, root):
    browse_text.set("loading...")
    file = askopenfile(parent=root, mode='rb', title="Choose a file", filetypes=[("Pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        #text box
        text_box = tk.Text(root, height=10, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")
        return True
    else:
        return False