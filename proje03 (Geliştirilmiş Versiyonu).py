from gensim.models import KeyedVectors
import tkinter as tk

root = tk.Tk()
root.geometry("1000x1000")
root.title("Miray Anahtar Kelime Optimizasyonu")
entry = tk.Entry(root, bg = "purple", fg = "white")
entry.pack()
label = tk.Label(root, text="Gördüğünüz mor alana istediğiniz kelimeyi veya kelimeleri girebilirsiniz.")
label.pack()

print("Model Yükleniyor...")
kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

labels = []

def benzerKelimeler():
    anahtarKelimeler = entry.get().split()
    label1 = tk.Label(root, text="Girdiğiniz optimize edilecek kelimeler: " + " ".join(anahtarKelimeler))
    label1.pack()
    labels.append(label1)
    if anahtarKelimeler:
        try:
            oneriler = kelimeVektoru.most_similar(positive=anahtarKelimeler)
            for oneri in oneriler:
                if not any(keyword in oneri[0] for keyword in anahtarKelimeler):
                    label = tk.Label(root, text=oneri[0])
                    label.pack()
                    labels.append(label)
                    label = tk.Label(root, text="https://www.google.com.tr/search?q=" + oneri[0])
                    label.pack()
                    labels.append(label)
        except KeyError:
            label['text'] = "Girdiğiniz anahtar kelime veya kelimeler veri setinde bulunamadı."

def farkliBul():
    anahtarKelimeler = entry.get().lower().split()
    benzerlik = (kelimeVektoru.doesnt_match(anahtarKelimeler))
    label1 = tk.Label(root, text=benzerlik)
    label1.pack()
    labels.append(label1)

def temizle():
    for label in labels:
        label.pack_forget()
    labels.clear()

def quit():
    root.destroy()

button1 = tk.Button(root, text="Anahtar Kelimeleri Al", command=benzerKelimeler)
button1.pack()

button2 = tk.Button(root, text="Girilen Farklı Kelimeyi Bul", command=farkliBul)
button2.pack()

button3 = tk.Button(root, text="Yeni Arama Yapmadan Önce Çıktıları Temizle", command=temizle)
button3.pack()

button4 = tk.Button(root, text="Çıkış Yapmak İçin Tıkla", command=quit)
button4.pack()

root.mainloop()
