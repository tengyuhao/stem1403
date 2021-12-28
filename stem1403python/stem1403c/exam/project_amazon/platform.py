"""
Project name : The boxing day
# Coded by Yuhao Teng, Authorized to modify. Not authorized to copy. All rights reserved.
Version 1.0.0

TaxRate's information was from the Government of Canada and Quebec :
https://www.canada.ca/en/revenue-agency/services/tax/businesses/topics/gst-hst-businesses/charge-collect-which-rate.html
https://www.revenuquebec.ca/en/businesses/consumption-taxes/gsthst-and-qst/basic-rules-for-applying-the-gsthst-and-qst/
"""
from decimal import Decimal


# class for TaxRate
class TaxRate:
    GST = 0.05
    QST = 0.09975


# class for Status
class Status:
    SHIPPING_SHIPPED = 'Shipped'
    SHIPPING_READY = 'Ready to Ship'
    SHIPPING_NOT_READY = 'We\'re processing your order'
    ORDER_PAID = 'PAID'
    ORDER_UNPAID = 'UNPAID'
    ORDER_CANCELLED = 'Canceled'


# class for attribute the OrderNumber
class OrderNumberSystem:
    last_order_number = 202112260000

    @staticmethod
    def getNextOrderNo():
        OrderNumberSystem.last_order_number += 1
        return OrderNumberSystem.last_order_number


# class for Address
class AddressSystem:
    # Generate all address
    def __init__(self, number, street, apt_no, city, province, postalcode):
        self._number = number
        self._street = street
        self._apt_no = apt_no
        self._city = city
        self._province = province
        self._country = "Canada"
        self._postalcode = postalcode

    def getAddress(self):
        return f"{self._apt_no}-{self._number} {self._street}  {self._city} {self._province} {self._country} {self._postalcode}"


# class for Order
class OrderSystem:
    # To generate all orders, include the customer's detail (Customer's name, address) and to calculate the amount.
    def __init__(self):
        # To protect customer's privacy, added _, to modify, you need add a function to do that.
        self.company_name = "Amazon.ca"
        self.order_number = "000000000000"
        self.itemL = []
        self._customer_name = None
        self._billing_address = None
        self.order_date = None
        self.order_time = None
        self._receiver_name = None
        self._shipping_address = None
        self.order_status = None
        self.shipping_status = None
        self._payment_method = None
        # Amount
        self.freight = 0    # freight is 0 if > 50$
        self.gst = 0
        self.qst = 0
        self.tax = 0
        self.grand_total = 0    # subtotal + tax
        self.subtotal = 0

    def addToCart(self, item):
        # TO DO
        # list=[{self.item_no}, {self.item_name}, {self.item_detail}, {self.unit_price}, {self.price}, {self.quantity}]
        item_number = item[0]
        self.itemL.append(item)
        print(f"New Message from {self.company_name}: Item: {item[1]} (Item no. {item_number}) has been added in your Bag.")

    # F02 Place order
    def placeOrder(self, receiver_name, customer_name, shipping_address, billing_address):
        self.order_number = OrderNumberSystem.getNextOrderNo()
        # Receiver's information
        self._receiver_name = receiver_name
        self._shipping_address = shipping_address
        # Customer's (Buyer's) information
        self._billing_address = billing_address
        self._customer_name = customer_name
        self.order_status = Status.ORDER_UNPAID
        # OrderSystem.printOrder()    # print the order
        print(f"""Nqew Message from {self.company_name}: Order No.{self.order_number}) has been placed.""")

    # F03 Checkout
    def checkout(self, payment_method):
        self._payment_method = payment_method
        self.order_status = Status.ORDER_PAID
        print(f"New Message from {self.company_name}: Order-{self.order_number} has been {self.order_status}.")

    # F04 Packaging
    # Package Not Ready to Ship
    def packaging(self):
        self.shipping_status = Status.SHIPPING_NOT_READY
        # print(f"New Message from {self.company_name}: Order-{self.order_number}. {self.shipping_status}.")

    # F05 Ship
    def readyToShip(self):
        self.shipping_status = Status.SHIPPING_READY
        print(f"New Message from {self.company_name}: Order-{self.order_number} was {self.shipping_status}.")

    def getFreight(self):
        self.freight = 25
        if self.subtotal >= 50:
            self.freight = 0

    def shipping(self):
        self.shipping_status = Status.SHIPPING_SHIPPED
        print(f"New Message from {self.company_name}: Order-{self.order_number} has been {self.shipping_status}.")

    # tax
    def getGST(self):
        self.gst = self.subtotal * TaxRate.GST
        self.gst = round(self.gst, 2)
        # print(self.gst)

    def getQST(self):
        self.qst = self.subtotal * TaxRate.QST
        self.qst = round(self.qst, 2)

    def getTax(self):
        self.getQST()
        self.getGST()
        self.tax = self.gst + self.qst

    # Amount
    def calculate_subtotal(self):
        self.subtotal = 0
        # list=[{self.item_no}, {self.item_name}, {self.item_detail}, {self.unit_price}, {self.price}, {self.quantity}]
        # print(self.itemL)
        for item in self.itemL:
            # print(item)
            item_price = item[3] * item[5]
            self.subtotal += item_price

        self.subtotal = round(self.subtotal, 2)

    def calculateGrandtotal(self):
        self.calculate_subtotal()
        self.getTax()
        # print(self.tax)
        self.getFreight()
        self.grand_total = self.subtotal + self.tax + self.freight
        # print(self.grand_total)
        self.grand_total = round(self.grand_total, 2)

    def checkStatus(self):
        if self.order_status == Status.ORDER_PAID:
            print(f"Your order's status was {self.shipping_status} such us your order is {self.order_status}.\n")
        else:
            print(f"Your order's status was {self.order_status}.")

    def printOrder(self):
        line = "------------------------------------------------------------------------\n"
        # Title
        title = line
        title += f"{self.company_name}\t\t\t\t\t\t\t\t\t\t\t Order Confirmation\n\n"
        title += "Thank you for your order.\n"
        if self.order_status == Status.ORDER_PAID:
            title += "Once your items have been dispatched, we will send you an email notification.\n"
        content = f"Order number: {self.order_number}\n"
        content += f"Order date: {self.order_date}\n"
        content += f"Order time: {self.order_time}\n"
        content += line
        content += "Ship to :\t"
        content += f"{self._receiver_name}\n"
        content += f"\t\t\t{self._shipping_address}\n"
        content += line
        content += "Billing and Payment\n"
        content += f"Bill to: \t{self._customer_name}\n"
        content += f"\t\t\t{self._billing_address}\n"
        if self.order_status == Status.ORDER_PAID:
            content += f"Payment method: {self._payment_method} \n"
            content += "Items to be shipped\n"
        else:
            content += "Items"
        content += line
        # Section Invoice
        # list=[{self.item_no}, {self.item_name}, {self.item_detail}, {self.unit_price}, {self.price}, {self.quantity}]
        for itemLine in self.itemL:
            content += f"{itemLine[0]} \t\t {itemLine[1]}\t\t {itemLine[2]} \t{itemLine[3]} \t{itemLine[5]}  {itemLine[4]}\n"
        content += line
        content += f"Subtotal: \t\t\t {self.subtotal}$\n"
        content += f"Freight: \t\t\t {self.freight}$\n"
        content += f"GST/HST @{TaxRate.GST}% \t\t {self.gst}$\n"
        content += f"QST @{TaxRate.QST}% \t\t {self.qst}$\n"
        content += f"Grand Total \t\t {self.grand_total}$\n"
        content += line

        receipt = title + content
        print(receipt)
        # content +=
        """
        {Amazon.ca}
        
        Once your items have been dispatched, we will send you an email notification.


        Order number: 202112260001
        Order date:	12-26-2021
        Order time:	20:00:00
        -------------------------------------------------------------------------
        Delivery address :
        Ship To: 	Peter
         	        9-1000 Boul. Decarie  Montreal, Quebec Canada H2A 1K3
        -------------------------------------------------------------------------
        Billing and payment
        Bill To: 	Peter
         	        9-1000 Boul. Decarie  Montreal, Quebec Canada H2A 1K3
        Payment method : # if paid
        -------------------------------------------------------------------------
        Items to be shipped # if paid
        ------------------------------------------------------------------------
         1 101001 iPhone13        5.25", 64GB memory, black  1200.00  1  1200.00
         2 102005 USB flash drive 8GB                          14.99  2    29.98
         3 201006 Book            Art of Code                  59.99  1    59.99
        -------------------------------------------------------------------------
        Subtotal:	   1289.97$
        Freight:	      0.00$
        GST/HST @5.000%: 64.50$
        QST @9.975%:    128.67$
        Tax:		    193.17$
        Grand Total:   1483.14$
        """

    def setOrderTime(self, orderTime):
        self.order_time = orderTime

    def setOorderDate(self, orderDate):
        self.order_date = orderDate


# class for OrderItem, created for OrderSystem
class OrderItemSystem:
    # To Order the Item
    def __init__(self, qty, item_no, item_name, item_detail, unit_price):
        self.item_no = item_no
        self.item_name = item_name
        self.item_detail = item_detail
        self.unit_price = unit_price
        self.quantity = qty
        self.price = 0

    def calculateAmount(self):
        self.price = self.quantity * self.unit_price

    def getItemInfo(self):
        self.calculateAmount()
        return [self.item_no, self.item_name, self.item_detail, self.unit_price, self.price, self.quantity]


# Order 1
print("Order 1")
order1 = OrderSystem()
addressPeter = AddressSystem(9, 1000, "Boul. Decarie", "Montreal", "Quebec", "H2A 1K3")
addressPeter = addressPeter.getAddress()
article1 = OrderItemSystem(1, "101001", "iPhone 13", "5.25\",64Gb memory, black", 1200.00)
article2 = OrderItemSystem(2, "102005", "USB flash drive", "8GB", 14.99)
article3 = OrderItemSystem(1, "201006", "Book", "Art of Code", 59.99)
article1 = article1.getItemInfo()
article2 = article2.getItemInfo()
article3 = article3.getItemInfo()
# print(article1)
order1.addToCart(article1)
order1.addToCart(article2)
order1.addToCart(article3)
order1.placeOrder("Peter", "Peter", addressPeter, addressPeter)
order1.checkout("Visa Infinite")
order1.packaging()
order1.readyToShip()
order1.shipping()
order1.calculateGrandtotal()
order1.printOrder()
order1.checkStatus()
