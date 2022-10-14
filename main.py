import tkinter
from tkinter import ttk
from tkinter import filedialog as fd


app = tkinter.Tk()
app.title('Teste')
app.resizable(False, False)
app.geometry('800x600')

text = tkinter.Text(app, height=12)
text.grid(column=0, row=0, sticky='nsew')

def open_text_file():
    filetypes = (
        ('text files', '*.pdf')
    )

    file = fd.askopenfile(filetypes=filetypes)
    filename = file.name
    text.insert('1.0', filename)

open_button = ttk.Button(
    app,
    text = 'Open a File',
    command = open_text_file
)

open_button.grid(column=0, row=1, sticky='w', padx=10, pady=10)

app.mainloop()

