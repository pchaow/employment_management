# Copyright (c) 2023, Zezembly Co.,Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import gettext
_ = gettext.gettext

class JobItem(Document):

    def before_insert(self):
        if (self.postby is None):
            current_user_doc = frappe.get_user().doc
            self.postby = current_user_doc.name
            pass
        pass

    pass

    def validate(self):

        if(self.date_start is not None and self.date_end is not None):
            if(self.date_start >= self.date_end) :
                frappe.throw(_("Date start must before Date end"))

        if(self.time_start is not None and self.time_end is not None):
            if (self.time_start >= self.time_end):
                frappe.throw(_("Time start must before Time end"))

        pass
