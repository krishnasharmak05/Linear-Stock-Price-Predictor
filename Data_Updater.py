
import tkinter as tk
from tkinter import filedialog
import customtkinter as ctk
import os
import sys
import datetime
import webbrowser
from Ml import model_trainer


def get_file():
    """This function prompts the user to select a file using a file dialog.
    If the user does not select a file, it defaults to "IRFC.NS.csv".
    The function returns the selected file name or the default file name."""

    file_name = filedialog.askopenfilename()
    if not file_name:
        file_name = "IRFC.NS.csv"
    return file_name


update = False


def update_data():
    """
    A function to update data, which destroys an alert, opens a web browser to a specific URL, creates a Tkinter window to display information, and inserts text into the window.
    """
    alert.destroy()
    webbrowser.open("https://finance.yahoo.com/quote/IRFC.NS/history")
    info = tk.Tk()
    info.geometry("600x110")
    info.resizable(False, False)
    info.attributes("-topmost", True)
    text_in_alert = tk.Text(info, bg="black", fg="white", height=5, width=52)
    text = f"Click on the Download button and save the file to {excel_file_container_path} as IRFC.NS.csv"
    label = tk.Label(info)
    label.config(font=("Courier", 14))
    text_in_alert.pack()
    label.pack()
    text_in_alert.insert(tk.END, text)
    info.mainloop()


def request_update():
    """
    A function to request an update with a pop-up alert in the GUI.
    """
    print("Requesting update...")
    global alert
    global update
    update = True
    alert = ctk.CTk()
    alert.geometry("300x100")
    alert.resizable(False, False)
    alert.attributes("-topmost", True)
    alert.title("Update the data")
    text_in_alert = tk.Text(alert, bg="black", fg="white", height=5, width=52)
    text = f"Your data is outdated. Please click update for further instructions on updating it."
    label = tk.Label(alert)
    label.config(font=("Courier", 14))
    text_in_alert.pack()
    label.pack()
    text_in_alert.insert(tk.END, text)
    tk.Button(
        alert, text="Update Data", command=update_data
    ).pack()  # Read Yahoo Finance's Terms of Service and see if I can get the data automatically from there. Also, fix the UI of the button.
    alert.mainloop()


def update_checker():
    script_path = os.path.abspath(__file__)
    folder_path = os.path.dirname(script_path)
    sys.path.append(folder_path + r"\data")
    global excel_file_container_path
    excel_file_container_path = sys.path[-1]
    os.listdir(excel_file_container_path)
    global file
    file = os.path.join(excel_file_container_path, "IRFC.NS.csv")
    last_modified = datetime.datetime.fromtimestamp(os.path.getmtime(file)).date()
    print(last_modified)
    if str(last_modified) != str(datetime.date.today()):
        request_update()
        global update
        model_trainer(file, update)
    else:
        update = False

def accuracy():
    global scores
    scores = model_trainer(file, update)


# scores is unbound. Use an else condition also, for the above if condition. -- Test it. I think it's fixed.


if __name__ == "__main__":
    update_checker()
