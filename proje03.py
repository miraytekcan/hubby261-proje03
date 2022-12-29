from gensim.models import KeyedVectors
import tkinter as tk

root = tk.Tk()
root.geometry("500x300")
root.title("Miray Anahtar Kelime Optimizasyonu")
entry = tk.Entry(root, bg = "purple", fg = "white")
entry.pack()
label = tk.Label(root, text="Gördüğünüz mor alana istediğiniz kelimeyi veya kelimeleri girebilirsiniz.")
label.pack()

print("Model Yükleniyor...")
kelimeVektoru = KeyedVectors.load_word2vec_format('trModel100', binary=True)
print(kelimeVektoru)

def benzerKelimeler():
    anahtarKelimeler = entry.get().split()
    print("Girdiğiniz optimize edilecek kelimeler: " + " ".join(anahtarKelimeler))
    if anahtarKelimeler:
        try:
            oneriler = kelimeVektoru.most_similar(positive=anahtarKelimeler)
            for oneri in oneriler:
                if not any(keyword in oneri[0] for keyword in anahtarKelimeler):
                    print(oneri[0])
                    print("https://www.google.com.tr/search?q=" + oneri[0])
        except KeyError:
            print("Girdiğiniz anahtar kelime veya kelimeler veri setinde bulunamadı.")

def quit():
    root.destroy()

button1 = tk.Button(root, text="Anahtar Kelimeleri Al", command=benzerKelimeler)
button1.pack()
button2 = tk.Button(root, text="Çıkış", command=quit)
button2.pack()
root.mainloop()
