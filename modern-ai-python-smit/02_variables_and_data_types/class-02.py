# 🧱 Step 02 — Variables & Data Types (Desi Edition)
# Created by Shah Meer (Sensei)
# Agentic AI Trainer @ SMIT
# ----------------------------------------------------
# Aaj hum seekhenge Python me data ko kaise store karte hain
# aur kis tarah ke data types hote hain.

# ----------------------------------------------------
# 🧠 1. What is a Variable?
# Soch lo Ammi ke kitchen me dabbe hain — har dabbe ka label aur andar data.
# Python me bhi variable ek dabba hai jahan hum data store karte hain.

cheeni = "Sugar"
namak = "Salt"
chai_patti = "Tea Leaves"

print("Ammi ke dabbe:", cheeni, ",", namak, "aur", chai_patti)

# ----------------------------------------------------
# ⚙️ 2. Rules for Naming Variables
# ✅ Letters, numbers, underscore allowed
# ❌ Spaces, special characters not allowed

# Example (valid):
first_name = "Ayesha"
# Example (invalid):
# first name = "Ayesha"  ❌

# ----------------------------------------------------
# 🧩 3. Data Types
# Python automatically samajh leta hai kis type ka data hai.

# String (text)
student_name = "Hamza"

# Integer (whole number)
student_age = 18

# Float (decimal number)
student_marks = 92.5

# Boolean (True/False)
is_present = True

print("Name:", student_name)
print("Age:", student_age)
print("Marks:", student_marks)
print("Present:", is_present)

# ----------------------------------------------------
# 🧮 4. Simple Math Example — Chotu ki Chai Dhaba Bill ☕
# Chotu ke dhaba par chai 80 rupees ki aur paratha 60 ka.
# 2 chai aur 3 parathay ka total bill nikaalo.

chai_price = 80
paratha_price = 60
total_bill = (2 * chai_price) + (3 * paratha_price)
print("Chotu ka Total Bill:", total_bill, "Rupees 💵")

# ----------------------------------------------------
# 🔄 5. Type Casting — Converting Data Types
# Kabhi kabhi data string me hota hai, use number me convert karna padta hai.

item_price = "1500"  # string
quantity = 2

# Convert string to integer
item_price = int(item_price)
total = item_price * quantity
print("Total Shopping Cost =", total, "Rupees 🛍️")

# ----------------------------------------------------
# 🔗 6. String Concatenation — Mixing Text
# Do strings combine karne ke liye + ya f-string use hoti hai.

city = "Karachi"
food = "Biryani"
print("Mujhe " + food + " pasand hai from " + city)
print(f"Mujhe {food} pasand hai from {city} 😋")

# ----------------------------------------------------
# 🎤 7. Personal Intro (Practice)
# Apna naam, city, aur hobby likho.

name = "Aisha"
city = "Lahore"
hobby = "Painting"

print(f"Hi! Mera naam {name} hai, main {city} se hoon aur mujhe {hobby} ka shoq hai 🎨")
# ----------------------------------------------------