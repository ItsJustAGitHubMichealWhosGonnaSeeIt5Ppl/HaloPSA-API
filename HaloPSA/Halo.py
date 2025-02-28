import requests
import urllib.parse
import json
import os

#TODO create parent/child system for all the classes in here, so API key is not needed each time
#TODO track progress per "endpoint"
#TODO start documentation
#TODO fix changelog.md
#TODO update readme.md
#TODO add versioning
#TODO implement all base endpoints (the ones in the main documentation)

#TEMPLATE STRING FOR CLASSES
"""[ENDPOINT NAME] Endpoint
[Brief description]
Official Documentation: https://halopsa.halopsa.com/apidoc/resources/[Endpoint] OR No official documentation
Progress:
"""
class HaloBase:
    """Base halo class"""
    def _createToken(self,clientid:str,secret:str,scope:str='all'):
        # Return auth token from Halo.
        authheader = { # Required by Halo, don't ask me why
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = { # Create payload for Halo auth
        'grant_type': 'client_credentials',
        'client_id': clientid,
        'client_secret': secret,
        'scope': scope 
        }
        request = self._requester('post', self.authURL, headers=authheader, payload=payload)
        return request['access_token']

        
    def _requester(self, method, url:str=None, payload=None,headers=None):
        url = self.apiURL if url == None else url # Fix URL
        # Set params or data depending on what type of request is being done
        #TODO allow method to be set to "Search" and use that rather than adding the ID directly into the main URL. May also require some tweaks to how request formatting is handled
        params = payload if method == 'get' else None
        data = json.dumps([payload]) if headers == None and method == 'post' else payload if  method == 'post' else None # Why is it this way?
        
        response = self.session.request(method, url, params=params,data=data)
        reason = response.reason
        code = response.status_code
        
        
        # These responses usually don't have JSON content, so should be checked first.  Codes are in lists in case I find more later
        if code in [403]: # Forbidden
            raise PermissionError(f'{reason} - You do not have permission to do this. If this is unexpected, make sure you have set the right permissions in Halo.')
        elif code in [404]:# Invalid URL
           raise Exception(f'{code} - The specified URL is invalid. URL: {self.url}')
        elif code in [500]: # Internal Server Error
            raise Exception(f'{code} - {reason}.  Is your Tenant ID right?') # Got this when I gave it a bad tenant #TODO make this a custom error?
        
        
        try: # Hopefully the data is JSON now
            content = json.loads(response.content)
        except UnicodeDecodeError: # bytes resposne.
            content = response.content
            return content
        except json.decoder.JSONDecodeError:
            raise Exception('Uh oh I don\'t know how you got this.  Your JSON did not decode.') #TODO fix this error
        
        # Success
        if code in [200,201]:
            # 201 = Created/updated
            # 200 = OK
            return content

        elif code in [401]:
            if content['error'] == 'invalid_client': # Add some more helpful info to the error
                error_desc = content['error_description'] + ' Make sure your client ID and secret are correct.'
            else:
                error_desc = content['error_description']
            
            raise ValueError(f'{reason}. {error_desc}')
        

        elif code in [400]: # Bad reqeust 
            raise ValueError(f'{code} Bad Request - {content}') # URL is good, but the request is no #TODO maybe parse the error so its easier to read? #TODO custom errors!
                
        else:
            raise Exception( f'{code} - Other failure')

    def _requestFormatter(self,params):
        try:
            paramsToAdd = params | params['others'] # Copy params and add any additional items
            paramsToAdd.pop('others') # Remove 'others' dict item to avoid confusion

        except KeyError: # Not all endpoints have "others"
            paramsToAdd = params
        
        paramsToAdd.pop('self')
        formattedData = {}
        
        pageinateToggle = False
        for item, value in paramsToAdd.items(): # Check params, add anything that isn't blank to the query

            if item == 'pageinate' and value == True:
                pageinateToggle = True

            if pageinateToggle == False and item in ['page_size','page_no']: # Skip redundant values
                continue
            
            if value !=None:
                formattedData.update({item : value})
            
        return formattedData


    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        
        self.session = requests.Session() # Create a session
        #TODO handle a full URL being sent
        self.authURL = f'https://{tenant}.halopsa.com/auth/token' # auth URL used only once to get a token 
        self.apiURL = f'https://{tenant}.halopsa.com/api' # API url used for everything else
        self.token = self._createToken(clientID,secret) # Create token
        self.session.headers.update({ # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  self.token
            })

class Actions(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/Actions'
    
    def search(self): #TODO add actions search
        pass
    
    def get(self): #TODO add actions get
        pass
    
    def update(self): #TODO add actions update
        """Update one or more actions"""
        pass
    
    def delete(): #TODO add actions delete
        pass

class Agents(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/Agent'
        
class Appointments(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/Appointment'


class Assets(HaloBase): # TODO this is the only endpoint that actually works?
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/Asset'
        self.formattedParams = []
    #TODO add progress start in here somewhere
    """
    Assets Endpoint.
    Get, update, and delete your Halo Assets
    Official Documentation: https://halopsa.halopsa.com/apidoc/resources/assets
    Progress: TBD
    """
    
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

        rawParams = locals().copy()
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
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
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
        return response
    
    def getAll(self):
        """Get all halo assets

        Returns:
            list: List of assets OR error
        """
        print('Removing this, use search with no parameters instead')
        response = self._requester('get',self.apiURL)
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
        
        rawParams = locals().copy()
        
        if queueMode == 'disabled': # Sent request immediately
        
            response = self._requester('post',self.apiURL,self._requestFormatter(rawParams))
            return response
        
        elif queueMode == 'queue': # Queue request.
            self.formattedParams += [self._requestFormatter(rawParams)]
        
        elif queueMode == 'update':
            response = self._requester('post',self.apiURL,self._requestFormatter(rawParams))
            self.formattedParams = [] # reset queue
            return response
        
class Attachments(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/Attachment'
    
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
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
        return response
        
    def get(self, #TODO add docstring
            id:int,
            includedetails:bool=False,
            **others):
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL+f'/{id}',self._requestFormatter(rawParams))
        return response
    def upload(self,
            id:int=None,
            filename:str=None,
            ticket_id:int=None,
            data_base64:str=None,
            **others):
        
        rawParams = locals().copy()
        response = self._requester('post',self.apiURL,self._requestFormatter(rawParams))
        return response
        

    def delete():
        pass
        
class Clients(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/Client'
        self.formattedParams = []

    def search(self,
        pageinate:bool=False,
        page_size:int=None, # Switched to none
        page_no:int=1,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        toplevel_id:int=None,
        includeinactive:bool=None, #TODO should these be set to their defaults? instead of none
        includeactive:bool=None,
        count:int=50,
        newFormat:bool=False,
        **others
               ):
        """Search clients. Supports unlisted parameters.
        By default, only the first 50 results are returned.  If more than 50 are needed, you must explicitely set count variable.  Leaving count blank will still return 50.

        Args:
            paginate (bool, optional): Whether to use Pagination in the response. Defaults to False.
            page_size (int, optional): The size of the page if using pagination. Defaults to 50.
            page_no (int, optional): The page number to return if using pagination. Defaults to 1.
            count (int, optional): When not using pagination, the number of results to return. Set to 50 by default (even if not included).
            order (str, optional): The name of the field to order by.
            orderdesc (bool, optional): Whether to order ascending or descending. Defaults to decending sort.
            search (str, optional): Filter by Customers like your search.
            toplevel_id (int, optional): Filter by Customers belonging to a particular top level.
            includeinactive (bool, optional): Include inactive Customers in the response. Defaults to False.
            includeactive (bool, optional): Include active Customers in the response. Defaults to True.
            newFormat: (bool, optional): Return clients and record count separately. Defaults to False.
            
        Returns:
            newFormat=False (default)
                dict: Results and record count
            newFormat=True
                list: List of results
                int: Record count (total number of responses)
            
        """
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL, self._requestFormatter(rawParams))
        if newFormat==True:
            return response['clients'], response['record_count']
        else:
            return response
        
    def getAll(self, #TODO add docsting #TODO add any other potentially useful toggles
        includeinactive:bool=False,
        includeactive:bool=True,):
        #This is literally just search but wrapped
        #TODO should include details be available here?  Would require separate calls for all clients, could get intensive
        response = self.search(count=100000,includeinactive=includeinactive,includeactive=includeactive) #TODO make sure to note that the maximum here is 100000
        return response['clients']
        
    def get(self, #TODO test Get
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
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL+f'/{id}',self._requestFormatter(rawParams))
        return response
        
    def update(self, #TODO update the docstring
        id:int=None,
        name:str=None,
        toplevel_id:int=None,
        due_date_type:int=None,
        invoiceduedaysextraclient:int=None, # This is due date int in other places
        queueMode:str='disabled',
        **others
            ):
        """Create or update one or more clients.  If ID is included, client(s) will be updated.  If ID is not included new client(s) will be created.

        Args:
            id (int, optional): Client ID.
            queueMode (str, optional): Queue asset data to be sent as a batch update.  Valid modes: disabled - Default, will update asset immediately. queue

        Returns:
            dict: Updated or created client(s).
        """
        if queueMode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queueMode} is not a valid Queue Mode.')
        
        rawParams = locals().copy()
        
        if queueMode == 'disabled': # Sent request immediately
        
            response = self._requester('post',self.apiURL,self._requestFormatter(rawParams))
            return response
        
        elif queueMode == 'queue': # Queue request.
            self.formattedParams += [self._requestFormatter(rawParams)]
        
        elif queueMode == 'update':
            response = self._requester('post',self.apiURL,self._requestFormatter(rawParams))
            self.formattedParams = [] # reset queue
            return response
    
    def delete():
        pass



class Contracts(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)     

class Items(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/Item'
    
    def getDetails(self, item):
        """ Get details about an item

        Args:
            item INT: Item ID

        Returns:
            Dictionay: Item details
        """

        
    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        count:int=None,
        **others):
        """Search items

        Args:
            pageinate (bool, optional): _description_. Defaults to False.
            page_size (int, optional): _description_. Defaults to 50.
            page_no (int, optional): _description_. Defaults to 1.
            order (str, optional): _description_. Defaults to None.
            orderdesc (bool, optional): _description_. Defaults to None.
            search (str, optional): _description_. Defaults to None.
            count (int, optional): _description_. Defaults to None.


        Returns:
            list: List of currency items
        """         
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
        return response
    
    def get(self): 
        pass
    
    def getAll(self):
        response = self.search()
        return response #TODO figure out what the dict name is for this
    

    
    def create(self, payload):
        pass
    
    def update(self,
        id:int=None,
        costprice:float=None,
        recurringcost:float=None,
        baseprice:float=None,
        recurringprice:float=None,
        update_recurring_invoice_price:bool=None,
        update_recurring_invoice_cost:bool=None,
        queueMode:str='disabled',
        **others
               ):
        """Creates or updates one or more assets.  If ID is included, asset(s) will be updated.  If ID is not included new asset(s) will be created.

        Args:
            id (int, optional): Asset ID.
            fields (list, optional): Fields to be updated.
            queueMode (str, optional): Queue asset data to be sent as a batch update.  Valid modes: disabled - Default, will update asset immediately. queue

        Returns:
            _type_: I dont think it returns anything...
        """
        if queueMode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queueMode} is not a valid Queue Mode.')
        
        rawParams = locals().copy()
        
        if queueMode == 'disabled': # Sent request immediately
        
            response = self._requester('post',self.apiURL,self._requestFormatter(rawParams))
            return response
        
        elif queueMode == 'queue': # Queue request.
            self.formattedParams += [self._requestFormatter(rawParams)]
        
        elif queueMode == 'update':
            response = self._requester('post',self.apiURL,self._requestFormatter(rawParams))
            self.formattedParams = [] # reset queue
            return response

class Invoices(HaloBase): #TODO add docstring here
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        
    def search(self, #TODO fix this
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
        
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL+'/Invoice',self._requestFormatter(rawParams))
        return response

class KnowledgeBase(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class Opportunities(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class Projects(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class Quotes(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class RecurringInvoices(HaloBase):
    """
    Recurring Invoices (RecurringInvoiceHeader) Endpoint.
    Get, update, and delete your recurring invoices
    Official Documentation: Not officially listed in documentation, listed under "RecurringInvoiceHeader" in swagger (link below)
    Swagger: https://halo.halopsa.com/api/swagger/index.html
    
    Progress
    - Search: Partially tested
    - Get: Not implemented
    - GetAll: Tested, needs docstring
    - Update: Partially tested
    - UpdateLines: Not tested
    - Delete: Not implemented
    """
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/RecurringInvoice'

    def search(self, #TODO add docstring #TODO figure out why page size is being returned at all if it isnt being used. #TODO add more relevant variables if any
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        count:int=None,
        client_id:int=None,
        includelines:bool=False,
        **others):
        
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
        return response
    
    def get(self,): 
        pass
    
    def getAll(self, #TODO add docsting #TODO add any other potentially useful toggles
        includelines:bool=False):
        #This is literally just search but wrapped
        response = self.search(includelines=includelines)
        return response['invoices']
    
    def update(self, #TODO Test update #TODO fix docstring 
        id:int=None,
        due_date_type:int=None, #
        due_date_int:int=None, # 
        **others):
        """Update or create a recurring invoice (Not used for updating line items).

        Args:
            id (int, optional): Recurring invoice ID.  If no ID is provided, a new recurring invoice will be created
            due_date_type (int, optional): Set due date type to use. (see list below)
            due_date_type (int, optional): Set due date count.  If using a days after, count will be taken as a number.  If using "of the _ month" will be taken as a date.  If date is larger than last day of month, last day of the month will be used instead.
        
        Due date types:
        - 0: Day(s) after the invoice date.
        - 1: Day(s) after the end of the invoice month. 
        - 2: of the next month. 
        - 3: of the current month.
        
        Returns:
            dict: Updated invoice(s)
        """
        
        queueMode = 'disabled' #TODO Implement and test queueMode
        if queueMode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queueMode} is not a valid Queue Mode.')
        
        rawParams = locals().copy()
        
        if queueMode == 'disabled': # Sent request immediately
        
            response = self._requester('post',self.apiURL,self._requestFormatter(rawParams)) #TODO should params be formatted later?
            return response
        
        elif queueMode == 'queue': # Queue request.
            self.formattedParams += [self._requestFormatter(rawParams)]
        
        elif queueMode == 'update':
            response = self._requester('post',self.apiURL,self._requestFormatter(rawParams))
            self.formattedParams = [] # reset queue
            return response
    
    def updateLines(self, #TODO test updateLines #TODO fix docstring
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
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL+'/UpdateLines',self._requestFormatter(rawParams))
        return response        

    def delete():
        pass
class Reports(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        
class Sites(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class Status(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class Suppliers(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class Teams(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class TicketTypes(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class Tickets(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
    
        
class Users(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/Users'
        
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
        
        rawParams = locals().copy() 
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
        return response
        
    def get(self, # TODO test me
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
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
        return response
        
    def update():
        """Update one or more users"""
        pass
    def delete():
        pass

# NON STANDARD

class DistributionLists(HaloBase): 
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/DistributionLists'
        
    def getAll(self): # All distribution lists

        rawParams = locals().copy()
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
        return response
    
    def get(self, # Only accepts one item #TODO check if there are any hidden params #TODO allow a way to get users?
            id:int
            ):

        rawParams = locals().copy()
        response = self._requester('get',self.apiURL+f'/{id}?includedetails=true',self._requestFormatter(rawParams))
        return response
    
    def create(self,
        name:str,
        description:str="",
        mailbox_from:int="",
        mailbox_replyto:int="",
        third_party_url:any="",
        dynamic_members:bool="",
        **others
        ):
        rawParams = locals().copy()
        response = self._requester('post',self.apiURL,self._requestFormatter(rawParams))
        return response
    
    
    def update(self,
        id:int,
        addtheseusers:list=None,
        removetheseusers:list=None): # TODO add docstring
        rawParams = locals().copy()
        response = self._requester('post',self.apiURL,self._requestFormatter(rawParams))
        return response

class TopLevel(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/TopLevel'

    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        count:int=None,
        **others):
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
        return response
    
    def get(self): 
        pass
    
    def getAll(self): #TODO add docsting #TODO add any other potentially useful toggles
        #This is literally just search but wrapped
        response = self.search()
        return response['tree']
    
    
class Currency(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/Currency'

    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:str =None,
        orderdesc:bool=None,
        search:str=None,
        count:int=None,
        **others):
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
        return response
    
    def get(self): 
        pass
    
    def getAll(self):
        pass
    
