# Copyright (c) 2024, wael and contributors
# For license information, please see license.txt
import datetime
import frappe
from frappe import _
from frappe.utils import today,add_to_date, get_datetime, getdate
from frappe.model.document import Document
from frappe import utils

class CallTest(Document):

	def validate(self):
		
		frappe.msgprint(_("This is the {0} ").format(self.employee))
		frappe.db.sql( """UPDATE `tabCall Test` SET custom_status = 'Closed' WHERE custom_date_1 < CURDATE() AND  employee = '{0}' """.format(self.employee)) 
		#frappe.msgprint(_("This is the {0} ").format(d))
		frappe.db.commit()		
		
		