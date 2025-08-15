Gereksinimler
- Python 3.9+  
- SMTP destekli bir e-posta hesabı (ör. Gmail – uygulama şifresi ile)

> Not: Standart kütüphaneler (csv, os, datetime, smtplib, random) kullanıldığı için ek bağımlılık zorunlu değildir.

Yapılandırma
`alarm_sistemi.py` içinde:
- **Eşikler:** `MIN_TEMP` ve `MAX_TEMP` (örn. 800–900°C)
- **E-posta:** SMTP sunucusu, port, gönderici/alıcı adresleri

Gmail kullanıyorsanız 2FA + **Uygulama Şifresi** oluşturup onu kullanın.

Çalıştırma
1) (İsteğe bağlı) Sanal ortam:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
