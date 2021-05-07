# Raspberry-Pi-Pico-Motor-Driver-Webcam-LDR-Control-IR-Cut-IR-Led

Bu program hiçbir garanti vermez..USB KAMERA'ya IR-Filtre ve IR-Led ekleme amacıyla yapıldı..

LDR gece ve gündüz değerlerini okur ,koşullar sağlanırsa makine kendini Resetler ve START fonksiyonu çalışır.Resetleme amacı temiz bir başlangıç için.Program bu haliyle gece ve gündüz modlarına geçmeden önce PİCO kendini resetler şeklindedir..

Start fonksiyonu ADC(26)pin'i ,yani LDR sinyali'nin bağlı olduğu Analog pin'i sayıya çevirerek okur ,gecemi / gündüzmü bakar ,duruma göre işlem yapar...

IR-LED pini (25)"onboard led" olarak ayarlı,deiştirin..

Resimdeki IR-FİLTRE 5V-110ma max çekiyor..100 ohm direnç ile 60ma 'e düşürebilirsiniz..Filtreyi sorunsuz döndürür..Filtre döndükten sonra 
LB1838 kapatılır..Ledler açılır.



EKLEMELER YAKINDA !
