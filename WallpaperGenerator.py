import requests

for i in range(60, 101):
    img = requests.get("https://picsum.photos/1920/1080")
    img_file = open('D:\Code\Web\Проекты\WallpaperGenerator\images\img' + str(i) + '.jpg', 'wb')
    img_file.write(img.content)
    img_file.close()