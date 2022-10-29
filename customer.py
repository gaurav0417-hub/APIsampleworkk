#Create a Customer

#The following endpoint creates or add a customer with basic details such as name and contact details. You can use this API for various Razorpay Solution offerings.

# Post / customers


import razorpay
client = razorpay.Client(auth=("YOUR_ID", "YOUR_SECRET"))

client.customer.create({
  "name": "Gaurav Kotecha",
  "contact": 9123456780,
  "email": "gaurav.k@example.com",
  "fail_existing": 0,
  "gstin": "29XAbbA4369J1PA",
  "notes": {
    "notes_key_1": "Tea, Earl Grey, Hot",
    "notes_key_2": "Tea, Earl Grey… decaf."
  }
})

