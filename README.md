# Raspberry-Pi-Pico-Motor-Driver-USBcamera-LDR-Control-IR-Cut-IR-Led

Bu program hiçbir garanti vermez..USB KAMERA'ya IR-Filtre ve IR-Led ekleme amacıyla yapıldı..

Şemya göre yapılan prototip çalışıyor..Uzun süreli kullanım testi sonucu yazılacak..

LDR gece ve gündüz değerlerini okur ,koşullar sağlanırsa makine kendini Resetler ve START fonksiyonu çalışır.Resetleme amacı temiz bir başlangıç için.Program bu haliyle gece ve gündüz modlarına geçmeden önce PİCO kendini resetler şeklindedir..

Start fonksiyonu ADC(26)pin'i ,yani LDR sinyali'nin bağlı olduğu Analog pin'i sayıya çevirerek okur ,gecemi / gündüzmü bakar ,duruma göre işlem yapar...


Resimdeki IR-FİLTRE 5V-110ma max çekiyor..100 ohm direnç ile 60ma 'e düşürebilirsiniz..Filtreyi sorunsuz döndürür..Filtre döndükten sonra 
LB1838 kapatılır..Ledler açılır.

KAYNAK makinesi :

http://docs.micropython.org/en/latest/library/index.html

https://www.raspberrypi.org/documentation/rp2040/getting-started/#rp2040-boards

https://www.raspberrypi.org/documentation/rp2040/getting-started/#board-specifications

https://www.raspberrypi.org/documentation/rp2040/getting-started/#getting-started-with-micropython

https://www.kontrolkalemi.com/forum/members/kesmez.3801/


: ![Alt Text](https://github.com/kungfumasterv11/Raspberry-Pi-Pico-Motor-Driver-USBcamera-LDR-Control-IR-Cut-IR-Led/blob/main/Raspberry%20Pico%20USB%20Camera%20IR-CUT%20IR%20LED.png)

VİDEO : [![Watch the video](https://github.com/kungfumasterv11/Raspberry-Pi-Pico-Motor-Driver-USBcamera-LDR-Control-IR-Cut-IR-Led/blob/main/no-ir-led-transistor-demo.jpeg)](https://streamable.com/krb86q)

