import csv
import json

def calculate_egfr(scr, age, sex):
    # Variables based on the 2021 CKD-EPI Equation from your prompt
    c = 142
    if sex.lower() == 'female':
        k, a, gender_multiplier = 0.7, -0.241, 1.012
    else:
        k, a, gender_multiplier = 0.9, -0.302, 1.0

    # The formula: c * min(scr/k, 1)**a * max(scr/k, 1)**-1.200 * 0.9938**age * gender_multiplier
    term1 = min(scr / k, 1) ** a
    term2 = max(scr / k, 1) ** -1.200
    term3 = 0.9938 ** age

    egfr = c * term1 * term2 * term3 * gender_multiplier
    return egfr

def main():
    # 1. Load Demographics
    try:
        with open('patient_demographics.csv', mode='r') as f:
            demographics = list(csv.DictReader(f))

        # 2. Load JSON Lab Results
        with open('cmp.json', 'r') as f:
            labs = json.load(f)
    except FileNotFoundError:
        print("Error: Make sure patient_demographics.csv and cmp.json are in your CKD_Project folder!")
        return

    results = []

    # 3. Process each patient
    for patient in demographics:
        p_id = patient['patient_id']
        scr = 0

        # Safety check: ensures labs is a list and finds the matching patient
        if isinstance(labs, list):
            for entry in labs:
                if isinstance(entry, dict) and entry.get('patient_id') == p_id:
                    scr = float(entry.get('serum_creatinine', 0))
                    break

        # Only calculate if we found a lab result
        if scr > 0:
            age = float(patient['age'])
            sex = patient['sex']

            egfr_val = calculate_egfr(scr, age, sex)

            if egfr_val <= 65:
                results.append({
                    'Patient ID': p_id,
                    'patient full name': f"{patient['first_name']} {patient['last_name']}",
                    'patient mobile phone number': patient['phone_number'],
                    'calculated eGFR': round(egfr_val, 2)
                })

    # 4. Save to results.csv
    keys = ['Patient ID', 'patient full name', 'patient mobile phone number', 'calculated eGFR']
    with open('results.csv', 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)

    print("Success! 'results.csv' has been created.")

if __name__ == "__main__":
    main()
