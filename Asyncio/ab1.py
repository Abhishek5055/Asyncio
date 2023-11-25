import time 
import asyncio
import requests

async def function1():
    print("func1")
    URL="https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("Abhi.ico","wb").write(response.content)
    
    return "Abhi"

async def function2():
    print("func2")
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("Abhi3.jpg","wb").write(response.content)
    
async def function3():
    print("func3")
    URL = "https://p4.wallpaperbetter.com/wallpaper/490/433/199/nature-2560x1440-tree-snow-wallpaper-preview.jpg"
    response = requests.get(URL)
    open("Abhi3.ico","wb").write(response.content)
    
async def main():
    L= await asyncio.gather(
        function1(),
        function2(),
        function3(),
     )
    print(L)
asyncio.run(main())

    