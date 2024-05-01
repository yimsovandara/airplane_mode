# Copyright (c) 2024, Yim Sovandara and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document


class AirplaneFlight(WebsiteGenerator, Document):

    def before_submit(self):
        self.status = "Completed"
