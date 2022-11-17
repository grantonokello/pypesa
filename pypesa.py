from pypesa.vodacome import MPESA

api_key = "" # your api key
public_key = "" # your public key

# intialise mpesa api
m_pesa = MPESA(api_key=api_key, public_key=public_key)

# costomer data C2B
def c2b(amount, number, item):
    parameters = {
        'input_Amount': amount,  # amount to be charged atleast 10
        'input_Country': 'TZN',  # input your country
        'input_Currency': 'TZS',  # input your currency
        'input_CustomerMSISDN': number,
        'input_ServiceProviderCode': '000000',  # get service provider code from the portal
        'input_ThirdPartyConversationID': 'c9e794e10c63479992a8b08703abeea36',
        'input_TransactionReference': 'T23434ZE3',  # get transactionReference code from the portal
        'input_PurchasedItemsDesc': item
    }


response = m_pesa.customer2business(parameters)


# query transaction status
def status():
    parameters = {
        'input_QueryReference': '000000000000000000001',  # input reference code
        'input_ServiceProviderCode': '000000',  # get service provider code from the portal
        'input_ThirdPartyConversationID': 'asv02e5958774f7ba228d83d0d689761',
        # get third party conversation id from the portal
        'input_Country': 'TZN'  # your country
    }
    results = m_pesa.status(parameters)

