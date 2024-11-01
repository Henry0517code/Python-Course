import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, folder_path):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    # Request the content of the URL
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch page: {response.status_code}")
        return
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all image tags
    img_tags = soup.find_all('img')
    
    # Download each image
    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue
        
        # Resolve the image URL
        img_url = urljoin(url, img_url)
        
        # Get the image name from the URL
        img_name = os.path.basename(img_url)
        
        # Download the image
        try:
            img_data = requests.get(img_url).content
            with open(os.path.join(folder_path, img_name), 'wb') as img_file:
                img_file.write(img_data)
                print(f"Downloaded: {img_name}")
        except Exception as e:
            print(f"Failed to download {img_url}: {e}")

if __name__ == "__main__":
    url = input("Enter the URL to scrape images from: ")
    folder_path = input("Enter the folder path to save images: ")
    download_images(url, folder_path)
