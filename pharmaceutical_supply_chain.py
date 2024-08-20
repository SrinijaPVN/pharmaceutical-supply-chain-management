class PharmaSupplyChain:
    def __init__(self):
        # A dictionary to store transactions with batch number as the key
        self.supply_chain = {}

    def add_transaction(self, batch_number, drug_name, manufacturer, date_of_manufacture, expiry_date, quantity):
        # Add a new transaction to the supply chain
        self.supply_chain[batch_number] = {
            'drug_name': drug_name,
            'manufacturer': manufacturer,
            'date_of_manufacture': date_of_manufacture,
            'expiry_date': expiry_date,
            'quantity': quantity
        }
        print(f"Transaction for batch {batch_number} added successfully.")

    def get_transaction(self, batch_number):
        # Retrieve transaction details by batch number
        transaction = self.supply_chain.get(batch_number)
        if transaction:
            return transaction
        else:
            print(f"No transaction found for batch {batch_number}.")
            return None

def main():
    # Instantiate the PharmaSupplyChain class
    pharma_supply_chain = PharmaSupplyChain()

    while True:
        print("\nPharma Supply Chain System")
        print("1. Add a Transaction")
        print("2. Get a Transaction")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Collect transaction details from user
            batch_number = input("Enter batch number: ")
            drug_name = input("Enter drug name: ")
            manufacturer = input("Enter manufacturer: ")
            date_of_manufacture = input("Enter date of manufacture (YYYY-MM-DD): ")
            expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
            quantity = int(input("Enter quantity: "))
            
            # Add the transaction to the supply chain
            pharma_supply_chain.add_transaction(
                batch_number=batch_number,
                drug_name=drug_name,
                manufacturer=manufacturer,
                date_of_manufacture=date_of_manufacture,
                expiry_date=expiry_date,
                quantity=quantity
            )

        elif choice == '2':
            # Retrieve transaction details
            batch_number = input("Enter batch number to retrieve: ")
            transaction = pharma_supply_chain.get_transaction(batch_number)
            if transaction:
                print(f"Transaction Details for batch {batch_number}:")
                for key, value in transaction.items():
                    print(f"{key}: {value}")

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
