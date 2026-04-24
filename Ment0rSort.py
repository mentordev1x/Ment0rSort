import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox

# Uygulama Teması: Modern ve Temiz
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MasaustuDuzenleyici(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Pencere Ayarları
        self.title("Dosya Düzenleyici")
        self.geometry("650x500")
        
        # Dosya Grupları (Sadeleştirilmiş İsimler)
        self.gruplar = {
            'Resimler': ['.jpg', '.jpeg', '.png', '.gif', '.svg', '.webp', '.ico', '.heic'],
            'Belgeler': ['.pdf', '.doc', '.docx', '.txt', '.xlsx', '.csv', '.ppt', '.pptx'],
            'Videolar': ['.mp4', '.mkv', '.avi', '.mov', '.wmv', '.webm'],
            'Ses Dosyalari': ['.mp3', '.wav', '.flac', '.m4a', '.aac'],
            'Arsivler': ['.zip', '.rar', '.7z', '.tar', '.gz'],
            'Kod Dosyalari': ['.py', '.html', '.css', '.js', '.json', '.cpp', '.sql', '.bat'],
            'Tasarim': ['.psd', '.ai', '.fig', '.sketch', '.dwg'],
            'Kitaplar': ['.epub', '.mobi', '.azw3'],
            'Uygulamalar': ['.exe', '.msi', '.apk', '.dmg']
        }

        self.arayuz_hazirla()

    def arayuz_hazirla(self):
        # Üst Panel
        self.header = ctk.CTkLabel(self, text="Dosya Düzenleme Paneli", font=("Segoe UI", 22, "bold"))
        self.header.pack(pady=(25, 5))
        
        self.info = ctk.CTkLabel(self, text="Dizindeki dosyaları türlerine göre klasörlere ayırır.", font=("Segoe UI", 12))
        self.info.pack(pady=(0, 20))

        # Ana Panel
        self.panel = ctk.CTkFrame(self)
        self.panel.pack(padx=30, pady=10, fill="both", expand=True)

        # Klasör Seçme Butonu
        self.secim_btn = ctk.CTkButton(self.panel, text="Klasör Seçin", 
                                       command=self.dizin_sec, 
                                       fg_color="#3b8ed0", hover_color="#1f538d",
                                       height=40, font=("Segoe UI", 13, "bold"))
        self.secim_btn.pack(pady=20)

        self.yol_yazisi = ctk.CTkLabel(self.panel, text="Lütfen bir hedef dizin belirleyin.", text_color="#aaaaaa")
        self.yol_yazisi.pack()

        # Süreç Takibi (Log Ekranı)
        self.log_ekrani = ctk.CTkTextbox(self.panel, width=550, height=150, font=("Consolas", 12))
        self.log_ekrani.pack(pady=15, padx=15)
        self.log_ekrani.configure(state="disabled")

        # İşlem Butonu
        self.baslat_btn = ctk.CTkButton(self, text="İŞLEMİ BAŞLAT", 
                                        command=self.calistir,
                                        fg_color="#27ae60", hover_color="#1e8449",
                                        height=45, font=("Segoe UI", 14, "bold"))
        self.baslat_btn.pack(pady=20)

    def log_yaz(self, metin):
        self.log_ekrani.configure(state="normal")
        self.log_ekrani.insert("end", f"> {metin}\n")
        self.log_ekrani.see("end")
        self.log_ekrani.configure(state="disabled")
        self.update()

    def dizin_sec(self):
        yol = filedialog.askdirectory()
        if yol:
            self.secilen_yol = yol
            self.yol_yazisi.configure(text=f"Hedef Dizin: {yol}", text_color="#57bb8a")
            self.log_yaz(f"Dizin seçildi: {os.path.basename(yol)}")

    def calistir(self):
        if not hasattr(self, 'secilen_yol') or not self.secilen_yol:
            messagebox.showwarning("Uyarı", "Lütfen önce bir klasör seçin.")
            return

        dosyalar = [f for f in os.listdir(self.secilen_yol) if os.path.isfile(os.path.join(self.secilen_yol, f))]
        
        if not dosyalar:
            self.log_yaz("Klasör içerisinde düzenlenecek dosya bulunamadı.")
            return

        tasinanlar = 0
        self.log_yaz("Düzenleme işlemi başlatıldı...")

        for dosya in dosyalar:
            eski_konum = os.path.join(self.secilen_yol, dosya)
            uzanti = os.path.splitext(dosya)[1].lower()
            
            # Kategori tespiti
            kategori = "Diger Dosyalar"
            for grup_adi, uzantilar in self.gruplar.items():
                if uzanti in uzantilar:
                    kategori = grup_adi
                    break

            yeni_klasor = os.path.join(self.secilen_yol, kategori)
            
            if not os.path.exists(yeni_klasor):
                os.makedirs(yeni_klasor)

            # Çakışma kontrolü
            yeni_konum = os.path.join(yeni_klasor, dosya)
            if os.path.exists(yeni_konum):
                isim, uz = os.path.splitext(dosya)
                dosya = f"{isim}_yeni{uz}"
                yeni_konum = os.path.join(yeni_klasor, dosya)

            try:
                shutil.move(eski_konum, yeni_konum)
                self.log_yaz(f"Aktarıldı: {dosya}")
                tasinanlar += 1
            except:
                self.log_yaz(f"HATA: {dosya} taşınamadı.")

        messagebox.showinfo("Tamamlandı", f"İşlem başarıyla bitti.\nToplam {tasinanlar} dosya kategorize edildi.")
        self.log_yaz("--- İşlem Sonlandırıldı ---")

if __name__ == "__main__":
    app = MasaustuDuzenleyici()
    app.mainloop()