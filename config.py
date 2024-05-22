import os

import heron

heron.basic_auth_username = os.getenv("HERON_USERNAME")
heron.basic_auth_password = os.getenv("HERON_PASSWORD")

# Experimental: if you pull from a fintech API, specify it here to get
# automatic conversion into a Heron Data API format. Supported: plaid,
# finicity, yodlee, truelayer
heron.provider = "plaid"