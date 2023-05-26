# Project 7/8 - Time-lapsefotografie
- Jaouad Kachoura
- Raekwon Killop
- Sabri Demir
- Tobias de Bildt

## Inhoudsopgave
- [Introductie](#introductie)
- [Probleembeschrijving](#probleembeschrijving)
- [Installatie](#installatie)
    - [Benodigdheden](#benodigdheden)
    - [Building](#building)
        - [Raspberry Pi imager](#raspberry-pi-imager)
        - [PuTTY](#putty)
        - [Terminal](#terminal)
        - [Access Point Opzetten](#access-point-opzetten)
            - [requirements installeren](#requirements-installeren)
            - [Commando's uitvoeren](#commandos-uitvoeren)
        - [Fix voor processen die lang lopen](#fix-voor-processen-die-lang-lopen)

    - [Usage](#usage)
## Introductie
Voor project 7/8 hebben wij de opdracht gekregen om een time-lapse-fotografie-programma te ontwikkelen voor een ZOE-fluorescentiemicroscoop. Dit project voeren we uit voor de Biologie en Medisch Labaratoriumonderzoek (BML) afdeling aan het Hogeschool Rotterdam - Academieplein.

## Probleembeschrijving
De opleiding Biologie en Medisch Laboratoriumonderzoek bezit een fluorescentiemicroscoop die via een touchscreen te bedienen is. De microscoop wordt gebruikt om in levende cellen de fluorescentie te activeren om hiermee bepaalde structuren en bewegingen zichtbaar te maken. Hierbij is het van essentieel belang dat dit gebaseerd wordt op tijd, zodat verandering waargenomen kan worden. Momenteel kan de fluorescentie gemeten worden via drie led lichten: rood, groen en blauw. Daarnaast wordt er een witte lamp gebruikt voor doorvallend licht. Bij sommige processen moet er gedurende langere tijd meerdere opnamen gemaakt worden in verschillende kleuren. Het zou erg fijn zijn dit proces geautomatiseerd te hebben. Jammer genoeg staat de huidige software dit niet toe. Het verzoek is dus om nieuwe software te creëren die het automatiseren wel toestaat.

## Installatie
**Note**: Alleen windows supported
### Benodigdheden
Installeer de volgende benodigheden

- [python](https://www.python.org/downloads/release/python-3110/) (versie 3.11.0)
- [pip](https://pip.pypa.io/en/stable/installation/) (indien niet geinstalleerd)
- [Raspberry Pi Zero W](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
- [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
- [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) of OpenSSH
- Persoonlijke Hotspot
- Micro USB kabel
- SD kaart (lezer)

### Building
Volg de onderstaande stappen om via SSH een Access Point op te zetten op je Raspberry Pi:  
#### Raspberry Pi Imager 
1. Start de Raspberry Pi Imager app op.
2. Druk op Choose OS en kies Raspberry Pi OS lite. (32-bit)
3. Druk op Choose Storage en kies je SD kaart die in de lezer zit.
4. Druk op de tandwiel icoontje rechtsbeneden. 
5. Vul een hostname naar keuze in. 
6. Druk op Enable SSH en kies je eigen gebruikersnaam en wachtwoord in. 
7. Druk op configure WLAN en vul de naam en wachtwoord in van je persoonlijke hotspot.
8. Vervolgens druk je op write en wacht je tot de imager klaar is met schrijven naar de SD kaart. Daarna doe je de SD kaart in de Raspberry Pi.

#### PuTTY
1. Vul de hostname in die je hebt geconfigureerd in de Raspberry Pi Imager bijvoorbeeld: 

```bash
raspberrypi.local
```
2. Vul 22 in als port
3. Kies SSH als Connection Type en druk op open.

#### Terminal 
 Als je OpenSSH hebt geïnstalleerd op je besturingsysteem is er een alternatief voor het inloggen en heb je geen PuTTY nodig.

 1. Vul SSH username gevolgd door je hostname bijvoorbeeld:
 ```bash
ZOE@raspberrypi.local
```

**Note**: Het kan tot wel 10 minuten duren voordat je kan inloggen via SSH dus wacht als je een hostname error krijgt.


#### Access Point Opzetten

##### requirements installeren
Om de website volledig te laten werken is het erg belangrijk om de requirements.txt te installeren via onze repository. Om dit niet te vergeten moet dit altijd de eerste stap zijn, een access point opzetten kan namelijk een tijdje duren.

1. Clone de repository

```bash
$ git clone https://github.com/Jkachoura/Time-lapsefotografie.git
```

2. Installeer requirements.txt
```bash
$ pip install -r requirements.txt
```

3. Navigeer naar de hostname directory 
2. Installeer requirements.txt
```bash
$ cd /home 
  cd /hostname
```
**Note**: Hostname moet je eigen gekozen hostname zijn.

##### Commando's Uitvoeren
1. Voer de volgende commando's uit
```bash
sudo apt update
sudo apt upgrade
sudo apt install hostapd dnsmasq
```

2. Open het configuratiebestand voor de draadloze adapter met het volgende commando:
```bash
sudo nano /etc/dhcpcd.conf
```

3. Voeg de volgende regels toe aan het bestand om een statisch IP-adres voor de draadloze adapter in te stellen sla het daarna op:

```bash
interface wlan0
static ip_address=192.168.4.1/24
nohook wpa_supplicant
```

4. Configureer de DHCP-server (dnsmasq). Maak een nieuw configuratiebestand aan met het volgende commando:

```bash
sudo nano /etc/dnsmasq.conf
```

5. Voeg de volgende regels toe aan het bestand en sla het op.

```bash
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
```

6. Configureer de toegangspuntdienst (hostapd). Maak een nieuw configuratiebestand aan met het volgende commando:

```bash
sudo nano /etc/hostapd/hostapd.conf
```

7. Voeg de volgende configuratie toe aan het bestand en sla het op:
```bash
interface=wlan0
ssid=MyAccessPoint  # Vervang "MyAccessPoint" door de gewenste naam voor je access point
hw_mode=g
channel=7
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=MyPassphrase  # Vervang "MyPassphrase" door het gewenste wachtwoord voor je access point
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
```

8. Schakel IP-forwarding in. Open het configuratiebestand voor IP-forwarding met het volgende commando:

```bash
sudo nano /etc/sysctl.conf
```
9. Zoek de regel met #net.ipv4.ip_forward=1 en verwijder het hekje (#) aan het begin van de regel om het in te schakelen.

10. Unmask hostapd en dnsmasq:
```bash
sudo systemctl unmask hostapd
sudo systemctl unmask dnsmasq
```

11. Voeg de services toe aan het opstartproces, zodat ze automatisch starten bij het opstarten van de Raspberry Pi:
```bash
sudo systemctl enable hostapd
sudo systemctl enable dnsmasq
```

12. Start de services. Voer de volgende commando's uit:
```bash
sudo systemctl start hostapd
sudo systemctl start dnsmasq
```

13. Herstart de Raspberry Pi om de wijzigingen door te voeren:
```bash
sudo reboot
```
#### Fix voor processen die lang lopen

Voor langdurige processen doet er een probleem zich voort. Als je via SSH het process start zal het process beeindigen wanneer de SSH sessie afgesloten wordt. Het is niet wenselijk om vier dagen lang verbonden te zijn, daarom is er een andere oplossing vereist. 1 van die oplossingen is terminal multiplexing. Dit kan gestart worden met behulp van [tmux](https://www.tomshardware.com/how-to/run-long-running-scripts-raspberry-pi). Log in via SSH met de ingestelde static ip adres en start een tmux sessie. 

Echter is er betere oplossing. Door het aanmaken van een service kan je via SSH vertellen aan de RasPi dat hij lokaal het proces moet starten zodat het proces niet beeindigd wordt wanneer SSH sluit. Bovendien kan je instellen dat het programma zichzelf automatisch opstart. Dit instellen gaat als volgt:
1. `sudo nano /etc/systemd/system/zoe.service`
2. Zet deze code er in:
```
[Unit]
Description=My test service
After=multi-user.target
[Install]
WantedBy=multi-user.target
[Service]
Type=simple
User=rae
PermissionsStartOnly=true
ExecStart=/usr/bin/python /home/rae/Time-lapsefotografie-main/flask-app/main.py
Restart=on-failure
TimeoutSec=600
```
3. Reload de daemon files met `sudo systemctl daemon-reload`
4. Start de service en stel in dat hij start bij het opstarten van de raspberry pi `sudo systemctl enable zoe.service --now`

Voor meer informatie kan je [deze](https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267) webpagina raadplegen


## Usage

1. Verbindt met de WiFi, die is opgezet door de Raspberry Pi, via je 
toestel.
```bash
SSID: MyAccessPoint  # Vervang "MyAccessPoint" door de gewenste naam voor je access point
Wachtwoord: MyPassphrase  # Vervang "MyPassphrase" door het gewenste wachtwoord voor je access point 
```

2. De webbrowser is op de volgende url te vinden [http://192.168.4.1](http://192.168.4.1:8080)

3. Steek je USB in de microscoop. Zorg er voor dat er genoeg capaciteit er op zit. Voor veel fotocycli* en lange timelapse denk aan 4 GB.

4. Druk op de color pagina en configureer de settings

```
Enable White LED: Dit zorgt ervoor dat er foto's worden gemaakt met het witte licht. Vink aan om dit te gebruiken
Enable Blue LED: Dit zorgt ervoor dat er foto's worden gemaakt met het blauwe licht. Vink aan om dit te gebruiken
Enable Green LED: Dit zorgt ervoor dat er foto's worden gemaakt met het groene licht. Vink aan om dit te gebruiken
Enable Red LED: Dit zorgt ervoor dat er foto's worden gemaakt met het rode licht. Vink aan om dit te gebruiken
Enable Merge: Dit zorg ervoor dat de foto's die gemaakt worden samen gemengd worden. Vink aan om dit te gebruiken.
Cycle Amount: Hoeveel fotocycli* wil je nemen.
Cycle Interval: Hoeveelheid tijd tussen fotocycli in (minuten).

fotocycli: In een fotocyclus wordt er van elk gekozen LED een foto gemaakt plus merge foto indien geselecteerd

```

5. Bevestig de settings en druk vervolgens op <em>Make Timelapse</em>

6. Het programma gaat vervolgens aan de slag. Je kan de verbinding met het toestel verbreken.

7. Als de timelapse klaar is, zijn de foto's terug vinden op de usb.

**Notes** Onderaan het script moet de host veranderd worden door de jouw ingestelde IP-adres dus:

```python
if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
```

Naar bijvoorbeeld dit:
```python
if __name__ == "__main__":
    app.run(host="192.168.4.1", port=8080, debug=True)
```
