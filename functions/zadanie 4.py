def process_order(*products, **customer_info):

    product_list = ', '.join(products)

    print("Продукты: " + product_list)

    name = customer_info.get('name')
    print("name:"+ name)
    surname = customer_info.get('surname')
    print("surname: " + surname)


# Пример использования
process_order('Пицца', 'Суши',"Роллы", name='Райан', surname='Гослинг')