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

sungrowIp = '192.168.178.66'

addressMapping = {
    "Inside  Temperature": 5007,
    "MPPT 1 Voltage": 5010,
    "MPPT 1 Current": 5011,
    "MPPT 2 Voltage": 5012,
    "MPPT 2 Current": 5013,
    "Total DC Power": 5016,
    "Voltage Phase A": 5018,
    "Voltage Phase B": 5019,
    "Voltage Phase C": 5020,
    "Reactive Power": 5032,
    "Power Factor": 5034,
    "Grid Frequency": 5035,
    "System State": 12999,
    "Running State": 13000,
    "Load Power": 13007,
    "Export Power": 13009,
    "Battery Voltage": 13019,
    "Battery Current": 13020,
    "Battery Power": 13021,
    "Battery Level": 13022,
    "Battery State of Health": 13023,
    "Battery Temperature": 13024,
    "Grid State": 13029,
    "Phase A Current": 13030,
    "Phase B Current": 13031,
    "Phase C Current": 13032,
    "Battery Capacity": 13038,
    "Inverter Alarm": 13049,
    "Grid-side Fault": 13051,
    "System Fault 1": 13053,
    "System Fault 2": 13055,
    "DC-side Fault": 13057,
    "Permanent Fault": 13059,
    "BDC-side Fault": 13061,
    "BDC-side Permanent Fault": 13063,
    "Battery Fault": 13065,
    "Battery Alarm": 13067,
    "BMS Alarm": 13069,
    "BMS Protection": 13071,
    "BMS Fault 1": 13073,
    "BMS Fault 2": 13075,
    "BMS Alarm 2": 13077
}

unitMapping = {
    "Inside  Temperature": "°C",
    "MPPT 1 Voltage": "V",
    "MPPT 1 Current": "A",
    "MPPT 2 Voltage": "V",
    "MPPT 2 Current": "A",
    "Total DC Power": "W",
    "Voltage Phase A": "V",
    "Voltage Phase B": "V",
    "Voltage Phase C": "V",
    "Reactive Power": "VAR",
    "Power Factor": "",
    "Grid Frequency": "Hz",
    "System State": "",
    "Running State": "",
    "Load Power": "W",
    "Export Power": "W",
    "Battery Voltage": "V",
    "Battery Current": "A",
    "Battery Power": "W",
    "Battery Level": "%",
    "Battery State of Health": "%",
    "Battery Temperature": "°C",
    "Grid State": "",
    "Phase A Current": "A",
    "Phase B Current": "A",
    "Phase C Current": "A",
    "Battery Capacity": "kWh",
    "Inverter Alarm": "",
    "Grid-side Fault": "",
    "System Fault 1": "",
    "System Fault 2": "",
    "DC-side Fault": "",
    "Permanent Fault": "",
    "BDC-side Fault": "",
    "BDC-side Permanent Fault": "",
    "Battery Fault": "",
    "Battery Alarm": "",
    "BMS Alarm": "",
    "BMS Protection": "",
    "BMS Fault 1": "",
    "BMS Fault 2": "",
    "BMS Alarm 2": ""
}

factorMapping = {
    "Inside  Temperature": 0.1,
    "MPPT 1 Voltage": 0.1,
    "MPPT 1 Current": 0.1,
    "MPPT 2 Voltage": 0.1,
    "MPPT 2 Current": 0.1,
    "Total DC Power": 1,
    "Voltage Phase A": 0.1,
    "Voltage Phase B": 0.1,
    "Voltage Phase C": 0.1,
    "Reactive Power": 1,
    "Power Factor": 0.001,
    "Grid Frequency": 0.1,
    "System State": 1,
    "Running State": 1,
    "Load Power": 1,
    "Export Power": 1,
    "Battery Voltage": 0.1,
    "Battery Current": 0.1,
    "Battery Power": 1,
    "Battery Level": 0.1,
    "Battery State of Health": 0.1,
    "Battery Temperature": 0.1,
    "Grid State": 0.1,
    "Phase A Current": 0.1,
    "Phase B Current": 0.1,
    "Phase C Current": 0.1,
    "Battery Capacity": 0.1,
    "Inverter Alarm": 1,
    "Grid-side Fault": 1,
    "System Fault 1": 1,
    "System Fault 2": 1,
    "DC-side Fault": 1,
    "Permanent Fault": 1,
    "BDC-side Fault": 1,
    "BDC-side Permanent Fault": 1,
    "Battery Fault": 1,
    "Battery Alarm": 1,
    "BMS Alarm": 1,
    "BMS Protection": 1,
    "BMS Fault 1": 1,
    "BMS Fault 2": 1,
    "BMS Alarm 2": 1
}

lengthMapping = {
    "Inside  Temperature": 1,
    "MPPT 1 Voltage": 1,
    "MPPT 1 Current": 1,
    "MPPT 2 Voltage": 1,
    "MPPT 2 Current": 1,
    "Total DC Power": 2,
    "Voltage Phase A": 1,
    "Voltage Phase B": 1,
    "Voltage Phase C": 1,
    "Reactive Power": 2,
    "Power Factor": 1,
    "Grid Frequency": 1,
    "System State": 1,
    "Running State": 1,
    "Load Power": 2,
    "Export Power": 2,
    "Battery Voltage": 1,
    "Battery Current": 1,
    "Battery Power": 1,
    "Battery Level": 1,
    "Battery State of Health": 1,
    "Battery Temperature": 1,
    "Grid State": 1,
    "Phase A Current": 1,
    "Phase B Current": 1,
    "Phase C Current": 1,
    "Battery Capacity": 1,
    "Inverter Alarm": 2,
    "Grid-side Fault": 2,
    "System Fault 1": 2,
    "System Fault 2": 2,
    "DC-side Fault": 2,
    "Permanent Fault": 2,
    "BDC-side Fault": 2,
    "BDC-side Permanent Fault": 2,
    "Battery Fault": 2,
    "Battery Alarm": 2,
    "BMS Alarm": 2,
    "BMS Protection": 2,
    "BMS Fault 1": 2,
    "BMS Fault 2": 2,
    "BMS Alarm 2": 2
}
