# Task 01: Shopping Bill
# GST is calculated first, then discount is applied.

def calculateElectronicsGST(a, b):
    amount = a + b
    gst = amount * 18 / 100
    return amount + gst

def calculateFashionGST(c, d):
    amount = c + d
    gst = amount * 13 / 100
    return amount + gst

def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst

def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    total = electronics + fashion + food
    return total

def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    final_amount = total - discount

    return final_amount

# Sample values given in the task
a = 100
b = 100
c = 100
d = 100
e = 100

total = totalBill(a, b, c, d, e)
final_amount = calculateDiscountedBill(a, b, c, d, e)
discount = total - final_amount

print("Total after GST =", format(total, ".2f"))
print("Discount =", format(discount, ".2f"))
print("Final payable amount =", format(final_amount, ".2f"))
