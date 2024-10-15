# Entirely re-written with classes

# Apparently this is very, very bad

# Modules to interact with Halo.
# Some modules use specifc IDs, will try to clean this up as I go.

import requests
import urllib.parse
import json
import os

def gentleError(Text='Undefined Error'):
    print('[ERROR]',Text)
    exit()

# CONSTANTS
HALO_CLIENT_ID = os.getenv("HALO_CLIENT_ID") 
HALO_SECRET = os.getenv('HALO_SECRET') 
HALO_API_URL = os.getenv('HALO_API_URL') 
HALO_AUTH_URL = os.getenv('HALO_AUTH_URL')

assetURL = HALO_API_URL+ '/asset/'


# Confirm variables are present
nodata = [None,'']
if HALO_CLIENT_ID in nodata or HALO_SECRET in nodata or HALO_API_URL in nodata or HALO_AUTH_URL in nodata:
    gentleError('Missing env file, Fill out "example.env" and rename to ".env"')  


def responseParser(request,Verbose=False):
    """ Halo Response parser(?)

    Args:
        request (requests.models.Response): Halo API request
        Verbose (bool, optional): Return extra details about response. Defaults to False.

    Returns:
        any: API content and non critical error messages
    """
    code = request.status_code
    
    # Invalid URL
    if code in [404]:
        gentleError(f'404 -  The specified URL is invalid. URL: {request.url}')
    content = json.loads(request.content)
    
    # Success
    if code in [200,201]:
        # 201 = Created
        # 200 = OK
        if Verbose==True:
            return request.reason, content
        else:
            return content

    elif code in [401]:
        # Return clearer errors
        if content["error_description"] == 'The specified client credentials are invalid.':
            # Specify it is the client secret that is wrong, not the client ID.
            gentleError('The specified \'client_secret\' is invalid')
        else:
            gentleError(content["error_description"])
            
    # Add unique failures as found
    # If secret, client ID, or URL are wrong, error 401 is returned
    else:
        if Verbose==True:
            return 'Error',f'{code} - Other failure'
        else:
            return f'{code} - Other failure'


def createToken():
    # Return auth token from Halo. 
    authheader = { # Required by Halo, don't ask me why
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    payload = { # Create payload for Halo auth
    'grant_type': 'client_credentials',
    'client_id': HALO_CLIENT_ID,
    'client_secret': HALO_SECRET,
    'scope': 'all' 
    }
    
    request = requests.post(HALO_AUTH_URL, headers=authheader, data=urllib.parse.urlencode(payload)) # Request auth token
    response = responseParser(request,True)
    if response[0] == 'OK':
        return response[1]['access_token']
    else:
        return response

mainToken = createToken()


class asset():
    """ Asset actions 
    Initialize by running this once on its own, then run actions"""
    def __init__(self):
        token = createToken() # Maybe this can be moved out?
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
            }
    
    
    def get(self,id):
        """Get halo asset information

        Args:
            id (int): Halo Asset ID

        Returns:
            list: Halo asset details
        """    
        request = requests.get(assetURL + str(id) +'?includedetails=True', headers = self.headerJSON)
        return responseParser(request)

            

    
    def getAll(self):
        """Get all halo assets

        Returns:
            list: List of assets OR error
        """        
        request = requests.get(assetURL, headers = self.headerJSON)
        return responseParser(request)
    
    def search(self,query):
        """ Search Halo assets 
        DOES NOT DO ANYTHING RIGHT NOW """
        pass
    
    def update(self,payload):
        """ Update asset.  ID provided in Payload (for now.) 
        Payload should be formatted with json.dumps, will move that bit in here eventually."""
        
        # Allow retries in case connection times out (Have not seen this happen until today 11.04.2024)
        attempts = 0
        processed = False
        while attempts < 5 and processed == False:
            try:
                request = requests.post(assetURL, headers = self.headerJSON, data=payload)
                processed = True
            except:
                attempts +=1
        if processed != True:
            gentleError('Connection error')
        else:
            return responseParser(request)
    
    def updateRaw(self,deviceID,fields,**data):
        """ Working on it """
        payload = json.dumps([{ # Device update payload
        "_dontaddnewfields": True if data['addNewFields'] is None else data['addNewFields'],
        "isassetdetails": True if data['isAssetDetails'] is None else data['isAssetDetails'],
        "fields": fields,
        "id": f"{deviceID}", # Device ID
        "users": data['User'] if data['User'] is not None else ''}])

  
class ticket():
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
            }
    
    def create(self, payload):
        """ Create a ticket 
        Payload must be formatted for now, will create a formatting tool later"""
        request = requests.post(HALO_API_URL+ '/tickets/', headers = self.headerJSON, data=payload)
        return responseParser(request)

    def search(self,query):
        """ Search ticket using Query (Later query will be its own thing so its easier to use) """
        query = urllib.parse.urlencode(query)
        request = requests.get(HALO_API_URL+ '/tickets?' + query, headers = self.headerJSON)

        return responseParser(request)
    
    def merge(self,existingID,newID):
        """Merge two tickets

        Args:
            existingID (INT): ID of old ticket
            newID (INT): ID of ticket old ticket should be merged into

        Returns:
            JOSN: JSON formatted payload (merges, no need to send this anywhere)
        """        
        payload = json.dumps([{
        'id': existingID,# Marks ticket as completed.
        'merged_into_id': newID 
        }])
        self.create(payload)
        return payload
    
    def updateStatus(self,ID,statusID=20):
        """Update ticket status(es)

        Args:
            ID (int,list): ID(s) of ticket to be updated
            statusID (int, optional): ID of new status to be set. Defaults to 20 (this completes tickets for us).
        
        Returns:
            List of payloads (these are sent, payload sent as record for now.)
        """
        payloads = []
        if type(ID) is not list:
            ID = [ID]
        for ticID in ID:
            payload = json.dumps([{
                    'id': ticID,
                    'status_id': str(statusID) # Mark ticket as completed.
                    }])
            self.create(payload)
            payloads+= payload
            
        return payloads





def userSearch(query):
    """ Searches for a user """
    headers = { # Header with token
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + mainToken
        }
    request = requests.get(HALO_API_URL+ '/users?' + urllib.parse.urlencode(query), headers = headers)
    if request.status_code != 200:
        return 'Failed to get users'
    response = json.loads(request.content)
    return response


def invoiceActivator(ids=None):
    """ Set invoices to Active
    If no IDs are sent, all invoices will be set to Active """
    headers = { # Header with token
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + mainToken
        }
    query = {
        'type': 54,
    }
    request = requests.get(HALO_API_URL+ '/Template', headers = headers,params = query)
    if request.status_code != 200:
        return 'Failed to get Templates'
    response = json.loads(request.content)
    for invoice in response:
        print(invoice['id'])
        if invoice == 'more':
            invoice = invoice['more']
        if invoice['disabled'] == True:
            data = json.dumps([{
                'disabled': False,
                'end_date': '1901-01-01T00:00:00.000Z',
                'id':invoice['id']
                
            }])
            updateAttempt = requests.post(HALO_API_URL+ '/Template', headers = headers,data = data)
            if updateAttempt.status_code !=[200,201]:
                print('Failed')
            else:
                print(f'Updated {invoice["id"]}')
    return response


def manualTokenUpdate(key,id):
    """ Manually update tokens for halo integrations.

    Make sure you have the integration type set to bearer token :)"""
    headers = { # Header with token
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + mainToken
        }
    payload = json.dumps([{
        "new_client_secret": str(key),
        "id": id 
    }])
    attemptUpdate = requests.post(HALO_API_URL+ '/CustomIntegration', headers = headers, data=payload)
    return attemptUpdate


class currency():
    """ Check currency information
    
    Useful to convert pricing from secondary currency to primary currency.
    """
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
        }
    
    def getAll(self):
        """ 
        Get all active currencies
        """
        request = requests.get(HALO_API_URL + '/Currency', headers = self.headerJSON)
        return responseParser(request)
        

class items():
    """ Products (items) API 
    """
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
        }
    def getAll(self):
        pass
    
    def getDetails(self, item):
        """ Get details about an item

        Args:
            item INT: Item ID

        Returns:
            Dictionay: Item details
        """
        request = requests.get(HALO_API_URL + '/item/' + str(item) + '?includedetails=true', headers = self.headerJSON)
        return responseParser(request)
        
    def search(self, query):
        """ Search for an item

        Args:
            query DICT: Query dictionary

        Returns:
            Dictionary: Hopefully a list of items?
        """
        query = urllib.parse.urlencode(query)
        request = requests.get(HALO_API_URL+ '/item?' + query, headers = self.headerJSON)
        return responseParser(request)
    
    def create(self, payload):
        pass
    
    def update(self, payload):
        """ Update an existing item

        Args:
            payload DICT: Dictionary containing the fields that need updating

        Returns:
            Im not sure: Hopefully just a code saying SUCCESS?
        """
        payload = json.dumps([payload])
        
        postRequest = requests.post(HALO_API_URL+ '/item', headers = self.headerJSON, data = payload)
        return responseParser(postRequest)


class invoices():
    """Invoice endpoint(?)
    """
    
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
        }
    
    def searchRecurring(self, query):
        """ Search for a recurring invoice

        Args:
            query DICT: Query dictionary

        Returns:
            Dictionary: Hopefully a list of recurring invoices
        """
        query = urllib.parse.urlencode(query)
        request = requests.get(HALO_API_URL+ '/recurringinvoice?' + query, headers = self.headerJSON)
        return responseParser(request)


### OLD SHIT ###

def productUpdate(updateField,originalText,replacementText):
    """ Update a halo product by value. 
    Requires token, field to search on/update, text to search, text to replace with.
    """
    headers = { # Header with token
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + mainToken
        }
    def updateItemByID(ID,originalStr):
        payload = json.dumps([{
        updateField: originalStr.replace(originalText,replacementText),
        "id": ID
        }])
        attemptUpdate = requests.post(HALO_API_URL+ '/item', headers = headers, data=payload)
        return attemptUpdate.status_code

    request = requests.get(HALO_API_URL+ '/item', headers = headers)
    itemsList = json.loads(request.content)['items']
    for item in itemsList:
        if item == 'more': # Shows only 100 by default, this allows it to cycle through the remaining ones 
            item = item['more']
        if updateField in item:
            if originalText in item[updateField]:
                print(f'[{item["id"]}] {item["name"]}\n - {item[updateField]}') # Original string
                attemptUpdate = updateItemByID(item["id"],item[updateField])
                print(attemptUpdate) # Status of attempted assetUpdate
                



class payloadCreator():
    def PayloadCreator(ticketString,existingTicketID=False,action='alert',**extras): # Sends payload to halo and creates ticket
        if False:
            if True:
                pass
            elif existingTicketID is not False:
                payload = json.dumps([{
                'id': existingTicketID[0],
                "summary": ticketString,
                'apply_rules': 'true',
                "details": f"Previous Summary {existingTicketID[1]}", # HTML formatted info
                'status_id':'23', # Needs update
                }])
            else:
                payload = json.dumps([{
                    "tickettype_id": "21" if action == 'alert' else action, # Alert ticket type
                    "client_id": device['client_id'], # Client ID 
                    "site_id": device['site_id'], # Site ID
                    "summary": ticketString, #Ticket Subject
                    "details_html": f"<p> </p>", # HTML formatted info
                    "assets": [
                        {
                            "id": device['id'],  # Asset
                        }
                    ],
                    "user_id": userID,
                    "donotapplytemplateintheapi": True, # Is this needed
                    "form_id": "newticketf3f2abad-8df2-48b4-90ba-39b073c27c84", # Is this needed
                    "dont_do_rules": True, # Is this needed
                    }])
            print(existingTicketID)


def productDB():
    #TODO create DB for products to allow for easier searching, updating, etc.
    sqlQuery = "INSERT OR UPDATE OR IGNORE INTO (tbd) values=()"
    sqlData = ""
    pass

### Testing the above tool
# originalText = 'for (contract start date) - (contract end date) - billed monthly'
# newText = 'for contract period $CONTRACTSTARTDATE - $CONTRACTENDDATE (billed monthly)'
# productUpdate(getHaloToken(),'description',originalText,newText)

