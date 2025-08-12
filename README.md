# 🛒⭑.ᐟ Simple Online Shop System (Python)

## 📦 โครงสร้างโปรเจกต์

 𝝑𝝔โปรเจกต์แบ่งออกเป็น 3 เวอร์ชัน:

### ✅ Version 1 – Basic Product List🐻‍❄️ྀིྀི ⊹ ࣪ ˖
- ใช้ `dictionary` สำหรับเก็บสินค้า
- เพิ่มสินค้า และแสดงรายการสินค้า
   python
add_product(product_list, "Tomato", 20)
show_product(product_list)

### ✅✅ Version 2 – OOP Product Management🐻‍❄️ྀིྀི ⊹ ࣪ ˖
ใช้คลาส Product และ Store จัดการข้อมูลสินค้าแบบเป็นระบบมากขึ้น
   python
my_store = Store()
my_store.add_product("Chips", 15)
my_store.show_products()

### ✅✅✅ Version 3 – Simulated Online Shop System🐻‍❄️ྀིྀི ⊹ ࣪ ˖
-มีคลาส: Product, Customer, OnlineShop
-ลูกค้าสามารถเพิ่มของลงในตะกร้า
-มีระบบชำระเงิน (Checkout) และติดตามคำสั่งซื้อ (Order Tracking)
-มีการสร้าง Order ID อัตโนมัติด้วย UUID
   python
my_shop.addingItemsToCart(customer1, product1, 5)
my_shop.checkOut(customer1)
my_shop.orderTracking(customer1, order_id)

### ⚙️ วิธีการใช้งาน ദ്ദി ˉ͈̀꒳ˉ͈́ )✧
ดาวน์โหลดหรือ Clone โปรเจกต์:
git clone https://github.com/your-username/online-shop-simulation.git
cd online-shop-simulation
รันแต่ละไฟล์:
python version1_basic.py
python version2_oop.py
python version3_onlineshop.py

###### 📜 License
This project is for educational purposes only.
You may modify and reuse with proper credit.
