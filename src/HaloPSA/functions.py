import requests
import urllib.parse
import json
import os


class apiCaller:
    """All available functions, endpoint independant"""
    
    def __init__(self, baseURL, function, endpoint, params, header,*payload):
        self.allEndpoints = ['Action','Agent','Appointment','Asset','Attachment','Client','ClientContract','Invoice','Item','KBArticle','Opportunities','Projects','Quotation','Report','Site','Status','Supplier','Team','TicketType','Tickets','Users','RecurringInvoice','RecurringInvoice/UpdateLines'] # Endpoints function can be used with
        
        if function.lower() not in ['search','get','update','delete','me']:
            raise Exception('Invalid function')
        elif endpoint not in self.allEndpoints:
            raise Exception('Invalid endpoint')
        else:
            pass # No issues, continue
        self.url = baseURL + '/' + endpoint
        self.formattedData = {}
        self.validParams = [] # Placeholder for validation later
        self.header = header
        self.params = params
        self.payload = '' if len(payload) == 0 else payload
        
        self._formatter() # Format data
        
        
        if function.lower() == 'search':
            query = urllib.parse.urlencode(self.formattedData)
            self.url += '?' + query
            self._requester('get')
            
        elif function.lower() == 'get':
            eyeD = str(self.formattedData['id']) # get ID
            self.formattedData.pop('id') # Remove ID from query.
            query = urllib.parse.urlencode(self.formattedData)
            self.url += '/' + eyeD + '?' + query
            self._requester('get')
            
        elif function.lower() == 'update':
            self.payload = json.dumps([self.formattedData],indent=4)
            self._requester('post')
            
        elif function.lower() == 'delete':
            self.delete()



    def getData(self):
        return self.responseData
    
    def _formatter(self):
        paramsToAdd = self.params | self.params['others'] # Copy params and add any additional items
        paramsToAdd.pop('others') # Remove 'others' dict item to avoid confusion
        paramsToAdd.pop('self')
        
        pageinateToggle = False
        for item, value in paramsToAdd.items(): # Check params, add anything that isn't blank to the query

            if item == 'pageinate' and value == True:
                pageinateToggle = True

            if pageinateToggle == False and item in ['page_size','page_no']: # Skip redundant values
                continue
            
            if value !=None:
                self.formattedData.update({item : value})

    
    def _requester(self,method):
        response = requests.request(method,self.url,headers=self.header,data=self.payload)
        
        code = response.status_code
        
        # Invalid URL
        if code in [404]:
            print(f'404 -  The specified URL is invalid. URL: {self.url}')
        content = json.loads(response.content)
        
        # Success
        if code in [200,201]:
            # 201 = Created
            # 200 = OK
            self.responseData = content

        elif code in [401]:
            # Return clearer errors
            if content["error_description"] == 'The specified client credentials are invalid.':
                # Specify it is the client secret that is wrong, not the client ID.
                print('The specified \'client_secret\' is invalid')
            else:
                print(content["error_description"])
        elif code in [400]:
            print(f'{code} - Bad Request')
            raise Exception( f'{code} - Bad Request')
                
        # Add unique failures as found
        
        # If secret, client ID, or URL are wrong, error 401 is returned
        else:
            raise Exception( f'{code} - Other failure')
        
        
        pass
    def get(self):
        validEndpoints = self.allEndpoints
        pass
    def update(self):
        validEndpoints = self.allEndpoints
        pass
    def delete(self):
        validEndpoints = self.allEndpoints
        pass
    def me():
        validEndpoints = ['agents'] # Endpoints function can be used with
        
    
    
def testFunc(test='word',b=2,**other):
    copyLocals = locals().copy()
    fullList = copyLocals.copy()
    otherLocals = copyLocals['other'].copy()
    fullList = fullList | otherLocals
    print(fullList)

if __name__=="__main__":
    testFunc(data=2,otherData=3)

