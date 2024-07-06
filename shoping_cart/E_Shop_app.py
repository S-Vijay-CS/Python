
class e_shop: 
    shop_name='VIJAY E-COMM'
    location='chennai'
    phone_no= '+91 76******69'
    prod_list={}
    cart={'shirt': [10, 2000], 'pant': [12, 1000]}


    def __init__(self,prod_name,qty, price):
        self.prod_name=prod_name
        self.qty=qty
        self.price=price
        e_shop.prod_list[prod_name]=[qty,price]

    @classmethod
    def shop_display(cls):
        print(end='\n\n')
        print("Shop Name :",  cls.shop_name)
        print("Location :", cls.location)
        print("Phone No :", cls.phone_no)
        print(end='\n\n')
        print("******************************")
        sample.details1(0)
        sample.details(int(input("Enter The number")))
    @classmethod
    def produ_list(cls):
        print(end='\n\n')
        print("Prod", "Qty", "Price")
        print("---------------------")
        for i in e_shop.prod_list:
            print(i,e_shop.prod_list.get(i))
        print(end='\n\n')
        print("******************************")
        sample.details1(0)
        sample.details(int(input("Enter The number")))
    @classmethod
    def add_cart(cls):
        prod=input("Enter Product_Name : ")
        if prod in e_shop.prod_list:
            qty=int(input("Enter The Quantity : "))
            if qty <= e_shop.prod_list[prod][0]:
                if prod in e_shop.cart:
                    e_shop.prod_list[prod][0]+=e_shop.cart[prod][0]-qty
                    e_shop.cart[prod][0]=qty
                    print(end='\n')
                    print("Cart Product Details")
                    print("Prod", "Qty", "Price")
                    for i in e_shop.cart:
                        print(i,e_shop.cart.get(i))
                    print("---------------------")
                    print(end='\n')
                    print("Available Product")
                    print("Prod", "Qty", "Price")
                    print("---------------------")
                    for i in e_shop.prod_list:
                        print(i,e_shop.prod_list.get(i))
                    print(end='\n')
                    print("Product Update Successfully")
                    print(end='\n\n')
                    print("******************************")
                    sample.details1(0)
                    sample.details(int(input("Enter The number")))
                    
                else:
                    e_shop.cart[prod]=[qty,e_shop.prod_list[prod][1]]
                    print(end='\n')
                    print("Cart Product Details")
                    print("Prod", "Qty", "Price")
                    for i in e_shop.cart:
                        print(i,e_shop.cart.get(i))
                    print("---------------------")
                    e_shop.prod_list[prod][0]-=qty
                    print(end='\n')
                    print("Available Product")
                    print("Prod", "Qty", "Price")
                    print("---------------------")
                    for i in e_shop.prod_list:
                        print(i,e_shop.prod_list.get(i))
                    print(end='\n')
                    print("Product Added Successfully")
                    print(end='\n\n')
                    print("******************************")
                    sample.details1(0)
                    sample.details(int(input("Enter The number")))
            else:
                print(end='\n')
                print("Stock Not Available, ")
                print(f'Only{e_shop.prod_list[prod][0]} Left')
                print(end='\n\n')
                print("******************************")
                sample.details1(0)
                sample.details(int(input("Enter The number")))
                
        else:
            print(end='\n')
            print("This Product Is Not Available")
            print("Enter The Valid Product :")
            e_shop.add_cart()

    @classmethod
    def remove_cart(cls):
        if e_shop.cart!={}:
            prod=input("enter Product name : ")
            if prod in e_shop.cart:
                qty=int(input("Enter The Qty :"))
                if qty <=e_shop.cart[prod][0]:
                    if qty==0:
                        e_shop.prod_list[prod][0]+=e_shop.cart[prod][0]-qty
                        e_shop.cart.pop(prod)
                        print(end='\n')
                        print("Product removed")
                        print(end='\n')
                        print("Cart Product Details")
                        print(end='\n')
                        print("Prod", "Qty", "Price")
                        print("---------------------")
                        for i in e_shop.cart:
                            print(i,e_shop.cart.get(i))
                        print("---------------------")
                        print(end='\n')
                        print('Shop Available Product')
                        print(end='\n')
                        print("Prod", "Qty", "Price")
                        print("---------------------")
                        for i in e_shop.prod_list:
                            print(i,e_shop.prod_list.get(i))
                        print(end='\n\n')
                        print("******************************")
                        sample.details1(0)
                        sample.details(int(input("Enter The number")))
                    else:
                        
                        e_shop.prod_list[prod][0]+=e_shop.cart[prod][0]-qty
                        e_shop.cart[prod][0]=qty
                        print('Product Qty Updated')
                        print(end='\n')
                        print("Cart Product Details")
                        print(end='\n')
                        print("Prod", "Qty", "Price")
                        for i in e_shop.cart:
                            print(i,e_shop.cart.get(i))
                        print("---------------------")
                        print(end='\n')
                        print('Shop Available Product')
                        print(end='\n')
                        print("Prod", "Qty", "Price")
                        print("---------------------")
                        for i in e_shop.prod_list:
                            print(i,e_shop.prod_list.get(i))
                        print(end='\n\n')
                        print("******************************")
                        sample.details1(0)
                        sample.details(int(input("Enter The number")))
                            

                else:
                    print(end='\n')
                    print("Cannot Remove, ")
                    print(f'Only{e_shop.cart[prod][0]} are availble')
                    print(end='\n\n')
                    print("******************************")
                    sample.details1(0)
                    sample.details(int(input("Enter The number")))
                    
                        
            else:
                print(end='\n')
                print("This Product Not Available In your cart")
                print("Enter The Valid Product :")
                e_shop.remove_cart()
            
        else:
            print("Your Cart is Empty")
            print(end='\n\n')
            print("******************************")
            sample.details1(0)
            sample.details(int(input("Enter The number")))
        

            
class customer(e_shop):
    cus_name='Vijay'
    phone='+91 76******69'
    cus_location='Chennai'
    cart=e_shop.cart
    
    @classmethod
    def cus_display(cls):
        print(end='\n\n')
        print("Customer Name :",  cls.cus_name)
        print("Phone No :", cls.phone)
        print("Location :", cls.cus_location)
        
        if customer.cart =={}:
            print(end='\n')
            print("Your Cart Is empty")
            print(end='\n\n')
            print("******************************")
            sample.details1(0)
            sample.details(int(input("Enter The number")))
            
        else:
            grand_total=0
            sub_total=0
            print(end='\n')
            print("Prod", "Qty", "Price", 'Sub_Total')
            print("---------------------")
            for i in customer.cart:
                grand_total+=(e_shop.cart[i][0]*e_shop.cart[i][1])
                print(i,customer.cart.get(i),e_shop.cart[i][0]*e_shop.cart[i][1])
                
            print('Grand Total : ',grand_total )
            print(end='\n\n')
            print("******************************")
            sample.details1(0)
            sample.details(int(input("Enter The number")))
            
        
v1=e_shop('shirt',10,2000) 
v2=e_shop('pant',22,1000)
v3=e_shop('t-shirt',13,1400)
v3=e_shop('shoe',50,699)

class sample():

    def __init__(self):
        self.number=number
    def details1(self):
        print("SHOP_DETAILS : press 1")
        print("PRODUCT_DETAILS : press 2")
        print("CUSTOMER_DETAILS : press 3") 
        print("ADD_PROD To CART : press 4")
        print("REMOVE_CART PROD : Press 5")
        print("EXIT : press ")
        
    def details(number):
        
        if number==1:
            print(end='\n\n')
            e_shop.shop_display()
        elif number==2:
            print(end='\n\n')
            e_shop.produ_list()
        elif number==3:
            print(end='\n\n')
            customer.cus_display()
        elif number==4:
            print(end='\n\n')
            e_shop.add_cart()
        elif number==5:
            print(end='\n\n')
            e_shop.remove_cart()
        elif number==6:
            pass
print("SHOP_DETAILS : press 1")
print("PRODUCT_DETAILS : press 2")
print("CUSTOMER_DETAILS : press 3") 
print("ADD_PROD To CART : press 4")
print("REMOVE_CART PROD : Press 5")
print("EXIT : press 6 ")

number=int(input("Enter The number"))
if number in [1,2,3,4,5,6]:
    sample.details(number)
else:
    print(" Enter Valid Input : ")

