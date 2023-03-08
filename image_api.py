import os
import openai
from PIL import ImageTk,Image
openai.api_key = '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'
x=openai.Image.create(
  prompt="liken organ",
  n=1,
  size="1024x1024"
)
print(x)
import urllib.request
  
urllib.request.urlretrieve(x['data'][0]['url'],"gfg.png")
  
img = ImageTk.PhotoImage(Image.open("gfg.png"))
img.show()