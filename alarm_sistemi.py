import csv
import smtplib
from email.message import EmailMessage


CSV_DOSYASI = 'sensor_data.csv'
GONDEREN_EPOSTA = 'cimsastajyer@gmail.com'
GONDEREN_SIFRE = 'qnvfvddsatxgrssn'
ALICI_EPOSTA = 'enesmatci@gmail.com'
MIN_SICAKLIK = 800
MAX_SICAKLIK = 900
FIRIN_ADI = 'Firin-1' 

def son_sicakligi_oku():
    
    try:
        with open(CSV_DOSYASI, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            son_satir = list(reader)[-1] 
            sicaklik = float(son_satir['sicaklik'])
            print(f"Okunan son sıcaklık: {sicaklik}°C")
            return sicaklik
    except (IndexError, FileNotFoundError):
        print("Hata: CSV dosyası boş veya bulunamadı.")
        return None
    except Exception as e:
        print(f"Hata: CSV dosyası okunurken bir sorun oluştu: {e}")
        return None

def email_gonder(sicaklik):
    
    print("Kritik sıcaklık tespit edildi! E-posta gönderiliyor...")
    msg = EmailMessage()
    msg['Subject'] = f"ACİL: {FIRIN_ADI} YÜKSEK SICAKLIK ALARMI!"
    msg['From'] = GONDEREN_EPOSTA
    msg['To'] = ALICI_EPOSTA
    msg.set_content(
        f"Merhaba,\n\n{FIRIN_ADI} sıcaklığı kritik seviyeye ulaşmıştır.\n\n"
        f"Mevcut Sıcaklık: {sicaklik}°C\n\nLütfen acil kontrol ediniz."
    )
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(GONDEREN_EPOSTA, GONDEREN_SIFRE)
            smtp.send_message(msg)
            print("E-posta başarıyla gönderildi.")
    except Exception as e:
        print(f"Hata: E-posta gönderilirken bir sorun oluştu: {e}")

if __name__ == "__main__":
    mevcut_sicaklik = son_sicakligi_oku()
    if mevcut_sicaklik is not None:
        if not (MIN_SICAKLIK <= mevcut_sicaklik <= MAX_SICAKLIK):
            email_gonder(mevcut_sicaklik)
        else:
            print("Sıcaklık normal seviyede. İşlem yapılmadı.")