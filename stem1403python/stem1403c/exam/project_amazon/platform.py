"""

"""


class TaxRate:
    GST = 0.5
    QST = 0.09975


class Status:
    SHIPPING_SHIPPED = 'Shipped'
    SHIPPING_READY = 'Ready to Ship'
    SHIPPING_NOT_READY = 'We\'re processing your order'
    ORDER_PAID = 'PAID'
    ORDER_UNPAID = 'UNPAID'
    ORDER_CANCELLED = 'Canceled'


class OrderNumberSystem:
    last_order_number = 202112260000

    @staticmethod
    def getNextOrderNo():
        OrderNumberSystem.last_order_number += 1
        return OrderNumberSystem.last_order_number


class AddressSystem:
    # Generate all address
    def __init__(self, number, street, apt_no, city, province):
        self._number = number
        self._street = street
        self._apt_no = apt_no
        self._city = city
        self._province = province
        self._country = "Canada"

    def getAddress(self):
        return f"{self._number} {self._street} {self._apt_no} {self._city} {self._province} {self._country}"


class OrderSystem:
    # To generate all orders, include the customer's detail (Customer's name, address) and to calculate the amount.
    def __init__(self):
        # To protect customer's privacy, we added _, to modify, you need add a function to do that.
        self.company_name = "Apple.ca"
        self.order_number = "000000000000"
        self.item = []
        self._customer_name = None
        self._billing_address = None
        self.order_date = None
        self.order_time = None
        self._receiver_name = None
        self._shipping_address = None
        self.status = None
        # Amount
        self.freight = 0    # freight is 0 if > 50$
        self.gst = 0
        self.qst = 0
        self.tax = 0
        self.grand_total = 0    # subtotal + tax
        self.subtotal = 0

    def addShippingAddress(self, receiver_name, shipping_address):
        self._receiver_name = receiver_name
        self._shipping_address = shipping_address

    def addBillingAddress(self, customer_name, billing_address):
        self._billing_address = billing_address
        self._customer_name = customer_name

    def addToCart(self):
        item_number = self.item[1]
        return f"New Message from {self.company_name}: Item:{self.customer_name} (Item no. {item_number}) has been added in your Bag."

    def placeOrder(self):
        self.status = Status.ORDER_UNPAID
        return f"""New Message from {self.company_name}: Order No.{self.order_number}) has been placed. 
        Now, you need to paid that. Because the status is {self.status}"""

    def confirm(self):
        pass

    def checkout(self, payment_method):
        self.status = Status.ORDER_PAID
        return f"New Message from {self.company_name}: Order No.{self.order_number}) has been {self.status}."

    # Package Not Ready to Ship
    def packaging(self):
        self.status = Status.SHIPPING_NOT_READY
        return f"New Message from {self.company_name}: Order No.{self.order_number}) was {self.status}."

    def readyToShip(self):
        self.status = Status.SHIPPING_READY
        return f"New Message from {self.company_name}: Order No.{self.order_number}) was {self.status}."

    def freight(self):
        self.freight = 25
        if self.subtotal >= 50:
            self.freight = 0

    def shipping(self):
        status = Status.SHIPPING_SHIPPED
        return f"New Message from {self.company_name}: Order No.{self.order_number}) has been {status}."

    def tax(self):
        self.gst = self.subtotal * TaxRate.GST
        self.qst = self.subtotal * TaxRate.QST
        tax = self.gst + self.qst

        self.grand_total = self.subtotal + tax

    def checkStatus(self):
        return f"Your order's status wa {self.status}"

    def printOrder(self):
        pass

    def setOrderTime(self, orderTime):
        self.order_time = orderTime

    def setOorderDate(self, orderDate):
        self.order_date = orderDate


class OrderItemSystem:
    # To Order the Item
    def __init__(self, item_no, item_name, item_detail, unit_price, qty):
        self.item_no = item_no
        self.item_name = item_name
        self.item_detail = item_detail
        self.unit_price = unit_price
        self.quantity = qty
