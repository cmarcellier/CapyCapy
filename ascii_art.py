#!/usr/bin/python3

import argparse
import os
import cv2

class Image:
    def __init__(self, path):
        self.image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    def resize(self):
        resized_image = cv2.resize(self.image, (n_x, n_y), interpolation=cv2.INTER_AREA)
        size = os.get_terminal_size()
        #size.
        taille=n_y
        ratio = size.y/n_y
        resized_image = cv2.resize(self.image, (n_x, n_y), interpolation=cv2.INTER_AREA)
        pass

    def to_ascii(self, ascii_chars):
        tab=[]
        for i in range(n-y):
            tab1=[]
            for k in range()
                # déterminer l'index du charactère ascii (0-len(ascii_chars)) utiliser en fonction de la couleur (une valeur de 0-255)
                # ajouter ce charactère à ma ligne
            # ajouter à mon tableau ma ligne qui est la concaténation de tous les charactères de ma ligne
        # retourner la concaténation de toutes les lignes séparer par un "\n"
        pass

    def display(self, ascii_chars):
        # Modification du contraste (optionnel)
        # Conversion en Ascii
        pass

def main():
    parser = argparse.ArgumentParser(description="Convertir une image en ASCII")
    parser.add_argument("--path", required=True, type=str, help="Chemin vers l'image à convertir")
    args = parser.parse_args()
    print("Image à convertir :", args.path)

if __name__ == "__main__":
    main()