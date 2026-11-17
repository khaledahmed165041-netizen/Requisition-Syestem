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

    def respond_requisition(self, response):
        if self.status != "Pending":
            print("Requisition", self.requisition_id, "is not pending.")
            return

        if response.lower() == "approved":
            self.status = "Approved"
            self.approval_reference = self.staff_id + str(self.requisition_id)[-3:]

        elif response.lower() == "not approved":
            self.status = "Not approved"

        elif response.lower() == "pending":
            return

        else:
            print("Please enter a valid response.")
            return

    def display_requisitions(self):
        if len(requisition_list) == 0:
            print("No requisitions submitted.")
            return

        for requisition in requisition_list:
            print("Date:",requisition.date)
            print("Requisition ID:" ,requisition.requisition_id)
            print("Staff ID:" , requisition.staff_id)
            print("Staff Name:" , requisition.staff_name)
            print("Total: $" + str(requisition.total))
            print("Status:" , requisition.status)
            print("Approval Reference Number:" , requisition.approval_reference)
            print()

    def requisition_statistics(self):
        total_submitted = len(requisition_list)
        total_approved = 0
        total_pending = 0
        total_not_approved = 0

        for requisition in requisition_list:
            if requisition.status == "Approved":
                total_approved += 1

            elif requisition.status == "Pending":
                total_pending += 1

            elif requisition.status == "Not approved":
                total_not_approved += 1

        print("Statistics:")
        print("Displaying the Requisition Statistics")
        print("The total number of requisitions submitted:" ,total_submitted)
        print("The total number of approved requisitions:", total_approved)
        print("The total number of pending requisitions:" ,total_pending)
        print("The total number of not approved requisitions:" , total_not_approved)

        statistics = {
            "Submitted": total_submitted,
            "Approved": total_approved,
            "Pending": total_pending,
            "Not approved": total_not_approved
        }

        return statistics

while True:
    print()
    print("=====Requisition System=====")
    print("1. Submit a requisition")
    print("2. Manager response")
    print("3. Display all requisitions")
    print("4. Display statistics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date (dd/mm/yyyy): ")
        staff_id = input("Enter Staff ID: ")
        staff_name = input("Enter Staff Name: ")

        items = []
        while True:
            item_name = input("Enter item name (type done to finish): ")
            if item_name.lower() == "done":
                break

            price = input("Enter price: ")
            if price.isdigit() and int(price) > 0:
                items.append({"Item Name": item_name, "Price": int(price)})
            else:
                print("Price must be a number greater than zero.")

        if len(items) == 0:
            print("No items entered. Requisition not submitted.")
        else:
            req = Requisition(date, staff_id, staff_name)
            req.requisition_details(items)
            req.approve_requisition()
            print("Requisition", req.requisition_id, "submitted. Status:", req.status)

    elif choice == "2":
        req_id = input("Enter Requisition ID: ")
        if req_id.isdigit():
            found = False
            for requisition in requisition_list:
                if requisition.requisition_id == int(req_id):
                    response = input("Enter response (Approved / Not approved / Pending): ")
                    requisition.respond_requisition(response)
                    found = True

            if found == False:
                print("Requisition ID not found.")
        else:
            print("Requisition ID must be a number.")

    elif choice == "3":
        if len(requisition_list) == 0:
            print("No requisitions submitted.")
        else:
            requisition_list[0].display_requisitions()

    elif choice == "4":
        if len(requisition_list) == 0:
            print("No requisitions submitted.")
        else:
            requisition_list[0].requisition_statistics()

    elif choice == "5":
        print("Exiting the Requisition System.")
        break

    else:
        print("Please enter a valid choice.")



