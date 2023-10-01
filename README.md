# Project Description
This project is the third project for the ENGETO Python Academy. It provides a Python script for scraping 2017 election data from a website https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ and exporting it to a CSV file.

## Libraries Installation
The libraries that are used in the code are stored in `requirements.txt` To install run:
```
pip install -r requierements.txt
```
## Usage
To run the script, you will need two arguments. Use the following command:
```
python elections_scraper.py <city> <output_file_name.csv>
```
- **'\<city\>':** the name of the city for which you want to collect election data.

- **'<output_file_name.csv>':** the name of CSV file to which the data will be exported.

For argument **'\<city\>'** you can choose from:
```
['Praha', 'Benešov', 'Beroun', 'Kladno', 'Kolín', 'Kutná Hora', 'Mělník', 'Mladá Boleslav', 'Nymburk', 'Praha-východ', 'Praha-západ', 'Příbram', 'Rakovník', 'Zahraničí', 'České Budějovice', 'Český Krumlov', 'Jindřichův Hradec', 'Písek', 'Prachatice', 'Strakonice', 'Tábor', 'Domažlice', 'Klatovy', 'Plzeň-město', 'Plzeň-jih', 'Plzeň-sever', 'Rokycany', 'Tachov', 'Cheb', 'Karlovy Vary', 'Sokolov', 'Děčín', 'Chomutov', 'Litoměřice', 'Louny', 'Most', 'Teplice', 'Ústí nad Labem', 'Česká Lípa', 'Jablonec nad Nisou', 'Liberec', 'Semily', 'Hradec Králové', 'Jičín', 'Náchod', 'Rychnov nad Kněžnou', 'Trutnov', 'Chrudim', 'Pardubice', 'Svitavy', 'Ústí nad Orlicí', 'Havlíčkův Brod', 'Jihlava', 'Pelhřimov', 'Třebíč', 'Žďár nad Sázavou', 'Blansko', 'Brno-město', 'Brno-venkov', 'Břeclav', 'Hodonín', 'Vyškov', 'Znojmo', 'Jeseník', 'Olomouc', 'Prostějov', 'Přerov', 'Šumperk', 'Kroměříž', 'Uherské Hradiště', 'Vsetín', 'Zlín', 'Bruntál', 'Frýdek-Místek', 'Karviná', 'Nový Jičín', 'Opava', 'Ostrava-město']
```

Elections results will be exported as CSV file.

## Example
Election results for Prostějov:
  
- 1st argument: `Prostějov`
  
- 2nd argument: `vysledky-prostejov.csv`

Running the script:
```
python elections_scraper.py Prostějov vysledky-prostějov.csv
```
Exporting process:
```
Exporting data for Prostějov...
CSV file "vysledky_prostejov.csv" has been created.
```
Partial Output:
```
code,municipality,registered,envelopes,valid, ...
506761,Alojzov,205,145,144,0,0,4,18,0,0,0,17,5,1,0,15,0,6,0,1,29,0,5,32,-,1,0,9,0,1
589268,Bedihošť,834,527,524,0,0,2,34,1,0,0,123,13,14,1,82,1,26,0,2,51,0,6,140,-,0,0,28,0,0
589276,Bílovice-Lutotín,431,279,275,0,0,1,30,0,0,0,40,8,4,0,38,0,22,0,0,13,0,3,83,-,1,0,32,0,0
589284,Biskupice,238,132,131,2,0,2,10,0,0,0,24,5,1,0,19,0,10,0,1,14,0,0,34,-,0,0,9,0,0
...
```
