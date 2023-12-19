from bs4 import BeautifulSoup

# Replace 'your_file.html' with the path to your HTML file
with open('Google Maps.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Create a BeautifulSoup object
soup = BeautifulSoup(html_content, 'html.parser')

# Replace 'your_class_name' with the actual class name you want to target
labelNames = soup.find_all(class_='Io6YTe fontBodyLarge kR99db')
labelAddress = soup.find_all(class_='gSkmPd fontBodyMedium DshQNd')

labelDict = dict(zip(labelNames,labelAddress))

for k,v in labelDict.items():
     print(f"{k.text}|{v.text}")
