import tkinter as tk
import math

try:
    import tkinter as tk
    from tkinter import StringVar, IntVar, ttk
    import matplotlib.pyplot as plt
    import numpy as np

except ImportError:
    from subprocess import call
    from tkinter import StringVar, ttk, Tk

    def download():
        text_var.set("Der Download beginnt...")
        fenster.update()
        call("curl https://bootstrap.pypa.io/get-pip.py -o get -pip.py")
        call("python -m pip install -I pip")
        call("pip install matplotlib")
        call("pip install numpy")
        # call("pip install ttkthemes")
        text_var.set("Download abgeschlossen.")
        fenster.update()
        fenster.after(5000,fenster.destroy)

    fenster = Tk()
    fenster.config(bg="#3b3b3b")
    text_var = StringVar()
    text_var.set("Fehlende Daten downloaden?")
    ttk.Label(fenster,textvariable=text_var).grid(column=0,row=0,pady=4,padx=4)
    ttk.Button(fenster,text="Download",command=download).grid(column=0,row=1,pady=4,padx=4)

def ft():
    
### Quadratische Formel Fenster ###    
    
    def qf():
        def loesen():
            
            labelErgebnis = tk.Label(master=framel, text="")
            labelErgebnis.pack(side="right", padx=5, pady=5)
            labelErgebnis2 = tk.Label(master=framel2, text="")
            labelErgebnis2.pack(side="right", padx=5, pady=5)
            labelE2 = tk.Label(master=framel2, text="Nst. x2:", bg="#3b3b3b", fg="white")
            labelE2.pack(padx=5, pady=5)
            label = tk.Label(master=framel, text="Nst. x1:", bg="#3b3b3b", fg="white")
            label.pack(padx=5, pady=5)
            
            try:                
                a = int(entry1.get())
                b = int(entry2.get())
                c = int(entry3.get())
                
                ### Nullstelle ###
                
                x1 = (-b-math.sqrt(b**2-4*a*c)) / (2*a)
                x1 = round(x1, 2)
                x2 = (-b+math.sqrt(b**2-4*a*c)) / (2*a)
                x2 = round(x2, 2)
                labelErgebnis.config(text=str(x1))
                labelErgebnis2.config(text=str(x2))
                
                ### Symetrie ###
                
                
                ### Bildung Graph ###
                x = np.linspace(-5,5,60)
                y = a*x**2+b*x+c
                
                plt.xlabel("x-Achse")
                plt.ylabel("y-Achse")
                plt.title(str(a) + "x^2 +" + str(b) + "x +" + str(c))
                plt.grid(True)
                plt.plot(x,y)
                plt.show()
                
            except ValueError:
                labelErgebnis.config(text="Fehler, Ungültige Werte")
                labelErgebnis2.config(text="Fehler, Ungültige Werte")
        def back_qf():
            window_ft.deiconify()
            window_qf.destroy()
        
        window_qf = tk.Toplevel(window)
        window_qf.title("Recht. Dreieck")
        window_qf.config(bg="#CDC9C9")
        window.withdraw()
        
        frame1 = tk.Frame(master=window_qf, bg="#CDC9C9")
        frame1.pack(side="top")
        frameba = tk.Frame(master=frame1, bg="#CDC9C9")
        frameba.pack(side="bottom")
        framel2 = tk.Frame(master=frame1, bg="#3b3b3b")
        framel2.pack(side="bottom", padx=5, pady=5)
        framel = tk.Frame(master=frame1, bg="#3b3b3b")
        framel.pack(side="bottom", padx=5, pady=5)
        button = tk.Button(master=frame1, text="Lösen", command=loesen, bg="#303030", fg="white")
        button.pack(side="bottom", padx=5, pady=5)
        framec = tk.Frame(master=frame1, bg="#BABABA")
        framec.pack(side="bottom")
        frameb = tk.Frame(master=frame1, bg="#BABABA")
        frameb.pack(side="bottom")
        framea = tk.Frame(master=frame1, bg="#BABABA")
        framea.pack(side="bottom")
        
        label1 = tk.Label(master=frame1, text="f(x)=ax^2+bx+c", bg="#3b3b3b", fg="white")
        label1.pack(padx=5, pady=5)
        
        label2 = tk.Label(master=framea, text="a", bg="#3b3b3b", fg="white")
        label2.pack(side="left", padx=5, pady=5)
        entry1 = tk.Entry(master=framea)
        entry1.pack(padx=5, pady=5)
        
        label3 = tk.Label(master=frameb, text="b", bg="#3b3b3b", fg="white")
        label3.pack(side="left", padx=5, pady=5)
        entry2 = tk.Entry(master=frameb)
        entry2.pack(padx=5, pady=5)
        
        label4 = tk.Label(master=framec, text="c", bg="#3b3b3b", fg="white")
        label4.pack(side="left", padx=5, pady=5)
        entry3 = tk.Entry(master=framec)
        entry3.pack(padx=5, pady=5)
        
        button_back = tk.Button(master=frameba, text="Back", command=back_qf, bg="#666666", fg="white")
        button_back.pack(padx=5, pady=5)
    
    def back():
        window.deiconify()
        window_ft.destroy()

### Lineare Funktion Fenster ###

    def lft():
        def back_lft():
            window_ft.deiconify()
            window_lft.destroy()
            
        def loesen():
            try:
                framehl = tk.Frame(master=frame1)
                framehl.pack(side="bottom")
                frame5 = tk.Frame(master=frame1, bg="#3b3b3b")
                frame5.pack(side="bottom",padx=5, pady=5, fill="both")
                frame4 = tk.Frame(master=frame1, bg="#3b3b3b")
                frame4.pack(side="bottom",padx=5, pady=5, fill="both")
                label6 = tk.Label(master=frame5, text="Monotonie:", bg="#3b3b3b", fg="white")
                label6.pack(side="left", padx=5, pady=5)
                label7 = tk.Label(master=frame5, text="")
                label7.pack(padx=5, pady=5)
                label5 = tk.Label(master=frame4, text="Nulstelle:", bg="#3b3b3b", fg="white")
                label5.pack(side="left",padx=5, pady=5)
                label4 = tk.Label(master=frame4, text="")
                label4.pack(padx=5, pady=5)
                
                m = int(entryA.get())
                n = int(entryB.get())
                
                ### Nullstelle ###
                x1 = -(n/m)
                x1 = round(x1, 2)
                label4.configure(text=x1)
                
                ### Monotonie m ###
                sm = n/m
                if sm > 0:
                    label7.config(text="Steigt")
                elif sm < 0:
                    label7.config(text="Fällt")
                
                ### Bildung Graph ###
                x = np.linspace(-5,5,60)
                y = m*x+n
                
                plt.xlabel("x-Achse")
                plt.ylabel("y-Achse")
                plt.title(str(m) + "*x + " + str(n))
                plt.grid(True)
                plt.plot(x,y)
                plt.show()
            
            except ValueError:
                label4.config(text="Fehler, Ungültiger Wert")
            
        
        window_lft = tk.Toplevel(window)
        window_lft.title("Lineare Funktion")
        window_lft.config(bg="#CDC9C9")
        window_lft.resizable(False, False)
        window_ft.withdraw
        
        
        framef = tk.Frame(master=window_lft, bg="#CDC9C9")
        framef.pack(side="top")
        frame2 = tk.Frame(master=window_lft, bg="#BABABA")
        frame2.pack(side="top", fill="both")
        frame3 = tk.Frame(master=window_lft, bg="#BABABA")
        frame3.pack(side="top", fill="both")
        frame1 = tk.Frame(master=window_lft, bg="#CDC9C9")
        frame1.pack(side="top")
        frame5 = tk.Frame(master=frame1, bg="#CDC9C9")
        frame5.pack(side="top")
        frameba = tk.Frame(master=frame1, bg="#CDC9C9")
        frameba.pack(side="bottom")
        
        
        labelf = tk.Label(master=framef, text="f(x)=mx+n", bg="#3b3b3b", fg="white")
        labelf.pack(padx=5, pady=5)
        
        label1 = tk.Label(master=frame2, text="m", bg="#3b3b3b", fg="white")
        label1.pack(side="left",padx=5, pady=5)
        
        entryA = tk.Entry(master=frame2)
        entryA.pack(side="top",padx=5, pady=5)
        
        label2 = tk.Label(master=frame3, text="n", bg="#3b3b3b", fg="white")
        label2.pack(side="left",padx=5, pady=5, expand=True, fill="both")

        entryB = tk.Entry(master=frame3)
        entryB.pack(side="top",padx=5, pady=5)
        
        button = tk.Button(master=frame5, text="Lösen", bg="#303030", fg="white", command=loesen)
        button.pack(padx=5, pady=5)
        

        
        button_back = tk.Button(master=frameba , text="Back", command=back_lft, bg="#666666", fg="white")
        button_back.pack(padx=5, pady=5)

### Funktionen Fenster Main ###

    window_ft = tk.Toplevel(window)
    window_ft.title("Funktionen")
    window_ft.config(bg="#CDC9C9")
    window.withdraw()
    
    frame1 = tk.Frame(master=window_ft, bg="#CDC9C9")
    frame1.pack(side="top")
    
    lft_button = tk.Button(master=frame1, text="Lineare Funktion", command=lft, bg="#303030", fg="white")
    lft_button.pack(side="top", padx=8, pady=8, fill="both")
    qf_button = tk.Button(master=frame1, text="Quadratische Funktion", command=qf, bg="#303030", fg="white")
    qf_button.pack(side="top",padx=8, pady=8, fill="both")
    button = tk.Button(master=frame1, text="Back", command=back, bg="#666666", fg="white")
    button.pack(padx=10, pady=5)

### Quersumme Fenster ###

def qs():
    def loesen():
        try:
            number = entry.get()
            qs_l = sum([int(i) for i in number])
            labelErgebnis.config(text=qs_l)
        except ValueError:
            labelErgebnis.config(text="Fehler, Ungültige Werte")
    def back():
        window.deiconify()
        window_qs.destroy()
        
    window_qs = tk.Toplevel(window)
    window_qs.title("Quersumme")
    window_qs.config(bg="#CDC9C9")
    window.withdraw()
    
    frame1 = tk.Frame(master=window_qs, bg="#CDC9C9")
    frame1.pack(side="top")
    frame3 = tk.Frame(master=frame1, bg="#CDC9C9")
    frame3.pack(side="bottom")
    frame2 = tk.Frame(master=frame1, bg="#3b3b3b")
    frame2.pack(side="bottom", padx=5, pady=5)
    
    entry = tk.Entry(master=frame1)
    entry.pack(padx=10, pady=5)
    
    button = tk.Button(master=frame3, text="Back", command=back, bg="#666666", fg="white")
    button.pack(padx=10, pady=5, side="top")
    
    button = tk.Button(master=frame1, text="Lösen", command=loesen, bg="#303030", fg="white")
    button.pack(padx=5, pady=5)
    
    labelErgebnis = tk.Label(master=frame2, text="")
    labelErgebnis.pack(side="right", padx=5, pady=5)
    label = tk.Label(master=frame2, text="Ergebnis:", bg="#3b3b3b", fg="white")
    label.pack(padx=5, pady=5)

### Main Window ###
        
window = tk.Tk()
window.title("Formel Rechner")
window.resizable(False, False)

mainFrame = tk.Frame(master=window, bg="#CDC9C9") #Hintergrund Standard Farbe
mainFrame.pack(side="top")

qs_button = tk.Button(master=mainFrame, text="Quersumme", command=qs, bg="#303030", fg="white")
qs_button.pack(side="top", padx=8, pady=8, fill="both")

qua_formel = tk.Button(master=mainFrame, text="Funktionen", command=ft, bg="#303030", fg="white")
qua_formel.pack(side="top", padx=8, pady=8, fill="both")

test = tk.Button(master=mainFrame, text="Soon", bg="#303030", fg="white")
test.pack(side="top", padx=8, pady=8, fill="both")

close_button = tk.Button(master=mainFrame, text="Close", command=window.destroy, bg="#666666", fg="white")
close_button.pack(padx=10, pady=5)

window.mainloop()