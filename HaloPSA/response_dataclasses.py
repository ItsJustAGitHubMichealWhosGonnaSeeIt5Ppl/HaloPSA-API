# BUILT-IN
import collections
from dataclasses import dataclass
from dataclasses import field
from datetime import datetime
from typing import Any
import inspect

# EXTERNAL

#INTERNAL

#CODE
@dataclass
class Action:
    ticket_id: int | None
    id: int
    outcome: str | None
    

@dataclass
class Invoice: #TODO can fields that are none just not be returned. Is that even good practice?
    
    # Always returned
    customfields: list | None # TODO Create CustomField object
    id: int
    use: str | None
    client_id: int | None
    client_name: str | None
    sitenumber: int | None
    site_name: str | None
    uid: int | None
    invoicenumber: str | None
    thirdpartyinvoicenumber: str | None
    posted: bool | None
    name: str | None
    invoice_date: datetime | None
    schedule_date: datetime | None
    dateposted: datetime | None
    last_synced: datetime | None
    last_modified: datetime | None
    taken_by: str | None
    order_number: str | None
    cust_order_number: str | None
    payment_ref: str | None
    global_nom_code: str | None
    global_details: str | None
    invoice_type_code: str | None
    salesorder_id: int | None
    datetype: int | None
    percentold: int | None
    percent: int | None
    contract_id: int | None
    contract_ref: str | None
    datesent: datetime | None
    currency: str | None
    currency_code: int | None
    currency_conversion_rate: int | None
    paymentterms: int | None
    
    
    # Only returned if includedetails is True
    currency_code_name: str | None = field(default=None)
    
    # Not retuned if None/null
    disabled: bool | None = field(default=None)
    accountsid: str | None = field(default=None)
    address1: str | None = field(default=None)
    address2: str | None = field(default=None)
    address3: str | None = field(default=None)
    address4: str | None = field(default=None)
    address5: str | None = field(default=None)
    deladdress1: str | None = field(default=None)
    deladdress2: str | None = field(default=None)
    deladdress3: str | None = field(default=None)
    deladdress4: str | None = field(default=None)
    deladdress5: str | None = field(default=None)
    tel_number: str | None = field(default=None)
    contactname: str | None = field(default=None)
    global_tax_code: str | None = field(default=None)
    notes_1: str | None = field(default=None)
    notes_2: str | None = field(default=None)
    notes_3: str | None = field(default=None)
    
    
    def __post_init__(self):
        datetime_variables = [self.invoice_date, self.schedule_date, self.dateposted] # TODO can these be passed in from list
        
        if self.invoice_date: # Not blank or none
            self.invoice_date = datetime.strptime(self.invoice_date, "%Y-%m-%dT%H:%M:%S")
        
        if self.schedule_date: # Not blank or none
            self.schedule_date = datetime.strptime(self.schedule_date, "%Y-%m-%dT%H:%M:%S")
        
        if self.dateposted: # Not blank or none
            self.dateposted = datetime.strptime(self.dateposted, "%Y-%m-%dT%H:%M:%S.%f")
        
        if self.last_synced: # Not blank or none
            self.last_synced = datetime.strptime(self.last_synced, "%Y-%m-%dT%H:%M:%S.%f")
        
        if self.last_modified: # Not blank or none
            self.last_modified = datetime.strptime(self.last_modified, "%Y-%m-%dT%H:%M:%S.%f")
        
        if self.datesent: # Not blank or none
            self.datesent = datetime.strptime(self.datesent, "%Y-%m-%dT%H:%M:%S")
    
    # Ignore variables that are not currently in dataclass, this should be removed once the dataclass is completed
    # Code from: https://stackoverflow.com/a/55096964
    @classmethod 
    def from_dict(cls, dictionary:dict):
        return cls(**{
            k: v for k, v in dictionary.items() 
            if k in inspect.signature(cls).parameters 
        })
    
class InvoiceList(collections.UserList):

    def __init__(self, init_data: list[dict[str, Any]]):
        invoices = [Invoice(**data) for data in init_data]
        super().__init__(invoices)