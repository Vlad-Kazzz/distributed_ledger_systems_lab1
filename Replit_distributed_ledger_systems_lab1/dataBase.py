from replit import db

#Вставляем данные клиентов в Replit DB



def insert_product_information_data():
    product_information_data = [{
        'vendor_code': '12345',
        'color': 'black',
        'size': '600x1800',
        'quantity': '100',
        'price': '10500',
        'material': 'pine'
    }, {
        'vendor_code': '54321',
        'color': 'white',
        'size': '600x2000',
        'quantity': '12',
        'price': '14500',
        'material': 'birch'
    }, {
        'vendor_code': '67890',
        'color': 'brown',
        'size': '700x2100',
        'quantity': '58',
        'price': '1000',
        'material': 'oak'
    }, {
        'vendor_code': '12345345',
        'color': 'black',
        'size': '100x200',
        'quantity': '100',
        'price': '1000',
        'material': 'pine'
    }, {
        'vendor_code': '1234564445',
        'color': 'black',
        'size': '100x200',
        'quantity': '100',
        'price': '1000',
        'material': 'pine'
    }, {
        'vendor_code': '12334545',
        'color': 'black',
        'size': '100x200',
        'quantity': '100',
        'price': '1000',
        'material': 'pine'
    }, {
        'vendor_code': '1235646445',
        'color': 'black',
        'size': '100x200',
        'quantity': '100',
        'price': '1000',
        'material': 'pine'
    }, {
        'vendor_code': '2334243',
        'color': 'black',
        'size': '100x200',
        'quantity': '100',
        'price': '1000',
        'material': 'pine'
    }, {
        'vendor_code': '122343254345',
        'color': 'black',
        'size': '100x200',
        'quantity': '100',
        'price': '1000',
        'material': 'pine'
    }, {
        'vendor_code': '12212345',
        'color': 'black',
        'size': '100x200',
        'quantity': '100',
        'price': '1000',
        'material': 'pine'
    }]

    # db insertion logic here
    for idx, product in enumerate(product_information_data):
        if db is not None:
            db[f"product_{idx}"] = product

    return product_information_data

        
#Получаем данные по продуктам из Replit DB
def get_product_information():
    product_information_data = []
    if db is not None:
        for key in db.keys():
            if key.startswith("product_"):
                        product_information_data.append(db[key])
    return product_information_data


#Вставляем данные клиентов в Replit DB
insert_product_information_data()

#Получаем и выводим данные по продуктам из Replit DB
print(get_product_information())
