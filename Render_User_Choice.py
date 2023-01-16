# Importa funcoes da biblioteca pillow
from PIL import Image

#Abre o arquivo "img.jpg"

image_path = "img.jpg"
image_file = Image.open(image_path)

qualit = 0

qualit = int(input("\nDigite a qualidade desejada da nova imagem(pixels):"))
d = int(input("Digite o indice do arquivo -new_image[indice].jpg- :"))

image_file.save(f"new_image{d}.jpg", quality=qualit)
