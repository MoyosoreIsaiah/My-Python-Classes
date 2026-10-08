# age = 20
# passed_vision_test = True
# if age >= 18:
#     print("Age requirement met. ")
#
#     if passed_vision_test:
#         print("Status: Eligible for a driver's license!")
#
#     else:
#         print("Status: Ineligible- You must pass the vision test. ")

# else:
#     print("Status: Ineligible - You must be at least 18 years old.")


                    #Nested if versus logical operators (AND)

# if age >= 18 and passed_vision_test:
#     print("Eligible for lisense.")
# else: print("Ineligible")



cart_total = float(input("Cart total: "))
if cart_total >= 50.00:
    print("Eligible for free shipping")
    is_vip = str(input("VIP satus? "))
    if is_vip == "yes":
        print("Extra 10% discount applied ")
    else:
        print("Standard checkout")
else:
    print("Cart under 50: 5.00 shipping fee added")
    is_vip = str(input("VIP satus? "))
    if is_vip == "yes":
        print("Vip perk: Shipping fee waived!")
    else:
        print("Standard shipping applied")
