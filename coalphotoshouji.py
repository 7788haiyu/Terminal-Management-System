#pip install requests beautifulsoup4
#阿黄，你如果需要煤炭数据集，可以用这个下载，以后可以做一个训练，这个不在主程序中
import os
import requests
from bs4 import BeautifulSoup
import random

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def download_image(url, folder_path, index):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_path = os.path.join(folder_path, f'coal_photo_{index}.jpg')
            with open(file_path, 'wb') as file:
                file.write(response.content)
            print(f'Downloaded: {file_path}')
    except Exception as e:
        print(f'Failed to download {url}: {e}')

def search_and_download_coal_photos(search_query, num_photos):
    folder_path = r'C:\Users\Administrator\Desktop\hongweihuang_system\coalphoto'
    create_directory(folder_path)
    
    # Google Images search URL
    search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={search_query}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find image tags
        img_tags = soup.find_all('img')

        # Extract image URLs
        img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

        # Randomly select num_photos from available images
        selected_urls = random.sample(img_urls, min(num_photos, len(img_urls)))

        for index, url in enumerate(selected_urls, start=1):
            download_image(url, folder_path, index)

    except Exception as e:
        print(f'Error occurred: {e}')

if __name__ == "__main__":
    search_query = "coal"
    num_photos = 100
    search_and_download_coal_photos(search_query, num_photos)
