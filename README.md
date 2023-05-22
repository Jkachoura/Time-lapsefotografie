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
- Micro USB kabel
- SD kaart (lezer)

### Building
1. Clone the repository

```bash
$ git clone https://github.com/Jkachoura/Time-lapsefotografie.git
```

2. Enter the cloned repository and install the dependencies

```bash
$ pip install -r requirements.txt
```
## Usage

1. Verbindt met de WiFi, die is opgezet door de Raspberry Pi, via je 
toestel.
```bash
SSID: ZOE
Wachtwoord: 
```

2. De webbrowser is op de volgende url te vinden [http://142.122.32.80](http://142.122.32.80)

3. Steek je USB in de microscoop. Zorg er voor dat er genoeg capaciteit er op zit. Voor veel fotocycli* en lange timelapse denk aan 4 GB.

4. Druk op de color pagina en configureer de settings

```bash
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

