# This is the beginning of my code
while True:
	ussd_code = 966
	if ussd_code == 966:
	 	print("Welcome to Eazybanking by Zenith Bank")
	 	print("1>Open Account\n2>Get a Card\n3>Register\n4>Check Balance\n5>Airtime\n6>Transfer\n7>Self Service\n8>Next\n9>Agent Banking\n10>Bills\n11>Stop Debit on Account\n12>USSD on POS\n13>Eazymoney")
	 	option= eval(input("Please select an option:"))
	 	if option == 1:
	 		print("eaZybanking")
	 		print("Please select an option below:")
	 		print("1>Open Acct For Self\n2>Open Acct For 3rd Party\n3>Create Mobile Wallet\n4>Upgrade Zwallet to Acct\n5>Next")
	 		upper_top = eval(input(":"))
	 		for x in range(0,5):
	 			if x == upper_top:
	 				print('connection Problem or invalid MMI Code')
	 			
	 		if upper_top == 5:
	 			print("eaZybanking\nPlease select an option below:\n1>Retrieve Account Number(s)\n2>Reactivate Dormant Account\n3>Previous")

	 	elif option == 2:
	 		print("Select an Option\n>Get a Virtual Card\n>3Retrieve Card PAN/CVV\n4>Deactivate Card\n5>Reactivate Card")
	 		break
	 	elif option == 3:
	 		print("You already enrolled.Press any no. to start banking.:")
	 		break
	 	elif option == 4:
	 		account_number = eval(input("Enter account number to check balance:"))
	 		balance = 800000000
	 		print("Your account balance is {} Naira".format(balance))

	 		break
	 	elif option == 5:
	 		print('Buy Airtime\n1>Self\n2>Others')
	 		airtime =eval(input(":"))
	 		if airtime == 1:
	 			amount = eval(input("Enter amount:"))
	 			print("Transaction Successful")
	 		if airtime == 2:
	 			my_number = "9061512527"
	 			phone_number = eval(input("Enter Mobile No::"))
	 			amount = input("Enter amount:")
	 			print("You are about to buy Airtime for Phone Number:")
	 			print(phone_number)
	 			print("Amount:{}".format(amount))
	 			assure = eval(input("Enter Pin to Confirm:"))
	 			print("Transaction Successful")
	 			break
	 	elif option == 6:
	 		print("Transfer Funds:\n1>Keystone Bank\n2>Jaiz Bank\n3>Zenith Bank\n4>Other Bank")
	 		transfer = eval(input("select option:"))
	 		for x in range(0,4):
	 			if x == transfer:

	 				amount= eval(input("Enter Amount:"))
	 			
	 				print("You are about to send")
	 				print("Amount:{}".format(amount))
	 			
	 				assure = eval(input("Enter Pin to Confirm:"))
	 				print("Transaction Successful")
	 				
# This is the end of the program

			



