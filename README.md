# Dosya Düzenleyici

Bu Python uygulaması, seçtiğiniz bir dizindeki dosyaları uzantılarına göre otomatik olarak kategorilere ayırır ve ilgili klasörlere taşır.

## Özellikler

- **Otomatik Kategorilendirme**: Dosyaları uzantılarına göre aşağıdaki kategorilere ayırır:
  - Resimler (.jpg, .jpeg, .png, .gif, .svg, .webp, .ico, .heic)
  - Belgeler (.pdf, .doc, .docx, .txt, .xlsx, .csv, .ppt, .pptx)
  - Videolar (.mp4, .mkv, .avi, .mov, .wmv, .webm)
  - Ses Dosyaları (.mp3, .wav, .flac, .m4a, .aac)
  - Arşivler (.zip, .rar, .7z, .tar, .gz)
  - Kod Dosyaları (.py, .html, .css, .js, .json, .cpp, .sql, .bat)
  - Tasarım (.psd, .ai, .fig, .sketch, .dwg)
  - Kitaplar (.epub, .mobi, .azw3)
  - Uygulamalar (.exe, .msi, .apk, .dmg)
  - Diğer Dosyalar (tanımlanmayan uzantılar için)

- **Modern Arayüz**: CustomTkinter ile karanlık tema ve sezgisel tasarım.
- **Gerçek Zamanlı Log**: İşlem sırasında yapılan adımları takip edebilirsiniz.
- **Çakışma Önleme**: Aynı isimde dosya varsa otomatik olarak yeniden adlandırır.

## Gereksinimler

- Python 3.6 veya üzeri
- CustomTkinter kütüphanesi

## Kurulum

1. Bu projeyi bilgisayarınıza indirin veya klonlayın.
2. Gerekli bağımlılıkları yükleyin:
   ```
   pip install customtkinter
   ```
3. Uygulamayı çalıştırın:
   ```
   Ment0rSort.py
   ```

## Kullanım

1. Uygulamayı başlattığınızda ana pencere açılır.
2. "Klasör Seçin" butonuna tıklayarak düzenlemek istediğiniz dizini seçin.
3. "İŞLEMİ BAŞLAT" butonuna tıklayarak dosyaların kategorilere ayrılmasını başlatın.
4. Log ekranında işlemin ilerlemesini takip edebilirsiniz.
5. İşlem tamamlandığında bir onay mesajı alırsınız.

## Uyarılar

- Bu uygulama dosyaları taşır, silmez. Ancak, işlem geri alınamaz, dikkatli kullanın.
- Yedekleme yapmadan önce önemli dosyalarınızı yedekleyin.
- Uygulama sadece seçilen dizindeki dosyaları etkiler, alt dizinleri işlemez.

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasına bakın.
