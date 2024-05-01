# Copyright (c) 2024, Yim Sovandara and contributors
# For license information, please see license.txt
import frappe
from frappe.website.website_generator import WebsiteGenerator
from frappe.model.document import Document


class FlightPassenger(WebsiteGenerator, Document):
    def before_save(self):
        if self.last_name:
            self.last_name = self.first_name
        else:
            self.full_name = f'{self.first_name} {self.last_name or ""}'
