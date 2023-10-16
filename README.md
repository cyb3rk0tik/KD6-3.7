# KD6-3.7

![1](/kd6-3.7.png)
<i> KD6-3.7 is a character in the Blade Runner universe whose job is to catch old replicant models that can be 
identified by their ID number </i>

## About

Each of us has at least one identification number (ID) that allows governments to distinguish one person from another. 
In many countries IDs are not generated randomly, but according to a certain algorithm.

**KD6-3.7** is able to provide additional information about a person if you have his/her ID. This method can be useful in OSINT investigations when there is not much information about a person.

Currently, it is possible to get additional information about ID holders from the following countries:

| Country                | Types of ID                                          | Options      | Information                                                                                                |
|------------------------|------------------------------------------------------|--------------|------------------------------------------------------------------------------------------------------------|
| Albania                | National Identification Number                       | --nin        | Numri i Identitetit (NID)                                                                                  | 
| Belgium                | National Identification Number; Identity Card Number | --nin; --icn | National Register Number; Identity Card Number                                                             | 
| Bosnia and Herzegovina | National Identification Number                       | --nin        | Unique Master Citizen Number (UMCN)/Jedinstveni matični broj (JMB)/Jedinstveni matični broj građana (JMBG) | 
| Bulgaria               | National Identification Number                       | --nin        | Единен граждански номер (ЕГН)/Edinen grazhdanski nomer (EGN)                                               | 
| Czech Republic         | National Identification Number                       | --nin        | Birth Number/Rodné Číslo (RČ)                                                                              |        
| Denmark                | National Identification Number                       | --nin        | Det Centrale Personregister (CPR-nummer)                                                                   |             
| Estonia                | National Identification Number                       | --nin        | Isikukood (IK)                                                                                             |           
| Finland                | National Identification Number                       | --nin        | Henkilötunnus (HETU)                                                                                       |         
| France                 | Social Security Number                               | --ssn        | Numéro d'inscription au répertoire des personnes physiques (NIRP/NIR)                                      |        
| Slovakia               | National Identification Number                       | --nin        | Birth Number/Rodné Číslo (RČ)                                                                              |    

The list of countries and functionality will be expanded!

## Installation

### Cloning a repository

```bash
# clone and use
git clone https://github.com/duk3r4/KD6-3.7 && cd KD6-3.7
pip3 install -r requirements.txt
```

## Usage

```bash
python kd6-3.7.py -h             
usage: kd6-3.7-test.py [-h] [-c {alb,fin,fra,svk,cze,bgr,dnk,est,bih,bel}] [--nin NIN] [--icn ICN] [--ssn SSN]
                       [-a AUTO]

optional arguments:
  -h, --help            show this help message and exit
  -c {alb,fin,fra,svk,cze,bgr,dnk,est,bih,bel}, --country {alb,fin,fra,svk,cze,bgr,dnk,est,bih,bel}
                        Input country.
  --nin NIN             National Identification Number.
  --icn ICN             Identity Card Number.
  --ssn SSN             Social Security Number.
  -a AUTO, --auto AUTO  Autodetection.
```

### Usage examples

```bash
python kd6-3.7.py -с bel --icn 0106100013  

Here's what I got from that Belguim Identity Card Number:
The card owner is a EU/EEA/Swiss citizen

python kd6-3.7.py -с est --nin 48703230245

Here's what I got from that Estonian National Identification Number:
Day of birth:  23
Month of birth:  March
Year of birth:  1987
Sex:  Female
Sequence number of person with the same date of birth:  24
Checksum symbol:  5
Personal mail for contacting government agencies: 48703230245@eesti.ee

python kd6-3.7.py -a 187112b361052

Here's what I got from that French Social Security Number:
Month of birth:  November
Year of birth:  1987
Sex:  Male
The region of origin:  CORSE / Corse / Corse  ( 94 )
The department of origin:  HAUTE CORSE / Haute-Corse / Haute-Corse  ( 2B )
The commune of origin:  ZILIA / Zilia / Zilia
Sequence number of person with the same date of birth:  5
```

## License

MIT © [KD6-3.7](https://github.com/duk3r4/KD6-3.7)<br/>
