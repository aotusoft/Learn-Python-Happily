import requests
url = "https://images.dmzj1.com/s/%E5%B1%B1%E7%94%B0%E5%A6%96%E7%B2%BE%E5%A4%A7%E8%80%81%E5%B8%88%E7%9A%84%E5%9D%A0%E5%85%A5%E7%88%B1%E6%B2%B3%E7%BA%AF%E7%9C%9F%E9%A5%AD/%E7%AC%AC15%E8%AF%9D/0{}%20%E6%8B%B7%E8%B4%9D.jpg"
#格式化字符串
for i in range(463,493):
    image_name = i
    if i < 10:
        image_name = str("0"+str(i))
    else:
        image_name = str(i)
    response = requests.get(url.format(image_name))
    img_content = response.content
    with open(str(image_name) +".jpg","wb") as f:
        f.write(img_content)
