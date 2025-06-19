import requests

class CurrencyConverter():
    def __init__(self):
        self.amount = 0
        self.from_currency = ""
        self.to_currency = ""
        # App Start
        print("> [amount] [from_currency_type] [to_currency_type]")
        self.user_input = input()
        self.input_processor()

    def converter(self, value, currency_code, convert_to_code):
        try:
            url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{currency_code}.json"
            response = requests.get(url)
            data = response.json()
            output = round(data[currency_code][convert_to_code] * value, 2)
            print(f"{value:,} {currency_code.upper()} = {output:,} {convert_to_code.upper()}".replace(","," "))
        # Exception
        except Exception as e:
            print(f"ERROR: Currency not found: {e}.")

    def input_processor(self):
        input = self.user_input.split(" ")
        if len(input) == 3:
            try:
                self.amount = float(input[0])
                self.from_currency = str(input[1])
                self.to_currency = str(input[2])
                self.converter(self.amount, self.from_currency.lower(), self.to_currency.lower())
            # Exception
            except ValueError as e:
                print("ERROR: Incorrect data types.")
        else:
            print("ERROR: Incorrect amount of arguments.")

if __name__ == "__main__":
    app = CurrencyConverter()