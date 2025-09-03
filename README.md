# 🎓 Öğrenci Yönetim Sistemi (Python + MySQL)

Bu proje, **Python (Tkinter)** ve **MySQL** tabanlı geliştirilmiş bir **Öğrenci Yönetim Sistemi** uygulamasıdır.  
Kullanıcı dostu bir arayüz ile **öğrenci kayıt işlemleri, not takibi, arama/silme, şifre yönetimi ve transkript çıktısı (PDF)** gibi fonksiyonları sunar.  

---

## 🚀 Özellikler

- 🔐 **Giriş Sistemi**  
  - Admin kullanıcı adı ve şifre ile giriş yapabilme  
  - Şifre değiştirme modülü  

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

```bash
├── main.py               # Tkinter tabanlı öğrenci yönetim sistemi
├── requirements.txt      # Gerekli Python kütüphaneleri
├── student.sql           # MySQL veritabanı dump dosyası
└── README.md             # Proje dokümantasyonu
