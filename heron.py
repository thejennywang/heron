import json
 

def import_transactions():
	# Opening JSON file
	f = open('data.json')
	transactions = json.load(f)
	# Closing file
	f.close()
	return transactions

def main():
   # Import the input transaction data
   transactions = import_transactions()
   print(transactions)

if __name__ =="__main__":
	main()