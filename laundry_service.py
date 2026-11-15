import math


def parse_order(text):
    """Parse 'garment:kg' into (Garment, kg). Returns None for invalid input."""
    if not isinstance(text, str):
        return None
    parts = text.split(':')
    if len(parts) != 2:
        return None
    garment, kg = parts
    try:
        weight = float(kg)
    except ValueError:
        return None
    if not math.isfinite(weight):
        return None
    return garment.strip().title(), weight


def weight_average(weights_csv):
    """Average (floor) of comma-separated integer weights. Returns None for invalid input."""
    if not isinstance(weights_csv, str):
        return None
    try:
        values = [int(r) for r in weights_csv.split(',')]
    except ValueError:
        return None
    if not values:
        return None
    return sum(values) // len(values)


def payable_charge(text):
    """Parse 'charge|discount' and return the charge with 18% tax minus discount (min 0).
    Returns None for invalid input."""
    if not isinstance(text, str):
        return None
    parts = text.split('|')
    if len(parts) != 2:
        return None
    try:
        charge = float(parts[0])
        discount = float(parts[1])
    except ValueError:
        return None
    if not (math.isfinite(charge) and math.isfinite(discount)):
        return None
    total = charge * 1.18 - discount
    if not math.isfinite(total):
        return None
    return max(total, 0)


def main():
    print("==== Running parse_order ====")
    user_input = input("Enter garment:weight in kg (e.g. regular:6): ")
    result = parse_order(user_input)
    print("Garment and Weight:", result)

    print("\n==== Running weight_average ====")
    user_input = input("Enter garment weights as CSV (e.g. 3,5,8): ")
    result = weight_average(user_input)
    print("Average Weight:", result)

    print("\n==== Running payable_charge ====")
    user_input = input("Enter charge|discount (e.g. 300|40): ")
    result = payable_charge(user_input)
    print("Payable Charge:", result)

if __name__ == "__main__":
    main()
