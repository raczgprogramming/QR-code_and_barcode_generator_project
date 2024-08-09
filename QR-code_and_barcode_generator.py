import qrcode
import tkinter as tk
from datetime import datetime
import barcode
from barcode.writer import ImageWriter
import qrcode.constants


def generating_barcode():
    try:
        now_time1 = datetime.now()
        bdata = input_value.get()
        bcode = barcode.get("code128", bdata, writer=ImageWriter())
        time1 = now_time1.strftime("%Y%m%d%H%M%S")
        filename = bcode.save(f"barcode{time1}")
        return filename
    except barcode.errors.IllegalCharacterError as ICE:
        message_label.config(text="Nem engedélyezett karaktert használtál!", bg="red")
        mainwindow.after(5000,reset_message)
        print(ICE)

    except Exception as EX:
        message_label.config(text="Ismeretlen hiba történt!", bg="red")
        mainwindow.after(5000,reset_message)
        print(EX)



def generating_qrcode():
    try:
        now_time2 = datetime.now()
        qdata = input_value.get()
        qcode = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
        qcode.add_data(qdata)
        qcode.make(fit=True)
        img = qcode.make_image(fill_color="black", back_color="white")
        time2 = now_time2.strftime("%Y%m%d%H%M%S")
        filename = f"qrcode{time2}.png"
        img.save(filename)
        return filename
    except Exception as EX:
        message_label.config(text="Ismeretlen hiba történt!", bg="red")
        mainwindow.after(5000,reset_message)
        print(EX)

def reset_message():
    message_label.config(text="Szia! Legyen szép napod", bg="lightgreen")

mainwindow = tk.Tk()
mainwindow.title("QR-code and Barcode generator")

window_w = 400
window_h = 250
screen_w = mainwindow.winfo_screenwidth()
screen_h = mainwindow.winfo_screenheight()
x_pos = (screen_w // 2) - (window_w // 2)
y_pos = (screen_h // 2) - (window_h // 2)
mainwindow.geometry(f"{window_w}x{window_h}+{x_pos}+{y_pos}")

message_label = tk.Label(mainwindow, width=50, text="Szia! Legyen szép napod", bg="lightgreen")
message_label.pack(pady=10)

input_value = tk.Entry(mainwindow, width=50)
input_value.pack(pady=10)

barcode_button = tk.Button(mainwindow, text="Barcode generálás", command=generating_barcode)
barcode_button.pack(pady=10)

qrcode_button = tk.Button(mainwindow, text="QR-code generálás", command=generating_qrcode)
qrcode_button.pack(pady=10)

exit_button = tk.Button(mainwindow, text="Bezárás", command=mainwindow.destroy)
exit_button.pack(pady=10)

mainwindow.mainloop()