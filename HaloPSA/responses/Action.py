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
class Action: #/components/schemas/Actions
	ticket_id: int | None
	id: int
	outcome: str | None
	who_type: int | None
	who_imgpath: str | None
	who_agentid: int | None
	who_initials: str | None
	who_colour: str | None
	who_onlinestatus: int | None
	datetime: datetime | None
	last_updated: datetime | None
	note: str | None
	replied_to_ticket_id: int | None
	replied_to_action_id: int | None
	created_from_ticket_id: int | None
	created_from_action_id: int | None
	action_contract_id: int | None
	action_contract_ref: str | None
	action_travel_contract_id: int | None
	project_id: int | None
	twitter_id_str: str | None
	twitter_user_name: str | None
	tweet_sent: bool | None
	attachment_list: list
	customfields: list | None
	personal_unread: bool | None
	actionarrivaldate: datetime | None
	actioncompletiondate: datetime | None
	isjson: bool | None
	facebook_id: str | None
	facebook_sent: bool | None
	merged_from_ticketid: int | None
	reactions: list | None
	translations: list | None
	email_message_id: str | None
	post_translations: list | None
	ticket_guid: str | None
	instagram_id: str | None
	instagram_sent: bool | None
	on_behalf_of: int | None
	on_behalf_of_name: str | None
	actionby_agent_id: int | None
	warning_type: int | None
	guid: str | None
	actioncontractid: int | None
	actisbillable: bool | None
	actisreadyforprocessing: bool | None
	actioninternetmessageid: str | None
	senttowhatsapp: bool | None
	twa_delivered_date: datetime | None
	twa_read_date: datetime | None
	travelisreadyforprocessing: bool | None
	emailimportance: str | None
	emailbody: str | None
	emailsubject: str | None
	note_html: str | None
	emailbody_html: str | None
	actionuserdef: int | None
	userdesc: str | None
	actiondatecreated: datetime | None
	actioninvoicenumber: str | None
	actioninvoicenumber_isproject: bool | None
	action_invoice_line_id: int | None
	actiontravelinvoicenumber: str | None
	actionmileageinvoicenumber: str | None
	externalinvoicenumber: str | None
	actprocessid: int | None
	actiontravelamount: float | None
	actionmileageamount: float | None
	actiontravelmileageinvoicenumber: int | None
	actionbillingplanid: int | None
	actiontravelbillingplanid: int | None
	actioncalendarstatus: int | None
	actionapptid: str | None
	actionsmsstatus: int | None
	sitevisitunits: float | None
	svid: int | None
	asset_id: int | None
	asset_site: int | None
	lwwarrantyreported: bool | None
	from_mailbox_id: int | None
	sales_mailbox_override_id: int | None
	from_address_override: str | None
	actiontravelstartdate: datetime | None
	actiontravelenddate: datetime | None
	actionactualresponse: float | None
	actionslaresponsestate: str | None
	labourwarranty: bool | None
	actreviewed: bool | None
	actprocesseddate: datetime | None
	dateinvoicedtraveltime: datetime | None
	dateinvoicedmileage: datetime | None
	actionuserdefineddata: str | None
	emailtolistall: str | None
	reply_direct: bool | None
	actioninformownerofaction: bool | None
	agentnotificationneeded: int | None
	surchargeid: int | None
	travel_surchargeid: int | None
	achargetotalaction: bool | None
	achargetotalprocessed: bool | None
	tweetsent: bool | None
	tweetfrom: str | None
	twitterid: int | None
	send_to_facebook: bool | None
	replyto_facebook_id: str | None
	senttofb: bool | None
	facebookid: str | None
	facebookname: str | None
	facebook_parent_id: str | None
	calloutcomenum: int | None
	actionresponsedate: datetime | None
	actiontargetresponsedate: datetime | None
	pagerdutysendstatus: int | None
	mailentryid: str | None
	replytoaddress: str | None
	actsapuuid: str | None
	whowith: str | None
	chatid: int | None
	dynamicsactionid: str | None
	action_appointment_id: int | None
	action_supplier_id: int | None
	action_supplier_name: str | None
	new_tickettype: int | None
	new_chargerate: int | None
	new_contract_id: int | None
	new_parent_id: int | None
	new_priority: int | None
	new_category1: str | None
	new_category2: str | None
	new_category3: str | None
	new_category4: str | None
	new_estimate: float | None
	new_estimatedays: float | None
	new_impact: int | None
	new_urgency: int | None
	new_source: int | None
	new_subject: str | None
	new_matched_rule_id: int | None
	new_firsttimefix: bool | None
	new_team: str | None
	new_agent: int | None
	new_sla_id: int | None
	new_slastatus: int | None
	new_fixbydate: datetime | None
	new_followupdate: datetime | None
	new_deadlinedate: datetime | None
	new_deadlinenotificationhours: float | None
	new_startdate: datetime | None
	new_startdate_timezone: str | None
	new_startdate_with_timezone: list
	new_project_time_budget: float | None
	new_project_money_budget: float | None
	new_starttime: str | None
	new_starttimeslot: int | None
	new_targetdate: datetime | None
	new_targetdate_timezone: str | None
	new_targetdate_with_timezone: list
	new_targettime: str | None
	new_targettimeslot: int | None
	new_oppcontactname: str | None
	new_oppcompanyname: str | None
	new_oppemailaddress: str | None
	new_oppcustomertitle: str | None
	new_opptel: str | None
	new_oppcountry: str | None
	new_oppregion: str | None
	new_opptype: str | None
	new_opphear: str | None
	new_oppvalue: float | None
	new_oppvalue_monthly: float | None
	new_oppvalue_annual: float | None
	new_oppvalue_oneoff: float | None
	new_oppconversionprobability: float | None
	new_oppprofit: float | None
	new_oppcurrentsystem: str | None
	new_oppcompetitors: str | None
	new_opptrialdate: datetime | None
	new_oppdemodate: datetime | None
	new_oppdiscountdate: datetime | None
	new_oppattemptsmade: int | None
	new_oppconverteddate: datetime | None
	new_oppproductchosen: str | None
	new_oppreason: str | None
	new_opptimezonename: str | None
	new_oppclosurecategory: int | None
	new_oppdontaddtomailinglist: bool | None
	new_approvalprocess: int | None
	new_approvalprocess_agent_id: int | None
	new_approvalprocess_user_id: int | None
	new_approvalprocess_users: list | None
	new_approvalprocess_email: str | None
	new_approvalprocess_cab_id: int | None
	new_approvalprocess_cab: list | None
	new_product_id: int | None
	new_component_id: int | None
	new_version_id: int | None
	new_matched_kb_id: int | None
	new_matched_linked_id: int | None
	new_linkedticket_template_id: int | None
	new_supplier_id: int | None
	new_supplier_ref: str | None
	new_customer_ref: str | None
	new_supplier_contract_id: int | None
	new_supplier_priority_id: int | None
	new_supplier_response_date: datetime | None
	new_supplier_fix_date: datetime | None
	new_linkedticket_status: int | None
	new_appointment_type: int | None
	emailtemplate_id: int | None
	create_article: bool | None
	sendemail: bool | None
	action_showpreview: bool | None
	setnotetoemailbody: bool | None
	action_isresponse: bool | None
	validate_response: bool | None
	attachments: list | None
	update_children: bool | None
	update_parent: bool | None
	send_survey: bool | None
	signature_customer: str | None
	signature_customer_name: str | None
	signature_agent: str | None
	signature_agent_name: str | None
	follow: bool | None
	unfollow: bool | None
	primaryserviceusersfollow: bool | None
	appointment_id: int | None
	appointment_complete_status: int | None
	add_followup_appointment: bool | None
	add_followup_task: bool | None
	_appointment_force: bool | None
	copy_to_id: int | None
	third_party_product_id: str | None
	third_party_version_id: str | None
	_forcereassign: bool | None
	_appointment01_ok: bool | None
	_agent01_ok: bool | None
	_agent02_ok: bool | None
	_ticketclash01_ok: bool | None
	_canupdate: bool | None
	assets: list | None
	dont_do_rules: bool | None
	_includeticketinresponse: bool | None
	jira_original_estimate: float | None
	jira_remaining_estimate: float | None
	_warning: str | None
	actionoohtime: float | None
	actionholidaytime: float | None
	actiontotaloohtime: float | None
	quotation_id: int | None
	salesorder_id: int | None
	purchaseorder_id: int | None
	invoice_id: int | None
	recalculate_billing: bool | None
	dont_recalculate_time: bool | None
	_isimport: bool | None
	_isinboundsales: bool | None
	sendactiontopagerduty: bool | None
	oktoclose: bool | None
	remotetechid: int | None
	utcoffset: float | None
	statisfaction_level: int | None
	senttoapisupplierid: int | None
	send_jira_attachments: bool | None
	jira_reporter: int | None
	smsto: str | None
	sendsms: bool | None
	_dontupdate_devops: bool | None
	send_devops_note: bool | None
	_isnotify: bool | None
	_iscountersign: bool | None
	move_to_id: int | None
	sendactiontosplunkoncall: bool | None
	third_party_who: str | None
	_faultForce: bool | None
	private_note: str | None
	isBulkEmail: bool | None
	new_workflow_id: int | None
	_sendtweet: bool | None
	replyto_tweet_id: int | None
	replyto_tweet_haloid: int | None
	changeinformationhtml: str | None
	justification: str | None
	impactlevel: int | None
	impactdescription: str | None
	risklevel: int | None
	riskdescription: str | None
	backoutplan: str | None
	communicationplan: str | None
	testplan: str | None
	showonroadmap: bool | None
	roadmapnote: str | None
	releasenote: str | None
	releaseid: int | None
	releaseid2: int | None
	releaseid3: int | None
	releasenotegroupid: int | None
	releaseimportant: bool | None
	new_jira_components: list | None
	faultidfrom: int | None
	actionnumberfrom: int | None
	new_template_id: int | None
	new_primary_asset_status: int | None
	primary_asset_id: int | None
	new_rule_ids: str | None
	dont_update_fault: bool | None
	new_article_description: str | None
	new_article_resolution: str | None
	new_article_notes: str | None
	new_article_type: int | None
	new_tags: list | None
	new_faqlists: list | None
	new_related_articles: list | None
	ignoredatedoneisstartdate: bool | None
	sentinel_id: str | None
	_validate_travel: bool | None
	sync_to_sentinel: bool | None
	sentinel_classification: str | None
	sentinel_classification_reason: str | None
	g2aremote_id: str | None
	dontcreatechild: bool | None
	needcreatechild: bool | None
	customfieldvalidationreason: str | None
	servicestatusnote: str | None
	updateservicestatus: bool | None
	new_child_cat_1: str | None
	new_child_cat_2: str | None
	new_child_cat_3: str | None
	new_child_cat_4: str | None
	usecroverride: bool | None
	azure_action_complete: bool | None
	_dontupdate_jira: bool | None
	send_jira_note: bool | None
	entity_type: str | None
	rmm_close: bool | None
	dattormm_close: bool | None
	external_links: list | None
	new_external_link: list
	_match_thirdparty_id: str | None
	_match_integration_id: int | None
	_match_integration_name: str | None
	sync_to_salesforce: bool | None
	isbillingaction: bool | None
	ishiddenfrominternalit: bool | None
	new_consignment: list | None
	faultstimeentryid: int | None
	billingoverriddenbytimeentry: int | None
	sync_to_servicenow: bool | None
	new_service_id: int | None
	new_asset: list
	contract_date_override: datetime | None
	parentactionnumber: int | None
	parentactiondetails: str | None
	parentactiondate: datetime | None
	user_creation_failed: bool | None
	followers_user: list | None
	new_items_issued: list | None
	purchaseordernumber: str | None
	database_lookup_result: list
	new_supplier_contact_id: int | None
	new_pr_id: int | None
	new_branch_id: int | None
	_dontupdate_pagerduty: bool | None
	pagerdutyid: str | None
	facebook_from_id: str | None
	twitter_from_id: str | None
	sync_to_jira: bool | None
	is_jira_supplier: bool | None
	senttojirasupplierid: int | None
	_importtype: str | None
	itsm_summary: str | None
	send_to_halo: bool | None
	send_to_whatsapp: bool | None
	_ignore_ai: bool | None
	_ignore_translate: bool | None
	translate_note: bool | None
	new_approvalprocess_role_id: int | None
	new_approvalprocess_customfieldid: int | None
	new_thirdpartyreviewscore: int | None
	new_additional_agents: list | None
	instagramid: str | None
	instagramname: str | None
	instagram_parent_id: str | None
	send_to_instagram: bool | None
	replyto_instagram_id: str | None
	senttoinsta: bool | None
	instagram_from_id: str | None
	dont_recalculate_billing: bool | None
	is_third_party_supplier: bool | None
	senttoservicenowsupplierid: int | None
	timesheet_approval_status: int | None
	_changeprivate: bool | None
	defprepayinvoicenumber: str | None
	defprepaydateinvoiced: datetime | None
	defprepayamount: float | None
	new_colour: str | None
	send_to_googlebusiness: bool | None
	original_agent: int | None
	_isreplyaction: bool | None
	milestone_bill_id: int | None
	new_foppjobtitle: str | None
	bigpanda_id: str | None
	servicenow_type: int | None
	internet_message_id: str | None
	allow_automation_on_related: bool | None
	replying_to: int | None
	lapsafe_expiry_date: datetime | None
	lapsafe_asset: str | None
	lapsafe_bay: int | None
	lapsafe_bay_id: str | None
	lapsafe_installation: str | None
	_slackaction: int | None
	_isportalagentnote: bool | None
	devops_pipeline_id: int | None
	devops_pipeline_version: str | None
	new_step: int | None
	rr_log: list
	new_contributors: list | None
	nextcalldate: datetime | None
	satisfaction: str | None
	new_CRM_note: list
	new_template: list
	_agent03_ok: bool
	_can_edit_billing_time: bool | None
	run_ai_insights: bool | None
	new_customer_signature: str | None
	new_agent_signature: str | None
	_prevent_outgoing: bool | None
	new_client_id: int | None
	new_site_id: int | None
	new_user_id: int | None
	prepay_threshold: list
	outgoingid: int | None
	isundeliverable: bool | None
	new_distribution_list: int | None
	new_bulkemail: list
	bulkemail_users: list | None
	_novalidate: bool | None
	ishaloack: bool | None
	new_notepad: str | None
	sync_to_halo_api: int | None
	excludefromemailthreading: bool | None
	action_showkbpreview: bool | None
	portal_supplier_update: bool | None
	item_to_issue: int | None
	countersiguseagentsig: bool | None
	countersignature: str | None
	new_owning_service: int | None
	_apply_ai_suggestions: list | None
	subject_exceeds_max_length: bool | None
	_rule_user_update: list
	set_ticket_ai_indexing: bool | None
	new_is_maintenance: bool | None
	iseditaction: bool | None
	set_response_if_not_set: bool | None
	_kbduplicate01_ok: bool | None
	kb_ai_summary: str | None
	new_ticket_timezone: str | None
	adhoc_notify_team: int | None
	_dont_fire_automations: bool | None
	outcome_id: int | None
	action_systemid: int | None
	dateemailed: datetime | None
	timetaken: float | None
	timetakendays: float | None
	timetakenadjusted: float | None
	nonbilltime: float | None
	traveltime: float | None
	mileage: float | None
	actionchargehours: float | None
	actionnonchargeamount: float | None
	actionnonchargehours: float | None
	actionchargeamount: float | None
	actionprepayhours: float | None
	actionprepayamount: float | None
	actiontravelchargehours: float | None
	chargerate: int | None
	travel_chargerate: int | None
	hiddenfromuser: bool | None
	important: bool | None
	old_status: int | None
	new_status: int | None
	new_status_name: str | None
	emailfrom: str | None
	emailtonew: str | None
	emailto: str | None
	emailccnew: str | None
	emaildirection: str | None
	emailcc: str | None
	emailsubjectnew: str | None
	senttoapiurl: str | None
	colour: str | None
	attachment_count: int | None
	unread: int | None
	actionby_application_id: str | None
	action_travel_contract_ref: str | None
	actionby_user_id: int | None
	hide_user_visibility_toggle: bool | None

	def __post_init__(self):
		if self.datetime:
			self.datetime = datetime.fromisoformat(self.datetime)
		if self.last_updated:
			self.last_updated = datetime.fromisoformat(self.last_updated)
		if self.actionarrivaldate:
			self.actionarrivaldate = datetime.fromisoformat(self.actionarrivaldate)
		if self.actioncompletiondate:
			self.actioncompletiondate = datetime.fromisoformat(self.actioncompletiondate)
		if self.twa_delivered_date:
			self.twa_delivered_date = datetime.fromisoformat(self.twa_delivered_date)
		if self.twa_read_date:
			self.twa_read_date = datetime.fromisoformat(self.twa_read_date)
		if self.actiondatecreated:
			self.actiondatecreated = datetime.fromisoformat(self.actiondatecreated)
		if self.actiontravelstartdate:
			self.actiontravelstartdate = datetime.fromisoformat(self.actiontravelstartdate)
		if self.actiontravelenddate:
			self.actiontravelenddate = datetime.fromisoformat(self.actiontravelenddate)
		if self.actprocesseddate:
			self.actprocesseddate = datetime.fromisoformat(self.actprocesseddate)
		if self.dateinvoicedtraveltime:
			self.dateinvoicedtraveltime = datetime.fromisoformat(self.dateinvoicedtraveltime)
		if self.dateinvoicedmileage:
			self.dateinvoicedmileage = datetime.fromisoformat(self.dateinvoicedmileage)
		if self.actionresponsedate:
			self.actionresponsedate = datetime.fromisoformat(self.actionresponsedate)
		if self.actiontargetresponsedate:
			self.actiontargetresponsedate = datetime.fromisoformat(self.actiontargetresponsedate)
		if self.new_fixbydate:
			self.new_fixbydate = datetime.fromisoformat(self.new_fixbydate)
		if self.new_followupdate:
			self.new_followupdate = datetime.fromisoformat(self.new_followupdate)
		if self.new_deadlinedate:
			self.new_deadlinedate = datetime.fromisoformat(self.new_deadlinedate)
		if self.new_startdate:
			self.new_startdate = datetime.fromisoformat(self.new_startdate)
		if self.new_targetdate:
			self.new_targetdate = datetime.fromisoformat(self.new_targetdate)
		if self.new_opptrialdate:
			self.new_opptrialdate = datetime.fromisoformat(self.new_opptrialdate)
		if self.new_oppdemodate:
			self.new_oppdemodate = datetime.fromisoformat(self.new_oppdemodate)
		if self.new_oppdiscountdate:
			self.new_oppdiscountdate = datetime.fromisoformat(self.new_oppdiscountdate)
		if self.new_oppconverteddate:
			self.new_oppconverteddate = datetime.fromisoformat(self.new_oppconverteddate)
		if self.new_supplier_response_date:
			self.new_supplier_response_date = datetime.fromisoformat(self.new_supplier_response_date)
		if self.new_supplier_fix_date:
			self.new_supplier_fix_date = datetime.fromisoformat(self.new_supplier_fix_date)
		if self.contract_date_override:
			self.contract_date_override = datetime.fromisoformat(self.contract_date_override)
		if self.parentactiondate:
			self.parentactiondate = datetime.fromisoformat(self.parentactiondate)
		if self.defprepaydateinvoiced:
			self.defprepaydateinvoiced = datetime.fromisoformat(self.defprepaydateinvoiced)
		if self.lapsafe_expiry_date:
			self.lapsafe_expiry_date = datetime.fromisoformat(self.lapsafe_expiry_date)
		if self.nextcalldate:
			self.nextcalldate = datetime.fromisoformat(self.nextcalldate)
		if self.dateemailed:
			self.dateemailed = datetime.fromisoformat(self.dateemailed)
# Debug method for creating items from dictionary - This comment is required or dedent dedents everything
	@classmethod
	def from_dict(cls, dictionary:dict):
		return cls(**{
			k: v for k, v in dictionary.items()
			if k in inspect.signature(cls).parameters
		})