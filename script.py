import PIL.Image

# Caracteres ASCII usados para construir a saída
ASCII_CHARS = ["0", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]


# Redimensionar a imagem de acordo com a nova largura
def redimensionar_img(image, nova_largura):
    largura, altura = image.size
    proporcao = altura / largura
    nova_altura = int(nova_largura * proporcao)
    img_redimensionada = image.resize((nova_largura, nova_altura))
    return img_redimensionada


# Transformar a imagem em cinza
def cinzenta(image):
    img_cinza = image.convert("L")
    return img_cinza


# Converter pixels para caracteres ASCII
def pixels_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters


def main(nova_largura=100):
    image = ""
    img_correta = False

    # Tentativa de abrir a imagem da entrada do usuário
    while not img_correta:
        try:
            path = input("Digite um diretório válido da imagem que você deseja converter em ASCII: \n")
            image = PIL.Image.open(path)
            img_correta = True
        except FileNotFoundError:
            print(path, "não é um diretório válido.")
            continue
        except OSError:
            print(path, "não é um diretório válido.")
            continue

    nova_imagem = pixels_ascii(cinzenta(redimensionar_img(image, nova_largura)))

    # Formatar
    conategem_pixels = len(nova_imagem)
    img_ascii = "\n".join(nova_imagem[i:(i + nova_largura)] for i in range(0, conategem_pixels, nova_largura))

    print(img_ascii)

    # Salvar resultados
    with open("imagem_ascii.txt", "w") as f:
        f.write(img_ascii)


main()


