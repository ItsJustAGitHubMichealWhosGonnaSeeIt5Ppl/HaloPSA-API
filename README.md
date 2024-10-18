# HaloPSA API package for Python
EXTREMELY EARLY STAGE DEVELOPMENT.  READ CURRENTLY WORKING ENDPOINTS BEFORE TRYING ANYTHING!

For everyone's safety, none of the delete functions currently work.  This will be fixed/updated later.

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
0. Set permissions to either All or, if you know what you'll be using, enable just those permissions. (I recommend testing with All and then disabling permissions selectively, that way you know your connection is working before you start troubleshooting)
0. Click Save and move on to setting up your .env file.
## Setting up your .env file
1. Create a .env file with the following lines
```
HALO_CLIENT_ID = [Your Client ID]
HALO_SECRET = [Your Secret]
HALO_API_URL = https://[Your Halo Instance].halopsa.com/api
HALO_AUTH_URL = https://[Your Halo Instance].halopsa.com/auth/token
```
Now you're ready to go!

## Usage
Because of the way Halo is designed, anything you can do in the web interface, can be done from the API (and hopefully one day from this Python package too).

You can either import every endpoint

```
import HaloPSA.Halo
```
Or import only the ones you need (Full list below)
```
from HaloPSA.Halo import clients, invoices
```
I highly recommend you check the official Halo API documentation here: https://halo.halopsa.com/apidoc/info and for an even more in depth list, check out the swagger file here: https://halo.halopsa.com/api/swagger/index.html

Feel free to ask questions in the github issues area, I will try my best to answer.
# Endpoints
I am implementing these as I need them, and trying to keep them as consistent and easy to understand as possible.

## Partially implemented
### Assets
You Halo assets
#### Get
Working, has docstring.
### Search
Working, has docstring.
#### GetAll 
Working, but planning to remove this as you can just use search with no variables to get the same result.
#### Update (create)
Creates or updates one or more assets.  If ID is included, asset(s) will be updated.  If ID is not included, new asset(s) will be created.
- Working but requires "fields" to be sent in a specific JSON-like format.  Working on a better solution.  Has docstring.
#### Delete
Not implemented.
### Clients
You customers/clients
#### Get
Working, has docstring.
#### Search
Working, has docstring.
#### Update
Not implemented.
#### Delete
Not implemented.
### Recurring Invoices*
*Not in official documentation, found in Swagger + checking API calls from browser.
#### Get
Not implemented.
#### Search
Working, needs better docstring.
#### Update
Not implemented.
#### UpdateLines
Technically working, needs documentation and docstring.
#### Delete
Not implemented.
###Sites
#### Get
Not implemented.
#### Search
Implemented, has docstring.
#### Update
Not implemented.
#### Delete
Not implemented.


## Not implemented
### Planning to implement soon/Implemented in a previous version
- Currency
- Tickets
- Items
- Invoices
### Low Priority (if not listed, assume here)
- Actions
- Users
