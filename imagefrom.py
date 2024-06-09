import requests
from bs4 import BeautifulSoup

def importima(url, name):
    extension = url.split('.')[-1].lower()
    image_extensions = ['jpg', 'jpeg', 'png', 'gif']
    video_extensions = ['mp4', 'avi', 'mov', 'wmv']
    if extension in image_extensions:
        img_response = requests.get(url)
        with open(name, 'wb') as img_file:
                img_file.write(img_response.content)
        return img_response.content
    elif extension in video_extensions:
        video_response = requests.get(url)
        with open(name, 'wb') as video_file:
                video_file.write(_response.content)
        return video_response.content
        
