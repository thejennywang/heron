import json
import pandas as pd

def import_transactions():
	# Opening JSON file
	transactions = pd.read_json('data.json')
	transactions = pd.DataFrame.from_records(transactions['transactions'])

	transactions['date'] = pd.to_datetime(transactions['date'])
	transactions = transactions.set_index('date')

	return transactions

def main():
   # Import the input transaction data
   transactions = import_transactions()
   # print(transactions)

   monthly_reoccuring = transactions.groupby(pd.Grouper(freq='ME'))
   print(monthly_reoccuring.first())

   description_reoccuring = transactions.groupby(transactions.duplicated(subset=['description']))
   print(description_reoccuring.first())


if __name__ =="__main__":
	main()