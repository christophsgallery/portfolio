from bs4 import BeautifulSoup

# Read HTML from file
with open('portfolio-single-avd-2022.html', 'r') as file:
    html = file.read()

# Parse the HTML
soup = BeautifulSoup(html, 'html.parser')

# Find all divs with class "full-cover"
divs = soup.find_all('div', class_='full-cover')

# Extract the background image URLs
image_urls = []
for div in divs:
    style = div.get('style')
    image_url = style.split('url(')[1].split(')')[0]
    image_urls.append(image_url)

# Save the list of image URLs to a text file
with open('image_urls.txt', 'w') as file:
    for url in image_urls:
        file.write(url + '\n')