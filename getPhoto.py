import requests
import os
from lxml import html

url = "https://rusdate.net/filter/men"  # Замените на URL страницы, содержащей изображения
response = requests.get(url)
tree =  html.fromstring(response.text)
 
 
# Находим все изображения внутри элементов <div> с классом 'view__profile__img_wrapper'
images = tree.xpath("//div[@class='mainUsersPic counted ']/a/img")

print(len(images))
output_folder = r'C:/Users/katev/source/repos/Tinder/tinderAPI/Img/'  # Путь к папке для сохранения изображений

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for img in images:
    img_url = img.get('src')
    print(img_url)
    img_name = img_url.split('/')[-1]  # Получаем имя файла из URL
    img_data = requests.get(url+img_url).content

    with open(os.path.join(output_folder, img_name), 'wb') as img_file:
        img_file.write(img_data)
        print(f'Изображение {img_name} успешно сохранено в {output_folder}.')