import json
import pandas as pd

def import_transactions():
	# Opening JSON file
	transactions = pd.read_json('data.json')
	transactions = pd.DataFrame.from_records(transactions['transactions'])

	transactions['date'] = pd.to_datetime(transactions['date'])
	transactions = transactions.set_index('date')
	#transactions = pd.json_normalize(transactions)

	#for i, t in enumerate(transactions):
		#transactions[i].index = pd.to_datetime(transactions[i]['date'])
		#print(transactions[i]['date'])
		#transactions[i]['date'] = pd.to_datetime(transactions[i]['date'])
		# transactions[i] = transactions[i]['date'] = 
	#f = open('data.json')
	#transactions = json.load(f)
	# Closing file
	#f.close()
	# print(transactions)
	return transactions

def main():
   # Import the input transaction data
   transactions = import_transactions()
   # print(transactions)

   monthly_reoccuring = transactions.groupby(pd.Grouper(freq='ME'))
   print(monthly_reoccuring)

if __name__ =="__main__":
	main()