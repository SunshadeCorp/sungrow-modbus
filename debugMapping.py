'''
1	5007	Inside  Temperature	Temperatur im Wechselrichter	Â°C	int16be	1	0.1	0	value
1	5010	MPPT 1 Voltage	MPPT1 Spannung	V	uint16be	1	0.1	0	value
1	5011	MPPT 1 Current	MPPT1 Strom	A	uint16be	1	0.1	0	value
1	5012	MPPT 2 Voltage	MPPT2 Spannung	V	uint16be	1	0.1	0	value
1	5013	MPPT 2 Current	MPPT2 Strom	A	uint16be	1	0.1	0	value
1	5016	Total DC Power	PV-Leistung aktuell	W	uint32sw	2	1	0	value
1	5018	Spannung Ph A	Spannung Phase A	V	uint16be	1	0.1	0	value
1	5019	Spannung Ph B	Spannung Phase C	V	uint16be	1	0.1	0	value
1	5020	Spannung Ph C	Spannung Phase C	V	uint16be	1	0.1	0	value
1	5032	Reactive Power	Blindleistung	VAÂ®	int32sw	2		0	value
1	5034	Power Factor	Leistungsfaktor		int16be	1	0.001	0	value
1	5035	Grid Frequency	Netzfrequenz	Hz	uint16be	1	0.1	0	value
1	12999	System State	Systemstatus		uint16be	1	1	0	value
1	13000	Running State	Betriebsstatus		uint16be	1	1	0	value
1	13007	Load power 	Wirkleistung gesamt	W	uint32sw	2	1	0	value
1	13009	Export power	Aktuelle Leistung am Ãœbergabepunkt des Versorgungsnetzes	W	int32sw	2	1	0	value
1	13019	Battery voltage	Batteriespannung	V	uint16be	1	0.1	0	value
1	13020	Battery current 	Batteriestrom	A	uint16be	1	0.1	0	value
1	13021	Battery power 	Batterieladeleistung	W	uint16be	1	1	0	value
1	13022	Battery level 	BatteriekapazitÃ¤t	%	uint16be	1	0.1	0	value
1	13023	Battery state of health	Gesundheit der Batterie	%	uint16be	1	0.1	0	value
1	13024	Battery Temperature	Batterietemperatur	Â°C	int16be	1	0.1	0	value
1	13029	Grid state	Netzstatus		int16be	1	0.1	0	value
1	13030	Phase A current	Strom Phase A aktuell	A	uint16be	1	0.1	0	value
1	13031	Phase B current	Strom Phase B aktuell	A	uint16be	1	0.1	0	value
1	13032	Phase C current	Strom Phase C aktuell	A	uint16be	1	0.1	0	value
1	13038	Battery Capacity	Batterie-KapazitÃ¤t	Kwh	uint16be	1	0.1	0	value
1	13049	Inverter alarm	Inverter alarm		uint32sw	2	1	0	value
1	13051	Grid-side fault	Netzfehler		uint32sw	2	1	0	value
1	13053	System fault 1	System Fehler 1		uint32sw	2	1	0	value
1	13055	System fault 2	System Fehler 2		uint32sw	2	1	0	value
1	13057	DC-side fault	Fehler DC-Seitig		uint32sw	2	1	0	value
1	13059	Permanent fault	Permanenter Fehler		uint32sw	2	1	0	value
1	13061	BDC-side fault	BDC-side fault		uint32sw	2	1	0	value
1	13063	BDC-side permanent fault	BDC-side permanent fault		uint32sw	2	1	0	value
1	13065	Battery fault	Batterie Fehler		uint32sw	2	1	0	value
1	13067	Battery alarm	Battery Alarm		uint32sw	2	1	0	value
1	13069	BMS alarm	BMS Alarm		uint32sw	2	1	0	value
1	13071	BMS protection	BMS protection		uint32sw	2	1	0	value
1	13073	BMS fault 1	BMS fault 1		uint32sw	2	1	0	value
1	13075	BMS fault 2	BMS fault 2		uint32sw	2	1	0	value
1	13077	BMS alarm 2	BMS alarm 2		uint32sw	2	1	0	value
'''

sungrowIp = '192.168.0.240'

addressMapping = {
    "Voltage Phase A": 0x80,
    "Voltage Phase B": 0x81,
    "Voltage Phase C": 0x82,
}

unitMapping = {
    "Voltage Phase A": "V",
    "Voltage Phase B": "V",
    "Voltage Phase C": "V",
}

factorMapping = {
    "Voltage Phase A": 0.1,
    "Voltage Phase B": 0.1,
    "Voltage Phase C": 0.1,
}

lengthMapping = {
    "Voltage Phase A": 1,
    "Voltage Phase B": 1,
    "Voltage Phase C": 1,
}
