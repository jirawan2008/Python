customer = int(input("จำนวนลูกพระยานาหมื่นกีท่าน:"))
ราคาบุฟเฟ่ต์ต่อหัว = 219
refill = input("เอาน้ำรีฟิลบ่ (y = ก็ได้ๆเซ้าซี้จัง / n = ไอด็อนแคร์บอสตัน) : ")

if refill.strip().lower() == "y":
    refill_price = 39
    refill_text = "ก็ได้ๆเซ้าซี้จัง"
else:
    refill_price = 0
    refill_text = "ไอด็อนแคร์บอสตัน"

ยอดรวม = customer * (ราคาบุฟเฟ่ต์ต่อหัว + refill_price)
vat = ยอดรวม * 0.07
ราคารวมสุทธิ = ยอดรวม + vat

print(f"จำนวนลูกพระยานาหมื่น : {customer} องค์")
print(f"น้ำรีฟิล : {refill_text}")
print(f"ราคาก่อนรวม vat : {ยอดรวม:,.2f} บาท")
print(f"ภาษีมูลค่าเพิ่ม : {vat:,.2f} บาท")
print(f"ราคารวมสุทธิ : {ราคารวมสุทธิ:,.2f} บาท")