
import math


def parse_claim(text):
    try:
        if not isinstance(text, str):
            return None

        parts = text.split(':')

        if len(parts) != 2:
            return None

        plan, months = parts

        plan = plan.strip()
        months = float(months.strip())

        if not plan or not math.isfinite(months) or months < 0:
            return None

        return plan.title(), months

    except (ValueError, TypeError, OverflowError):
        return None


def age_average(ages_csv):
    try:
        if not isinstance(ages_csv, str) or not ages_csv.strip():
            return None

        parts = ages_csv.split(',')
        values = [int(r.strip()) for r in parts]

        if any(age < 0 for age in values):
            return None

        return sum(values) // len(values)

    except (ValueError, TypeError, OverflowError):
        return None


def payable_charge(text):
    try:
        if not isinstance(text, str):
            return None

        parts = text.split('|')

        if len(parts) != 2:
            return None

        charge, discount = parts

        charge = float(charge.strip())
        discount = float(discount.strip())

        if not math.isfinite(charge) or not math.isfinite(discount):
            return None

        if charge < 0 or discount < 0:
            return None

        total = charge * 1.18 - discount

        return max(total, 0)

    except (ValueError, TypeError, OverflowError):
        return None


def main():
    print("==== Running parse_claim ====")
    user_input = input("Enter plan:age in months (e.g. standard:30): ")
    result = parse_claim(user_input)
    print("Plan and Age:", result)

    print("\n==== Running age_average ====")
    user_input = input("Enter product ages as CSV (e.g. 12,24,36): ")
    result = age_average(user_input)
    print("Average Age:", result)

    print("\n==== Running payable_charge ====")
    user_input = input("Enter charge|discount (e.g. 1500|200): ")
    result = payable_charge(user_input)
    print("Payable Charge:", result)


if __name__ == "__main__":
    main()
