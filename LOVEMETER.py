import tkinter as tk

def ClickedButon():
  name1 = entry1.get()
  name2 = entry2.get()
  love_score = len(set(name1.lower() + name2.lower())) * 10
  result_label.config(text=f"Aşk Skorunuz: {love_score}%")
  
form = tk.Tk()
form.title('LOVE METER')
form.geometry('400x400+50+100')
form.configure(bg='violet')

label =tk.Label(form,text='LOVE TESTER',fg='blue',bg='purple',font='Times 20 italic bold')
label.pack()

entry1 = tk.Entry(form,bg='purple',show='*')
entry1.pack()

entry2 = tk.Entry(form,bg='purple',show='*')
entry2.pack()

button = tk.Button(form, text="Buton", command=ClickedButon,bg='pink')
button.pack()

result_label = tk.Label(form, text="")
result_label.pack()

label=tk.Label(form,text='Adınızı yazıp butona basın',fg='blue',bg='purple',font='Times 20 italic bold')
label.pack()

