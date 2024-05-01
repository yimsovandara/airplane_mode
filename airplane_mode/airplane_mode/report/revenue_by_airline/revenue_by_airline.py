import frappe


def execute(filters=None):
    columns = [
        {
            "label": "Airline",
            "fieldname": "airline",
            "fieldtype": "Data",
            "width": 150,
        },
        {
            "label": "Amount",
            "fieldname": "amount",
            "fieldtype": "Currency",
            "width": 150,
        },
    ]
    data = []

    # Get a list of all airlines
    airline_list = frappe.get_list("Airline", fields=["name"])

    airplan_tickey_list_list = frappe.get_all(
        "Airplane Ticket", fields=["flight.airplane", "total_amount"]
    )
    for item in airline_list:
        data.append({"airline": item.name, "amount": 0.00})

    for item in airplan_tickey_list_list:
        get_airline = frappe.get_value("Airplane", {"name": item.airplane}, ["airline"])
        index = 0
        for item_data in data:
            if item_data["airline"] == get_airline:
                data[index]["amount"] += item.get("total_amount")
            index = index + 1
    amount = []
    airline_label_chart = []
    for i in data:
        amount.append(i["amount"])
        airline_label_chart.append(i["airline"])

    # data.sort(key=myFuncD, reverse=True)

    chart_data = {
        "data": {
            "labels": airline_label_chart,
            "datasets": [{"name": "Amount", "values": amount, "chartType": "bar"}],
        },
        "type": "donut",
    }
    total = sum(amount)
    formatted_total = "${:,.2f}".format(total)

    message = [
        '<p style="text-align:center">Total Revenue By Airline</p>',
        f'<h3 style="text-align:center;color:green;font-size: 30px">{formatted_total}</h3>',
    ]

    return columns, data, message, chart_data
