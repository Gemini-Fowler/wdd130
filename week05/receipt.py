import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    products_dict = {}
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                key = row[key_column_index]
                products_dict[key] = [row[0], row[1], float(row[2])]
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except PermissionError:
        print(f"Error: Permission denied when accessing '{filename}'.")
        return None
    return products_dict

def calculate_discount(quantity, price):
    full_price_items = quantity // 2 + quantity % 2
    discounted_items = quantity // 2
    total = (full_price_items * price) + (discounted_items * price * 0.5)
    return total

def print_receipt(products_dict):
    subtotal = 0
    total_items = 0
    TAX_RATE = 0.06

    try:
        with open('request.csv', mode='r') as file:
            reader = csv.reader(file)
            next(reader)

            print("\n==== ABC Grocery Store ====")
            print("Items Purchased:")

            for row in reader:
                product_number = row[0]
                quantity = int(row[1])
                product = products_dict.get(product_number)

                if product is None:
                    raise KeyError(f"Product {product_number} not found.")

                product_name = product[1]
                product_price = product[2]

                if product_number == "D083":
                    item_total = calculate_discount(quantity, product_price)
                    print(f"{product_name}: {quantity} @ ${product_price:.2f}, Discounted Total = ${item_total:.2f}")
                else:
                    item_total = quantity * product_price
                    print(f"{product_name}: {quantity} @ ${product_price:.2f} each = ${item_total:.2f}")

                subtotal += item_total
                total_items += quantity

            tax = subtotal * TAX_RATE
            total = subtotal + tax

            print("\n---------------------------")
            print(f"Number of items: {total_items}")
            print(f"Subtotal: ${subtotal:.2f}")
            print(f"Sales Tax (6%): ${tax:.2f}")
            print(f"Total: ${total:.2f}")
            print("---------------------------")

            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Date: {current_time}")
            print("\nThank you for shopping at ABC Grocery Store!")
    
    except FileNotFoundError:
        print("Error: The file 'request.csv' was not found.")
    except PermissionError:
        print("Error: Permission denied when accessing 'request.csv'.")
    except KeyError as e:
        print(e)

def main():
    products_dict = read_dictionary('products.csv', 0)
    if products_dict is not None:
        print_receipt(products_dict)

if __name__ == "__main__":
    main()
