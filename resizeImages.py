# Creado por Natalie Jelenkiewicz para proyecto ELÜN bajo Licencia Creative Commons
import os
from PIL import Image

ubicacion = './'
carpeta = 'orquidea_litoral'
tam_img = (400, 400)

os.makedirs(carpeta + '_resize', exist_ok=True)
dir_completa = os.path.join(ubicacion, carpeta)


def recorrer_carpeta(dir_c=dir_completa):
    contenido = os.listdir(dir_c)
    imagenes = []
    for fichero in contenido:
        if os.path.isfile(os.path.join(dir_c, fichero)) and fichero.endswith('.jpg'):
            imagenes.append(fichero)
    return imagenes


def define_points(img):
    ancho, alto = img.size
    ls = [ancho, alto]
    min_value = min(ls)
    min_dim = ls.index(min_value)

    if min_dim == 0:
        left = 0
        right = ls[0]
        bottom = int((ls[1] / 2) - (ls[0] / 2))
        top = int((ls[1] / 2) + (ls[0] / 2))
    elif min_dim == 1:
        bottom = 0
        top = ls[1]
        left = int((ls[0] / 2) - (ls[1] / 2))
        right = int((ls[0] / 2) + (ls[1] / 2))

    return left, bottom, right, top


def cut_resize_save(img, name, size=tam_img):
    im = img.crop(define_points(img))
    im = im.resize(size)
    dir_file = os.path.join(carpeta + '_resize', f"{name}_resize.jpg")
    im.save(dir_file)

if __name__ == '__main__':
    contenido = recorrer_carpeta()

    for file in contenido:
        file_name = file[:-4]
        im = Image.open(os.path.join(carpeta, file))
        cut_resize_save(im, file_name)
