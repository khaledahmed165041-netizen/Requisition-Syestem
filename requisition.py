requisition_counter =0
requisition_list =[]
class Requisition:
    def __init__(self, date, staff_id, staff_name):
        global requisition_counter

        requisition_counter += 1

        self.date =date
        self.staff_id =staff_id
        self.staff_name =staff_name
        self.requisition_id =10000 + requisition_counter
        self.itemlist =[]
        self.total =0
        self.status ="Pending"
        self.approval_reference ="Not available"

        requisition_list.append(self)

    def requisition_details(self, items):
        if len(items) == 0:
            print("No items entered for requisition", self.requisition_id)
            return 0

        for item in items:
            if item["Price"] <= 0:
                print("Price for", item["Item Name"], "must be greater than zero.")
                return 0

        for item in items:
            self.itemlist.append(item)
            self.total += item["Price"]

        return self.total

    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"