import csv
import random
from datetime import datetime
import os 

CSV_DOSYASI = 'sensor_data.csv'
FIRIN_ADI = 'Firin-1'
BASLIKLAR = ['zaman_damgasi', 'firin_adi', 'sicaklik'] 

def veri_satiri_ekle():
    
    
    dosya_var_mi = os.path.exists(CSV_DOSYASI)
    
    try:
        
        with open(CSV_DOSYASI, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            
            if not dosya_var_mi:
                writer.writerow(BASLIKLAR)
            
            
            zaman = datetime.now().strftime('%d.%m.%Y %H:%M')
            if random.random() > 0.9:
                sicaklik = random.randint(901, 1000)
            else:
                sicaklik = random.randint(850, 900)
            
            yeni_satir = [zaman, FIRIN_ADI, sicaklik]
            
            
            writer.writerow(yeni_satir)
            
        print(f"Başarıyla eklendi: {yeni_satir}")

    except Exception as e:
        print(f"Hata: CSV dosyasına yazılırken bir sorun oluştu: {e}")

if __name__ == "__main__":
    veri_satiri_ekle()