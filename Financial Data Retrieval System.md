# Financial Data Retrieval System 🐍

![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.](https://quickbooks.intuit.com/oidam/intuit/sbseg/en_us/Blog/Graphic/accounting-automation-header-image-us-en.png)

### ✳️ Description:
You are tasked with developing a Financial Data Retrieval System that interacts with external APIs to retrieve information about currencies and company shares. This system will be used to provide users with up-to-date financial data for analysis and decision-making.


    
### ✳️ Requirements for Each Method:
1. get_currency_exchange_rate(base_currency, target_currency): This method should retrieve the current exchange rate between two currencies using the currency API. It should take the base currency and target currency as parameters and return the exchange rate.
2. get_company_share_price(company_symbol): This method should retrieve the current price of shares for a given company using the share API. It should take the company symbol as a parameter and return the share price.
3. get_currency_conversion(amount, base_currency, target_currency): This method should convert the given amount from one currency to another based on the current exchange rate. It should take the amount, base currency, and target currency as parameters and return the converted amount.
4. get_company_info(company_symbol): This method should retrieve additional information about a company (e.g., name, sector) using the share API. It should take the company symbol as a parameter and return the company information.
5. get_top_gainers(): This method should retrieve the top gaining companies from the share API. It should return information about the top gainers.
6. get_top_losers(): This method should retrieve the top losing companies from the share API. It should return information about the top losers.

   
### Now, let's write the code for this project:
```python

import requests

class FinancialDataRetrievalSystem:
    def __init__(self, currency_api_key, share_api_key):
        # Initialize attributes
        pass

    def get_currency_exchange_rate(self, base_currency, target_currency):
        # Retrieve the current exchange rate between two currencies using the currency API
        pass

    def get_company_share_price(self, company_symbol):
        # Retrieve the current price of shares for a given company using the share API
        pass

    def get_currency_conversion(self, amount, base_currency, target_currency):
        # Convert the given amount from one currency to another
        pass

    def get_company_info(self, company_symbol):
        # Retrieve additional information about a company (e.g., name, sector) using the share API
        pass

    def get_top_gainers(self):
        # Retrieve the top gaining companies from the share API
        pass

    def get_top_losers(self):
        # Retrieve the top losing companies from the share API
        pass

# Example usage of the Financial Data Retrieval System
if __name__ == "__main__":
    # Configure API keys
    currency_api_key = 'YOUR_CURRENCY_API_KEY'
    share_api_key = 'YOUR_SHARE_API_KEY'
    
    # Initialize the FinancialDataRetrievalSystem object
    financial_system = FinancialDataRetrievalSystem(currency_api_key, share_api_key)

    # Call methods of the FinancialDataRetrievalSystem object as needed...


```
