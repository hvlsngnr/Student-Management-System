# 🎓 Öğrenci Yönetim Sistemi (Python + MySQL)

Bu proje, **Python (Tkinter)** ve **MySQL** tabanlı geliştirilmiş bir **Öğrenci Yönetim Sistemi** uygulamasıdır.  
Kullanıcı dostu bir arayüz ile **öğrenci kayıt işlemleri, not takibi, arama/silme, şifre yönetimi ve transkript çıktısı (PDF)** gibi fonksiyonları sunar.  

---

## 🚀 Özellikler

- 🔐 **Giriş Sistemi**  
  - Admin kullanıcı adı ve şifre ile giriş yapabilme
  - Şifre değiştirme modülü
  - Username and Password: admin/123

- 👨‍🎓 **Öğrenci Yönetimi**  
  - Yeni öğrenci ekleme  
  - Öğrenci bilgilerini güncelleme / silme  
  - Öğrencileri listeleme ve arama  

- 📊 **Not ve Transkript Sistemi**  
  - Öğrencilerin ders bazlı notlarını (vize, final) kaydetme  
  - Ortalamaların otomatik hesaplanması  
  - Transkript görüntüleme ve **PDF çıktısı alma** (ReportLab ile)  

- 📂 **Veritabanı Yapısı**  
  - **students**: Öğrenci bilgileri  
  - **grades**: Not bilgileri  
  - **subjects**: Ders bilgileri  
  - **admin**: Yönetici giriş bilgileri  

---

## 🗂️ Proje Yapısı

```text
├── main.py           # Tkinter tabanlı öğrenci yönetim sistemi
├── requirements.txt  # Gerekli Python kütüphaneleri
├── student.sql       # MySQL veritabanı dump dosyası
└── README.md         # Proje dokümantasyonu
```


## 🖼️ Ekran Görüntüleri

#XAMPP
![XAMPP](https://github.com/hvlsngnr/Student-Management-System/blob/main/screenshots/1.png)

### Giriş
![Giriş](https://github.com/hvlsngnr/Student-Management-System/blob/main/screenshots/2.png)

### Ana Sayfa
![Ana Sayfa](https://github.com/hvlsngnr/Student-Management-System/blob/main/screenshots/3.png)

### Ogrenci Ekle
![Öğrenci Ekle1](https://github.com/hvlsngnr/Student-Management-System/blob/main/screenshots/4.png)
![Öğrenci Ekle2](https://github.com/hvlsngnr/Student-Management-System/blob/main/screenshots/5.png)

### Ogrenci Sil
![Öğrenci Sil1](https://github.com/hvlsngnr/Student-Management-System/blob/main/screenshots/6.png)
![Öğrenci Sil2](https://github.com/hvlsngnr/Student-Management-System/blob/main/screenshots/7.png)

### Notlari Ekle
![Notlari Ekle](https://github.com/hvlsngnr/Student-Management-System/blob/main/screenshots/8.png)
