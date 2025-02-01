import pygame
import random


pygame.init()
pygame.display.set_caption("boule que se repliquent")


WHIDTH, HEIGHT = 800, 800
FPS = 60
WHITE = ((255, 255, 255))
RED = ((159, 0, 0))
GREEN = ((0, 150, 75))
BLUE = ((0, 0, 100))
BLACK = ((0, 0, 0))



screen = pygame.display.set_mode((WHIDTH, HEIGHT))

liste_vitesse_x = []
liste_vitesse_y = []
liste_couleurs = []
liste_positions = []

choix1 = random.choice([True, False])
if choix1 == True:
    choix2 = random.randint(0, 495)/100
    liste_vitesse_x.append(choix2)
    liste_vitesse_y.append(5-choix2)
elif choix1 == False:
    choix2 = random.randint(0, 495)/100
    liste_vitesse_x.append(-choix2)
    liste_vitesse_y.append(-(5-choix2))

color = random.choice([GREEN, RED, BLUE, WHITE])
liste_couleurs.append(color)
liste_positions.append([400, 400])
def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        global liste_positions, liste_vitesse_x, liste_vitesse_y, liste_couleurs
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        screen.fill(BLACK)


        for i in range(len(liste_positions)):
            liste_positions[i][0] += liste_vitesse_x[i]
            liste_positions[i][1] += liste_vitesse_y[i]
            pygame.draw.circle(screen, liste_couleurs[i], (liste_positions[i][0], liste_positions[i][1]), 20)
        for i in range(len(liste_positions)):
            if liste_positions[i][0] > 800 or liste_positions[i][0] < 0: 
                n = random.randint(-50, 50)/100
                liste_vitesse_x[i] = -liste_vitesse_x[i]+n
                liste_vitesse_y[i] = -liste_vitesse_y[i]-n
                if liste_positions[i][0] > 800:
                    liste_positions[i][0] = 795
                elif liste_positions[i][0] < 0:
                    liste_positions[i][0] = 5
                color = random.choice([GREEN, RED, BLUE, WHITE])
                liste_couleurs.append(color)
                liste_positions.append([liste_positions[i][0], liste_positions[i][1]])
                liste_vitesse_x.append(liste_vitesse_x[i]*(random.randint(50, 150)  /100))
                liste_vitesse_y.append(-liste_vitesse_y[i]*(random.randint(50, 150) / 100))
            elif liste_positions[i][1] < 0 or liste_positions[i][1] > 800: 
                n = random.randint(-50, 50)/100
                liste_vitesse_x[i] = -liste_vitesse_x[i]+n
                liste_vitesse_y[i] = -liste_vitesse_y[i]-n
                if liste_positions[i][1] > 800:
                    liste_positions[i][1] = 795
                elif liste_positions[i][1] < 0:
                    liste_positions[i][1] = 5
                color = random.choice([GREEN, RED, BLUE, WHITE])
                liste_couleurs.append(color)
                liste_positions.append([liste_positions[i][0], liste_positions[i][1]])
                liste_vitesse_x.append(-liste_vitesse_x[i]*(random.randint(50, 150) / 100))
                liste_vitesse_y.append(liste_vitesse_y[i]*(random.randint(50, 150) / 100))

        if len(liste_positions) > 5000:
            liste_positions = []
            liste_couleurs = []
            liste_vitesse_x = []
            liste_vitesse_y = []
            liste_couleurs.append(random.choice([RED, WHITE, BLUE, GREEN]))
            liste_positions.append([400, 400])
            n = random.randint(-495, 495)/100
            if n > 0:
                liste_vitesse_x.append(n)
                liste_vitesse_y.append(5-n)
            elif n < 0:
                liste_vitesse_x.append(n)
                liste_vitesse_y.append(-(5-n))

        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()