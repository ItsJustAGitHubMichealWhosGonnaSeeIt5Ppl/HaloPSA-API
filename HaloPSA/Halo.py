
import requests
import json
from typing import Optional, Literal

#TODO create parent/child system for all the classes in here, so API key is not needed each time
#TODO start documentation
#TODO fix changelog.md
#TODO update readme.md
#TODO add versioning
#TODO implement dataclasses
#TODO dont use .locals()

# # # FORMATTING GUIDELINES # # #

## General
# Stick to US english as that is what Halo uses
# Leave Halo variables/params unchanged unless there is an extremely good reason to make it different.  If changed, make sure its documented clearly
# use_snake_case, notCamelCase


## Classes
# Capitalize AllWordsLikeThis, dontUse camelCase

# # # TEMPLATES # # # (is it docstring or doc string)

#TEMPLATE FOR ENDPOINT
'''
class EndpointName(HaloBase):
    """[ENDPOINT NAME] Endpoint.

    [Brief description]

    Official Documentation: https://halopsa.halopsa.com/apidoc/resources/[Endpoint] OR No official documentation

    Requires _ permission

    Progress (Temporary)
    - Get:
    - get_all: (should this be removed?)
    - Search:
    - Update:
    - Delete: 
    """
    def __init__(self, tenant:str, clientid:str, secret:str, scope:str='all', tenant_type:str='psa', log_level:str='Normal'):
        super().__init__(tenant=tenant, clientid=clientid, secret=secret, scope=scope, tenant_type=tenant_type, log_level=log_level)
        self.url+='/EndpointLink'
        
        
    def get(self, id:int, **others): #TODO test me #TODO Confirm variables
        """Get [Brief description]

        Requires _ permission [ONLY INCLUDE IF PERMISSION DIFFERS FROM OVERALL ENDPOINT]

        Last tested: YYYY/MM/DD, V[HALO VERSION]
        """
        resp = self._get(id=id, others=others)
        return resp
    
    def search(self, **others): #TODO test me
        """Search [Brief description]

        Requires _ permission [ONLY INCLUDE IF PERMISSION DIFFERS FROM OVERALL ENDPOINT]

        Last tested: YYYY/MM/DD, V[HALO VERSION]
        """
        resp = self._search(others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        """Update or create [Brief description]

        Requires _ permission [ONLY INCLUDE IF PERMISSION DIFFERS FROM OVERALL ENDPOINT]

        Last tested: YYYY/MM/DD, V[HALO VERSION]
        """
        resp = self._update(queue_mode=queue_mode, others=others)
        return resp
'''
#TEMPLATE STRING FOR CLASSES
"""[ENDPOINT NAME] Endpoint.

[Brief description]

Official Documentation: https://halopsa.halopsa.com/apidoc/resources/[Endpoint] OR No official documentation

Requires _ permission

Progress (Temporary)
- Get:
- get_all: (should this be removed?)
- Search:
- Update:
- Delete: 
"""

#METHOD TEMPLATE/FORMATTING
"""[METHOD] [Brief description]

Requires _ permission [ONLY INCLUDE IF PERMISSION DIFFERS FROM OVERALL ENDPOINT]

Last tested: YYYY/MM/DD, V[HALO VERSION]
"""

#variable descriptions (to keep them as consistent as possible)
"""Try to keep them sorted alphabetically

"""

# # # CODE # # #
TENANT_TYPES = Literal['psa', 'itsm']

class Halo:
    def __init__(self, tenant:str, clientid:str, secret:str, scope:str='all', tenant_type:TENANT_TYPES='psa', log_level:str='Normal'):
        """Halo Base Class

        Args:
            tenant (str): Your Tenant
            clientid (str): Your API client iD
            secret (str): Your API secret
            tenant_type (str, optional): Your tenant type.  Valid options ['psa', 'itsm']. Defaults to psa. 
            scope (str, optional): _description_. Defaults to 'all'.
            logLevel (str, optional): Does nothing. Defaults to 'Normal'.
        """
        # Better way to initialize these.
        self._mh = _MethodsHelper(tenant=tenant, clientid=clientid, secret=secret, scope=scope,tenant_type=tenant_type, log_level=log_level)
        
        self.Actions = _Actions(mh=self._mh)
        self.Agents = _Agents(mh=self._mh)
        self.Appointments = _Appointments(mh=self._mh)
        self.Assets = _Assets(mh=self._mh)
        self.Attachments = _Attachments(mh=self._mh)
        self.Clients = _Clients(mh=self._mh)
        self.Contracts = _Contracts(mh=self._mh)
        self.Items = _Items(mh=self._mh)
        self.Invoices= _Invoices(mh=self._mh)
        self.KnowledgeBase = _KnowledgeBase(mh=self._mh)
        self.Opportunities = _Opportunities(mh=self._mh)
        self.Projects = _Projects(mh=self._mh)
        self.Quotes = _Quotes(mh=self._mh)
        self.RecurringInvoices = _RecurringInvoices(mh=self._mh)
        self.Reports = _Reports(mh=self._mh)
        self.Sites = _Sites(mh=self._mh)
        self.Status = _Status(mh=self._mh)
        self.Suppliers = _Suppliers(mh=self._mh)
        self.Teams= _Teams(mh=self._mh)
        self.TicketTypes = _TicketTypes(mh=self._mh)
        self.Tickets = _Tickets(mh=self._mh)
        self.Users = _Users(mh=self._mh)
        # Undocumented
        self.DistributionLists = _DistributionLists(mh=self._mh)
        self.TopLevel = _TopLevel(mh=self._mh)
        self.Currency = _Currency(mh=self._mh)
        self.SoftwareLicences = _SoftwareLicences(mh=self._mh)
        self.UserRoles = _UserRoles(mh=self._mh)
        self.InvoiceChange = _InvoiceChange(mh=self._mh)
        

class _MethodsHelper:
    """Halo Method Helper"""
    def _create_token(self, clientid:str, secret:str, scope:str='all'): # Return auth token from Halo.
        authheader = { # Required by Halo, I don't know why
        'Content-Type': 'application/x-www-form-urlencoded'
        }
        payload = { # Create payload for Halo auth
        'grant_type': 'client_credentials',
        'client_id': clientid,
        'client_secret': secret,
        'scope': scope
        }
        request = self._requester('post', self.auth_url, headers=authheader, payload=payload)
        return request['access_token']

        
    def _requester(self, method:str, url:str, payload=None,headers=None):
        #TODO allow method to be set to "Search" and use that rather than adding the ID directly into the main URL. May also require some tweaks to how request formatting is handled
        params = payload if method == 'get' else None # Set params or data depending on what type of request is being done
        data = json.dumps([payload]) if headers == None and method == 'post' else payload if  method == 'post' else None # Why is it this way?
        
        response = self.session.request(method, url, params=params, data=data)
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
            content:dict = json.loads(response.content)
        except UnicodeDecodeError: # bytes resposne.
            content: bytes = response.content
            return content
        except json.decoder.JSONDecodeError:
            raise Exception('Uh oh I don\'t know how you got this.  Your JSON did not decode.') #TODO fix this error
        
        # Success
        if code in [200,201]:
            # 201 = Created/updated
            # 200 = OK
            return content

        elif code in [401]:
            assert isinstance(content, dict)
            if content['error'] == 'invalid_client': # Add some more helpful info to the error
                error_desc = content['error_description'] + ' Make sure your client ID and secret are correct.'
            else:
                error_desc = content['error_description']
            
            raise ValueError(f'{reason}. {error_desc}')
        

        elif code in [400]: # Bad reqeust 
            raise ValueError(f'{code} Bad Request - {content}') # URL is good, but the request is no #TODO maybe parse the error so its easier to read? #TODO custom errors!
                
        else:
            raise Exception( f'{code} - Other failure')

    def _format_requests(self, params, params_to_pop:list=[]):
        
        params_to_pop += ['queue_mode','self','others']
        try:
            unformatted_params = params | params['others'] # Copy params and add any additional items
        except KeyError: # Not all endpoints have "others" but they should
            unformatted_params = params
            
        for param in params_to_pop: # Remove unneeded/unwanted parameters
            try:
                unformatted_params.pop(param)
            except KeyError:
                pass
            
        formatted_params = {}
        
        #TODO maybe there is a better way to do this
        if 'pageinate' in unformatted_params and unformatted_params['pageinate']:
            toggle_pageinate = True
        else:
            toggle_pageinate = False
            
        for item, value in unformatted_params.items(): # Check params, add anything that isn't blank to the query

            if toggle_pageinate == False and item in ['page_size','page_no']: # Skip redundant values
                continue
            
            if value !=None:
                formatted_params.update({item : value})
            
        return formatted_params
    
    # Another new response system that needs testing
    def _get(self, url:str, id:int, **allvars)-> dict: # New get system
        response = self._requester('get',url+f'/{id}',self._format_requests(allvars))
        return response
    
    def _search(self, url:str, **allvars)-> dict:
        response:dict = self._requester('get',url, self._format_requests(allvars))
        return response
    
    def _update(self, url:str, queue_mode:str, **allvars):
        if queue_mode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queue_mode} is not a valid Queue Mode.')
        
        #TODO get rid of queue mode
        if queue_mode == 'disabled': # Sent request immediately
            response:dict = self._requester('post',url,self._format_requests(allvars))
            return response
        
        elif queue_mode == 'queue': # Queue request.
            self.formatted_params += [self._format_requests(allvars)]
            return "Item queued"
        
        elif queue_mode == 'update': # Add the last request, then send
            self.formatted_params += [self._format_requests(allvars)]
            response:dict = self._requester('post',url,self.formatted_params)
            self.formatted_params = [] # reset queue
            return response
    
    
    
    def __init__(self, tenant:str, clientid:str, secret:str, scope:str='all', tenant_type:str='psa', log_level:str='Normal'):
        """Halo Base Class

        Args:
            tenant (str): Your Tenant
            clientid (str): Your API client iD
            secret (str): Your API secret
            tenant_type (str, optional): Your tenant type.  Valid options ['psa', 'itsm']. Defaults to psa. 
            scope (str, optional): _description_. Defaults to 'all'.
            logLevel (str, optional): Does nothing. Defaults to 'Normal'.
        """
        self.session = requests.Session() # Create a session
        #TODO handle a full URL being sent
        self.auth_url = f'https://{tenant}.halo{tenant_type}.com/auth/token' # auth URL used only once to get a token 
        self.url = f'https://{tenant}.halo{tenant_type}.com/api' # API url used for everything else
        self.token = self._create_token(clientid, secret, scope) # Create token
        self.session.headers.update({ # Header with token
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' +  self.token
            })
        self.formatted_params = [] 

class _Actions: #TODO what permissions are required here
    """Actions Endpoint.
    
    Get, add, and update actions.
    
    Requires ? permission
    
    Official Documentation: https://halopsa.halopsa.com/apidoc/resources/actions

    Progress (Temporary)
    - Get: Working, no docstring
    - get_all: Not implemented
    - Search: Working, partial docstring
    - Update: Untested, no docstring
    - Delete: Not implemented
    """
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Actions'
    def get(self,
            id:int,
            ticket_id:int,
            includeemail:Optional[bool] = None,
            includedetails:bool=True,
            mostrecent:Optional[bool] = None,
            agentonly:Optional[bool] = None,
            emailonly:Optional[bool] = None,
            nonsystem:Optional[bool] = None,
            **others
            ):
        rawParams = locals().copy()
        
        resp = self._mh._get(url=self.url, id=id, others=rawParams)
        return resp
    
    def search(self,
        count:Optional[int] = None,
        ticket_id:Optional[int] = None,
        startdate:Optional[str] = None,
        enddate:Optional[str] = None,
        agentonly:bool=False,
        conversationonly:Optional[bool] = None,
        supplieronly:Optional[bool] = None,
        importantonly:Optional[bool] = None,
        slaonly:Optional[bool] = None,
        excludesys:Optional[bool] = None,
        excludeprivate:Optional[bool] = None,
        includehtmlnote:Optional[bool] = None,
        includehtmlemail:Optional[bool] = None,
        includeattachments:Optional[bool] = None,
        ischildnotes:Optional[bool] = None,
        **others
        ):
        """Search/filter Actions.  Requires Ticket ID, or start and end date.  If neither are provided, nothing will be returned.
        
        Date range can be 1 day at most.
        
        Last tested: YYYY/MM/DD, V[HALO VERSION]

        Args:
            count (int, optional): Maximum actions to return.
            ticket_id (int, optional): Ticket ID.
            startdate (str, optional): Start Date (format 2025-03-04T12:53:05) Time is optional.
            enddate (str, optional): End Date (format 2025-03-04T12:53:05) Time is optional.
            agentonly (bool, optional): Only get actions done by Agents. Defaults to False.
            conversationonly (bool, optional): Only get actions relating to the Agent to End User conversation. Defaults to None.
            supplieronly (bool, optional): Only get actions relating to Suppliers. Defaults to None.
            importantonly (bool, optional): Only get important actions. Defaults to None.
            slaonly (bool, optional): Only get SLA hold and release actions. Defaults to None.
            excludesys (bool, optional): Exclude system actions. Defaults to None.
            excludeprivate (bool, optional): Exclude prviate actions. Defaults to None.
            includehtmlnote (bool, optional): _description_. Defaults to None.
            includehtmlemail (bool, optional): _description_. Defaults to None.
            includeattachments (bool, optional): _description_. Defaults to None.
            ischildnotes (bool, optional): _description_. Defaults to None.

        Returns:
            list: List of actions.
        """

        rawParams = locals().copy()
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
    
    
    def update(self, queue_mode:str='disabled', **others): #TODO test update
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp


class _Agents:
    """Agent Endpoint.

    Interact with agents endpoint.

    Official Documentation: https://halopsa.halopsa.com/apidoc/resources/agents

    Requires ? permission

    Progress (Temporary)
    - Get: Untested, no docstring
    - Search: Untested, no docstring
    - Update: Untested, no docstring
    - Delete: Not implemented
    """
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Agent'
        
    def get(self,id:int, includedetails:bool=False, **others): #TODO test get
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, team:Optional[str] = None, **others):
        
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test update
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp


class _Appointments:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Appointment'

    def get(self,id:int, includedetails:bool=False, **others): #TODO test get
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, **others): #TODO test search
        
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test update
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp


class _Assets: # TODO this is the only endpoint that actually works?
    """Assets Endpoint
    
    Get, add, and update your assets.
    
    Requires _ permission
    
    Official Documentation: https://halopsa.halopsa.com/apidoc/resources/assets
    
    Progress:
    - Get: Working
    - Search: Working
    - get_all: Working
    - Update: Partially working
    - Delete: Not implemented
    """
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Asset'
        self.formatted_params = []

    def get(self,
            id:int,
            includedetails:bool=True,
            includediagramdetails:bool=False,
            **others
            ):
        """
        Get a single asset's details. Requires atleast the asset ID.

        Supports all Halo parameters, even if not listed.  
        
        Args:
            id (int): Asset ID
            includedetails (bool, optional): Whether to include extra details (objects) in the response. Defaults to True.
            includediagramdetails (bool, optional): Whether to include diagram details in the response. Defaults to False.
            others (any): Any other supported Halo parameters
            
        Returns:
            dict: Asset information
        """

        rawParams = locals().copy()
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, includediagramdetails=includediagramdetails, others=others)
        return resp
    
    
    def search(self,
    pageinate:bool=False,
    page_size:int=50,
    page_no:int=1,
    order:Optional[str] = None,
    orderdesc:Optional[bool] = None,
    search:str | None = None,
    ticket_id:Optional[int] = None,
    client_id:Optional[int] = None,
    site_id:Optional[int] = None,
    username:str | None = None,
    assetgroup_id:Optional[int] = None,
    assettype_id:Optional[int] = None,
    linkedto_id:Optional[int] = None,
    includeinactive:Optional[bool] = None,
    includeactive:Optional[bool] = None,
    includechildren:Optional[bool] = None,
    contract_id:Optional[int] = None,
    **others
    ) -> dict:
        """
        Search assets.  Running with no parameters will get all assets.
        
        Supports all Halo parameters, even if not listed.  

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
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
    
    def get_all(self):
        """Get all halo assets

        Returns:
            list: List of assets OR error
        """
        print('Removing this, use search with no parameters instead')
        response = self._mh._requester('get',self.url)
        return response
        
    def update(self,
        id:Optional[int] = None,
        client_id:Optional[int] = None,
        site_id:Optional[int] = None,
        users:Optional[list] = None,
        fields:Optional[list] = None,
        queue_mode:str='disabled',
        **others
               ):
        """Add or update asset(s).  If ID is included, asset(s) will be updated, if ID is not included asset(s) will be added.
        
        QUEUE MODE CURRENTLY NOT WORKING

        Args:
            id (int, optional): Asset ID.
            client_id (int, optional): Client ID. 
            site_id (int, optional): Site ID. 
            users (list, optional): User IDs. 
            fields (list, optional): Fields to be updated.
            queue_mode (str, optional): Queue asset data to be sent as a single update update.  
            
            Queue modes: 
                disabled: Default, will update asset immediately. 
                queue: Queue the asset update to be sent later.
                update: Send queued updates to Halo.

        Returns:
            _type_: I dont think it returns anything...
        """
        if queue_mode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queue_mode} is not a valid Queue Mode.')
        
        rawParams = locals().copy()
        
        if queue_mode == 'disabled': # Sent request immediately
        
            response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams))
            return response
        
        elif queue_mode == 'queue': # Queue request.
            self.formatted_params += [self._mh._format_requests(rawParams)]
        
        elif queue_mode == 'update':
            response = self._mh._requester('post',self.url,self.formatted_params)
            self.formatted_params = [] # reset queue
            return response

class _Attachments:
    """Attachments Endpoint.

    [Brief description]

    Official Documentation: https://halopsa.halopsa.com/apidoc/resources/attachments

    Requires ? permission

    Progress (Temporary)
    - Get: Working
    - Search: Working
    - Update: Not implemented
    - Upload: In progress
    - Delete: Not implemented
    """
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Attachment'
    
    def search(self, 
        ticket_id:Optional[int] = None,
        action_id:Optional[int] = None,
        type:Optional[int] = None,
        unique_id:Optional[int] = None,
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
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
        
    def get(self, #TODO add docstring
            id:int,
            includedetails:bool=False,
            **others):
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def upload(self,
            id:Optional[int] = None,
            filename:Optional[str] = None,
            ticket_id:Optional[int] = None,
            data_base64:Optional[str] = None,
            **others):
        
        rawParams = locals().copy()
        response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams))
        return response
        

    def delete(self):
        pass
        
class _Clients:
    """Clients Endpoint.

    Get, create, update, and delete clients.

    Official Documentation: https://halopsa.halopsa.com/apidoc/resources/clients

    Requires _ permission

    Progress (Temporary)
    - Get: Working
    - get_all: Working, no docstring
    - Search: Working
    - Update: Working, partial docstring
    - Delete: Not implemented
    """
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Client'

    def search(self, # Test client_ids and client_id
        pageinate:bool=False,
        page_size:Optional[int] = None, # Switched to none
        page_no:int=1,
        order:Optional[str] = None,
        orderdesc:Optional[bool] = None,
        search:Optional[str] = None,
        toplevel_id:Optional[int] = None,
        includeinactive:Optional[bool] = None, #TODO should these be set to their defaults? instead of none
        includeactive:Optional[bool] = None,
        count:int=50,
        **others
               ):
        """Search clients. Supports unlisted parameters.
        By default, only the first 50 results are returned.  If more than 50 are needed, you must explicitely set count variable.  Leaving count blank will still return 50.

        Last tested: YYYY/MM/DD, V[HALO VERSION]
        
        Args:
            pageinate (bool, optional): Whether to use Pagination in the response. Defaults to False.
            page_size (int, optional): The size of the page if using pagination. Defaults to 50.
            page_no (int, optional): The page number to return if using pagination. Defaults to 1.
            count (int, optional): When not using pagination, the number of results to return. Set to 50 by default (even if not included).
            order (str, optional): The name of the field to order by.
            orderdesc (bool, optional): Whether to order ascending or descending. Defaults to decending sort.
            search (str, optional): Filter by Customers like your search.
            toplevel_id (int, optional): Filter by Customers belonging to a particular top level.
            includeinactive (bool, optional): Include inactive Customers in the response. Defaults to False.
            includeactive (bool, optional): Include active Customers in the response. Defaults to True.     
                   
        Returns:
            dict: Results and record count
            
        """
        rawParams = locals().copy()
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
        
    def get_all(self, #TODO add docsting #TODO add any other potentially useful toggles
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
        
        Last tested: YYYY/MM/DD, V[HALO VERSION]
        
        Args:
            id (int): Client ID
            includedetails (bool, optional): Whether to include extra details (objects) in the response. Defaults to False.
            includediagramdetails (bool, optional): Whether to include diagram details in the response. Defaults to False.

        Returns:
            dict: Single client details
        """

        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails,includediagramdetails=includediagramdetails,others=others) # Testing a new get system
        return resp
        
    def update(self, #TODO update the docstring
        id:Optional[int] = None,
        name:Optional[str] = None,
        toplevel_id:Optional[int] = None,
        due_date_type:Optional[int] = None,
        invoiceduedaysextraclient:Optional[int] = None, # This is due date int in other places
        queue_mode:str='disabled',
        **others
            ):
        """Create or update one or more clients.  If ID is included, client(s) will be updated.  If ID is not included new client(s) will be created.
        
        Last tested: YYYY/MM/DD, V[HALO VERSION]
        Args:
            id (int, optional): Client ID.
            queue_mode (str, optional): Queue asset data to be sent as a batch update.  Valid modes: disabled - Default, will update asset immediately. queue

        Returns:
            dict: Updated or created client(s).
        """
        if queue_mode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queue_mode} is not a valid Queue Mode.')
        rawParams = locals().copy()
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=rawParams)
        return resp



class _Contracts:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/ClientContract'
        
    def get(self,id:int, **others): #TODO test me
        
        resp = self._mh._get(url=self.url, id=id, others=others)
        return resp
    
    def search(self, 
        pageinate:bool=False,
        page_size:Optional[int] = None,
        page_no:Optional[int] = None,
        order:Optional[str] = None,
        orderdesc:Optional[bool] = None,
        search:Optional[str] = None,
        count:Optional[int] = None,
        **others):
        
        rawParams = locals().copy()
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp
    

class _Items:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Item'

    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:Optional[str] = None,
        orderdesc:Optional[bool] = None,
        search:Optional[str] = None,
        count:Optional[int] = None,
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
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
    
    def get(self,id:int, includedetails:bool=False, **others): #TODO test me
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def get_all(self):
        response = self.search()
        return response #TODO figure out what the dict name is for this
    
    def update(self,
        id:Optional[int] = None,
        costprice:Optional[float] = None,
        recurringcost:Optional[float] = None,
        baseprice:Optional[float] = None,
        recurringprice:Optional[float] = None,
        update_recurring_invoice_price:Optional[bool] = None,
        update_recurring_invoice_cost:Optional[bool] = None,
        queue_mode:str='disabled',
        **others
               ):
        """Creates or updates one or more assets.  If ID is included, asset(s) will be updated.  If ID is not included new asset(s) will be created.

        Args:
            id (int, optional): Asset ID.
            fields (list, optional): Fields to be updated.
            queue_mode (str, optional): Queue asset data to be sent as a batch update.  Valid modes: disabled - Default, will update asset immediately. queue

        Returns:
            _type_: I dont think it returns anything...
        """
        if queue_mode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queue_mode} is not a valid Queue Mode.')
        
        rawParams = locals().copy()
        
        if queue_mode == 'disabled': # Sent request immediately
        
            response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams))
            return response
        
        elif queue_mode == 'queue': # Queue request.
            self.formatted_params += [self._mh._format_requests(rawParams)]
        
        elif queue_mode == 'update':
            response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams))
            self.formatted_params = [] # reset queue
            return response

class _Invoices:
    """Invoices Endpoint.
    
    Get, add, and update your invoices.

    Official Documentation: https://halopsa.halopsa.com/apidoc/resources/invoices
    
    Progress:
    """
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Invoice' #TODO add docstring here
        
    def search(self, #TODO fix this #TODO add client_ids variable
        pageinate:bool=False,
        page_size:Optional[int] = None,
        page_no:Optional[int] = None,
        order:Optional[str] = None,
        orderdesc:Optional[bool] = None,
        search:Optional[str] = None,
        count:Optional[int] = None,
        ticket_id:Optional[int] = None,
        client_id:Optional[int] = None,
        site_id:Optional[int] = None,
        user_id:Optional[int] = None,
        postedonly:Optional[bool] = None,
        notpostedonly:Optional[bool] = None,
        includelines:bool=False,
        **others):
        
        rawParams = locals().copy()
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
    
    def get(self, #TODO test Get
            id:int,
            **others
            ):
        
        resp = self._mh._get(url=self.url, id=id, others=others)
        return resp
    
    def update(self,
               id:Optional[int] = None,
               lines:Optional[list] = None,
               **others
               ):
        
        rawParams = locals().copy()
        response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams))
        return response


class _KnowledgeBase:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/KBArticle'

    def get(self,id:int, includedetails:bool=False, **others): #TODO test me
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, **others): #TODO test me
        
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp

class _Opportunities:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Opportunities'
        
    def get(self,id:int, includedetails:bool=False, **others): #TODO test me
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, **others): #TODO test me
        
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp

class _Projects:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Projects'
        
    def get(self,id:int, includedetails:bool=False, includelastaction:bool=False, ticketidonly:bool=False, **others): #TODO test me
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, includelastaction=includelastaction, ticketidonly=ticketidonly, others=others)
        return resp
    
    def search(self, **others): #TODO test me
        
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp

class _Quotes:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Quotation'
        
    def get(self,id:int, includedetails:bool=False, **others): #TODO test me
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, **others): #TODO test me
        
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp

class _RecurringInvoices:
    """
    Recurring Invoices (RecurringInvoiceHeader) Endpoint.  Get, update, and delete your recurring invoices
    
    Official Documentation: Not officially listed in documentation, listed under "RecurringInvoiceHeader" in swagger (link below)
    Swagger: https://halo.halopsa.com/api/swagger/index.html
    
    Progress
    - Search: Partially tested
    - Get: Not implemented
    - get_all: Tested, needs docstring
    - Update: Partially tested
    - update_lines: Not tested
    - Delete: Not implemented
    """
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/RecurringInvoice'

    def search(self, #TODO add docstring #TODO figure out why page size is being returned at all if it isnt being used. #TODO add more relevant variables if any
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:Optional[str] = None,
        orderdesc:Optional[bool] = None,
        search:Optional[str] = None,
        count:Optional[int] = None,
        client_id:Optional[int] = None,
        includelines:bool=False,
        **others)-> dict:
        
        rawParams = locals().copy()
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
    
    def get(self,id:int, includedetails:bool=False, **others): #TODO test me
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def get_all(self, #TODO add docsting #TODO add any other potentially useful toggles
        includelines:bool=False)-> list[dict]:
        #This is literally just search but wrapped
        response = self.search(includelines=includelines)
        return response['invoices']
    
    def update(self, #TODO Test update #TODO fix docstring 
        id:Optional[int] = None,
        due_date_type:Optional[int] = None, #
        due_date_int:Optional[int] = None, # 
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
        
        queue_mode = 'disabled' #TODO Implement and test queue_mode
        if queue_mode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queue_mode} is not a valid Queue Mode.')
        
        rawParams = locals().copy()
        
        if queue_mode == 'disabled': # Sent request immediately
        
            response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams)) #TODO should params be formatted later?
            return response
        
        elif queue_mode == 'queue': # Queue request.
            self.formatted_params += [self._mh._format_requests(rawParams)]
        
        elif queue_mode == 'update':
            response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams))
            self.formatted_params = [] # reset queue
            return response
    
    def update_lines(self, #TODO test update_lines #TODO fix docstring
        id:int,
        ihid:int,
        **others):
        """Update recurring invoice lineitem(s).   
        
        WARNING: Ceej from TechPulse says this can cause issues.  Recommendation: Instead of using update_lines, copy all existing lines, add or make changes as needed, send ALL lines back using lines[<Your Lines Here>] with update method.

        Args:
            id (int): Recurring invoice line item ID (required)
            ihid (int): Recurring invoice ID (required)

        Returns:
            _type_: _description_
        """
        
        rawParams = locals().copy()
        response = self._mh._requester('get',self.url+'/UpdateLines',self._mh._format_requests(rawParams))
        return response        

class _Reports:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Report'
        
    def get(self,id:int, includedetails:bool=False, **others): #TODO Confirm variables
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, **others): #TODO test me
        
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp
        
class _Sites:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Site'
        
    def get(self,id:int, includedetails:bool=False, **others): #TODO Confirm variables
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, **others): #TODO test me
        
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp
        

class _Status:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Status'
        
    def get(self,id:int, includedetails:bool=False, **others): #TODO Test me
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, type:Optional[str] = None, showcounts:Optional[bool] = None, domain:Optional[str] = None, view_id:Optional[int] = None, excludepending:Optional[bool] = None, excludeclosed:Optional[bool] = None, **others): #TODO test me
        
        resp = self._mh._search(url=self.url, type=type, showcounts=showcounts, domain=domain, view_id=view_id, excludepending=excludepending, excludeclosed=excludeclosed, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp

class _Suppliers:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Supplier'
        
    def get(self,id:int, includedetails:bool=False, **others): #TODO Confirm variables
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, **others): #TODO test me
        
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp

class _Teams:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Team'
        
    def get(self,id:int, includedetails:bool=False, **others): #TODO Confirm variables
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, **others): #TODO test me
        
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp

class _TicketTypes:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/TicketType'
        
    def get(self,id:int, includedetails:bool=False, **others):
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def search(self, client_id:Optional[int] = None, showcounts:Optional[bool] = None, domain:Optional[str] = None, view_id:Optional[int] = None, showinactive:Optional[bool] = None, **others):

        rawParams = locals().copy()
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp

class _Tickets:
    """Tickets Endpoint.

    Get, create, update, and delete tickets.

    Official Documentation: https://halopsa.halopsa.com/apidoc/resources/tickets

    Requires _ permission

    Progress (Temporary)
    - Get: Working
    - Search: Working
    - Update: Working
    - Delete: Not implemented
    """
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Tickets'
    
    def update(self,
        actioncode:Optional[int] = None,
        id:Optional[int] = None,
        dateoccurred:Optional[str] = None,
        summary:Optional[str] = None,
        details:Optional[str] = None,
        details_html:Optional[str] = None,
        status_id:Optional[int] = None,
        tickettype_id:Optional[int] = None,
        sla_id:Optional[int] = None,
        client_id:Optional[int] = None,
        client_name:Optional[str] = None,
        site_id:Optional[int] = None,
        site_name:Optional[str] = None,
        user_id:Optional[int] = None,
        user_name:Optional[str] = None,
        agent_id:Optional[int] = None,
        parent_id:Optional[int] = None,
        queue_mode:str='disabled',
        **others
        ):
        """Creates or updates one or more tickets.  If ID is included, tickets(s) will be updated.  If ID is not included new ticket(s) will be created.
        
        Updating multiple tickets can be done by passing a list of tickets with relevant fields, or by passing individual updates with the queue_mode set to 'queue'.
        
        Last tested: 2025/04/03, V2.186.9
        
        Args:
            actioncode (int, optional): _description_. 
            id (int, optional): Ticket ID. If not provided, a new ticket will be created.
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
            parent_id (int, optional): Parent ticket ID.
            queue_mode (str, optional): Queue ticket data to be sent as a batch update.  This is done to reduce POST requests sent to Halo, by sending one POST request with all the needed updates.
                Modes: 
                - disabled - (Default) Updates ticket
                - queue - Queues a single item ready to be sent later.
                - update - Sends queued tickets to be updated/created.

        Returns:
            list: Created/updated ticket(s).
        """
        
        queue_mode = 'disabled'
        if queue_mode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queue_mode} is not a valid Queue Mode.')
        
        rawParams = locals().copy()
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=rawParams)
        return resp

    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:Optional[str] = None,
        orderdesc:Optional[bool] = None,
        search:Optional[str] = None,
        ticketidonly:Optional[bool] = None,
        view_id:Optional[int] = None,
        columns_id:Optional[int] = None,
        includecolumns:Optional[bool] = None,
        includeslaactiondate:Optional[bool] = None,
        includeslatimer:Optional[bool] = None,
        includetimetaken:Optional[bool] = None,
        includesupplier:Optional[bool] = None,
        includerelease1:Optional[bool] = None,
        includerelease2:Optional[bool] = None,
        includerelease3:Optional[bool] = None,
        includechildids:Optional[bool] = None,
        includenextactivitydate:Optional[bool] = None,
        includefirstresponse:Optional[bool] = None,
        include_custom_fields:Optional[str] = None,
        list_id:Optional[int] = None,
        agent_id:Optional[int] = None,
        status_id:Optional[int] = None,
        requesttype_id:Optional[int] = None,
        supplier_id:Optional[int] = None,
        client_id:Optional[int] = None,
        site:Optional[int] = None,
        username:Optional[str] = None,
        user_id:Optional[int] = None,
        release_id:Optional[int] = None,
        asset_id:Optional[int] = None,
        itil_requesttype_id:Optional[int] = None,
        open_only:Optional[bool] = None,
        closed_only:Optional[bool] = None,
        unlinked_only:Optional[bool] = None,
        contract_id:Optional[int] = None,
        withattachments:Optional[bool] = None,
        team:Optional[int] = None,
        agent:Optional[int] = None,
        status:Optional[int] = None,
        requesttype:Optional[int] = None,
        itil_requesttype:Optional[int] = None,
        category_1:Optional[int] = None,
        category_2:Optional[int] = None,
        category_3:Optional[int] = None,
        category_4:Optional[int] = None,
        sla:Optional[int] = None,
        priority:Optional[int] = None,
        products:Optional[int] = None,
        flagged:Optional[int] = None,
        excludethese:Optional[int] = None,
        searchactions:Optional[bool] = None,
        datesearch:Optional[str] = None,
        startdate:Optional[str] = None,
        enddate:Optional[str] = None,
        search_user_name:Optional[str] = None,
        search_summary:Optional[str] = None,
        search_details:Optional[str] = None,
        search_reportedby:Optional[str] = None,
        search_version:Optional[str] = None,
        search_release1:Optional[str] = None,
        search_release2:Optional[str] = None,
        search_release3:Optional[str] = None,
        search_releasenote:Optional[str] = None,
        search_inventory_number:Optional[str] = None,
        search_oppcontactname:Optional[str] = None,
        search_oppcompanyname:Optional[str] = None,
        count:int=50,
        **others
               ):

        rawParams = locals().copy()
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp

        
    def get(self,
        id:int,
        includedetails:bool=False,
        includelastaction:bool=False,
        ticketidonly:bool=False,
        **others
        ):
        """
        Get a single ticket.  Requires atleast ID to be provided.
        
        Args:
            id (int): Ticket ID
            includedetails (bool, optional): Whether to include extra details (objects) in the response. Defaults to False.
            includelastaction (bool, optional): Whether to include the last action in the response. Defaults to False.
            ticketidonly (bool, optional): Returns only the ID fields (Ticket ID, SLA ID, Status ID, Client ID and Name and Lastincomingemail date) of the Tickets. Defaults to False.

        Returns:
            dict: Ticket information/details
        """

        rawParams = locals().copy()
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, includelastaction=includelastaction, ticketidonly=ticketidonly, others=others)
        return resp
    
        
class _Users:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Users'
        
    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:Optional[str] = None,
        orderdesc:Optional[bool] = None,
        search:Optional[str] = None,
        search_phonenumbers:Optional[bool] = None,
        toplevel_id:Optional[int] = None,
        client_id:Optional[int] = None,
        site_id:Optional[int] = None,
        organisation_id:Optional[int] = None,
        department_id:Optional[int] = None,
        asset_id:Optional[int] = None,
        includeinactive:Optional[bool] = None,
        includeactive:Optional[bool] = None,
        approversonly:Optional[bool] = None,
        excludeagents:Optional[bool] = None,
        count:Optional[int] = None,
        **others):
        """Search Users

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
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
        
    def get(self, # TODO test me
            id:int,
            includedetails:bool=True,
            includeactivity:Optional[bool] = None,
            includepopups:Optional[bool] = None,
            **others
            ):
        """Get a single user's details.  Requires atleast ID to be provided.
        
        Supports all Halo parameters, even if not listed.  
        
        Args:
            id (int): User ID
            includedetails (bool, optional): Whether to include extra details in the response. Defaults to True.
            includeactivity (bool, optional): Whether to include User's ticket activity in the response. Defaults to False.
            includepopups (bool, optional): Whether to include customer pop ups in the response. Defaults to False.

        Returns:
            dict: Single users details
        """
        
        rawParams = locals().copy()
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, includeactivity=includeactivity, includepopups=includepopups, others=others)
        return resp
    
    def get_all(self):
        """Get all users.

        Returns:
            list: All your users
        """
        
        response = self.search(count=1000000) #TODO make sure to note that the maximum here is 100000
        return response['users']

    def update(self,
        id:Optional[int] = None,
        name:Optional[str] = None,
        site_id:Optional[int] = None,
        site_name:Optional[str] = None,
        client_name:Optional[str] = None,
        firstname:Optional[str] = None,
        surname:Optional[str] = None,
        initials:Optional[str] = None,
        title:Optional[str] = None,
        emailaddress:Optional[str] = None,
        phonenumber_preferred:Optional[str] = None,
        sitephonenumber:Optional[str] = None,
        phonenumber:Optional[str] = None,
        homenumber:Optional[str] = None,
        mobilenumber:Optional[str] = None,
        mobilenumber2:Optional[str] = None,
        fax:Optional[str] = None,
        telpref:Optional[int] = None,
        activedirectory_dn:Optional[str] = None,
        container_dn:Optional[str] = None,
        login:Optional[str] = None,
        inactive:Optional[bool] = None,
        colour:Optional[str] = None,
        isimportantcontact:Optional[bool] = None,
        other1:Optional[str] = None,
        other2:Optional[str] = None,
        other3:Optional[str] = None,
        other4:Optional[str] = None,
        other5:Optional[str] = None,
        neversendemails:Optional[bool] = None,
        roles:Optional[list] = None,
        queue_mode = 'disabled',
        **others):
        """Update or create user(s).

        Args:
            id (int, optional): User ID.  If no ID is provided, a new user will be created
            ILL ADD THE REST LATER ON GOD
        
        Returns:
            dict: Updated/created user(s)
        """
        
        queue_mode = 'disabled' #TODO Implement and test queue_mode
        if queue_mode.lower() not in ['disabled','queue','update']:
            raise AttributeError(f'{queue_mode} is not a valid Queue Mode.')
        
        rawParams = locals().copy()
        
        if queue_mode == 'disabled': # Sent request immediately
        
            response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams)) #TODO should params be formatted later?
            return response
        
        elif queue_mode == 'queue': # Queue request.
            self.formatted_params += [self._mh._format_requests(rawParams)]
        
        elif queue_mode == 'update':
            response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams))
            self.formatted_params = [] # reset queue
            return response
        
    def delete(self):
        pass

# NON STANDARD

class _DistributionLists:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/DistributionLists'
        
    def get_all(self): # All distribution lists

        rawParams = locals().copy()
        response = self._mh._requester('get',self.url,self._mh._format_requests(rawParams))
        return response
    
    def get(self, # Only accepts one item #TODO check if there are any hidden params #TODO allow a way to get users?
            id:int
            ):

        rawParams = locals().copy()
        resp = self._mh._get(url=self.url, id=id)
        return resp
    
    def create(self,
        name:str,
        description:Optional[str] = None,
        mailbox_from:Optional[int] = None,
        mailbox_replyto:Optional[int] = None,
        third_party_url:Optional[str] = None,
        dynamic_members:Optional[bool] = None,
        **others
        ):
        rawParams = locals().copy()
        response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams))
        return response
    
    
    def update(self,
        id:int,
        addtheseusers:Optional[list] = None,
        removetheseusers:Optional[list] = None,): # TODO add docstring
        rawParams = locals().copy()
        response = self._mh._requester('post',self.url,self._mh._format_requests(rawParams))
        return response

class _TopLevel:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/TopLevel'

    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:Optional[str] = None,
        orderdesc:Optional[bool] = None,
        search:Optional[str] = None,
        count:Optional[int] = None,
        **others):
        
        rawParams = locals().copy()
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
    
    def get(self,id:int, includedetails:bool=False, **others): #TODO Confirm variables
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    def get_all(self): #TODO add docsting #TODO add any other potentially useful toggles
        #This is literally just search but wrapped
        response = self.search()
        return response['tree']
    
    
class _Currency:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/Currency'

    def search(self,
        pageinate:bool=False,
        page_size:int=50,
        page_no:int=1,
        order:Optional[str] = None,
        orderdesc:Optional[bool] = None,
        search:Optional[str] = None,
        count:Optional[int] = None,
        **others):
        
        rawParams = locals().copy()
        
        resp = self._mh._search(url=self.url, others=rawParams)
        return resp
    
    def get(self,id:int, includedetails:bool=False, **others): #TODO Confirm variables
        
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    

class _SoftwareLicences:
    """Software Licences/Subscriptions Endpoint.

    Get, create, update, and delete customer software licenses or subscriptions

    No official documentation

    Requires ? permission

    Progress (Temporary)
    - Get: Working
    - Search: Untested
    - Update: Untested
    - Delete: Not implemented
    """
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/SoftwareLicence'

        
        
    def get(self,id:int, **others): #TODO Confirm variables
        """Get Software License/Subscription.
        Args:
            id (int, optional): ID of license/subscription.
            
        Last tested: 2025/03/28, V2.184.45
        
        
        """
        resp = self._mh._get(url=self.url, id=id, others=others)
        return resp
    
    def search(self, **others):
        """Search Software Licenses/Subscriptions.

        Last tested: 2025/04/15, V2.188.7
        """
        resp = self._mh._search(url=self.url, others=others)
        return resp
    
    def update(self, id:Optional[int] = None, type:Optional[int] = None, name:Optional[str] = None, queue_mode:str='disabled', **others): 
        """Update or create Software Licenses/Subscriptions.
        
        Args:
            id (int, optional): ID of existing license/subscription.  If none provided, a new item will be created
            type (int): Item type (Software License, Subscription, etc.).
            name (str, optional): Licence/subscription name. Optional if updating existing item
        
        Last tested: 2025/04/15, V2.188.7
        """
        resp = self._mh._update(url=self.url, id=id, type=type, name=name, queue_mode=queue_mode, others=others)
        return resp #TODO will using ID and TYPE cause problems
    

class _UserRoles:
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/UserRoles'

    
    def get_all(self):
        """Get all User Roles.

        Returns:
            list: User Roles
        """
        
        rawParams = locals().copy()
        response = self._mh._requester('get',self.url,self._mh._format_requests(rawParams))
        return response
    
    def get(self,
            id:int,
            includedetails:bool=True,
            **others
            ):
        """Get a single User Role by ID.  Using this currently requires the API permission "all", not just "all:standard"

        Args:
            id (int): User Role ID
            includedetails (bool, optional): Include additional details/information. Defaults to True.

        Returns:
            dict: User Role information
        """
    
        resp = self._mh._get(url=self.url, id=id, includedetails=includedetails, others=others)
        return resp
    
    
class _InvoiceChange:
    """Invoice Change endpoint

    Get, create, and update invoice change information.  Includes recurring invoices.

    No official documentation

    Requires ? permission

    Progress (Temporary)
    - Get: No option to get a single item, use search with filters instead. 
    - Search: Working
    - Update: Untested
    """
    def __init__(self, mh:_MethodsHelper):
        self._mh = mh
        self.url = mh.url + '/InvoiceChange'
    
    def search(self, search:Optional[str] = None, invoice_id:Optional[int] = None, line_id:Optional[int] = None, idonly:Optional[bool] = None, type_id:Optional[int] = None, count:Optional[int] = None, **others):
        """Search Invoice Changes.

        Last tested: 2025/04/01, V2.184.45

        Args:
            search (str, optional): Filter by string.
            invoice_id (int, optional):Filter by invoice ID.
            line_id (int, optional): Filter by invoice line ID.
            idonly (bool, optional): Whether to return only the ID.
            type_id (int, optional): Filter by type ID.
            count (int, optional): Maximum items to return.

        Returns:
            list: List of matching changes
        """
        
        resp = self._mh._search(url=self.url, search=search, count=count, invoice_id=invoice_id, line_id=line_id, idonly=idonly, type_id=type_id, others=others)
        return resp
    
    def update(self, queue_mode:str='disabled', **others): #TODO test me
        
        resp = self._mh._update(url=self.url, queue_mode=queue_mode, others=others)
        return resp

