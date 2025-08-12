class Product: 
    def __init__(self, name, quantity): 
        self.name = name
        self.quantity = quantity

class Store: 
    def __init__(self): 
        self.__products = []   # สร้าง list สำหรับเก็บ Product

    def add_product(self, name, quantity): 
        product = Product(name, quantity)  # สร้าง Product object
        self.__products.append(product)    # เพิ่มเข้า list

    def show_products(self): 
        for product in self.__products:
            print(f"{product.name} : {product.quantity}")  # แสดงสินค้า

# --- ตัวอย่างการทดสอบโปรแกรม ---
my_store = Store() 
my_store.add_product("Tomato", 20)
my_store.add_product("Chips", 15) 
my_store.add_product("Milk", 15)
my_store.show_products()
