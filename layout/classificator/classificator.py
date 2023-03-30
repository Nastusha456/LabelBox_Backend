# это пока не работает, так сказать в процессе

import requests
import io
import tensorflow as tf
from bs4 import BeautifulSoup
from PIL import Image

# URL веб-сайта, на котором находится изображение

def classificator(url):
    # Получаем HTML-страницу с веб-сайта
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Находим тег <img> с изображением
    img_tag = soup.find('img')

    # Получаем ссылку на изображение
    img_url = img_tag['src']

    # Получаем бинарные данные изображения
    image_response = requests.get(img_url)
    image_binary = io.BytesIO(image_response.content)

    # Загружаем модель TensorFlow для распознавания объектов на изображении
    model = tf.keras.applications.InceptionV3()

    # Преобразуем изображение в формат, который может быть обработан моделью TensorFlow
    image = Image.open(image_binary).convert('RGB')
    image = image.resize((299, 299))
    image = tf.keras.preprocessing.image.img_to_array(image)
    image /= 255.0
    image = tf.keras.preprocessing.image.smart_resize(image, (299, 299))

    # Получаем предсказание модели и определяем объект на изображении
    prediction = model.predict(tf.expand_dims(image, axis=0))
    index = tf.argmax(prediction, axis=-1)
    object_name = tf.keras.applications.imagenet_utils.decode_predictions(prediction, top=1)[0][0][1]

    # Отправляем результат обратно на веб-сайт
    result = f"На изображении изображён {object_name}"
    return result

# f'На изображении изображен {object_name}'
#url = здесь пока не совсем понятно в каком формате будет подаваться изображение