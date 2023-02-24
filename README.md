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
## Introductie
Voor project 7/8 hebben wij de opdracht gekregen om een time-lapse-fotografie-programma te ontwikkelen voor een ZOE-fluorescentiemicroscoop. Dit project voeren we uit voor de Biologie en Medisch Labaratoriumonderzoek (BML) afdeling aan het Hogeschool Rotterdam - Academieplein.

## Probleembeschrijving
De opleiding Biologie en Medisch Laboratoriumonderzoek bezit een fluorescentiemicroscoop die via een touchscreen te bedienen is. De microscoop wordt gebruikt om in levende cellen de fluorescentie te activeren om hiermee bepaalde structuren en bewegingen zichtbaar te maken. Hierbij is het van essentieel belang dat dit gebaseerd wordt op tijd, zodat verandering waargenomen kan worden. Momenteel kan de fluorescentie gemeten worden via drie led lichten: rood, groen en blauw. Daarnaast wordt er een witte lamp gebruikt voor doorvallend licht. Bij sommige processen moet er gedurende langere tijd meerdere opnamen gemaakt worden in verschillende kleuren. Het zou erg fijn zijn dit proces geautomatiseerd te hebben. Jammer genoeg staat de huidige software dit niet toe. Het verzoek is dus om nieuwe software te creëren die het automatiseren wel toestaat.

## Installatie
**Note**: Alleen windows supported
### Benodigdheden
Installeer de volgende benodigheden

- [python](https://www.python.org/downloads/release/python-3110/)(versie 3.11.0)
- [pip](https://pip.pypa.io/en/stable/installation/)(indien niet geinstalleerd)

### Building
1. Clone the repository

```bash
$ git clone https://github.com/Jkachoura/Time-lapsefotografie.git
```

2. Enter the cloned repository and install the dependencies

```bash
$ pip install -r requirements.txt
```