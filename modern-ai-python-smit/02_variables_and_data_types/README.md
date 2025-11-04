# 🧱 Step 02 — Variables & Data Types (Desi Edition)

Welcome back, coder! 😎  
Ab hum programming ke **sabse core concept** ko samjhenge —  
kaise computer data ko yaad rakhta hai aur kis form me rakhta hai.  

---

## 🧠 What is a Variable?

Socho Ammi ke kitchen me bohot saare *dabbe* hain —  
ek me **cheeni**, ek me **namak**, ek me **chai patti**.  
Har dabbe ka **label (naam)** hota hai aur andar **data** (value).  
Python me variable bhi waise hi kaam karta hai.

**Example:**
```python
cheeni = "Sugar"
namak = "Salt"
chai_patti = "Tea Leaves"

print("Kitchen Boxes:", cheeni, ",", namak, ",", chai_patti)
````

💬 *Variable = label + value.*

---

## ⚙️ Rules for Naming Variables

1. Name letter ya underscore se start hona chahiye.
   ✅ `my_name`, `_rollNumber`
   ❌ `2name` (galat)

2. Spaces allowed nahi. Use `_` for multi-word names.
   ✅ `first_name`
   ❌ `first name`

3. Case-sensitive hota hai.
   `age`, `Age`, `AGE` — 3 different variables!

4. Reserved keywords (like `if`, `class`, `True`) use nahi kar sakte.

---

## 🧩 Data Types — Different Kinds of Dabba

Python automatically samajh leta hai kis type ka data store kar rahe ho.

| Type                 | Example          | Real-Life Analogy           |
| -------------------- | ---------------- | --------------------------- |
| **String (`str`)**   | `"Ammi ki chai"` | Text (jaise label on dabba) |
| **Integer (`int`)**  | `10`, `-5`       | Count of rotiyan            |
| **Float (`float`)**  | `3.5`, `99.99`   | Price per kg                |
| **Boolean (`bool`)** | `True`, `False`  | Switch ON/OFF               |

---

## 🧮 Example 1 — Student Info

```python
name = "Ali"
age = 18
grade = 9.5
is_present = True

print("Name:", name)
print("Age:", age)
print("Grade:", grade)
print("Present today:", is_present)
```

💡 Python automatically understands each type!

---

## 🔄 Type Casting — Converting Boxes

Kabhi kabhi data ek form me hota hai, aur tumhe doosri form me chahiye.
Use **type casting** kehte hain.

```python
price = "500"   # string
price = int(price)   # convert to number
print(price + 100)   # 600
```

Ya vice versa 👇

```python
age = 20
print("Meri umar " + str(age) + " saal hai")
```

---

## 🔗 Concatenation — Mixing Text

Strings ko combine karne ke liye `+` ya **f-string** use karte hain.

```python
city = "Karachi"
food = "Biryani"
print("Mujhe " + food + " pasand hai from " + city)
# or better 👇
print(f"Mujhe {food} pasand hai from {city}")
```

---

## 🧠 Key Takeaways

* Variable = data storage box
* Data types define kis tarah ka data store hai
* Python automatically detect karta hai
* `str()`, `int()`, `float()` se convert kar sakte ho
* f-strings are best for clean printing

---

👨‍🏫 **Next Step:**
Now it’s time for **practice** — real-life mini tasks that lock these ideas in your brain 😄

```
