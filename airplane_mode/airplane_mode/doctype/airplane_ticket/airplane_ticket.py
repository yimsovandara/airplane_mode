# Copyright (c) 2024, Yim Sovandara and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import random

doctype_airplane_flight = "Airplane Flight"
doctype_airplane = "Airplane"
doctype_airplane_ticket = "Airplane Ticket"


class AirplaneTicket(Document):

    def before_save(self):
        self.total_amount = calculate_total_amount(self)

        ckeck_capacity(self)

    def before_submit(self):
        ckeck_capacity(self)

    def before_insert(self):
        self.seat = generate_random_code(self)

    def on_submit(self):
        if self.status == "Boarded":
            frappe.throw(
                "You cannot submit this item to the flight because the flight is already boarded"
            )

    def validate(self):
        unique_data = set()
        filtered_res = []
        for item in self.add_on:
            if item.get("item") not in unique_data:
                filtered_res.append(item)
            unique_data.add(item.get("item"))

            self.set("add_on", filtered_res)


def calculate_total_amount(self):
    add_on_total = 0
    for item in self.add_on:
        add_on_total += item.amount
    return add_on_total + float(self.price_flght)


def generate_random_code(self):
    if self.seat == None:
        random_integer = random.randint(1, 99)
        random_alphabet = random.choice("ABCDE")
        ramdom_code = str(random_integer) + random_alphabet
        return ramdom_code


def ckeck_capacity(self):
    flight = self.flight
    get_airplane_flight = frappe.db.get_value(
        doctype_airplane_flight, flight, "airplane"
    )
    get_airplane = frappe.db.get_value(
        doctype_airplane, get_airplane_flight, "capacity"
    )
    get_airplane_ticket = frappe.db.get_list(
        doctype_airplane_ticket,
        fields=["name", "docstatus"],
        filters={"flight": flight, "docstatus": 1},
    )
    if get_airplane == len(get_airplane_ticket):
        frappe.throw("You cannot book this flight because the flight is already full")
