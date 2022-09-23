def user_list(**user_data):
    for key, value in user_data.items():
        print(f"{key} = {value}")

user_list(Name="Burak", Sur_Name="Karhan", Age=24, E_mail="aburakkarhan@gmail.com")