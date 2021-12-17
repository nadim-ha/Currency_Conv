from tkinter import Tk, Radiobutton, Button, Label, StringVar, Entry

class Currencyconv():
        def __init__(self):
            window = Tk()
            window.title("Currency Converter App")
            window.configure(background="Gray")
            window.geometry("350x250")
            window.resizable(width=False,height=False)

            self.amount_to_convert = StringVar()
            self.Conversion_rate = StringVar()
            self.Converted_amount = StringVar()

            amount_to_convert_label = Label(window,text ="Amount to convert",bg="Gray",fg="black")
            amount_to_convert_label.grid(column=0,row=0,padx=15,pady=20)

            amount_to_convert_entry= Entry(window,textvariable = self.amount_to_convert,width=14)
            amount_to_convert_entry.grid(column=1,row=0,padx=15,pady=20)

            Conversion_rate_label = Label(window,text ="Conversion rate",bg="Gray",fg="black")
            Conversion_rate_label.grid(column=0,row=1,padx=15,pady=20)

            Conversion_rate_entry= Entry(window,textvariable = self.Conversion_rate,width=14)
            Conversion_rate_entry.grid(column=1,row=1,padx=15,pady=20)

            Converted_amount_label = Label(window,text ="Converted amount",bg="Gray",fg="black")
            Converted_amount_label.grid(column=0,row=2,padx=15,pady=20)

            Converted_amount_entry= Entry(window,textvariable = self.Converted_amount,width=14)
            Converted_amount_entry.grid(column=1,row=2,padx=15,pady=20)

            Convert_button = Button(window,text="Convert",bg="black",fg="white",command=self.Convert_fn)
            Convert_button.grid(column=0,row=3,padx=15,pady=20)

            Clear_button = Button(window,text="Clear",bg="white",fg="black",command=self.Clear)
            Clear_button.grid(column=1,row=3,padx=15,pady=20)

            window.mainloop()

        def Convert_fn(self):
            amount_value = float(self.amount_to_convert.get())
            Conversion_rate_value = float(self.Conversion_rate.get())
            Converted_amount_value = amount_value * Conversion_rate_value
            self.Converted_amount.set("%.3f" % Converted_amount_value)

        def Clear(self):
            self.amount_to_convert.set("")
            self.Conversion_rate.set("")
            self.Converted_amount.set("")

Currencyconv()
