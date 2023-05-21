# Copyright (c) 2023, Zezembly Co.,Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class EmploymentProfile(Document):

	def autoname(self):
		print(self.user)
		self.name = self.user

	pass
