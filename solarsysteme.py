import turtle
import math

# Initialisation de l'écran
screen = turtle.Screen()
screen.bgcolor("black")

def dessiner_corps_celeste(forme, couleur, taille):
    corps_celeste = turtle.Turtle()
    corps_celeste.shape(forme)
    corps_celeste.color(couleur)
    corps_celeste.shapesize(taille)
    return corps_celeste

def mouvement_orbital(corps_celeste, distance, vitesse_rotation):
    angle = 0
    while True:
        x = distance * math.cos(angle)
        y = distance * math.sin(angle)
        corps_celeste.setpos(x, y)
        angle += vitesse_rotation

# Soleil
soleil = dessiner_corps_celeste("circle", "yellow", 5)

# Terre
terre = dessiner_corps_celeste("circle", "blue", 2)
distance_terre_soleil = 150
terre.penup()
terre.goto(distance_terre_soleil, 0)
terre.pendown()

# Lune
lune_terre_distance = 30
lune = dessiner_corps_celeste("circle", "white", 0.7)
lune.penup()
lune.goto(distance_terre_soleil + lune_terre_distance, 0)
lune.pendown()

# Mouvement orbital
while True:
    mouvement_orbital(terre, distance_terre_soleil, 0.01)
    
    # Mise à jour de la position de la Lune par rapport à la Terre
    x_terre, y_terre = terre.position()
    lune.setpos(x_terre + lune_terre_distance * math.cos(lune.heading()),
                y_terre + lune_terre_distance * math.sin(lune.heading()))
    
    mouvement_orbital(lune, lune_terre_distance, 0.1)
    
    # Réinitialisation pour empêcher la perte de performance
    terre.clear()
    lune.clear()
