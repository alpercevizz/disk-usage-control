# Disk Kullanımı İzleme Sistemi

Gerçek zamanlı disk kullanımı takibi, kayıt altına alma ve e-posta bildirimi özelliğiyle sistem yöneticileri için geliştirilmiş bir araçtır.



📜 İçindekiler
📌 Genel Bakış
⚙️ Özellikler
🚀 Kurulum
🛠 Kullanım
📧 E-posta Bildirimleri
📊 Arayüz
📂 JSON Log Kayıtları
📄 Lisans
📌 Genel Bakış
Bu proje, bilgisayarın disk kullanımını sürekli olarak izleyerek, belirlenen bir eşik değeri aştığında sistem yöneticisine otomatik e-posta bildirimi gönderir. Ayrıca, veriler JSON formatında kaydedilir ve gerçek zamanlı olarak grafiksel arayüzde gösterilir.

📍 Amaç: Sistem kaynaklarının takibini kolaylaştırmak ve disk doluluk problemlerini önceden tespit etmek.

⚙️ Özellikler
✔ Gerçek zamanlı disk kullanımı takibi
✔ % Kullanım eşik değeri aşıldığında e-posta bildirimi
✔ Verilerin JSON formatında kaydedilmesi
✔ Tkinter ile grafiksel arayüz
✔ Grafik gösterimi (Matplotlib)

🚀 Kurulum
Gereksinimler
Python 3.10+
psutil (Sistem verilerini almak için)
smtplib (E-posta gönderimi için)
json (Log kayıtları için)
matplotlib (Grafik arayüzü için)
tkinter (Arayüz için)

Adım 1: Bağımlılıkları Kur
Terminal veya Komut İstemi'nde şu komutu çalıştır:
```
pip install psutil matplotlib
```
Adım 2: Projeyi Klonla
```
git clone https://github.com/KULLANICI_ADI/disk-usage-control.git
cd disk-usage-control
```
🛠 Kullanım
Komut Satırından Çalıştırma
```
python app.py
```
Bu komut, terminalde gerçek zamanlı disk kullanımı takibi başlatır.

📧 E-posta Bildirimleri
📌 E-posta bildirimlerini kullanmak için: 1️⃣ config.json dosyasına gönderici e-posta adresi ve şifre bilgilerini ekleyin.
2️⃣ Eşik değeri (%) belirleyin. Disk kullanımı bu seviyeyi aşarsa otomatik bildirim gönderilir.

🔹 Örnek config.json dosyası:
```
{
  "email": "admin@example.com",
  "password": "şifreniz",
  "threshold": 80
}
```
📊 Arayüz
🖥 Tkinter ile tasarlanmış arayüz, disk kullanımını grafiksel olarak gösterir.
📊 Matplotlib ile anlık grafikler çizilir.

💡 Arayüzde gösterilen veriler:

Disk ismi
Kullanım yüzdesi
Gerçek zamanlı grafik
📂 JSON Log Kayıtları
🔹 Disk kullanım verileri disk_usage_log.json dosyasına kaydedilir.
🔹 E-posta bildirimi gönderilen olaylar loglanır.

📌 Örnek Kayıt Formatı:

```
{
  "timestamp": "2025-03-03 09:36:16",
  "disk": "C:\\",
  "usage": "85.3%",
  "status": "Warning - Disk usage exceeded threshold!"
}
```
📄 Lisans
Bu proje MIT Lisansı altında lisanslanmıştır.

📜 Telif Hakkı © 2025 - Alper
