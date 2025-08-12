import uuid

# คลาส Product
class Product:
    def __init__(self, name, description, price, online_shop):
        self.__name = name
        self.__description = description
        self.__price = price
        self.__online_shop = online_shop

    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @property
    def price(self):
        return self.__price

    @property
    def online_shop(self):
        return self.__online_shop


# คลาส Customer
class Customer:
    def __init__(self, name, email, address):
        self.__name = name
        self.__email = email
        self.__address = address
        self.__cart = []         # เก็บสินค้าในตะกร้า [(Product, quantity), ...]
        self.__past_orders = []  # ประวัติการสั่งซื้อ

    @property
    def name(self):
        return self.__name

    @property
    def email(self):
        return self.__email

    @property
    def address(self):
        return self.__address

    @property
    def cart(self):
        return self.__cart

    @property
    def past_orders(self):
        return self.__past_orders


# คลาส OnlineShop
class OnlineShop:
    def __init__(self, name, url):
        self.__name = name
        self.__url = url
        self.__products = []

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def products(self):
        return self.__products

    def add_product(self, product):
        self.__products.append(product)

    def addingItemsToCart(self, customer, product, quantity):
        # เพิ่มสินค้าและจำนวนลงในตะกร้าของลูกค้า
        for i, (p, q) in enumerate(customer.cart):
            if p.name == product.name:
                customer.cart[i] = (p, q + quantity)
                print(f"เพิ่มสินค้า {quantity} ชิ้น ลงในตะกร้า {customer.name} (เพิ่มจำนวนเดิม)")
                return
        customer.cart.append((product, quantity))
        print(f"เพิ่มสินค้า {quantity} ชิ้น ลงในตะกร้า {customer.name}")

    def checkOut(self, customer):
        if not customer.cart:
            print("ตะกร้าว่าง ไม่มีสินค้าให้ชำระเงิน")
            return

        total = 0
        items = []
        for product, qty in customer.cart:
            cost = product.price * qty
            total += cost
            items.append({
                'product_name': product.name,
                'quantity': qty,
                'price_per_item': product.price,
                'total_price': cost
            })

        order_id = str(uuid.uuid4())
        order = {'order_id': order_id, 'items': items, 'total_price': total}
        customer.past_orders.append(order)
        customer.cart.clear()
        print(f"ชำระเงินเรียบร้อย Order ID: {order_id} ยอดรวม: {total:.2f} บาท")

    def orderTracking(self, customer, order_id):
        for order in customer.past_orders:
            if order['order_id'] == order_id:
                print(f"Order ID: {order['order_id']}")
                print("รายการสินค้า:")
                for item in order['items']:
                    print(f" - {item['product_name']} x{item['quantity']} ราคา/ชิ้น {item['price_per_item']} บาท รวม {item['total_price']} บาท")
                print(f"ราคารวม {order['total_price']} บาท")
                return
        print(f"ไม่พบ Order ID {order_id} ในประวัติของลูกค้า {customer.name}")


# ---------------- ตัวอย่างการใช้งาน ----------------

if __name__ == "__main__":
    # สร้างร้านค้าออนไลน์
    my_shop = OnlineShop("Grooming Shop", "www.groomingshop.com")

    # สร้างสินค้า
    product1 = Product("Tomato", "มะเขือเทศแดง", 49.99, my_shop)
    product2 = Product("Chips", "ขนมมันฝรั่งทอดกรอบ", 89.99, my_shop)
    product3 = Product("Milk", "นมพร่องมันเนย", 132.85, my_shop)

    # เพิ่มสินค้าเข้าในร้าน
    my_shop.add_product(product1)
    my_shop.add_product(product2)
    my_shop.add_product(product3)

    # สร้างลูกค้า
    customer1 = Customer("สมชาย บ้านอยู่ไหน", "somchai@banyunai.com", "123 หมู่ 5 กรุงเทพฯ")
    
    # ลูกค้าเพิ่มสินค้าในตะกร้า
    my_shop.addingItemsToCart(customer1, product1, 5)  
    my_shop.addingItemsToCart(customer1, product2, 2) 
    my_shop.addingItemsToCart(customer1, product3, 6)

    # ลูกค้าทำการชำระเงิน (checkout)
    my_shop.checkOut(customer1)

    # ตรวจสอบสถานะคำสั่งซื้อ (order tracking)
    order_id = customer1.past_orders[0]['order_id']
    my_shop.orderTracking(customer1, order_id)
