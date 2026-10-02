import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk

class main:
    def window(self, root):
        self.root = root
        self.root.title("Генератор QR-кодов")
        self.root.geometry("360x450")
        
        tk.Label(root, text="Введите ссылку на сайт:", font=("Arial", 12)).pack(pady=10)
        self.entry = tk.Entry(root, width=35, font=("Arial", 11))
        self.entry.pack(pady=5)
        self.entry.insert(0, "https://")
        tk.Button(root, text="Сгенерировать QR-код", font=("Arial", 11, "bold"), 
                  bg="#2196F3", fg="white", command=self.generate_qr).pack(pady=10)
        self.qr_label = tk.Label(root, bg="white")
        self.qr_label.pack(pady=10)

    def generate_qr(self):
        link = self.entry.get().strip()
        if not link or link == "https://":
            messagebox.showwarning("Ошибка", "Введите корректную ссылку!")
            return
        qr = qrcode.QRCode(version=1, box_size=8, border=2)
        qr.add_data(link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        self.photo = ImageTk.PhotoImage(img)
        self.qr_label.config(image=self.photo)

root = tk.Tk()
app = main()
app.window(root)
root.mainloop()
