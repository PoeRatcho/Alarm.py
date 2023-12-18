from datetime import datetime
import pygame
import time
from playsound import playsound

i = int(input("Ne kadar tekrar etsin: "))
x = 0


saat = input("Saat: ")
dakika = input("Dakika: ")
saniye = input("Saniye: ")

while True:
    suan = datetime.now()
    dt = datetime.strftime(suan, "%H:%M:%S") #dt demek datetime değişkeninin kısaltılmış hali
    time.sleep(1) #sleep demek kaç defa tekrar etsin demek

    if dt == f"{saat}:{dakika}:{saniye}":
        while x < i:
            pygame.init()
            playsound("C:\\Users\\yabur\\OneDrive\\Masaüstü\\alarm.mp3")
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy(): #üstte yazan kodları sonsuz şekilde kontrol et
                pygame.event.get() #Eğer doğru çalışıyorsa çalıştır (get sorgu demek hatırla)
            x+=1 #while içi her çalıştığında x değişkenini 1 arttır demek.