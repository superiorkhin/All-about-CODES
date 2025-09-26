import requests


def main():
    # Prompt user for input
    from_currency = input(
        "Enter the source currency code (e.g., USD): ").strip().upper()
    to_currency = input(
        "Enter the target currency code (e.g., EUR): ").strip().upper()

    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    # API endpoint
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    try:
        response = requests.get(url)
        response.raise_status()  # Raises an HTTPError for bad responses

        data = response.json()

        # Check if the target currency is supported
        if to_currency not in data['rates']:
            print(f"Unsupported target currency: {to_currency}")
            return

        # Get the exchange rate
        exchange_rate = data['rates'][to_currency]
        converted_amount = amount * exchange_rate

        # Display the result
        print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
        print(
            f"Current exchange rate: 1 {from_currency} = {exchange_rate} {to_currency}")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to the API: {e}")
    except KeyError:
        print(f"Unsupported source currency: {from_currency}")


if __name__ == "__main__":
    main()
