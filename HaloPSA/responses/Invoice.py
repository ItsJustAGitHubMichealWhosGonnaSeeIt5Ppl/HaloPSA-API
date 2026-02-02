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
class Invoice: #/components/schemas/InvoiceHeader
	customfields: list | None
	id: int
	use: str | None
	client_id: int | None
	client_name: str | None
	sitenumber: int | None
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
	salesorder_id: int | None
	datetype: int | None
	percentold: int | None
	percent: float | None
	contract_id: int | None
	contract_ref: str | None
	datesent: datetime | None
	currency: str | None
	currency_code: int | None
	currency_conversion_rate: float | None
	paymentterms: int | None
	hideinvoice: bool | None
	ticket_id: int | None
	invoicetype: int | None
	datepaid: datetime | None
	paymentstatus: int | None
	xeroid: str | None
	amountpaid: float | None
	amountdue: float | None
	emailstatus: int | None
	address: list
	shipaddress: list
	originaddress: list
	lines: list | None
	pdftemplate_id: int | None
	total: float
	duedate: datetime | None
	is_recurring_invoice: bool | None
	recurring_invoice_id: int | None
	add_contract_assets: int | None
	add_labour: int | None
	add_project: int | None
	add_travel: int | None
	add_mileage: int | None
	add_itemsissued: int | None
	add_prepay: int | None
	add_salesorder: int | None
	qboid: int | None
	billingcategory: int | None
	xero_tenant_id: str | None
	xero_branding_theme_id: str | None
	xero_branding_theme_name: str | None
	due_date_int: int | None
	due_date_type: int | None
	createdbyagentname: str | None
	internal_note: str | None
	kashflow_tenant_id: int | None
	kashflow_pdf: str | None
	original_client_id: int | None
	original_client_name: str | None
	xero_status: str | None
	merge_data: list | None
	snelstart_id: str | None
	date_created: datetime | None
	qbo_company_id: str | None
	dbc_id: str | None
	dbc_company_id: str | None
	creditlinkedtoinvoiceid: int | None
	creditlinkedtoinvoiceid_thirdpartynumber: str | None
	sage_business_cloud_details_id: int | None
	sage_business_cloud_id: str | None
	exact_id: str | None
	exact_division: int | None
	xero_line_tax: str | None
	schedule_ignore_delete: bool | None
	assigned_agent: int | None
	assigned_agent_name: str | None
	approval_status: int | None
	approvalagent: int | None
	approvalemailaddress: str | None
	approvalnote: str | None
	approvalagentid: int | None
	approvaldatetime: datetime | None
	requires_approval: bool | None
	xero_online_invoice_payment_url: str | None
	take_payment_on_duedate: int | None
	credit_total: float | None
	customer_paid_total: float | None
	supplier_id: int | None
	include_in_autopay: bool | None
	twilio_invoice: bool | None
	invoice_separately: bool | None
	minimum_price_active: bool | None
	minimum_amount: float | None
	voided: bool | None
	mark_credit_as_used: bool | None
	invoice_display: str | None
	change_seq: int | None
	is_down_payment: bool | None
	recognised_from_invoice: int | None
	tax_total: float | None
	revenue: float | None
	type: int
	client: list
	disabled: bool | None = field(default=None)
	site_name: str | None = field(default=None)
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
	taken_by: str | None = field(default=None)
	order_number: str | None = field(default=None)
	cust_order_number: str | None = field(default=None)
	payment_ref: str | None = field(default=None)
	global_nom_code: str | None = field(default=None)
	global_details: str | None = field(default=None)
	invoice_type_code: str | None = field(default=None)
	currency_code_name: str | None = field(default=None)
	amount_remaining: float | None = field(default=None)
	add_lines: list | None = field(default=None)
	_print_preview: bool | None = field(default=None)
	_print_generate: bool | None = field(default=None)
	printhtml: str | None = field(default=None)
	pdf_attachment_id: int | None = field(default=None)
	pdf_attachment_date_created: datetime | None = field(default=None)
	pdftemplate_name: str | None = field(default=None)
	composite_tax_total: float | None = field(default=None)
	reference: str | None = field(default=None)
	last_reminder_sent: datetime | None = field(default=None)
	_is_invoice_run: bool | None = field(default=None)
	_billing_cut_off: datetime | None = field(default=None)
	schedule_id: int | None = field(default=None)
	lastcreated: datetime | None = field(default=None)
	nextcreationdate: datetime | None = field(default=None)
	period: int | None = field(default=None)
	schedule: list | None = field(default=None)
	create_recurring_invoice: bool | None = field(default=None)
	take_auto_payment: bool | None = field(default=None)
	force_creation: bool | None = field(default=None)
	_create_from_areaitems: list | None = field(default=None)
	_create_from_contract: int | None = field(default=None)
	_validateonly: bool | None = field(default=None)
	_sendmassinvoice: bool | None = field(default=None)
	xero_branding_theme: list | None = field(default=None)
	mailboxid: int | None = field(default=None)
	period_type: int | None = field(default=None)
	kashflowid: int | None = field(default=None)
	time: datetime | None = field(default=None)
	startdate: datetime | None = field(default=None)
	enddate: datetime | None = field(default=None)
	daysplus: int | None = field(default=None)
	invoiceday: int | None = field(default=None)
	periodname: str | None = field(default=None)
	_isimport: bool | None = field(default=None)
	duedatename: str | None = field(default=None)
	invoice_prorata_periods_ahead: int | None = field(default=None)
	nextcreationperiod: str | None = field(default=None)
	intacct_recordno: int | None = field(default=None)
	period_start_date: datetime | None = field(default=None)
	period_end_date: datetime | None = field(default=None)
	payments: list | None = field(default=None)
	markaspaid: bool | None = field(default=None)
	markaspaidmoduleid: int | None = field(default=None)
	reviewrequired: bool | None = field(default=None)
	_warning: str | None = field(default=None)
	_xmlwarning: str | None = field(default=None)
	creditlinkedtoinvoiceid_typeid: int | None = field(default=None)
	purchaseorder_id: int | None = field(default=None)
	invoice_auto_increase_period: int | None = field(default=None)
	invoice_percent_increase: float | None = field(default=None)
	approvalticketid: int | None = field(default=None)
	ticket_summary: str | None = field(default=None)
	ticket_note: str | None = field(default=None)
	approval_start: bool | None = field(default=None)
	new_approvalprocess_agent_id: int | None = field(default=None)
	new_approvalprocess_email: str | None = field(default=None)
	new_approvalprocess_cab_id: int | None = field(default=None)
	new_approvalprocess_users: list | None = field(default=None)
	new_approvalprocess_cab: list | None = field(default=None)
	approval_process_id: int | None = field(default=None)
	generic_online_invoice_payment_url: str | None = field(default=None)
	intacct_save_location: str | None = field(default=None)
	intacctseparatetaxline: int | None = field(default=None)
	intacct_class: str | None = field(default=None)
	intacct_class_name: str | None = field(default=None)
	contains_calculated_quantity: bool | None = field(default=None)
	intacct_tax_solution: str | None = field(default=None)
	intacct_tax_solution_name: str | None = field(default=None)
	intacct_project: str | None = field(default=None)
	intacct_project_name: str | None = field(default=None)
	_create_credit_note: bool | None = field(default=None)
	supplier_name: str | None = field(default=None)
	_dont_fire_automations: bool | None = field(default=None)
	_is_process: bool | None = field(default=None)
	_is_task_schedule: bool | None = field(default=None)
	payments_pending: int | None = field(default=None)
	_forcethirdpartysync: bool | None = field(default=None)
	client_to_invoice_to_id: int | None = field(default=None)
	creation_source: str | None = field(default=None)
	typeid: int | None = field(default=None)
	minimum_line_description: str | None = field(default=None)
	avalara_details_id: int | None = field(default=None)
	qbo_term_name: str | None = field(default=None)
	qbo_term_id: int | None = field(default=None)
	qbo_term: list | None = field(default=None)
	exact_payment_conditon_name: str | None = field(default=None)
	exact_payment_conditon_id: str | None = field(default=None)
	exact_payment_conditon: list | None = field(default=None)
	avalara_details_name: str | None = field(default=None)
	credit_date: datetime | None = field(default=None)
	credit_outstanding_for_customer: float | None = field(default=None)
	credit_outstanding: float | None = field(default=None)
	credit_used: float | None = field(default=None)
	apply_credit: bool | None = field(default=None)
	apply_credit_id: int | None = field(default=None)
	apply_credit_amount: float | None = field(default=None)
	apply_credit_description: str | None = field(default=None)
	apply_credit_long_description: str | None = field(default=None)
	apply_credit_tax_type: int | None = field(default=None)
	_novalidate: bool | None = field(default=None)
	sqlimport_id: int | None = field(default=None)
	invoice_match_id: str | None = field(default=None)
	sync_include_paid: bool | None = field(default=None)
	dont_set_original_client_id: bool | None = field(default=None)
	_docommitsync: bool | None = field(default=None)
	_ignore_dont_send_invoice: bool | None = field(default=None)
	sendinvoicereminder: bool | None = field(default=None)
	ticket_client_to_invoice_to_id: int | None = field(default=None)
	originaddress1: str | None = field(default=None)
	originaddress2: str | None = field(default=None)
	originaddress3: str | None = field(default=None)
	originaddress4: str | None = field(default=None)
	originaddress5: str | None = field(default=None)
	most_recent_invoice_id: int | None = field(default=None)
	most_recent_invoice_type: int | None = field(default=None)
	custombuttons: list | None = field(default=None)
	extratabs: list | None = field(default=None)
	update_invoice_conversion_rate: bool | None = field(default=None)
	conversion_rate: float | None = field(default=None)
	dont_sync_to_3rd_party: bool | None = field(default=None)
	is_invoice_screen: bool | None = field(default=None)
	note_count: int | None = field(default=None)
	csp_invoice_id: int | None = field(default=None)
	cloned_from_client_id: int | None = field(default=None)
	bcd_posted: bool | None = field(default=None)
	invoice_totals: list | None = field(default=None)
	immediate_prorata_recurring_invoice_id: int | None = field(default=None)
	toplevel_name: str | None = field(default=None)
	suppliers_order_reference: str | None = field(default=None)
	apply_credit_credit_outstanding: float | None = field(default=None)
	quickbooks_close_period_date: datetime | None = field(default=None)
	quickbooks_period_closed: bool | None = field(default=None)
	last_change_agent: int | None = field(default=None)
	last_change_seq: int | None = field(default=None)
	ignore_change_seq: bool | None = field(default=None)
	invoice_template_id: int | None = field(default=None)
	is_recognition: bool | None = field(default=None)
	xero_default_payment_nominalcode: str | None = field(default=None)
	_dotaxsync: bool | None = field(default=None)
	external_links: list | None = field(default=None)
	_importtypeid: int | None = field(default=None)
	_importthirdpartyid: str | None = field(default=None)
	_importtype: str | None = field(default=None)
	new_external_link: list | None = field(default=None)
	import_details_id: int | None = field(default=None)
	_isupdateimport: bool | None = field(default=None)
	site: list | None = field(default=None)

	def __post_init__(self):
		if self.invoice_date:
			self.invoice_date = datetime.fromisoformat(self.invoice_date)
		if self.schedule_date:
			self.schedule_date = datetime.fromisoformat(self.schedule_date)
		if self.dateposted:
			self.dateposted = datetime.fromisoformat(self.dateposted)
		if self.last_synced:
			self.last_synced = datetime.fromisoformat(self.last_synced)
		if self.last_modified:
			self.last_modified = datetime.fromisoformat(self.last_modified)
		if self.datesent:
			self.datesent = datetime.fromisoformat(self.datesent)
		if self.datepaid:
			self.datepaid = datetime.fromisoformat(self.datepaid)
		if self.pdf_attachment_date_created:
			self.pdf_attachment_date_created = datetime.fromisoformat(self.pdf_attachment_date_created)
		if self.duedate:
			self.duedate = datetime.fromisoformat(self.duedate)
		if self.last_reminder_sent:
			self.last_reminder_sent = datetime.fromisoformat(self.last_reminder_sent)
		if self._billing_cut_off:
			self._billing_cut_off = datetime.fromisoformat(self._billing_cut_off)
		if self.lastcreated:
			self.lastcreated = datetime.fromisoformat(self.lastcreated)
		if self.nextcreationdate:
			self.nextcreationdate = datetime.fromisoformat(self.nextcreationdate)
		if self.time:
			self.time = datetime.fromisoformat(self.time)
		if self.startdate:
			self.startdate = datetime.fromisoformat(self.startdate)
		if self.enddate:
			self.enddate = datetime.fromisoformat(self.enddate)
		if self.date_created:
			self.date_created = datetime.fromisoformat(self.date_created)
		if self.period_start_date:
			self.period_start_date = datetime.fromisoformat(self.period_start_date)
		if self.period_end_date:
			self.period_end_date = datetime.fromisoformat(self.period_end_date)
		if self.approvaldatetime:
			self.approvaldatetime = datetime.fromisoformat(self.approvaldatetime)
		if self.credit_date:
			self.credit_date = datetime.fromisoformat(self.credit_date)
		if self.quickbooks_close_period_date:
			self.quickbooks_close_period_date = datetime.fromisoformat(self.quickbooks_close_period_date)
# Debug method for creating items from dictionary - This comment is required or dedent dedents everything
	@classmethod
	def from_dict(cls, dictionary:dict):
		return cls(**{
			k: v for k, v in dictionary.items()
			if k in inspect.signature(cls).parameters
		})