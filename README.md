# Raspberry-Pi-Pico-Motor-Driver-USBcamera-LDR-Control-IR-Cut-IR-Led

Bu program hiçbir garanti vermez..USB KAMERA'ya IR-Filtre ve IR-Led ekleme amacıyla yapıldı..

LDR gece ve gündüz değerlerini okur ,koşullar sağlanırsa makine kendini Resetler ve START fonksiyonu çalışır.Resetleme amacı temiz bir başlangıç için.Program bu haliyle gece ve gündüz modlarına geçmeden önce PİCO kendini resetler şeklindedir..

Start fonksiyonu ADC(26)pin'i ,yani LDR sinyali'nin bağlı olduğu Analog pin'i sayıya çevirerek okur ,gecemi / gündüzmü bakar ,duruma göre işlem yapar...

IR-LED pini (25)"onboard led" olarak ayarlı,deiştirin..

Resimdeki IR-FİLTRE 5V-110ma max çekiyor..100 ohm direnç ile 60ma 'e düşürebilirsiniz..Filtreyi sorunsuz döndürür..Filtre döndükten sonra 
LB1838 kapatılır..Ledler açılır.



IR-LED pin GPIO-13: ![Alt Text](https://github.com/kungfumasterv11/Raspberry-Pi-Pico-Motor-Driver-USBcamera-LDR-Control-IR-Cut-IR-Led/blob/main/Raspberry%20Pico%20USB%20Camera%20IR-CUT%20IR%20LED.png)


<div style="width:100%;height:0px;position:relative;padding-bottom:66.667%;"><iframe src="https://streamable.com/e/z064lg" frameborder="0" width="100%" height="100%" allowfullscreen style="width:100%;height:100%;position:absolute;left:0px;top:0px;overflow:hidden;"></iframe></div>
