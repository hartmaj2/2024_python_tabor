import requests
import os

def download_image(url, file_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
        print(f"Image saved to {file_path}")
    else:
        print(f"Failed to retrieve image from {url}")

def download_ten_images():
    base_url = "https://picsum.photos/500/300"
    image_dir = "lorem_picsum_images"
    os.makedirs(image_dir, exist_ok=True)
    
    for i in range(1, 11):
        file_path = os.path.join(image_dir, f"image_{i}.jpg")
        download_image(base_url, file_path)

if __name__ == "__main__":
    download_ten_images()
