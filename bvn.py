import tkinter as tk
import requests, json

HEIGHT = 500
WIDTH = 600


# def search(entry):
#     print('this is the entry form', entry)

def validate(entry):
    """
     validate the arg passed to the function validate
     test_key = 'sk_test_8549721191670666fc4e554f71ccaf5f939c9f10'
    """
    new = int(entry)
    url = 'https://api.paystack.co/bank/resolve_bvn/' 
    #entry={BVN}
    payload = { 'q':new }
    files = { 'q':new}
    headers = {
        'Authorization': 'Bearer sk_test_8549721191670666fc4e554f71ccaf5f939c9f10', 
        
    }

    response = requests.get( url, headers=headers, data = payload, files = files)
    print(response)

root = tk.Tk()
canvas = tk.Canvas(root, height=HEIGHT, width = WIDTH)
canvas.pack()
frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')



entry = tk.Entry(frame, bg='white')
entry.place(relwidth=0.65, relheight=1)



button = tk.Button(frame, text='Search', font=40, command=lambda: validate(entry.get()))
button.place(relx=0.7,  relwidth=0.3, relheight=1)


lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
