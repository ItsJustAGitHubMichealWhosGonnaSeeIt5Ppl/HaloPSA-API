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
class Ticket: #/components/schemas/Faults
	id: int
	dateoccurred: datetime | None
	summary: str | None
	details: str | None
	status_id: int | None
	tickettype_id: int | None
	sla_id: int | None
	sla_name: str | None
	priority_id: int | None
	client_id: int | None
	client_name: str | None
	site_id: int | None
	site_name: str | None
	user_id: int | None
	user_name: str | None
	team_id: int | None
	team: str | None
	agent_id: int | None
	category_1: str | None
	category_2: str | None
	category_3: str | None
	category_4: str | None
	estimate: float | None
	estimatedays: float | None
	timetaken: float | None
	supplier_name: str | None
	child_count: int | None
	attachment_count: int | None
	flagged: bool | None
	read: bool | None
	enduserstatus: int | None
	onhold: bool | None
	respondbydate: datetime | None
	fixbydate: datetime | None
	excludefromsla: bool | None
	slaholdtime: float | None
	site_timezone: str | None
	lastactiondate: datetime | None
	last_update: datetime | None
	organisation_id: int | None
	department_id: int | None
	matched_kb_id: int | None
	product_id: int | None
	product_name: str | None
	release_id: int | None
	release2_id: int | None
	release3_id: int | None
	workflow_name: str | None
	lastincomingemail: datetime
	workflow_id: int | None
	workflow_step: int | None
	pipeline_stage_id: int | None
	is_vip: bool | None
	isimportantcontact: bool | None
	inactive: bool | None
	impact: int | None
	urgency: int | None
	starttime: str | None
	starttimeslot: int | None
	targetdate: datetime | None
	targettime: str | None
	targettimeslot: int | None
	deadlinedate: datetime | None
	oppcountry: str | None
	oppregion: str | None
	oppvalueadjusted: float | None
	cost: float | None
	quantity: int | None
	userdef1: str | None
	userdef2: str | None
	userdef3: str | None
	userdef4: str | None
	userdef5: str | None
	source: int | None
	release_important: bool | None
	releasenotegroup_id: int | None
	supplier_status: int | None
	appointment_type: int | None
	customfields: list | None
	section_timezone: str | None
	projectinternaltask: bool | None
	impactlevel: int | None
	reviewed: bool | None
	merged_into_id: int | None
	details_html: str | None
	takenby: str | None
	datecreated: datetime | None
	createdfrom_id: int | None
	top_level_id: int | None
	site_sla_id: int | None
	supplier_contract_id: int | None
	supplier_breachrespsent: bool | None
	supplier_breachfixbysent: bool | None
	showforusers: bool | None
	messsent: str | None
	agreedcleared: bool | None
	backoutplan: str | None
	communicationplan: str | None
	testplan: str | None
	riskdescription: str | None
	risklevel: int | None
	impactdescription: str | None
	surveysent: bool | None
	approval_process_step_name: str | None
	inform3rdpartysystem: bool | None
	surveyneeded: bool | None
	knownerror: bool | None
	development: bool | None
	changeseq: int | None
	mailboxid: int | None
	actisbillabledefault: bool | None
	chargerate: int | None
	timezonename: str | None
	forwardinboundupdates: bool | None
	loggedoutofhdworkinghours: bool | None
	acctmaninformedsurvey: bool | None
	laststatuschangeinformed: int | None
	loggedonbehalfby: str | None
	auditstatus: int | None
	auditunum: int | None
	auditdate: datetime | None
	oppdontaddtomailinglist: bool | None
	sendprintrequest: int | None
	pagerdutyid: str | None
	pagerdutyincidentidstring: str | None
	pagerdutystatus: int | None
	component_id: int | None
	version_id: int | None
	mailentryid: str | None
	contract_id: int | None
	workflow_stepstarted: datetime | None
	laststatuschangeinformedmanager: int | None
	currency: int | None
	projectconsignmentheaderid: int | None
	projectconsignmentdetailid: int | None
	servicefailurestid: int | None
	hdid: int | None
	deleted: bool | None
	matched_rule_id: int | None
	ignore_kb_match: bool | None
	deadlinenotificationhours: float | None
	showonroadmap: bool | None
	phonenumberfrom: str | None
	addressfrom: str | None
	changeinformation_html: str | None
	team_department_id: int | None
	newaction_emailfrom: int | None
	_canupdate: bool | None
	appointment_count: int | None
	open_chat_count: int | None
	task_count: int | None
	email_start_tag_override: str | None
	email_end_tag_override: str | None
	follower_count: int | None
	todo_count: int | None
	service_count: int | None
	businessapp_count: int | None
	is_opportunity: bool | None
	is_project: bool | None
	items_issued_count: int | None
	quotation_count: int | None
	salesorder_count: int | None
	purchaseorder_count: int | None
	invoice_line_count: int | None
	budgettype_id: int | None
	azure_tenants_name: str | None
	canbechild: bool | None
	locked: bool | None
	has_related: bool | None
	pagerdutyeragent: int | None
	devops_agent: str | None
	devops_comment_count: int | None
	your_vote: int | None
	your_vote_comment: str | None
	scomalertstate: int | None
	orionalertid: int | None
	orionalertactiveid: int | None
	orionacknowledgestate: int | None
	orionclosestate: int | None
	orionacknowledgedby: int | None
	orionacknowledgedate: datetime | None
	orionacknowledgenote: str | None
	orionalertname: str | None
	servicenow_id: str | None
	splunkoncall_id: str | None
	splunkoncallurl: str | None
	splunkoncallstatus: int | None
	connectwise_id: int | None
	connectwise_project_id: int | None
	servicenow_number: str | None
	autotask_id: int | None
	autotask_number: str | None
	atera_alert_id: int | None
	laststatuschangestatus: int | None
	laststatuschangestatusdate: datetime | None
	meraki_device: str | None
	meraki_alert_type: str | None
	powershell_script_count: int | None
	devops_workitem_count: int | None
	ninja_alert_id: str | None
	ninja_device_id: int | None
	isbillable: bool | None
	itemsarebillable: bool | None
	who: str | None
	resourcetype_id: int | None
	resource_booking_type: int | None
	faultapprovalfailed: bool | None
	article_type: int | None
	automate_id: int | None
	device_automate_id: int | None
	auvik_id: str | None
	auvik_url: str | None
	jira_issue_count: int | None
	call_log_count: int | None
	freshdesk_id: int | None
	external_links: list | None
	alluserscanview: int | None
	sync_to_salesforce: bool | None
	visible_child_tickets: int
	expenses: list | None
	ncentral_details_id: int | None
	supplier_contact_id: int | None
	pagerdutyservice: str | None
	linked_halo_ticket_count: int | None
	whatsappcreatedfromid: str | None
	sms_override: str | None
	thirdpartyreviewscore: int | None
	datto_alert_state: int | None
	reviewed_date: datetime | None
	is_sensitive: bool | None
	contract_schedule_plan_id: int | None
	hide_feedback: bool | None
	ola_count: int | None
	ai_suggested_urgency: int | None
	ai_suggested_impact: int | None
	_can_view_att: bool | None
	_can_upload_att: bool | None
	_can_download_att: bool | None
	_can_edit_att: bool | None
	_can_view_action_history: bool | None
	table: list
	use: str | None
	canbevotedfor: bool | None
	ticketage: float | None
	useful_count: int | None
	notuseful_count: int | None
	updateservicestatus: bool | None
	servicestatusnote: str | None
	itil_requesttype_id: int | None
	ticket_tags: str | None
	opp_region_name: str | None
	invoiceseperatelyoverride: bool | None
	purchaseordernumber: str | None
	billable_time: float | None
	_open_search_score: int
	reference: str | None
	status_name: str | None = field(default=None)
	tickettype_name: str | None = field(default=None)
	agent_name: str | None = field(default=None)
	categoryid_1: int | None = field(default=None)
	categoryid_2: int | None = field(default=None)
	categoryid_3: int | None = field(default=None)
	categoryid_4: int | None = field(default=None)
	category_1_display: str | None = field(default=None)
	category_2_display: str | None = field(default=None)
	category_3_display: str | None = field(default=None)
	category_4_display: str | None = field(default=None)
	projecttimepercentage: float | None = field(default=None)
	projectcompletionpercentage: float | None = field(default=None)
	projectearlieststart: datetime | None = field(default=None)
	projectlatestend: datetime | None = field(default=None)
	faigeneratedsummary_list: str | None = field(default=None)
	chargehours: float | None = field(default=None)
	nonchargehours: float | None = field(default=None)
	travelhours: float | None = field(default=None)
	totalmileage: float | None = field(default=None)
	itemsprice: float | None = field(default=None)
	items: str | None = field(default=None)
	parent_id: int | None = field(default=None)
	child_count_open: int | None = field(default=None)
	responsedate: datetime | None = field(default=None)
	first_responsedate: datetime | None = field(default=None)
	responsestartdate: datetime | None = field(default=None)
	slaresponsestate: str | None = field(default=None)
	dateclosed: datetime | None = field(default=None)
	dateassigned: datetime | None = field(default=None)
	parentguid: str | None = field(default=None)
	parentassign: bool | None = field(default=None)
	slaactiondate: datetime | None = field(default=None)
	slapercused: float | None = field(default=None)
	slatimeleft: float | None = field(default=None)
	currentelapsedhours: float | None = field(default=None)
	lastchildactiondate: datetime | None = field(default=None)
	reportedby: str | None = field(default=None)
	user_email: str | None = field(default=None)
	emailtolist: str | None = field(default=None)
	emailtolistsupplier: str | None = field(default=None)
	emailcclist: str | None = field(default=None)
	emailcclistsupplier: str | None = field(default=None)
	release_note: str | None = field(default=None)
	release_name: str | None = field(default=None)
	release2_name: str | None = field(default=None)
	release3_name: str | None = field(default=None)
	child_ticket_id_string: str | None = field(default=None)
	asset_key_field_string: str | None = field(default=None)
	asset_type_name: str | None = field(default=None)
	workflow_stage: str | None = field(default=None)
	workflow_stage_id: int | None = field(default=None)
	workflow_stage_number: str | None = field(default=None)
	child_ticket_ids: list | None = field(default=None)
	nextactivitydate: datetime | None = field(default=None)
	nextactivityorappointmentdate: datetime | None = field(default=None)
	inventory_number: str | None = field(default=None)
	workflow_seq: int | None = field(default=None)
	pipeline_stage_name: str | None = field(default=None)
	hasbeenclosed: bool | None = field(default=None)
	unread_child_action_count: int | None = field(default=None)
	unread_related_action_count: int | None = field(default=None)
	child_action_count: int | None = field(default=None)
	parent_subject: str | None = field(default=None)
	related_action_count: int | None = field(default=None)
	startdate: datetime | None = field(default=None)
	startdate_timezone: str | None = field(default=None)
	startdate_with_timezone: list | None = field(default=None)
	targetdate_timezone: str | None = field(default=None)
	targetdate_with_timezone: list | None = field(default=None)
	targetpercused: float | None = field(default=None)
	targettimeleft: float | None = field(default=None)
	followupdate: datetime | None = field(default=None)
	oppcontactname: str | None = field(default=None)
	oppcompanyname: str | None = field(default=None)
	oppemailaddress: str | None = field(default=None)
	oppcustomertitle: str | None = field(default=None)
	opptel: str | None = field(default=None)
	oppaddr1: str | None = field(default=None)
	oppaddr2: str | None = field(default=None)
	oppaddr3: str | None = field(default=None)
	oppaddr4: str | None = field(default=None)
	opppostcode: str | None = field(default=None)
	opptype: str | None = field(default=None)
	oppvalue: float | None = field(default=None)
	oppvalue_monthly: float | None = field(default=None)
	oppvalue_annual: float | None = field(default=None)
	oppvalue_oneoff: float | None = field(default=None)
	oppconversionprobability: float | None = field(default=None)
	oppprofit: float | None = field(default=None)
	oppcurrentsystem: str | None = field(default=None)
	oppcompetitors: str | None = field(default=None)
	opptrialdate: datetime | None = field(default=None)
	oppdemodate: datetime | None = field(default=None)
	oppdiscountdate: datetime | None = field(default=None)
	oppattemptsmade: int | None = field(default=None)
	oppconverteddate: datetime | None = field(default=None)
	oppproductchosen: str | None = field(default=None)
	oppreason: str | None = field(default=None)
	opphear: str | None = field(default=None)
	opptimezonename: str | None = field(default=None)
	oppclosurecategory: int | None = field(default=None)
	projecttimebudget: float | None = field(default=None)
	projectmoneybudget: float | None = field(default=None)
	projecttimeactual: float | None = field(default=None)
	projectmoneyactual: float | None = field(default=None)
	lastnote: str | None = field(default=None)
	releasenotegroup_name: str | None = field(default=None)
	third_party_id: int | None = field(default=None)
	third_party_id_string: str | None = field(default=None)
	contract_refextra: str | None = field(default=None)
	timeentries: list | None = field(default=None)
	itilname: str | None = field(default=None)
	related_service_descriptions: str | None = field(default=None)
	related_businessapps_descriptions: str | None = field(default=None)
	related_service_category_names: str | None = field(default=None)
	appointment_id: int | None = field(default=None)
	nextappointmentdate: datetime | None = field(default=None)
	firstname: str | None = field(default=None)
	lastname: str | None = field(default=None)
	connectedinstance_id: int | None = field(default=None)
	web_url: str | None = field(default=None)
	api_url: str | None = field(default=None)
	action_number: int | None = field(default=None)
	action_ticket_id: int | None = field(default=None)
	action_datetime: datetime | None = field(default=None)
	action_outcome: str | None = field(default=None)
	action_chargerate: str | None = field(default=None)
	action_contract_ref: str | None = field(default=None)
	action_note: str | None = field(default=None)
	ticket_invoices_for_each_site: bool | None = field(default=None)
	salesorder_id: int | None = field(default=None)
	orderhead_id: int | None = field(default=None)
	budgettype: str | None = field(default=None)
	requesttype_name: str | None = field(default=None)
	recalculate_billing: bool | None = field(default=None)
	supplier_id: int | None = field(default=None)
	pr_id: int | None = field(default=None)
	branch_id: int | None = field(default=None)
	branch_name: str | None = field(default=None)
	update_milestone_id: int | None = field(default=None)
	milestone_id: int | None = field(default=None)
	milestone_name: str | None = field(default=None)
	milestone_billing_type: int | None = field(default=None)
	milestone_value: float | None = field(default=None)
	milestone_sequence: int | None = field(default=None)
	milestone_status: int | None = field(default=None)
	milestone_startdate: datetime | None = field(default=None)
	milestone_enddate: datetime | None = field(default=None)
	colour: str | None = field(default=None)
	action_agent_name: str | None = field(default=None)
	reassigncount: int | None = field(default=None)
	parent_status: int | None = field(default=None)
	parent_agent: int | None = field(default=None)
	child_status: int | None = field(default=None)
	date_fully_closed: datetime | None = field(default=None)
	lastaction_chargerate: str | None = field(default=None)
	hover_summary: str | None = field(default=None)
	slatimeelapsed: float | None = field(default=None)
	ai_summary: str | None = field(default=None)
	search_score: float | None = field(default=None)
	main_project_id: int | None = field(default=None)
	is_maintenance: bool | None = field(default=None)
	phonenumber: str | None = field(default=None)
	createdfrom_summary: str | None = field(default=None)
	clonedfrom_id: int | None = field(default=None)
	clonedfrom_summary: str | None = field(default=None)
	closure_note: str | None = field(default=None)
	closure_note_html: str | None = field(default=None)
	closure_time: float | None = field(default=None)
	customer_relationships: str | None = field(default=None)
	asset_number: int | None = field(default=None)
	asset_site: int | None = field(default=None)
	slastate: str | None = field(default=None)
	slaexcuse: str | None = field(default=None)
	client_reference: str | None = field(default=None)
	supplier_slaexcuse: str | None = field(default=None)
	supplier_date: datetime | None = field(default=None)
	supplier_contract_ref: str | None = field(default=None)
	supplier_sla_id: int | None = field(default=None)
	supplier_priority_id: int | None = field(default=None)
	supplier_responsestate: str | None = field(default=None)
	supplier_responsedate: datetime | None = field(default=None)
	supplier_responsetime: float | None = field(default=None)
	supplier_respondbydate: datetime | None = field(default=None)
	supplier_slastate: str | None = field(default=None)
	supplier_slatimeelapsed: float | None = field(default=None)
	supplier_dateclosed: datetime | None = field(default=None)
	supplier_fixbydate: datetime | None = field(default=None)
	changestate: str | None = field(default=None)
	approvedby: int | None = field(default=None)
	satisfactionlevel: int | None = field(default=None)
	satisfactioncomment: str | None = field(default=None)
	invoicenumber: str | None = field(default=None)
	invoicenote: str | None = field(default=None)
	invoicedate: datetime | None = field(default=None)
	invoicepaiddate: datetime | None = field(default=None)
	nonbillable_time: float | None = field(default=None)
	mileage: float | None = field(default=None)
	planneddate: datetime | None = field(default=None)
	ccaddress: str | None = field(default=None)
	responsetime: float | None = field(default=None)
	first_responsetime: float | None = field(default=None)
	alsoinform: str | None = field(default=None)
	justification: str | None = field(default=None)
	service_id: int | None = field(default=None)
	isparentservice: bool | None = field(default=None)
	planneddateend: datetime | None = field(default=None)
	currentfaactionnumber: int | None = field(default=None)
	approval_process_step: int | None = field(default=None)
	approval_cab_name: str | None = field(default=None)
	approval_process_id: int | None = field(default=None)
	faultcodeopen: int | None = field(default=None)
	faultcode: int | None = field(default=None)
	laststatus3rdparty: int | None = field(default=None)
	deliverycontact: str | None = field(default=None)
	delivery_address: list | None = field(default=None)
	causedby: int | None = field(default=None)
	messsentlast: str | None = field(default=None)
	unapprovedchangestatus: int | None = field(default=None)
	lastrecurringemailsentdate: datetime | None = field(default=None)
	template_id: int | None = field(default=None)
	template_name: str | None = field(default=None)
	child_template_id: int | None = field(default=None)
	slaholdreminderdatelastemailed: datetime | None = field(default=None)
	closurereminderdatelastemailed: datetime | None = field(default=None)
	assetstring: str | None = field(default=None)
	alerttype: str | None = field(default=None)
	emaildisplayname: str | None = field(default=None)
	emailpriority: int | None = field(default=None)
	gfialerttype: str | None = field(default=None)
	quotedescription: str | None = field(default=None)
	quotelabouramount: float | None = field(default=None)
	quotepriority: int | None = field(default=None)
	budgetcode: int | None = field(default=None)
	actualcost: float | None = field(default=None)
	invoicestatus: int | None = field(default=None)
	invoicedescription: str | None = field(default=None)
	invoicelabouramount: float | None = field(default=None)
	invoicematerialsamount: float | None = field(default=None)
	firsttimefix: int | None = field(default=None)
	quotematerialsamount: float | None = field(default=None)
	ukasaccredited: bool | None = field(default=None)
	labno: str | None = field(default=None)
	twitterscreenname: str | None = field(default=None)
	twitterid: int | None = field(default=None)
	facebook_id: str | None = field(default=None)
	fixbydateadjusted: bool | None = field(default=None)
	alternativecontactno: str | None = field(default=None)
	operationalserviceid: int | None = field(default=None)
	requestdetailsprinted: bool | None = field(default=None)
	serviceformprinted: bool | None = field(default=None)
	auditnote: str | None = field(default=None)
	auditfaileddate: datetime | None = field(default=None)
	auditfailednote: str | None = field(default=None)
	userrequestedapprover: int | None = field(default=None)
	pagerdutyurl: str | None = field(default=None)
	pagerdutyincidentid: str | None = field(default=None)
	opportunity_third_party_url: str | None = field(default=None)
	pr_link: str | None = field(default=None)
	github_repository: str | None = field(default=None)
	component_name: str | None = field(default=None)
	version_name: str | None = field(default=None)
	contract_ref: str | None = field(default=None)
	billing_address: list | None = field(default=None)
	lessonslearned: str | None = field(default=None)
	lastbugzillasync: datetime | None = field(default=None)
	sapid: str | None = field(default=None)
	sapattachmentsuuid: str | None = field(default=None)
	matched_rule_name: str | None = field(default=None)
	matched_rule_dont_show_notification: bool | None = field(default=None)
	asset_type: int | None = field(default=None)
	roadmapnote: str | None = field(default=None)
	sendack: bool | None = field(default=None)
	newaction_emailfrom_address_override: str | None = field(default=None)
	_mustupdateticketuser: bool | None = field(default=None)
	_spam: bool | None = field(default=None)
	_spamblock: bool | None = field(default=None)
	users_name: str | None = field(default=None)
	sibling_count_open: int | None = field(default=None)
	parent_summary: str | None = field(default=None)
	parent_status_name: str | None = field(default=None)
	new_approvalprocess: int | None = field(default=None)
	new_approvalprocess_agent_id: int | None = field(default=None)
	new_approvalprocess_user_id: int | None = field(default=None)
	new_approvalprocess_email: str | None = field(default=None)
	new_approvalprocess_cab_id: int | None = field(default=None)
	approvers: list | None = field(default=None)
	approvers_history: list | None = field(default=None)
	create_article: bool | None = field(default=None)
	qualifications: list | None = field(default=None)
	target_adjust: int | None = field(default=None)
	start_adjust: int | None = field(default=None)
	dont_do_rules: bool | None = field(default=None)
	dont_do_databaselookups: bool | None = field(default=None)
	apply_rules: bool | None = field(default=None)
	apply_this_rule: int | None = field(default=None)
	_forcereassign: bool | None = field(default=None)
	_appointment01_ok: bool | None = field(default=None)
	_agent01_ok: bool | None = field(default=None)
	_agent02_ok: bool | None = field(default=None)
	_asset01_ok: bool | None = field(default=None)
	return_this: bool | None = field(default=None)
	_validate_form: bool | None = field(default=None)
	_validate_updates: bool | None = field(default=None)
	attachments: list | None = field(default=None)
	documents: list | None = field(default=None)
	popup_notes: list | None = field(default=None)
	current_action_type: str | None = field(default=None)
	current_action_name: str | None = field(default=None)
	_ispreview: bool | None = field(default=None)
	assets: list | None = field(default=None)
	nochangesequpdate: bool | None = field(default=None)
	_reclose: bool | None = field(default=None)
	_reclose_oid: int | None = field(default=None)
	_recover: bool | None = field(default=None)
	contact_address: list | None = field(default=None)
	chat_id: int | None = field(default=None)
	actioncode: int | None = field(default=None)
	clone_count: int | None = field(default=None)
	copy_milestone: bool | None = field(default=None)
	todo_list: list | None = field(default=None)
	unsubscribedfromserviceid: int | None = field(default=None)
	items_issued: list | None = field(default=None)
	project_items_issued: list | None = field(default=None)
	third_party_client_id: str | None = field(default=None)
	_refreshresponse: bool | None = field(default=None)
	_isimport: bool | None = field(default=None)
	_isalert: bool | None = field(default=None)
	_novalidate: bool | None = field(default=None)
	is_closure_reminder_closure: bool | None = field(default=None)
	is_slahold_reminder_closure: bool | None = field(default=None)
	_importid: int | None = field(default=None)
	sendtopagerduty: bool | None = field(default=None)
	splunkurl: str | None = field(default=None)
	splunksearch: str | None = field(default=None)
	budgettype_name: str | None = field(default=None)
	budgets: list | None = field(default=None)
	process_ai: bool | None = field(default=None)
	send_remoteinvite: bool | None = field(default=None)
	invite_emaillist: str | None = field(default=None)
	third_party_call_id: str | None = field(default=None)
	remotetechid: int | None = field(default=None)
	linkremotesession: bool | None = field(default=None)
	remotesessionid: int | None = field(default=None)
	utcoffset: float | None = field(default=None)
	form_id: str | None = field(default=None)
	database_lookup_result: list | None = field(default=None)
	azure_tenants: str | None = field(default=None)
	_warning: str | None = field(default=None)
	_warning_is_error: str | None = field(default=None)
	close_unassigned: bool | None = field(default=None)
	_changefreeze01_ok: bool | None = field(default=None)
	_maintenance01_ok: bool | None = field(default=None)
	_force: bool | None = field(default=None)
	_ticketclash01_ok: bool | None = field(default=None)
	_milestonedate01_ok: bool | None = field(default=None)
	_ignoremilestonedates: bool | None = field(default=None)
	elapsed_response_hours: float | None = field(default=None)
	elapsed_resolution_hours: float | None = field(default=None)
	sla_start_date: datetime | None = field(default=None)
	_print_generate: bool | None = field(default=None)
	printhtml: str | None = field(default=None)
	pdf_attachment_id: int | None = field(default=None)
	journeys: list | None = field(default=None)
	_dontupdate_devops: bool | None = field(default=None)
	category_note_1: str | None = field(default=None)
	category_user_note_1: str | None = field(default=None)
	category_include_note_1: bool | None = field(default=None)
	category_itil_1: int | None = field(default=None)
	category_note_2: str | None = field(default=None)
	category_user_note_2: str | None = field(default=None)
	category_include_note_2: bool | None = field(default=None)
	category_itil_2: int | None = field(default=None)
	category_note_3: str | None = field(default=None)
	category_user_note_3: str | None = field(default=None)
	category_include_note_3: bool | None = field(default=None)
	category_itil_3: int | None = field(default=None)
	category_note_4: str | None = field(default=None)
	category_user_note_4: str | None = field(default=None)
	category_include_note_4: bool | None = field(default=None)
	category_itil_4: int | None = field(default=None)
	_iszapier: bool | None = field(default=None)
	ncentral_ticketid: str | None = field(default=None)
	_isnotify: bool | None = field(default=None)
	created_from_action_id: int | None = field(default=None)
	created_from_action_name: str | None = field(default=None)
	createacknowledgement: bool | None = field(default=None)
	donotapplytemplateintheapi: bool | None = field(default=None)
	_create_outstanding_appointments: bool | None = field(default=None)
	_create_outstanding_appointment_email: bool | None = field(default=None)
	_acknowledgealert: bool | None = field(default=None)
	orionacknowledgedbyname: str | None = field(default=None)
	third_party_parent_id: str | None = field(default=None)
	third_party_problem_id: str | None = field(default=None)
	opened_by: str | None = field(default=None)
	resolved_by: str | None = field(default=None)
	sendtosplunkoncall: bool | None = field(default=None)
	splunkoncalltarget: int | None = field(default=None)
	splunkoncalltarget_id: str | None = field(default=None)
	prepay_balance_hours: float | None = field(default=None)
	prepay_balance_amount: float | None = field(default=None)
	parent_ticket_type_name: str | None = field(default=None)
	createdfrom_ticket_type_name: str | None = field(default=None)
	clonedfrom_ticket_type_name: str | None = field(default=None)
	syncro_alert_id: int | None = field(default=None)
	mark_as_read_only: bool | None = field(default=None)
	audit_log: list | None = field(default=None)
	matched_rules: list | None = field(default=None)
	usertype: int | None = field(default=None)
	actionworkflowset: bool | None = field(default=None)
	childrenlefttocreate: bool | None = field(default=None)
	resourcetype_name: str | None = field(default=None)
	resource_booking_timeslot: datetime | None = field(default=None)
	resource_booking_asset: int | None = field(default=None)
	matched_rule_ids: str | None = field(default=None)
	forceruleupdate: bool | None = field(default=None)
	teams_user_id: str | None = field(default=None)
	_isteams: bool | None = field(default=None)
	article_description: str | None = field(default=None)
	article_resolution: str | None = field(default=None)
	article_notes: str | None = field(default=None)
	tags: list | None = field(default=None)
	dontcreatechild: bool | None = field(default=None)
	needcreatechild: bool | None = field(default=None)
	sentinel_id: str | None = field(default=None)
	sentinel_resourcegroup: str | None = field(default=None)
	sentinel_subscriptionid: str | None = field(default=None)
	sentinel_workspace: str | None = field(default=None)
	faultapprovalexists: bool | None = field(default=None)
	_validate_only: bool | None = field(default=None)
	_validation_key: str | None = field(default=None)
	azuremonitor_id: str | None = field(default=None)
	domotz_alertid: int | None = field(default=None)
	domotz_deviceid: int | None = field(default=None)
	domerge: bool | None = field(default=None)
	isnew: bool | None = field(default=None)
	contract_balance: str | None = field(default=None)
	bookingurl: str | None = field(default=None)
	isclone: bool | None = field(default=None)
	clonedfrom: int | None = field(default=None)
	slatimeremaining: float | None = field(default=None)
	customfieldvalidationreason: str | None = field(default=None)
	_has_automations: bool | None = field(default=None)
	chat_count: int | None = field(default=None)
	_dont_update_project_dates: bool | None = field(default=None)
	_dontupdate_jira: bool | None = field(default=None)
	sentinel_url: str | None = field(default=None)
	sentinel_display_id: int | None = field(default=None)
	postloggedview: int | None = field(default=None)
	addigy_alert_id: str | None = field(default=None)
	ninja_alert_type: str | None = field(default=None)
	_match_thirdparty_id: str | None = field(default=None)
	_match_integration_id: int | None = field(default=None)
	_match_integration_name: str | None = field(default=None)
	kaseya_agent_id: str | None = field(default=None)
	kaseya_asset_name: str | None = field(default=None)
	salesforce_contactid: str | None = field(default=None)
	salesforce_accountid: str | None = field(default=None)
	salesforce_parentid: str | None = field(default=None)
	salesforce_status: str | None = field(default=None)
	newrelic_id: str | None = field(default=None)
	newrelicincident_id: str | None = field(default=None)
	backup_radar_id: int | None = field(default=None)
	backup_radar_state: int | None = field(default=None)
	linktypesarray: list | None = field(default=None)
	kaseyaid: str | None = field(default=None)
	_dontupdate_salesforce: bool | None = field(default=None)
	salesforce_stage: int | None = field(default=None)
	_newticket_quickclose: bool | None = field(default=None)
	service_request_detail_id: int | None = field(default=None)
	check_status_freeze: bool | None = field(default=None)
	clear_feedback: bool | None = field(default=None)
	facebook_message_id: str | None = field(default=None)
	twitter_message_id: int | None = field(default=None)
	requesttype_published_id: str | None = field(default=None)
	chat_key_id: str | None = field(default=None)
	parent_itil_ticket_type: int | None = field(default=None)
	parent_release_note: str | None = field(default=None)
	parent_release_name: str | None = field(default=None)
	parent_release2_name: str | None = field(default=None)
	parent_release3_name: str | None = field(default=None)
	pagerdutyservice_name: str | None = field(default=None)
	_dontupdate_pagerduty: bool | None = field(default=None)
	_dont_fire_automations: bool | None = field(default=None)
	teamsmessage: str | None = field(default=None)
	zoom_default_message: str | None = field(default=None)
	default_teams_chat_name: str | None = field(default=None)
	show_chat_create: bool | None = field(default=None)
	htmlmessage: str | None = field(default=None)
	halolink_ticketid: int | None = field(default=None)
	override_opening_action_who: bool | None = field(default=None)
	unotes: str | None = field(default=None)
	smemo: str | None = field(default=None)
	amemo: str | None = field(default=None)
	_matchintacctclass: bool | None = field(default=None)
	intacct_class: str | None = field(default=None)
	intacct_class_name: str | None = field(default=None)
	device_name: str | None = field(default=None)
	milestones: list | None = field(default=None)
	disable_milestone_modification: bool | None = field(default=None)
	email_message_id: str | None = field(default=None)
	seenby: str | None = field(default=None)
	recaptcha_token: str | None = field(default=None)
	resource_booking_site: int | None = field(default=None)
	extratabs: list | None = field(default=None)
	new_approvalprocess_role_id: int | None = field(default=None)
	new_approvalprocess_customfieldid: int | None = field(default=None)
	linked_ecommerce_order_number: str | None = field(default=None)
	linked_ecommerce_order_url: str | None = field(default=None)
	parent_milestones: list | None = field(default=None)
	vectors: list | None = field(default=None)
	ai_matched_tickets: list | None = field(default=None)
	ai_matched_tickets_incidents: list | None = field(default=None)
	ai_matched_tickets_requests: list | None = field(default=None)
	ai_matched_tickets_problems: list | None = field(default=None)
	ai_matched_articles: list | None = field(default=None)
	ai_suggestions: list | None = field(default=None)
	_apply_ai_suggestions: list | None = field(default=None)
	_dismiss_ai_suggestions: list | None = field(default=None)
	suggested_category1: str | None = field(default=None)
	forwarded_by: int | None = field(default=None)
	instagram_message_id: str | None = field(default=None)
	default_reporter: int | None = field(default=None)
	defaultsendattachments: bool | None = field(default=None)
	devops_key: str | None = field(default=None)
	related_tickets: list | None = field(default=None)
	new_related_tickets: list | None = field(default=None)
	unrelate_from_ticket_id: int | None = field(default=None)
	ecommerce_orders: list | None = field(default=None)
	workflow_history: list | None = field(default=None)
	connectwisermm_ticketid: str | None = field(default=None)
	colour_rule: int | None = field(default=None)
	google_reviewdata: list | None = field(default=None)
	google_questiondata: list | None = field(default=None)
	original_agent: int | None = field(default=None)
	oppjobtitle: str | None = field(default=None)
	do_lookups: bool | None = field(default=None)
	liongard_system_id: int | None = field(default=None)
	bigpanda_id: str | None = field(default=None)
	contributors: list | None = field(default=None)
	internet_message_id: str | None = field(default=None)
	matching_value: str | None = field(default=None)
	sqlimport_id: int | None = field(default=None)
	respondbydateadjusted: bool | None = field(default=None)
	date_dependencies: list | None = field(default=None)
	new_milestone_ticket: int | None = field(default=None)
	assets_columns: list | None = field(default=None)
	slaresponseexcuse: str | None = field(default=None)
	can_add_cc_followers: bool | None = field(default=None)
	_fromchatprofileid: str | None = field(default=None)
	lapsafe_count: int | None = field(default=None)
	olas: list | None = field(default=None)
	new_workflow_history: list | None = field(default=None)
	default_slack_channel_name: str | None = field(default=None)
	show_channel_create: bool | None = field(default=None)
	slack_channel_id: str | None = field(default=None)
	slack_callback_id: str | None = field(default=None)
	ai_suggested_priority: str | None = field(default=None)
	ai_suggested_resolution: str | None = field(default=None)
	ai_generated_summary: str | None = field(default=None)
	ai_search_query: str | None = field(default=None)
	ai_suggested_type: str | None = field(default=None)
	ai_sentiment_analysis: str | None = field(default=None)
	ai_satisfaction_level: str | None = field(default=None)
	ai_tonality: str | None = field(default=None)
	_isagentuser: bool | None = field(default=None)
	ai_survey_score: int | None = field(default=None)
	ai_survey_comment: str | None = field(default=None)
	freshdesk_ticket_data: list | None = field(default=None)
	freshdesk_group_name: str | None = field(default=None)
	freshdesk_agent_name: str | None = field(default=None)
	freshdesk_agent_email: str | None = field(default=None)
	freshdesk_product_name: str | None = field(default=None)
	matched_kb_id_acessible_to_user: bool | None = field(default=None)
	remotesession_count: int | None = field(default=None)
	search_index_sync_timestamp: datetime | None = field(default=None)
	search_index_sync_batches: int | None = field(default=None)
	new_whe_: datetime | None = field(default=None)
	new_actioncode: int | None = field(default=None)
	notepad: str | None = field(default=None)
	embedding_match_timestamp: datetime | None = field(default=None)
	_re_index: bool | None = field(default=None)
	_fetch_matches: bool | None = field(default=None)
	workflow_move_date_override: datetime | None = field(default=None)
	lookup_search: str | None = field(default=None)
	agent_booking_type: int | None = field(default=None)
	agent_booking: list | None = field(default=None)
	pandadoc_attachment: int | None = field(default=None)
	pandadoc_attachment_name: str | None = field(default=None)
	pandadoc_attachment_url: str | None = field(default=None)
	thirdparty_url: str | None = field(default=None)
	security_signal_id: str | None = field(default=None)
	datadog_id: str | None = field(default=None)
	ai_conversation_summary: str | None = field(default=None)
	incomingevent_count: int | None = field(default=None)
	azure_connection_id: int | None = field(default=None)
	kblinkid: int | None = field(default=None)
	ticket_client_to_invoice_to_id: int | None = field(default=None)
	ticket_client_to_invoice_to_name: str | None = field(default=None)
	_prevent_outgoing: bool | None = field(default=None)
	dont_copy_history: bool | None = field(default=None)
	user_linked_sites: list | None = field(default=None)
	prepay_threshold: list | None = field(default=None)
	automation_entity_type: int | None = field(default=None)
	make_automation_entity_inactive: bool | None = field(default=None)
	is_downtime: bool | None = field(default=None)
	add_tags: list | None = field(default=None)
	locked_by_agentid: int | None = field(default=None)
	_forceunlock: bool | None = field(default=None)
	_is_aisuggestion_merge: bool | None = field(default=None)
	service_linked_device: int | None = field(default=None)
	quick_ticket_link_text: str | None = field(default=None)
	_override_child_merge_type: int | None = field(default=None)
	next_review_date: datetime | None = field(default=None)
	kb_pdf_template: int | None = field(default=None)
	kb_pdftemplate_name: str | None = field(default=None)
	template_when_linked: int | None = field(default=None)
	templatewhenlinked_name: str | None = field(default=None)
	statement_of_work_added: bool | None = field(default=None)
	_remove_pipeline_stage: bool | None = field(default=None)
	order_line_price: float | None = field(default=None)
	order_line_composite_key: list | None = field(default=None)
	risk_score: float | None = field(default=None)
	from_catalogue: bool | None = field(default=None)
	enduser_role_ids: list | None = field(default=None)
	order_sequence: int | None = field(default=None)
	order_update_to: int | None = field(default=None)
	order_update_from: int | None = field(default=None)
	workflow_html_to_show_on_progress: str | None = field(default=None)
	requesttype_group_id: int | None = field(default=None)
	is_ai_indexable: bool | None = field(default=None)
	qualifications_matched: str | None = field(default=None)
	hoursinvoiced: float | None = field(default=None)
	_kbduplicate01_ok: bool | None = field(default=None)
	kb_ai_summary: str | None = field(default=None)
	duplicate_kbs: str | None = field(default=None)
	billing_type: int | None = field(default=None)
	supplier_reference: str | None = field(default=None)
	top_level_name: str | None = field(default=None)
	deleted_date: datetime | None = field(default=None)
	isbeingclosed: bool | None = field(default=None)
	maximumRestrictedPriority: int | None = field(default=None)
	primary_service_name: str | None = field(default=None)
	idsummary: str | None = field(default=None)
	scomclearance: str | None = field(default=None)
	scomalertid: str | None = field(default=None)
	statusseq: int | None = field(default=None)
	statuscolor: str | None = field(default=None)
	next_appointment_type: int | None = field(default=None)
	account_manager: str | None = field(default=None)
	orionalert: int | None = field(default=None)
	orionnote: str | None = field(default=None)
	orionwho: int | None = field(default=None)
	product_key: str | None = field(default=None)
	rapid7_action_count: str | None = field(default=None)
	rapid7_ticketrrn: str | None = field(default=None)
	rapid7_ticketinvid: str | None = field(default=None)
	ninja_id: str | None = field(default=None)
	teams_ticket_icon: str | None = field(default=None)
	lastactiondateteams: str | None = field(default=None)
	priority_name: str | None = field(default=None)
	sitepostcode: str | None = field(default=None)
	mailbox: str | None = field(default=None)
	userdepartments: str | None = field(default=None)
	startdatetime: datetime | None = field(default=None)
	enddatetime: datetime | None = field(default=None)
	closure_agent_id: int | None = field(default=None)
	closed_in_integration_system: bool | None = field(default=None)
	createdfromautomationstdid: int | None = field(default=None)
	created_from_automation_entityid: int | None = field(default=None)
	status_change_frozen: bool | None = field(default=None)
	approval_status: int | None = field(default=None)
	opp_country_name: str | None = field(default=None)
	overrideticketcost: float | None = field(default=None)
	budgethours: str | None = field(default=None)
	created_by: str | None = field(default=None)
	additional_agents: list | None = field(default=None)
	client_to_invoice_to_id: int | None = field(default=None)
	primary_issue: list | None = field(default=None)
	primary_workitem: list | None = field(default=None)
	billing_plan_text: str | None = field(default=None)
	default_appointment_summary: str | None = field(default=None)
	default_appointment_details: str | None = field(default=None)
	agent_signature: str | None = field(default=None)
	customer_signature: str | None = field(default=None)
	new_agent_signature: str | None = field(default=None)
	new_customer_signature: str | None = field(default=None)
	invoiceable_time: float | None = field(default=None)
	owning_service: int | None = field(default=None)
	owning_service_name: str | None = field(default=None)
	ticket_timezone: str | None = field(default=None)
	_importtypeid: int | None = field(default=None)
	_importthirdpartyid: str | None = field(default=None)
	_importtype: str | None = field(default=None)
	new_external_link: list | None = field(default=None)
	import_details_id: int | None = field(default=None)
	_isupdateimport: bool | None = field(default=None)

	def __post_init__(self):
		if self.dateoccurred:
			self.dateoccurred = datetime.fromisoformat(self.dateoccurred)
		if self.projectearlieststart:
			self.projectearlieststart = datetime.fromisoformat(self.projectearlieststart)
		if self.projectlatestend:
			self.projectlatestend = datetime.fromisoformat(self.projectlatestend)
		if self.respondbydate:
			self.respondbydate = datetime.fromisoformat(self.respondbydate)
		if self.responsedate:
			self.responsedate = datetime.fromisoformat(self.responsedate)
		if self.first_responsedate:
			self.first_responsedate = datetime.fromisoformat(self.first_responsedate)
		if self.responsestartdate:
			self.responsestartdate = datetime.fromisoformat(self.responsestartdate)
		if self.fixbydate:
			self.fixbydate = datetime.fromisoformat(self.fixbydate)
		if self.dateclosed:
			self.dateclosed = datetime.fromisoformat(self.dateclosed)
		if self.dateassigned:
			self.dateassigned = datetime.fromisoformat(self.dateassigned)
		if self.slaactiondate:
			self.slaactiondate = datetime.fromisoformat(self.slaactiondate)
		if self.lastactiondate:
			self.lastactiondate = datetime.fromisoformat(self.lastactiondate)
		if self.last_update:
			self.last_update = datetime.fromisoformat(self.last_update)
		if self.lastchildactiondate:
			self.lastchildactiondate = datetime.fromisoformat(self.lastchildactiondate)
		if self.lastincomingemail:
			self.lastincomingemail = datetime.fromisoformat(self.lastincomingemail)
		if self.nextactivitydate:
			self.nextactivitydate = datetime.fromisoformat(self.nextactivitydate)
		if self.nextactivityorappointmentdate:
			self.nextactivityorappointmentdate = datetime.fromisoformat(self.nextactivityorappointmentdate)
		if self.startdate:
			self.startdate = datetime.fromisoformat(self.startdate)
		if self.targetdate:
			self.targetdate = datetime.fromisoformat(self.targetdate)
		if self.deadlinedate:
			self.deadlinedate = datetime.fromisoformat(self.deadlinedate)
		if self.followupdate:
			self.followupdate = datetime.fromisoformat(self.followupdate)
		if self.opptrialdate:
			self.opptrialdate = datetime.fromisoformat(self.opptrialdate)
		if self.oppdemodate:
			self.oppdemodate = datetime.fromisoformat(self.oppdemodate)
		if self.oppdiscountdate:
			self.oppdiscountdate = datetime.fromisoformat(self.oppdiscountdate)
		if self.oppconverteddate:
			self.oppconverteddate = datetime.fromisoformat(self.oppconverteddate)
		if self.nextappointmentdate:
			self.nextappointmentdate = datetime.fromisoformat(self.nextappointmentdate)
		if self.action_datetime:
			self.action_datetime = datetime.fromisoformat(self.action_datetime)
		if self.milestone_startdate:
			self.milestone_startdate = datetime.fromisoformat(self.milestone_startdate)
		if self.milestone_enddate:
			self.milestone_enddate = datetime.fromisoformat(self.milestone_enddate)
		if self.date_fully_closed:
			self.date_fully_closed = datetime.fromisoformat(self.date_fully_closed)
		if self.datecreated:
			self.datecreated = datetime.fromisoformat(self.datecreated)
		if self.supplier_date:
			self.supplier_date = datetime.fromisoformat(self.supplier_date)
		if self.supplier_responsedate:
			self.supplier_responsedate = datetime.fromisoformat(self.supplier_responsedate)
		if self.supplier_respondbydate:
			self.supplier_respondbydate = datetime.fromisoformat(self.supplier_respondbydate)
		if self.supplier_dateclosed:
			self.supplier_dateclosed = datetime.fromisoformat(self.supplier_dateclosed)
		if self.supplier_fixbydate:
			self.supplier_fixbydate = datetime.fromisoformat(self.supplier_fixbydate)
		if self.invoicedate:
			self.invoicedate = datetime.fromisoformat(self.invoicedate)
		if self.invoicepaiddate:
			self.invoicepaiddate = datetime.fromisoformat(self.invoicepaiddate)
		if self.planneddate:
			self.planneddate = datetime.fromisoformat(self.planneddate)
		if self.planneddateend:
			self.planneddateend = datetime.fromisoformat(self.planneddateend)
		if self.lastrecurringemailsentdate:
			self.lastrecurringemailsentdate = datetime.fromisoformat(self.lastrecurringemailsentdate)
		if self.slaholdreminderdatelastemailed:
			self.slaholdreminderdatelastemailed = datetime.fromisoformat(self.slaholdreminderdatelastemailed)
		if self.closurereminderdatelastemailed:
			self.closurereminderdatelastemailed = datetime.fromisoformat(self.closurereminderdatelastemailed)
		if self.auditdate:
			self.auditdate = datetime.fromisoformat(self.auditdate)
		if self.auditfaileddate:
			self.auditfaileddate = datetime.fromisoformat(self.auditfaileddate)
		if self.workflow_stepstarted:
			self.workflow_stepstarted = datetime.fromisoformat(self.workflow_stepstarted)
		if self.lastbugzillasync:
			self.lastbugzillasync = datetime.fromisoformat(self.lastbugzillasync)
		if self.sla_start_date:
			self.sla_start_date = datetime.fromisoformat(self.sla_start_date)
		if self.orionacknowledgedate:
			self.orionacknowledgedate = datetime.fromisoformat(self.orionacknowledgedate)
		if self.laststatuschangestatusdate:
			self.laststatuschangestatusdate = datetime.fromisoformat(self.laststatuschangestatusdate)
		if self.resource_booking_timeslot:
			self.resource_booking_timeslot = datetime.fromisoformat(self.resource_booking_timeslot)
		if self.reviewed_date:
			self.reviewed_date = datetime.fromisoformat(self.reviewed_date)
		if self.search_index_sync_timestamp:
			self.search_index_sync_timestamp = datetime.fromisoformat(self.search_index_sync_timestamp)
		if self.new_whe_:
			self.new_whe_ = datetime.fromisoformat(self.new_whe_)
		if self.embedding_match_timestamp:
			self.embedding_match_timestamp = datetime.fromisoformat(self.embedding_match_timestamp)
		if self.workflow_move_date_override:
			self.workflow_move_date_override = datetime.fromisoformat(self.workflow_move_date_override)
		if self.next_review_date:
			self.next_review_date = datetime.fromisoformat(self.next_review_date)
		if self.deleted_date:
			self.deleted_date = datetime.fromisoformat(self.deleted_date)
		if self.startdatetime:
			self.startdatetime = datetime.fromisoformat(self.startdatetime)
		if self.enddatetime:
			self.enddatetime = datetime.fromisoformat(self.enddatetime)
# Debug method for creating items from dictionary - This comment is required or dedent dedents everything
	@classmethod
	def from_dict(cls, dictionary:dict):
		return cls(**{
			k: v for k, v in dictionary.items()
			if k in inspect.signature(cls).parameters
		})