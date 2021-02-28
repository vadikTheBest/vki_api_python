import requests
from api_key import my_token 
api_url = 'https://api.vk.com/method/'
id_group = '-202262558'

def getjson(api_method):
    response = requests.get(f"{api_url}{api_method}", params={"owner_id": id_group, "count": 10, "offset": 0, "access_token": my_token, "v": "5.52"})
    response = response.json()
    return response

def crud_read():
    wall = getjson("wall.get")
    counter = wall['response']['count']
    while counter != 0:
        print("id поста =", wall['response']['items'][counter-1]['id'], " Текст сообщения = ", wall['response']['items'][counter-1]['text'], '\n')
        counter -= 1

def crud_create(text_message):
    api_method = 'wall.post'
    response = requests.get(f"{api_url}{api_method}", params={"owner_id": id_group, "message": text_message, "offset": 0, "access_token": my_token, "v": "5.52"})
    print("Запись на стене успешно была добавлена\n")
    crud_read()

def crud_delete(id_post):
    api_method = 'wall.delete'
    response = requests.get(f"{api_url}{api_method}", params={"owner_id": id_group, "post_id": id_post, "offset": 0, "access_token": my_token, "v": "5.52"})
    print("Запись на стене успешно была удалена, если вы ввели правильный id\n")
    crud_read()  

def crud_update(id_post, new_message):
    api_method = 'wall.edit'
    response = requests.get(f"{api_url}{api_method}", params={"owner_id": id_group, "post_id": id_post, "message": new_message, "offset": 0, "access_token": my_token, "v": "5.52"})
    print("Запись на стене успешно была изменена, если вы ввели правильный id\n")
    crud_read()  

print("Добро пожаловать в приложение для работы с текстовами постами в вк\nЧтобы создать запись, напишите create\nЧтобы удалить запись, напишите delete\nЧтобы изменить запись, напишите edit\nЧтобы прочесть записи, напишите read\nЧтобы выйти из приложения, напишите exit\n")

while True:
  keyboard = input()
  if keyboard == 'create':
      new_message = input("Пожалуйста, введите новое сообщение\n")
      crud_create(new_message)
  elif keyboard == 'delete':
      id_delete_post = input("Пожалуйста, введите существующий id сообщения, который хотите удалить\n")
      crud_delete(id_delete_post)
  elif keyboard == 'edit':
      id_edit_post = input("Пожалуйста, введите существующий id сообщения, который собирайтесь изменить\n")
      edit_message = input("Пожалуйста, введите новое измененное сообщение\n")
      crud_update(id_edit_post, edit_message)
  elif keyboard == 'read':
      crud_read()
  elif keyboard == 'exit':
      break 

