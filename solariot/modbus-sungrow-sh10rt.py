read_register = {
    '5000': 'device_type_code',
    '5001': 'nominal_output_power_10',
    '5003': 'daily_output_energy_10',
    '5004': 'total_output_energy_10',
    '5008': 'inside_temperature_10',
    '5011': 'mppt_1_voltage_10',
    '5012': 'mppt_1_current_10',
    '5013': 'mppt_2_voltage_10',
    '5014': 'mppt_2_current_10',
    '5017': 'total_dc_power',
    '5019': 'spannung_ph_a_10',
    '5020': 'spannung_ph_b_10',
    '5021': 'spannung_ph_c_10',
    '5033': 'reactive_power',
    '5035': 'power_factor_1000.0',
    '5036': 'grid_frequency_10',
    '13000': 'system_state',
    '13001': 'running_state',
    '13002': 'daily_pv_generation_10',
    '13003': 'total_pv_generation',
    '13005': 'daily_export_energy_from_pv_10',
    '13006': 'total_export_energy_from_pv_10',
    '13008': 'load_power',
    '13010': 'export_power',
    '13012': 'daily_battery_charge_energy_from_pv',
    '13013': 'total_battery_charge_energy_from_pv_10',
    '13015': 'co2-reduction_10',
    '13017': 'daily_direct_energy_consumption_10',
    '13018': 'total_direct_energy_consumption_10',
    '13020': 'battery_voltage_10',
    '13021': 'battery_current_10',
    '13022': 'battery_power',
    '13023': 'battery_level_10',
    '13024': 'battery_state_of_health_10',
    '13025': 'battery_temperature_10',
    '13026': 'daily_battery_discharge_energy_10',
    '13027': 'total_battery_discharge_energy_10',
    '13029': 'self-consumption_of_today_10',
    '13030': 'grid_state_10',
    '13031': 'phase_a_current_10',
    '13032': 'phase_b_current_10',
    '13033': 'phase_c_current_10',
    '13034': 'total_active_power',
    '13036': 'daily_import_energy_10',
    '13037': 'total_import_energy_10',
    '13039': 'battery_capacity_10',
    '13040': 'daily_charge_energy_10',
    '13041': 'total_charge_energy_10',
    '13045': 'daily_export_energy_10',
    '13046': 'total_export_energy_10',
    '13050': 'inverter_alarm',
    '13052': 'grid-side_fault',
    '13054': 'system_fault_1',
    '13056': 'system_fault_2',
    '13058': 'dc-side_fault',
    '13060': 'permanent_fault',
    '13062': 'bdc-side_fault',
    '13064': 'bdc-side_permanent_fault',
    '13066': 'battery_fault',
    '13068': 'battery_alarm',
    '13070': 'bms_alarm',
    '13072': 'bms_protection',
    '13074': 'bms_fault_1',
    '13076': 'bms_fault_2',
    '13078': 'bms_alarm_2',
    '6227': 'monthly_pv_energy_yields_january_10',
    '6228': 'monthly_pv_energy_yields_february_10',
    '6229': 'monthly_pv_energy_yields_march_10',
    '6230': 'monthly_pv_energy_yields_april_10',
    '6231': 'monthly_pv_energy_yields_may_10',
    '6232': 'monthly_pv_energy_yields_june_10',
    '6233': 'monthly_pv_energy_yields_july_10',
    '6234': 'monthly_pv_energy_yields_august_10',
    '6235': 'monthly_pv_energy_yields_september_10',
    '6236': 'monthly_pv_energy_yields_october_10',
    '6237': 'monthly_pv_energy_yields_november_10',
    '6238': 'monthly_pv_energy_yields_december_10',
    '6417': 'monthly_direct_energy_consumption_from_pvjanuary_10',
    '6418': 'monthly_direct_energy_consumption_from_pv_february_10',
    '6419': 'monthly_direct_energy_consumption_from_pv_march_10',
    '6420': 'monthly_direct_energy_consumption_from_pv_april_10',
    '6421': 'monthly_direct_energy_consumption_from_pv_may_10',
    '6422': 'monthly_direct_energy_consumption_from_pv_june_10',
    '6423': 'monthly_direct_energy_consumption_from_pv_july_10',
    '6424': 'monthly_direct_energy_consumption_from_pv_august_10',
    '6425': 'monthly_direct_energy_consumption_from_pv_septemper_10',
    '6426': 'monthly_direct_energy_consumption_from_pv_october_10',
    '6427': 'monthly_direct_energy_consumption_from_pv_november_10',
    '6428': 'monthly_direct_energy_consumption_from_pv_december_10',
    '6597': 'monthly_export_energy_from_pv_february_10',
    '6598': 'monthly_export_energy_from_pv_march_10',
    '6599': 'monthly_export_energy_from_pv_april_10',
    '6600': 'monthly_export_energy_from_pv_may_10',
    '6601': 'monthly_export_energy_from_pv_june_10',
    '6602': 'monthly_export_energy_from_pv_july_10',
    '6603': 'monthly_export_energy_from_pv_august_10',
    '6604': 'monthly_export_energy_from_pv_september_10',
    '6605': 'monthly_export_energy_from_pv_october_10',
    '6606': 'monthly_export_energy_from_pv_november_10',
    '6607': 'monthly_export_energy_from_pv_dezember_10',
    '6596': 'monthly_export_energy_from_pv_january_10'
}

holding_register = {
    "5000": "year",
    "5001": "month",
    "5002": "day",
    "5003": "hour",
    "5004": "minute",
    "5005": "second"
}

scan = """{
    "read": [
        {
            "start": "5000",
            "range": "100"
        },
        {
            "start": "13000",
            "range": "100"
        }
  ],
  "holding": [
    {
      "start": "4999",
      "range": "10"
    }
  ]
}"""

# Match Modbus registers to pvoutput api fields
# Reference: https://pvoutput.org/help.html#api-addstatus
pvoutput = {
    "Energy Generation": "daily_power_yield",
    "Power Generation": "total_active_power",
    "Temperature": "internal_temp",
    "Voltage": "grid_voltage_a"
}
