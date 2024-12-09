# 11. [IGA] Creating Basic Custom Functions Part 2
brand_name = "Kia"
brand_release_date = 1960
brand_market_value = 245.233
def car_brand(brand_name, branad_release_date, brand_market_value):
    brand_name = brand_name + " Motors"
    brand_release_date = branad_release_date + 10
    brand_market_value = brand_market_value + 15
    print(brand_name, brand_release_date, brand_market_value)

car_brand(brand_name, brand_release_date, brand_market_value)

# let's give it another try because I need to do so  .
phone_brand = "Samsung"
phone_series = "A"
phone_model = 52
phone_sub_series = "s"
phone_release_price = 12500.250
def phone(phone_brand, phone_series, phone_model, phone_sub_series, phone_release_price):
    phone_brand01 = phone_brand
    phone_series01 = phone_series + " Series "
    phone_model01 = phone_model
    phone_sub_series01 = phone_sub_series + " Sub Series "

    print(phone_brand01, phone_series01, phone_model01, phone_sub_series01, phone_release_price)
    print(f"It's a phone called \n {phone_series}{phone_model01}{phone_sub_series} form {phone_brand01}  ")

phone(phone_brand, phone_series, phone_model, phone_sub_series, phone_release_price)

# function 03
# let's do more than declaring variables outside the scope of the function.
# calling inside the function and asking the user for input too
company_name = "Dell"
company_product = ["Pcs", "Laptops", "Workstations"]
def(company_name, which_product_you_have, product_model, product_number, product_category):
    company_name01 = company_name + "Corporation "
    company_product01 = company_product  + "Electronic"




