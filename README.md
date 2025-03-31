# HaloPSA API package for Python
Inspired by [homotechsual's Powershell library for HaloPSA](https://docs.homotechsual.dev/modules/haloapi/)

All base endpoints are currently implemented to some extent.  No endpoints have delete functionality yet, as I was worried I would accidentally delete something while testing.

# Installation and setup
## Requirements
1. Python (tested from Python 3.9 to 3.13 right now)
2. HaloPSA API key
3. Some basic understanding of the Halo API (will try to reduce this)

## Installing
```
pip install HaloPSA
```

## Getting an API key from Halo

1. Login to your Halo instance and go to HaloPSA API here: (your tenant).halopsa.com/config/integrations/api
0. Under Applications, click "View Applications"
0. Create a new application, and set type to Client ID and Secret (Service).
0. Name it something memorable, so it doesn't get deleted accidentally.
0. Set login type to Agent and select any agent (Make sure the account you pick has permissions to do the actions you will be using)
0. Make sure that "Active" is ticked and click save (Not: this shouldn't be needed, but I have lost my progress too many times to risk it)
0. Note your Client ID and Secret, you will need these later!
0. Click on the integration/Application you just created and go to Permissions.
0. Set permissions to either All or, if you know what you'll be using, enable just those permissions. (I recommend testing with `all:standard` and then disabling permissions selectively, that way you know your connection is working before you start troubleshooting)
0. Click Save and move on to the next step.
## Getting Started in Python
Now that you have your API information, you can get up and running in Python!

1. Add your API credentials (Highly recommend putting this in a .env file, or literally anywhere other than hardcoded into your script)

```
HALO_CLIENT_ID = [Your Client ID]
HALO_SECRET = [Your Secret]
HALO_TENANT = [Your Halo Instance/tenant]  Eg: https://[THIS PART OF THE URL].halopsa.com
```
2. Import the HaloPSA package

```
from HaloPSA import *
```
Or import only the ones you need (Recommended)
```
from HaloPSA import Clients, Invoices
```
3. Run your first request!

```
users = Users(HALO_TENANT,HALO_ID,HALO_SECRET)
all_users = users.search() # Get all users
for single_user in all_users: # Print each user, one by one
    print(single_user)
```

## Further reading
I highly recommend you check the official Halo API documentation here: https://halo.halopsa.com/apidoc/info and for an even more in depth list, check out the swagger file here: https://halo.halopsa.com/api/swagger/index.html

Feel free to ask questions in the github issues area, I will try my best to answer.
# Endpoints

## Base/Officially documented Endpoints
All base endpoints are now implemented at some level. No endpoints have delete functionality yet.

## Unofficial endpoints
In addition to the base endpoints, the following unofficial endpoints (from the swagger) are implemented at some level
- Distribution Lists
- TopLevel
- Currency
- SoftwareLicences (Subscriptions)
- UserRoles