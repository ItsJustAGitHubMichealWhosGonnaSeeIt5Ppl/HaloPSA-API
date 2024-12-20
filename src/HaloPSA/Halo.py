# Entirely re-written with classes
# Modules to interact with Halo.
# Some modules use specifc IDs, will try to clean this up as I go.

import requests
import urllib.parse
import json
import os
from HaloPSA.functions import apiCaller


# CONSTANTS
HALO_CLIENT_ID = os.getenv("HALO_CLIENT_ID") 
HALO_SECRET = os.getenv('HALO_SECRET') 
HALO_API_URL = os.getenv('HALO_API_URL') 
HALO_AUTH_URL = os.getenv('HALO_AUTH_URL')



# Confirm variables are present
nodata = [None,'']
if HALO_CLIENT_ID in nodata or HALO_SECRET in nodata or HALO_API_URL in nodata or HALO_AUTH_URL in nodata:
    raise('Missing env file, Fill out "example.env" and rename to ".env"')  


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
    responseR = request.reason
    if responseR == 'OK':
        content = json.loads(request.content)
        return content['access_token']
    else:
        return print('Error')



#### Classes

class actions: # Placeholder
    def search():
        pass
    def get():
        pass
    def update():
        """Update one or more actions"""
        pass
    def delete():
        pass
    

class assets: 
    """ Asset actions 
    Initialize by running this once on its own, then run actions"""
    def __init__(self):
        token = createToken() # Maybe this can be moved out?
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
            }
        self.formattedParams = []


    def get(self,
            id:int,
            includedetails:bool=True,
            includediagramdetails:bool=False,
            **others
            ):
        """
        Get a single asset's details.
        Supports all Halo parameters, even if not listed.  
        Requires atleast ID to be provided
        Args:
            id (int): Asset ID
            includedetails (bool, optional): Whether to include extra details (objects) in the response. Defaults to True.
            includediagramdetails (bool, optional): Whether to include diagram details in the response. Defaults to False.

        Returns:
            dict: Single asset details
        """

        newVars = locals().copy()
        request = apiCaller(HALO_API_URL,'get','Asset',newVars,self.headerJSON)
        response = request.getData()
        return response
    
    
    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        ticket_id:int=None,
        client_id:int=None,
        site_id:int=None,
        username:str=None,
        assetgroup_id:int=None,
        assettype_id:int=None,
        linkedto_id:int=None,
        includeinactive:bool=None,
        includeactive:bool=None,
        includechildren:bool=None,
        contract_id:int=None,
        **others
    ):
        """Search Assets.
        Supports all Halo parameters, even if not listed.  
        Running with no parameters will get all assets.

        Args:
            paginate (bool, optional): Whether to use Pagination in the response. Defaults to False.
            page_size (int, optional): When using Pagination, the size of the page. Defaults to 50.
            page_no (int, optional): When using Pagination, the page number to return. Defaults to 1.
            order (str, optional): The name of the field to order by.
            orderdesc (bool, optional): Whether to order ascending or descending. Defaults to decending sort.
            search (str, optional): Filter by Assets with an asset field like your search.
            ticket_id (int, optional): Filter by Assets belonging to a particular ticket. 
            client_id (int, optional): 	Filter by Assets belonging to a particular client.
            site_id (int, optional): Filter by Assets belonging to a particular site.
            username (str, optional): Filter by Assets belonging to a particular user. 
            assetgroup_id (int, optional): Filter by Assets belonging to a particular Asset group. 
            assettype_id (int, optional): Filter by Assets belonging to a particular Asset type. 
            linkedto_id (int, optional): Filter by Assets linked to a particular Asset. 
            includeinactive (bool, optional): Include inactive Assets in the response. Defaults to False/No.
            includeactive (bool, optional): Include active Assets in the response. Defaults to True/Yes.
            includechildren (bool, optional): Include child Assets in the response. Defaults to False/No.
            contract_id (int, optional): Filter by Assets assigned to a particular contract.
            
        Returns:
            dict: Search results.
        """
        
        newVars = locals().copy()
        request = apiCaller(HALO_API_URL,'search','Asset',newVars,self.headerJSON)
        response = request.getData()
        return response
    
    def getAll(self):
        """Get all halo assets

        Returns:
            list: List of assets OR error
        """
        print('Removing this, use search with no parameters instead')
        request = apiCaller(HALO_API_URL,'search','Asset',{},self.headerJSON)
        response = request.getData()
        return response
        
    def update(self,
        id:int=None,
        client_id:int=None,
        site_id:int=None,
        users:list=None,
        fields:list=None,
        queueMode:str='disabled',
        **others
               ):
        """Creates or updates one or more assets.  If ID is included, asset(s) will be updated.  If ID is not included new asset(s) will be created.

        Args:
            id (int, optional): Asset ID.
            client_id (int, optional): Client ID. 
            site_id (int, optional): Site ID. 
            users (list, optional): User IDs. 
            fields (list, optional): Fields to be updated.
            queueMode (str, optional): Queue asset data to be sent as a batch update.  Valid modes: disabled - Default, will update asset immediately. queue

        Returns:
            _type_: I dont think it returns anything...
        """
        if queueMode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queueMode} is not a valid Queue Mode.')
        
        newVars = locals().copy()
        
        if queueMode == 'disabled': # Sent request immediately
            request = apiCaller(HALO_API_URL,'update','Asset',newVars,self.headerJSON)
            response = request.getData()
            return response
        
        elif queueMode == 'queue': # Queue request.
            self.formattedParams += [_formatter(newVars)]
        
        elif queueMode == 'update':
            request = apiCaller(HALO_API_URL,'update','Asset',newVars,self.headerJSON, self.formattedParams)
            response = request.getData()
            self.formattedParams = [] # reset queue
            return response
               

class attachments: 
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
            }
        
    def search(self,
        ticket_id:int=None,
        action_id:int=None,
        type:int=None,
        unique_id:int=None,
        **others):
        """Get list of attachment(s).

        Args:
            ticket_id (int, optional): Returns attachments from the ticket ID specified. 
            action_id (int, optional): Returns attachments from the action ID specified (requires ticket_id). 
            type (int, optional): Returns attachments of the specified type. 
            unique_id (int, optional): Returns an attachment with the unique ID specified.
        
        Returns:
            dict: Attachment(s) details and IDs (attachment will not be included, use get for that)
        """
        
        newVars = locals().copy()
        request = apiCaller(HALO_API_URL,'search','Attachment',newVars,self.headerJSON)
        response = request.getData()
        return response
        
    def get(self,
            id:int,
            includedetails:bool=False,
            **others):
        
        newVars = locals().copy()
        request = apiCaller(HALO_API_URL,'get','Attachment',newVars,self.headerJSON)
        response = request.getData()
        return response
    def update():
        pass
    def delete():
        pass


class clients: # Not fully functional yet
    """Client endpoint
    """
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
            }
        self.url = HALO_API_URL + '/Client'
    """Clients endpoint"""
    
    def search(self,
        pageinate:bool=False,
        page_size:int=None, # Switched to none
        page_no:int=1,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        toplevel_id:int=None,
        includeinactive:bool=None,
        includeactive:bool=None,
        count:int=50,
        newFormat:bool=False,
        **others
               ):
        """Search clients.  Supports unlisted parameters 
        By default, only the first 50 results are returned.  If more than 50 are needed, you must explicitely set count variable.  Leaving count blank will still return 50

        Args:
            paginate (bool, optional): Whether to use Pagination in the response. Defaults to False.
            page_size (int, optional): When using Pagination, the size of the page. Defaults to 50.
            page_no (int, optional): When using Pagination, the page number to return. Defaults to 1.
            order (str, optional): The name of the field to order by.
            orderdesc (bool, optional): Whether to order ascending or descending. Defaults to decending sort.
            search (str, optional): Filter by Customers like your search.
            toplevel_id (int, optional): Filter by Customers belonging to a particular top level.
            includeinactive (bool, optional): Include inactive Customers in the response. Defaults to False/No.
            includeactive (bool, optional): Include active Customers in the response. Defaults to True/Yes.
            newFormat: (bool, optional): Send 
            count (int, optional): When not using pagination, the number of results to return. Set to 50 by default (even if not included)
        
        Returns:
            newFormat=False (default)
                dict: Results and record count
            newFormat=True
                list: List of results
                int: Record count (total number of responses)
            
        """
        newVars = locals().copy()
        newVars.pop('newFormat') # Unneeded
        request = apiCaller(HALO_API_URL,'search','Client',newVars,self.headerJSON)
        response = request.getData()
        if newFormat==True:
            return response['clients'], response['record_count']
        else:
            return response
        
    def get(self,
            id:int,
            includedetails:bool=False,
            includediagramdetails:bool=False,
            **others
            ):
        """
        Get a single client's details.
        Supports all Halo parameters, even if not listed.  
        Requires atleast ID to be provided
        Args:
            id (int): Client ID
            includedetails (bool, optional): Whether to include extra details (objects) in the response. Defaults to False.
            includediagramdetails (bool, optional): Whether to include diagram details in the response. Defaults to False.

        Returns:
            dict: Single client details
        """
        
        newVars = locals().copy()
        request = apiCaller(HALO_API_URL,'get','Client',newVars,self.headerJSON)
        response = request.getData()
        return response
        
    def update():
        """Update one or more clients"""
        pass
    def delete():
        pass


class currency: # Not updated
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
        #return _responseParser(request)
        

class items: # OUTDATED
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
        #return _responseParser(request)
        
    def search(self, query):
        """ Search for an item

        Args:
            query DICT: Query dictionary

        Returns:
            Dictionary: Hopefully a list of items?
        """
        query = urllib.parse.urlencode(query)
        request = requests.get(HALO_API_URL+ '/item?' + query, headers = self.headerJSON)
        #return _responseParser(request)
    
    def create(self, payload):
        pass
    
    def update(self,
        id:int=None,
        fields:list=None,
        queueMode:str='disabled',
        **others
               ):
        """Creates or updates one or more assets.  If ID is included, asset(s) will be updated.  If ID is not included new asset(s) will be created.

        Args:
            id (int, optional): Asset ID.
            client_id (int, optional): Client ID. 
            site_id (int, optional): Site ID. 
            users (list, optional): User IDs. 
            fields (list, optional): Fields to be updated.
            queueMode (str, optional): Queue asset data to be sent as a batch update.  Valid modes: disabled - Default, will update asset immediately. queue

        Returns:
            _type_: I dont think it returns anything...
        """
        if queueMode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queueMode} is not a valid Queue Mode.')
        
        newVars = locals().copy()
        
        if queueMode == 'disabled': # Sent request immediately
            request = apiCaller(HALO_API_URL,'update','Site',newVars,self.headerJSON)
            response = request.getData()
            return response
        
        elif queueMode == 'queue': # Queue request.
            self.formattedParams += [_formatter(newVars)]
        
        elif queueMode == 'update':
            request = apiCaller(HALO_API_URL,'update','Site',newVars,self.headerJSON, self.formattedParams)
            response = request.getData()
            self.formattedParams = [] # reset queue
            return response


class invoices:
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
        #return _responseParser(request)


class recurringInvoices:
    """Recurring Invoice endpoint
    """
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
            }
        self.url = HALO_API_URL + '/RecurringInvoice'
    
    def search(self,
        pageinate:bool=False,
        page_size:int=None,
        page_no:int=None,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        count:int=None,
        client_id:int=None,
        includelines:bool=None,
        **others):
        
        
        
        newVars = locals().copy()
        request = apiCaller(HALO_API_URL,'search','RecurringInvoice',newVars,self.headerJSON)
        response = request.getData()
        return response
        
        
        pass
    def get():
        pass
    def update():
        pass
    
    def updateLines(self,
        id:int,
        ihid:int,
        **others):
        """Update recurring invoice lineitem(s)

        Args:
            id (int): Recurring invoice line item ID (required)
            ihid (int): Recurring invoice ID (required)

        Returns:
            _type_: _description_
        """
        
        
        newVars = locals().copy()
        request = apiCaller(HALO_API_URL,'update','RecurringInvoice/UpdateLines',newVars,self.headerJSON)
        response = request.getData()
        return response
    def delete():
        pass
    
    
class sites:
    """Sites endpoint
    """
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
            }
        self.url = HALO_API_URL + '/Client'    
    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        toplevel_id:int=None,
        client_id:int=None,
        includeinactive:bool=None,
        includeactive:bool=None,
        count:int=None,
        **others
               ):
        """Search Sites.  Supports unlisted parameters 

        Args:
            paginate (bool, optional): Whether to use Pagination in the response. Defaults to False.
            page_size (int, optional): When using Pagination, the size of the page. Defaults to 50.
            page_no (int, optional): When using Pagination, the page number to return. Defaults to 1.
            order (str, optional): The name of the field to order by.
            orderdesc (bool, optional): Whether to order ascending or descending. Defaults to decending sort.
            search (str, optional): Filter by Sites like your search.
            toplevel_id (int, optional): Filter by Sites belonging to a particular top level.
            client_id (int, optional): Filter by Sites belonging to a particular customer.
            includeinactive (bool, optional): Include inactive Sites in the response. Defaults to False/No.
            includeactive (bool, optional): Include active Sites in the response. Defaults to True/Yes.
            count (int, optional): When not using pagination, the number of results to return.
        
        Returns:
            dict: Search results.
        """
        newVars = locals().copy()
        
        request = apiCaller(HALO_API_URL,'search','Site',newVars,self.headerJSON)
        response = request.getData()
        return response
        
    def get():
        pass
    def update():
        """Update one or more sites"""
        pass
    def delete():
        pass
    

class softwareLicences:
    """Software Licenscs endpoint.  
    """
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
            }
        self.url = HALO_API_URL + '/SoftwareLicence'
    
    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        licence_type:int=None,
        tenant_id:int=None,
        toplevelid:int=None,
        client_id:int=None,
        site_id:int=None,
        includeinactive:bool=None,
        includeactive:bool=None,
        count:int=None,
        **others):
        """Search (Software) Licenses.

        Args:
            pageinate (bool, optional): _description_. Defaults to False.
            page_size (int, optional): _description_. Defaults to 50.
            page_no (int, optional): _description_. Defaults to 1.
            order (str, optional): _description_. Defaults to None.
            orderdesc (bool, optional): _description_. Defaults to None.
            search (str, optional): _description_. Defaults to None.
            licence_type (int, optional): _description_. Defaults to None.
            tenant_id (int, optional): _description_. Defaults to None.
            toplevelid (int, optional): _description_. Defaults to None.
            client_id (int, optional): _description_. Defaults to None.
            site_id (int, optional): _description_. Defaults to None.
            includeinactive (bool, optional): _description_. Defaults to None.
            includeactive (bool, optional): _description_. Defaults to None.
            count (int, optional): _description_. Defaults to None.

        Returns:
            _type_: _description_
        """
        newVars = locals().copy()
        
        request = apiCaller(HALO_API_URL,'search','SoftwareLicence',newVars,self.headerJSON)
        response = request.getData()
        return response
        
    
    def get(self):
        pass
    
    def update(self,
        client_id:int,
        type:int,
        name:str,
        site_id:int=None,
        count:int=None,
        start_date:str=None,
        end_date:str=None,
        billing_cycle:str=None,
        term_duration:str=None,
        autorenew:bool=None,
        status:str=None,
        is_active:bool=None,
        supplier_id:int=None,
        manufacturer:str=None,
        purchase_price:int=None,
        price:int=None,
        monthly_cost:int=None,
        monthly_price:int=None,
        notes:str=None,
        **others,
        ):
        
        newVars = locals().copy()
        
        request = apiCaller(HALO_API_URL,'update','SoftwareLicence',newVars,self.headerJSON)
        response = request.getData()
        return response
    
    def delete():
        pass


class tickets: # Partially updated
    """Tickets endpoint.  Official documentation: https://halo.halopsa.com/apidoc/resources/tickets
    """
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
            }
        self.formattedParams = [] # create empty list
    
    def update(self,
        actioncode:int=None,
        id:int=None,
        dateoccurred:str=None,
        summary:str=None,
        details:str=None,
        details_html:str=None,
        status_id:int=None,
        tickettype_id:int=None,
        sla_id:int=None,
        client_id:int=None,
        client_name:str=None,
        site_id:int=None,
        site_name:str=None,
        user_id:int=None,
        user_name:str=None,
        agent_id:int=None,
        
        queueMode:str='disabled',
        **others
        ):
        """Creates or updates one or more tickets.  If ID is included, tickets(s) will be updated.  If ID is not included new ticket(s) will be created.
        
        Updating multiple tickets can be done by passing a list of tickets with relevant fields, or by passing individual updates with the queueMode set to 'queue'.
        
        Offical documentation including all possible fields https://halo.halopsa.com/apidoc/resources/tickets
        

        Args:
            actioncode (int, optional): _description_. 
            id (int, optional): Ticket ID. If none provided, new ticket will be created.
            dateoccurred (str, optional): _description_. 
            summary (str, optional): Ticket summary (subject). 
            details (str, optional): Ticket details. 
            details_html (str, optional): Details in HTML format. 
            status_id (int, optional): Status ID. 
            tickettype_id (int, optional): Ticket type ID. 
            sla_id (int, optional): SLA ID. 
            client_id (int, optional): Client ID.
            client_name (str, optional): Client name. 
            site_id (int, optional): Site ID. 
            site_name (str, optional):Site Name. 
            user_id (int, optional): User ID. 
            user_name (str, optional): User name. 
            agent_id (int, optional): Agent ID. 
            queueMode (str, optional): Queue ticket data to be sent as a batch update.  This is done to reduce POST requests sent to Halo, by sending one POST request with all the needed updates
                Modes: 
                - disabled - (Default) Updates ticket
                - queue - Queues a single item ready to be sent later.
                - update - Sends queued tickets to be updated/created.

        Returns:
            _type_: I dont think it returns anything... #TODO make this return status
        """
        """



        """
        
        queueMode=queueMode.lower()
        
        if queueMode not in ['disabled','queue','update']:
            raise AttributeError(f'{queueMode} is not a valid Queue Mode.')
        
        newVars = locals().copy()
        
        if queueMode == 'queue': # Queue request.
            self.formattedParams += [_formatter(newVars)]
        
        elif queueMode in ['update','disabled']:
            request = apiCaller(HALO_API_URL,'update','Tickets',newVars,self.headerJSON, self.formattedParams if self.formattedParams!=[] else None)
            response = request.getData()
            self.formattedParams = [] # reset queue
            return response

    def search(self,query):
        pass
        
    def get(self,
        id:int,
        includedetails:bool=False,
        includelastaction:bool=False,
        ticketidonly:bool=False,
        **others
        ):
        """
        Get a single ticket's details.
        Supports all Halo parameters, even if not listed.  
        Requires atleast ID to be provided
        Args:
            id (int): Ticket ID
            includedetails (bool, optional): Whether to include extra details (objects) in the response. Defaults to False.
            includelastaction (bool, optional): Whether to include the last action in the response. Defaults to False.
            ticketidonly (bool, optional): Returns only the ID fields (Ticket ID, SLA ID, Status ID, Client ID and Name and Lastincomingemail date) of the Tickets. Defaults to False.

        Returns:
            dict: Single ticket details
        """

        newVars = locals().copy()
        request = apiCaller(HALO_API_URL,'get','Ticket',newVars,self.headerJSON)
        response = request.getData()
        return response
    
    def merge(self,existingID,newID):
        pass
    
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
  
  
class users:
    """Users endpoint.  
    """
    def __init__(self):
        token = createToken()
        self.token = token
        self.headerJSON = { # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  token
            }
        self.url = HALO_API_URL + '/Users'
    
    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        search_phonenumbers:bool=None,
        toplevel_id:int=None,
        client_id:int=None,
        site_id:int=None,
        organisation_id:int=None,
        department_id:int=None,
        asset_id:int=None,
        includeinactive:bool=None,
        includeactive:bool=None,
        approversonly:bool=None,
        excludeagents:bool=None,
        count:int=None,
        **others
               ):
        """_summary_

        Args:
            paginate (bool, optional): Whether to use Pagination in the response. Defaults to False.
            page_size (int, optional): When using Pagination, the size of the page. Defaults to 50.
            page_no (int, optional): When using Pagination, the page number to return. Defaults to 1.
            order (str, optional): The name of the field to order by.
            orderdesc (bool, optional): Whether to order ascending or descending. Defaults to decending sort.
            search (str, optional): Query to filter by.
            search_phonenumbers (bool, optional): Filter by Users with a phone number like your search. Defaults to None.
            toplevel_id (int, optional): Filter by Users belonging to a particular top level.            
            client_id (int, optional): Filter by Users belonging to a particular customer.
            site_id (int, optional): Filter by Users belonging to a particular site.
            organisation_id (int, optional): Filter by Users belonging to a particular site.
            department_id (int, optional): Filter by Users belonging to a particular department.
            asset_id (int, optional): Filter by Users assigned to a particular asset.
            includeinactive (bool, optional): Include inactive Users in response. Defaults to False.
            includeactive (bool, optional): Include inactive Users in response. Defaults to True.
            approversonly (bool, optional): Include only Users that can approve appoval processes response. Defaults to False.
            excludeagents (bool, optional): Excluse Users that are linked to active agent accounts. Defaults to False.
            count (int, optional): When not using pagination, the number of results to return.

        Returns:
            dict: Search results
        """
    
        newVars = locals().copy()
        
        request = apiCaller(HALO_API_URL,'search','Users',newVars,self.headerJSON)
        response = request.getData()
        return response
        
    def get(self,
            id:int,
            includedetails:bool=None,
            includeactivity:bool=None,
            includepopups:bool=None,
            **others
            ):
        """
        Get a single user's details.
        Supports all Halo parameters, even if not listed.  
        Requires atleast ID to be provided
        Args:
            id (int): User ID
            includedetails (bool, optional): Whether to include extra details in the response. Defaults to False.
            includeactivity (bool, optional): Whether to include User's ticket activity in the response. Defaults to False.
            includepopups (bool, optional): Whether to include customer pop ups in the response. Defaults to False.

        Returns:
            dict: Single users details
        """
        
        newVars = locals().copy()
        request = apiCaller(HALO_API_URL,'get','User',newVars,self.headerJSON)
        response = request.getData()
        return response
        
    def update():
        """Update one or more users"""
        pass
    def delete():
        pass


def _formatter(params): # Format user input for API requests
    formattedData = {}
    paramsToAdd = params | params['others'] # Copy params and add any additional items
    
    # Remove Remove unneeded variables
    paramsToAdd.pop('others') 
    paramsToAdd.pop('self')
    paramsToAdd.pop('queueMode')
    
    pageinateToggle = False
    for item, value in paramsToAdd.items(): # Check params, add anything that isn't blank to the query

        if item == 'pageinate' and value == True:
            pageinateToggle = True

        if pageinateToggle == False and item in ['page_size','page_no']: # Skip redundant values
            continue
        
        if value !=None:
            formattedData.update({item : value})
    return formattedData
