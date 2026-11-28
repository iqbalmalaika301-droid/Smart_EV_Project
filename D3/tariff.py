def get_tariff_for_units(total_units, tariff_rows):
    for row in tariff_rows:
        minimum_units = float(row[0])
        maximum_units = float(row[1])

        if minimum_units <= total_units <= maximum_units:
            return row

    return None


def is_peak_hour(hour, tariff_row):
    peak_start = int(tariff_row[6])
    peak_end = int(tariff_row[7])

    return peak_start <= hour < peak_end


def calculate_energy_charge(peak_kwh, offpeak_kwh, total_units, tariff_rows):
    tariff_row = get_tariff_for_units(total_units, tariff_rows)

    if tariff_row is None:
        return None

    peak_rate = float(tariff_row[2])
    offpeak_rate = float(tariff_row[3])

    return (peak_kwh * peak_rate) + (offpeak_kwh * offpeak_rate)


def calculate_fixed_charge(total_units, tariff_rows):
    tariff_row = get_tariff_for_units(total_units, tariff_rows)

    if tariff_row is None:
        return None

    return float(tariff_row[4])


def calculate_tax_percent(total_units, tariff_rows):
    tariff_row = get_tariff_for_units(total_units, tariff_rows)

    if tariff_row is None:
        return None

    return float(tariff_row[5])


def calculate_tax_amount(subtotal, tax_percent):
    return subtotal * tax_percent / 100


def calculate_total_bill(energy_charge, fixed_charge, tax_percent):
    subtotal = energy_charge + fixed_charge
    tax_amount = calculate_tax_amount(subtotal, tax_percent)

    return subtotal + tax_amount
