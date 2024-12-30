import requests
import urllib.parse
import json
import os

#TODO create parent/child system for all the classes in here, so API key is not needed each time
#TODO track progress per "endpoint"
#TODO start documentation
#TODO fix changelog.md
#TODO update readme.md
#TODO implement all base endpoints (the ones in the main documentation)


class HaloBase:
    """Base halo class"""
    #TODO test bad token
    #TODO test bad URL
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
        params = payload if method == 'get' else None
        data = payload if method == 'post' else None
        response = self.session.request(method, url, params=params,data=data)
        reason = response.reason
        code = response.status_code
        
        #TODO find errors here
        # Invalid URL
        if code in [404]: # Raise error here
            print(f'404 -  The specified URL is invalid. URL: {self.url}')
        try:
            content = json.loads(response.content)
        except UnicodeDecodeError: # bytes resposne.
            content = response.content
            return content 
        
        # Success
        if code in [200,201]:
            # 201 = Created/updated
            # 200 = OK
            return content

        elif code in [401]:
            # Return clearer errors
            if content["error_description"] == 'The specified client credentials are invalid.':
                # Specify it is the client secret that is wrong, not the client ID.
                print('The specified \'client_secret\' is invalid')
            else:
                print(content["error_description"])
        elif code in [400]: # Bad reqeust 
            raise Exception(f'{code} Bad Request - {content('ClassName')}: {content('message')}') # URL is good, but the request is no
                
        else:
            raise Exception( f'{code} - Other failure')

    def _requestFormatter(self,params):
        paramsToAdd = params | params['others'] # Copy params and add any additional items
        paramsToAdd.pop('others') # Remove 'others' dict item to avoid confusion
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
        
class Appointments(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class Assets(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)
        self.apiURL+='/Asset'
        self.formattedParams = []
    #TODO add progress start in here somewhere
    """ Asset actions 
    Initialize by running this once on its own, then run actions"""
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
        
            response = self._requester('post',self.apiURL+'/Asset',self._requestFormatter(rawParams))
            return response
        
        elif queueMode == 'queue': # Queue request.
            self.formattedParams += [self._requestFormatter(rawParams)]
        
        elif queueMode == 'update':
            response = self._requester('post',self.apiURL+'/Asset',self._requestFormatter(rawParams))
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
        
    def get(self,
            id:int,
            includedetails:bool=False,
            **others):
        
        rawParams = locals().copy()
        response = self._requester('get',self.apiURL,self._requestFormatter(rawParams))
        return response
    def update():
        pass
    def delete():
        pass
        
class Clients(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

class Contracts(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)     

class Items(HaloBase):
    def __init__(self,tenant:str,clientID:str,secret:str,scope:str='all',logLevel:str='Normal'):
        super().__init__(tenant,clientID,secret,scope,logLevel)

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
