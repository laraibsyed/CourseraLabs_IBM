from PIL import Image
import requests
from io import BytesIO

# URL of the image
url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"

# Step 1: Download the image using requests
response = requests.get(url)

# Step 2: Check if the request was successful
if response.status_code == 200:
    # Open the image using PIL directly from the downloaded content
    img = Image.open(BytesIO(response.content))
    
    # Step 3: Display the image
    img.show()

else:
    print("Failed to retrieve the image. Status code:", response.status_code)
