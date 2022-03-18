#Importation math, pillow...
import os
import sys
from math import sqrt #On importe la racine pour la fusion
from PIL import Image




#Put the path of this folder below between the quotes
path_img = r''
#On définit nouvelle image, avec la même taille que l'ancienne
ImageFile = path_img+'\img1.jpg'
img = Image.open(ImageFile)
imgneww = Image.new(img.mode,img.size)
colonne,ligne = img.size

#Deux images à fusionner pour le flou
ImageFile1 = path_img+'\img1.jpg'
ImageFile2 = path_img+'\img2.jpg'

img1 = Image.open(ImageFile1)
img2 = Image.open(ImageFile2)

#2 nouvelles lignes/colonnes
colonne1,ligne1 = img1.size
colonne2,ligne2 = img2.size


colonne3 = min(colonne1, colonne2)
ligne3 = min(ligne1,ligne2)

#Troisieme image pour pas de conflit
img3 = Image.new('RGB', (colonne3,ligne3))
imgneww3 = Image.new(img3.mode,(colonne3,ligne3))
#rotation qui a besoin d'autres valeurs
imgrot = Image.new(img.mode,(ligne,colonne))

def clear():
     os.system('cls' if os.name=='nt' else 'clear')
     return("   ")


def initialisation(): #Menu de fonctions
    x=int(input("Entrez un nombre : \n 1 = Negatif \n 2 = Miroir \n 3 = Rotation à 90° \n 4 = fusion de 2 images \n 5 = Nuance de gris \n 6 = Filtre de couleurs \n 7 = Contours de l'image \n 8 = Flou \n 9 = quitter le programme \n :"))

    if x==1:
        negatif(img)
    elif x==2:
        miroir(img)
    elif x==3:
        rotation(img)
    elif x==4:
        fusion(img1,img2,imgneww3)
    elif x==5:
        gris(img)
        imgneww.show()
        initialisation()
    elif x==6:
        filtre()
    elif x==7:
        gris(img)
        contours(img)
    elif x==8:
        flou(img)
    elif x==9:
        SystemExit(0)
    else:
        print("Veuillez renseigner une valeur comprise entre 1 et 9")
        initialisation()
        
def fusion(img1,img2,imgneww3):#On définit 3 images, les 2 à fusionner + le resultat
  for i in range(ligne3):

    for j in range(colonne3):
  
      p1 = img1.getpixel((j,i))
  #On récupère les pixels des deux images
      p2 = img2.getpixel((j,i))
  
      p = (max(p1[0],p2[0]),max(p1[1],p2[1]),max(p1[2],p2[2])) #Maximum des pixels des deux images pour avoir un contraste à chaque fois
      
  
      imgneww3.putpixel((j,i), p)#On replace
  imgneww3.show()
  clear()
  initialisation()
  
def miroir(img):
  for i in range(ligne):

    for j in range(colonne):
  
      pixel = img.getpixel((j,i))
  
      imgneww.putpixel((colonne-j-1,i), pixel)#On inverse les pixels sur chaque colonne car "colonne-j-1"
  
  
  
  imgneww.show()
  clear()
  initialisation()
  
def gris(img):
    for i in range(ligne):
        for j in range(colonne):

            pixel = img.getpixel((j,i)) # récupération du pixel
        
            # calcul du poids de chaque composante du gris dans le pixel 
        
            gris = int(0.2125 * pixel[0] + 0.7154 * pixel[1] + 0.0721 * pixel[2])
        
        # gris = int(0.33 * pixel[0] + 0.33 * pixel[1] + 0.33 * pixel[2])
        
            p = (gris,gris,gris)
        
            # composition de la nouvelle image
        
            imgneww.putpixel((j,i), p)

def rotation(img):
  for i in range(ligne):

    for j in range(colonne):
  
      pixel = img.getpixel((j,i))
  
      imgrot.putpixel((i,j), pixel)
      
  imgrot.show()
  clear()
  initialisation()
  
  
def flou(img):
    for i in range(3,colonne-3):#on defini ou on veut le flou, ici on veut commencer à partir de 4 jusqu'à la derniere colonne -4

        for j in range(3,ligne-3): #Pareil, on commence à la ligne 4
            
            gauche=img.getpixel((i-3,j))#On récupère les pixels pour former un carré, ici 3x3
            droit=img.getpixel((i+3,j))
            haut=img.getpixel((i,j+3))
            bas=img.getpixel((i,j-3))
            pix=img.getpixel((i,j))
            rouge=(gauche[0]+pix[0]+haut[0]+bas[0]+pix[0])//5 #Le rouge du pixel sera l'addition du gauche, haut  bas (+ pixel(i,j))
            vert=(gauche[1]+pix[1]+haut[1]+bas[1]+pix[1])//5#vert addition de gauche haut bas (+ pixel(i,j))
            bleu=(gauche[2]+pix[2]+haut[2]+bas[2]+pix[2])//5#bleu = addition gauche haut bas (+ pixel(i,j))
            #partie entière de 5 pour avoir un résultat integer
                                    
            imgneww.putpixel((i,j),(rouge,vert,bleu)) #On recrée une image avec le tuple rouge vert bleu qu'on vient de créer
    imgneww.show()
    clear()
    initialisation()   



def contours(img):
    
    for i in range(1,ligne-1):

        for j in range(1,colonne-1):
        #récupération des pixels voisins
            p1 = img.getpixel((j-1,i))
        
            p2 = img.getpixel((j,i-1))
        
            p3 = img.getpixel((j+1,i))
        
            p4 = img.getpixel((j,i+1))
        #Distance qui sépare les pixels
            n = sqrt((p1[0]-p3[0])*(p1[0]-p3[0]) + (p2[0]-p4[0])*(p2[0]-p4[0]))
        
            if n < 32:
        #Comparaison avec le seuil  : 32
                p = (255,255,255)
        
            else:
        #blanc si la différence est minime (255)
                p = (0,0,0)
        
            imgneww.putpixel((j,i+1),p)#noir si la différence est importante
    imgneww.show()
    clear()
    initialisation()#On relance le prgrm pour pas avoir à faire Ctrl E
  
  

def negatif(img):
  for i in range(ligne):

    for j in range(colonne):
  
      pixel = img.getpixel((j,i)) # récupération du pixel
  
      # on calcule le complement à MAX pour chaque composante - effet négatif
  
      p = (255 - pixel[0], 255 - pixel[1], 255 - pixel[2])
  
      # composition de la nouvelle image
  
      imgneww.putpixel((j,i), p)
  
  imgneww.show()
  clear()
  initialisation()

  
  
def filtre():#Menu de filtres
    x=int(input("Choisissez un nombre pour chaque filtre : \n 1 = vert \n 2 = rouge \n 3 = bleu \n 4 = violet \n 5 = jaune \n 6 = turquoise \n 7 = orange \n :"))
    if x==1:
        filtrevert(img)
    elif x==2:
        filtrerouge(img)
    elif x==3:
        filtrebleu(img)
    elif x==4:
        filtreviolet(img)
    elif x==5:
        filtrejaune(img)
    elif x==6:
        filtreturquoise(img)
    elif x==7:
        filtreorange(img)
    else:
        print("Veuillez renseigner une valeur comprise entre 1 et 7")
        filtre()#On relance la fct si le nb n'est pas bon

#Chaque fct de filtre a le même code, on modifie juste la position du pixel[1] dans la variable p (pixel) pour avoir des filtres différents

def filtrevert(img):
    
    for i in range(ligne):

        for j in range(colonne):

            pixel = img.getpixel((j,i))

    # filtrage couleur - filtre vert

            p = (0,pixel[1],0)

            imgneww.putpixel((j,i), p)
    imgneww.show()
    clear()
    initialisation()
    
    
def filtrerouge(img):
    
    for i in range(ligne):

        for j in range(colonne):

            pixel = img.getpixel((j,i))

    # filtrage couleur - filtre rouge

            p = (pixel[1],0,0)

            imgneww.putpixel((j,i), p)
    imgneww.show()
    clear()
    initialisation()
            

def filtrebleu(img):
    
    for i in range(ligne):

        for j in range(colonne):

            pixel = img.getpixel((j,i))

    # filtrage couleur - filtre bleu

            p = (0,0,pixel[1])

            imgneww.putpixel((j,i), p)
    imgneww.show()
    clear()
    initialisation()


def filtreviolet(img):
    
    for i in range(ligne):

        for j in range(colonne):

            pixel = img.getpixel((j,i))

    # filtrage couleur - filtre violet

            p = (pixel[1],0,pixel[1])

            imgneww.putpixel((j,i), p)
    imgneww.show()
    clear()
    initialisation()


def filtrejaune(img):
    
    for i in range(ligne):

        for j in range(colonne):

            pixel = img.getpixel((j,i))

    # filtrage couleur - filtre jaune

            p = (pixel[1],pixel[1],0)

            imgneww.putpixel((j,i), p)
    imgneww.show()
    clear()
    initialisation()



def filtreturquoise(img):
    
    for i in range(ligne):

        for j in range(colonne):

            pixel = img.getpixel((j,i))

    # filtrage couleur - filtre turquoise

            p = (0,pixel[1],pixel[1])

            imgneww.putpixel((j,i), p)
    imgneww.show()
    clear()
    initialisation()


def filtreorange(img):
    
    for i in range(ligne):

        for j in range(colonne):

            pixel = img.getpixel((j,i))

    # filtrage couleur - filtre orangé

            p = (pixel[2],pixel[-3],-2)

            imgneww.putpixel((j,i), p)
    imgneww.show()
    clear()
    initialisation()
  
  
  
#on lance la fonction.. Pour arrêter, il faut faire 9 avec le system exit
initialisation()
  
