# Name = Mohd Shan
# Email-id = mohdshane@iul.ac.in



from tkinter import *
from tkinter import ttk
Converter = Tk()
Converter.geometry("600x400")
Converter.title("Currency Converter")
Converter.wm_iconbitmap("CC_icon.ico")
OPTIONS = {
    "Afghan Afghani":0.94,
    "Armenian Dram":0.14,
    "Pakistani Rupee":0.49,
    "Sri Lankan Rupee":0.37,
    "Bahraini Dinar":197.23,
    "Saudi Arabian Riyal":19.83,
    "Emirati Dirham":20,
    "Iraqi Dinar":0.062,
    "Iranian Rial": 0.0018,
    "Kuwaiti Dinar":246.22,
    "Qatari Riyal":20.42,
    "Russian Ruble":0.97,
    "Swiss Franc":80.06,
    "United States Dollar":74.35,
    "Canadian Dollar":58.97,
    "Jamaican Dollar":0.51,
    "South African Rand":5.11,
    "Egyptian Pound":4.72,
    "Australian Dollar":56.73,
    "New Zealand Dollar":52.25,
    "Kenyan Shilling":0.69,
    "Turkish Lira":9.10,
    "Japanese Yen":0.68,
    "Chinese Yuan":11.35

}

def ok():
    price = rupees.get()
    answer = variable.get()
    dict = OPTIONS.get(answer,None)
    converted = float(dict)*float(price)
    result.delete(1.0 ,END)
    result.insert(INSERT,"price in ",INSERT, answer, INSERT," = ", INSERT, converted)
app = Label(Converter,text = "Currrency",
            font = ("arial",25,"bold","underline"),fg = "dark red")
app.grid(row = 0 ,column = 0, padx = 10 )

app = Label(Converter,text = "Converter",
            font = ("arial",25,"bold","underline"),fg = "dark red")
app.grid(row = 0 ,column = 1,ipadx = 10)
result = Text(Converter, height = 5 , width = 50 , font = ("arial",10,"bold","underline"),bd = 5)
result.grid(row = 1 ,columnspan =10,padx = 3)

india = Label(Converter,text = "Indian Rupees: ",
            font = ("arial",10,"bold","underline"),fg = "red")
india.grid(row = 2, column = 0)
rupees = Entry(Converter, font=("Calibri",20))
rupees.grid(row = 2,column = 1)
choice = Label(Converter,text = "Choose Country: ",
            font = ("arial",10,"bold","underline"),fg = "red")
choice.grid(row = 3, column = 0)
variable = StringVar(Converter)
variable.set(None)
option = OptionMenu(Converter,variable,*OPTIONS)
option.grid(row = 3, column = 1 , sticky = "ew")
button = Button(Converter,text = "Convert",fg = "green",
                font=("Calibri",20),bg = "powder blue",command = ok)
button.grid(row = 3 , column = 2)
mainloop()