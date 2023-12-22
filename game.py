from tkinter import *
import pygame



#Creation de la fenêtre
width = 1088
height = 448
window=Tk()
window.configure(bg="#000000")
window.title("CRACKLANDERS")
window.geometry(f'{str(width)}x{str(height)}')

#Zone de dessin
can1=Canvas(window, bg="#000000",width=64*23 , height=64*35)

#Info
canArgent=Canvas(window,bg="#00F3FF",borderwidth="3",highlightthickness="0" , relief="ridge", width=100 , height=50)

canMission=Canvas(window,bg="#DBDBDB",borderwidth="3",highlightthickness="0" , relief="ridge", width=300 , height=50)

canTouche=Canvas(window,bg="#FFA118",borderwidth="3",highlightthickness="0" , relief="ridge",width=50 , height=50)

data = {}




toucheDico = {}
with open("touche.txt", "r") as f:
    for i in f.read().splitlines():
        toucheDico[i.split(":")[0]] = i.split(":")[1]

################################FONCTIONS DU MENU#############################
def playFonc():
    click_sound.play()
    maingroup.pack_forget()
    startFrame.pack(expand=YES)
    returnButton.place(x=0, y=0)

def toucheFonc():
    click_sound.play()
    global fond2
    maingroup.pack_forget()
    fond.delete(fond1)
    fond.delete(fond3)
    fond2 = fond.create_image(0, 0, image=imgFond2, anchor=NW)
    boxTouche.pack(expand=YES) 
    returnButton.place(x=0, y=0)



###########################################MUSIQUE###########################################
pygame.init()
son_intro = pygame.mixer.Sound("sons/son-intro.ogg")

son_ingame = pygame.mixer.Sound("sons/son-ingame.ogg")

course_poursuite = pygame.mixer.Sound("sons/course-poursuite.ogg")

bruitage_derapage = pygame.mixer.Sound("sons/bruitage-derapage.ogg")

sirene_police = pygame.mixer.Sound("sons/sirene-police.ogg")

collect_coin = pygame.mixer.Sound("sons/sound-effect-coin.ogg")

end_song = pygame.mixer.Sound("sons/end-song.ogg")

destruction_sound = pygame.mixer.Sound("sons/destruction.ogg")
destruction_sound.set_volume(0.3)

click_sound = pygame.mixer.Sound("sons/click-sound.ogg")
click_sound.set_volume(0.3)

#pygame.mixer.pause()

son_intro.play(-1, 0, 1000)

#######################################NOUVELLE PARTIE/CONTINUER LA PARTIE#######################################
def newgame():
    click_sound.play()
    startFrame.pack_forget()
    returnButton.place_forget()
    fond.delete(fond1)
    ecranCinematique()
    click_sound.play()
    son_intro.stop()
    course_poursuite.play(0, 0, 1000)



#RETOUR
def retour1():
    returnButton.place_forget()
    startFrame.pack_forget()
    boxTouche.pack_forget()
    fond.delete(fond2)
    fond.create_image(0, 0, image=imgFond1, anchor=NW)

    click_sound.play()
    maingroup.pack(expand=YES)


#TOUCHE FONCTION
def toucheSelect(event):
    click_sound.play()
    touchePress = event.keysym
    listTouche[numTouche]['text'] = touchePress
    fond.unbind('<Key>')
    toucheFonc()

    toucheDico['monter']=touche1.cget('text')
    toucheDico['descendre']=touche2.cget('text')
    toucheDico['gauche']=touche3.cget('text')
    toucheDico['droite'] = touche4.cget('text')
    toucheDico['interaction']=touche5.cget('text')
    toucheDico['ramasser']=touche6.cget('text')
    with open("touche.txt", "w") as f:
        for k in toucheDico.keys():
            f.write(f"{k}:{toucheDico[k]}\n")



numTouche = 0
def touche1():
    click_sound.play()
    global numTouche
    touche1['text']="?"
    fond.delete(fond2)
    fond.create_image(0, 0, image=imgFond3, anchor=NW)
    returnButton.place_forget()
    numTouche = touche1.grid_info()['row']
    fond.focus_set()
    fond.bind('<Key>', toucheSelect)

def touche2():
    click_sound.play()
    global numTouche
    touche2['text']="?"
    fond.delete(fond2)
    fond.create_image(0, 0, image=imgFond3, anchor=NW)
    returnButton.place_forget()
    numTouche = touche2.grid_info()['row']
    fond.focus_set()
    fond.bind('<Key>', toucheSelect)

def touche3():
    click_sound.play()
    global numTouche
    touche3['text']="?"
    fond.delete(fond2)
    fond.create_image(0, 0, image=imgFond3, anchor=NW)
    returnButton.place_forget()
    numTouche = touche3.grid_info()['row']
    fond.focus_set()
    fond.bind('<Key>', toucheSelect)

def touche4():
    click_sound.play()
    global numTouche
    touche4['text']="?"
    fond.delete(fond2)
    fond.create_image(0, 0, image=imgFond3, anchor=NW)
    returnButton.place_forget()
    numTouche = touche4.grid_info()['row']
    fond.focus_set()
    fond.bind('<Key>', toucheSelect)

def touche5():
    click_sound.play()
    global numTouche
    touche5['text']="?"
    fond.delete(fond2)
    fond.create_image(0, 0, image=imgFond3, anchor=NW)
    returnButton.place_forget()
    numTouche = touche5.grid_info()['row']
    fond.focus_set()
    fond.bind('<Key>', toucheSelect)

def touche6():
    click_sound.play()
    global numTouche
    touche6['text']="?"
    fond.delete(fond2)
    fond.create_image(0, 0, image=imgFond3, anchor=NW)
    returnButton.place_forget()
    numTouche = touche6.grid_info()['row']
    fond.focus_set()
    fond.bind('<Key>', toucheSelect)

def touche7():
    click_sound.play()
    global numTouche
    touche7['text']="?"
    fond.delete(fond2)
    fond.create_image(0, 0, image=imgFond3, anchor=NW)
    returnButton.place_forget()
    numTouche = touche7.grid_info()['row']
    fond.focus_set()
    fond.bind('<Key>', toucheSelect)




###################################Ecran d'accueil##################################


imgFond1 = PhotoImage(file="textures/background/main.png")
imgFond2 = PhotoImage(file="textures/background/touches1.png")
imgFond3 = PhotoImage(file="textures/background/touches2.png")

fond = Canvas(window, width=1088, height=448, bg="#000000", highlightthickness=0)
fond.place(x=0, y=0)
fond1 = fond.create_image(0, 0, image=imgFond1, anchor=NW)
fond2 = 0
fond3 = 0
########################

maingroup = Frame(window, bg="red")

playButton1 = Button(maingroup, text="Jouer", bg="#D2D2D2", fg="black", relief="groove", width=10, font=("Constantia", 24), command=playFonc)
toucheSettingsButton = Button(maingroup, text="Touches", bg="#D2D2D2", fg="black", relief="groove",width=10,font=("Constantia", 24), command=toucheFonc)
leaveButton = Button(maingroup, text="Quitter", bg="#FF0000", fg="white", relief="groove",width=10,font=("Constantia", 24), command=window.quit)

playButton1.grid(row=0)
toucheSettingsButton.grid(row=1)
leaveButton.grid(row=2)
maingroup.pack(expand=YES)


#############################
startFrame = Frame(window, bg="red")
#loadSaveButton = Button(startFrame, text="(INDISPONIBLE)", bg="#FF0000", fg="black", relief="groove", width=18, font=("Constantia", 18))
newSaveButton = Button(startFrame, text="LANCER LA PARTIE", bg="#D2D2D2", fg="black", relief="groove", width=18, font=("Constantia", 18), command=newgame)

#loadSaveButton.grid(row=0)
newSaveButton.grid(row=1)



#########################TOUCHES###########################
textTouche = Label(window, text="YO")
boxTouche = Frame(window, bg="red")
monter = Button(boxTouche, text="Monter", relief="ridge", bg="#00D8FE", font=("Constantia", 14))
descendre = Button(boxTouche, text="Descendre", relief="ridge", bg="#00D8FE", font=("Constantia", 14))
gauche = Button(boxTouche, text="Gauche", relief="ridge", bg="#00D8FE", font=("Constantia", 14))
droite = Button(boxTouche, text="Droite", relief="ridge", bg="#00D8FE", font=("Constantia", 14))
interaction = Button(boxTouche, text="Interaction", relief="ridge", bg="#00D8FE", font=("Constantia", 14))
ramasser = Button(boxTouche, text="Ramasser", relief="ridge", bg="#00D8FE", font=("Constantia", 14))
pompe = Button(boxTouche, text="Pompe", relief="ridge", bg="#00D8FE", font=("Constantia", 14))

listNomTouche = [monter, descendre, gauche, droite, interaction, ramasser, pompe]







touche1 = Button(boxTouche, text=toucheDico['monter'], bd=2,relief="groove", font=("Constantia", 14), command=touche1)
touche2 = Button(boxTouche, text=toucheDico['descendre'], bd=2,relief="groove", font=("Constantia", 14), command=touche2)
touche3 = Button(boxTouche, text=toucheDico['gauche'], bd=2,relief="groove", font=("Constantia", 14), command=touche3)
touche4 = Button(boxTouche, text=toucheDico['droite'], bd=2,relief="groove", font=("Constantia", 14), command=touche4)
touche5 = Button(boxTouche, text=toucheDico['interaction'], bd=2,relief="groove", font=("Constantia", 14), command=touche5)
touche6 = Button(boxTouche, text=toucheDico['ramasser'], bd=2,relief="groove", font=("Constantia", 14), command=touche6)
touche7 = Button(boxTouche, text=toucheDico['pompe'], bd=2,relief="groove", font=("Constantia", 14), command=touche7)
listTouche = [touche1, touche2, touche3, touche4, touche5, touche6, touche7]

for i in range(len(listTouche)):
    listTouche[i].grid(column=1, row=i, sticky=EW)
    listNomTouche[i].grid(column=0, row=i, sticky=EW)




returnButton = Button(window, text="Retour", bg="#FF0000",fg="white",relief="groove", highlightthickness=0,  height=1, font=("Caladea", 16), command=retour1)



#Mur intérieur
mur_coin1 = PhotoImage(file="textures/murs_interieurs/mur_coin1.gif")
mur_coin2 = PhotoImage(file="textures/murs_interieurs/mur_coin2.gif")
mur_coin3 = PhotoImage(file="textures/murs_interieurs/mur_coin3.gif")
mur_coin4 = PhotoImage(file="textures/murs_interieurs/mur_coin4.gif")
mur1 = PhotoImage(file="textures/murs_interieurs/mur1.gif")
mur2 = PhotoImage(file="textures/murs_interieurs/mur2.gif")
mur_intersection1 = PhotoImage(file="textures/murs_interieurs/mur_intersection1.gif")
mur_intersection2 = PhotoImage(file="textures/murs_interieurs/mur_intersection2.gif")
porte1 = PhotoImage(file="textures/murs_interieurs/porte1.gif")
porte1verticale = PhotoImage(file="textures/murs_interieurs/porte1verticale.gif")
porte2 = PhotoImage(file="textures/murs_interieurs/porte2.gif")

#mur exterieur
murExterieur1A = PhotoImage(file="textures/murs_exterieurs/exterieur1A.gif")
murExterieur1B = PhotoImage(file="textures/murs_exterieurs/exterieur1B.gif")
murExterieur2 = PhotoImage(file="textures/murs_exterieurs/exterieur2.gif")
murExterieur3 = PhotoImage(file="textures/murs_exterieurs/exterieur3.gif")
murExterieur4 = PhotoImage(file="textures/murs_exterieurs/exterieur4.gif")
murExterieur_coin1A = PhotoImage(file="textures/murs_exterieurs/exterieur_coin1A.gif")
murExterieur_coin1B = PhotoImage(file="textures/murs_exterieurs/exterieur_coin1B.gif")
murExterieur_coin2A = PhotoImage(file="textures/murs_exterieurs/exterieur_coin2A.gif")
murExterieur_coin2B = PhotoImage(file="textures/murs_exterieurs/exterieur_coin2B.gif")
murExterieur_coin3 = PhotoImage(file="textures/murs_exterieurs/exterieur_coin3.gif")
murExterieur_coin4 = PhotoImage(file="textures/murs_exterieurs/exterieur_coin4.gif")
sortie1 = PhotoImage(file="textures/murs_exterieurs/sortie1.gif")
sortie2 = PhotoImage(file="textures/murs_exterieurs/sortie2.gif")
sortie3 = PhotoImage(file="textures/murs_exterieurs/sortie3.gif")
sortie4 = PhotoImage(file="textures/murs_exterieurs/sortie4.gif")



#PERSONNAGE
prisonnier_b1 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_b1.gif")
prisonnier_b2 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_b2.gif")
prisonnier_d1 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_d1.gif")
prisonnier_d2 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_d2.gif")
prisonnier_d3 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_d3.gif")
prisonnier_g1 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_g1.gif")
prisonnier_g2 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_g2.gif")
prisonnier_g3 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_g3.gif")
prisonnier_h1 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_h1.gif")
prisonnier_h2 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_h2.gif")
prisonnier_immobile1 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_immobile1.gif")
prisonnier_immobile2 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_immobile2.gif")
prisonnier_immobile3 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_immobile3.gif")
prisonnier_immobile4 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_immobile4.gif")
prisonnier_pompe1 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_pompe1.gif")
prisonnier_pompe2 = PhotoImage(file="textures/personnage/prisonnier/prisonnier_pompe2.gif")


prisonnierpolice_b1 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_b1.gif")
prisonnierpolice_b2 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_b2.gif")
prisonnierpolice_d1 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_d1.gif")
prisonnierpolice_d2 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_d2.gif")
prisonnierpolice_d3 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_d3.gif")
prisonnierpolice_g1 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_g1.gif")
prisonnierpolice_g2 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_g2.gif")
prisonnierpolice_g3 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_g3.gif")
prisonnierpolice_h1 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_h1.gif")
prisonnierpolice_h2 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_h2.gif")
prisonnierpolice_immobile1 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_immobile1.gif")
prisonnierpolice_immobile2 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_immobile2.gif")
prisonnierpolice_immobile3 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_immobile3.gif")
prisonnierpolice_immobile4 = PhotoImage(file="textures/personnage/prisonniertenuepolicier/prisonnierpolice_immobile4.gif")



francois_b1 = PhotoImage(file="textures/personnage/francois/francois_b1.gif")
francois_b2 = PhotoImage(file="textures/personnage/francois/francois_b2.gif")
francois_d1 = PhotoImage(file="textures/personnage/francois/francois_d1.gif")
francois_d2 = PhotoImage(file="textures/personnage/francois/francois_d2.gif")
francois_d3 = PhotoImage(file="textures/personnage/francois/francois_d3.gif")
francois_g1 = PhotoImage(file="textures/personnage/francois/francois_g1.gif")
francois_g2 = PhotoImage(file="textures/personnage/francois/francois_g2.gif")
francois_g3 = PhotoImage(file="textures/personnage/francois/francois_g3.gif")
francois_h1 = PhotoImage(file="textures/personnage/francois/francois_h1.gif")
francois_h2 = PhotoImage(file="textures/personnage/francois/francois_h2.gif")
francois_immobile1 = PhotoImage(file="textures/personnage/francois/francois_immobile1.gif")
francois_immobile2 = PhotoImage(file="textures/personnage/francois/francois_immobile2.gif")
francois_immobile3 = PhotoImage(file="textures/personnage/francois/francois_immobile3.gif")
francois_immobile4 = PhotoImage(file="textures/personnage/francois/francois_immobile4.gif")

policier_b1 = PhotoImage(file="textures/personnage/policier/policier_b1.gif")
policier_b2 = PhotoImage(file="textures/personnage/policier/policier_b2.gif")
policier_d1 = PhotoImage(file="textures/personnage/policier/policier_d1.gif")
policier_d2 = PhotoImage(file="textures/personnage/policier/policier_d2.gif")
policier_d3 = PhotoImage(file="textures/personnage/policier/policier_d3.gif")
policier_g1 = PhotoImage(file="textures/personnage/policier/policier_g1.gif")
policier_g2 = PhotoImage(file="textures/personnage/policier/policier_g2.gif")
policier_g3 = PhotoImage(file="textures/personnage/policier/policier_g3.gif")
policier_h1 = PhotoImage(file="textures/personnage/policier/policier_h1.gif")
policier_h2 = PhotoImage(file="textures/personnage/policier/policier_h2.gif")
policier_immobile1 = PhotoImage(file="textures/personnage/policier/policier_immobile1.gif")
policier_immobile2 = PhotoImage(file="textures/personnage/policier/policier_immobile2.gif")
policier_immobile3 = PhotoImage(file="textures/personnage/policier/policier_immobile3.gif")
policier_immobile4 = PhotoImage(file="textures/personnage/policier/policier_immobile4.gif")

jimmy_b1 = PhotoImage(file="textures/personnage/jimmy/jimmy_b1.gif")
jimmy_b2 = PhotoImage(file="textures/personnage/jimmy/jimmy_b2.gif")
jimmy_d1 = PhotoImage(file="textures/personnage/jimmy/jimmy_d1.gif")
jimmy_d2 = PhotoImage(file="textures/personnage/jimmy/jimmy_d2.gif")
jimmy_d3 = PhotoImage(file="textures/personnage/jimmy/jimmy_d3.gif")
jimmy_g1 = PhotoImage(file="textures/personnage/jimmy/jimmy_g1.gif")
jimmy_g2 = PhotoImage(file="textures/personnage/jimmy/jimmy_g2.gif")
jimmy_g3 = PhotoImage(file="textures/personnage/jimmy/jimmy_g3.gif")
jimmy_h1 = PhotoImage(file="textures/personnage/jimmy/jimmy_h1.gif")
jimmy_h2 = PhotoImage(file="textures/personnage/jimmy/jimmy_h2.gif")
jimmy_immobile1 = PhotoImage(file="textures/personnage/jimmy/jimmy_immobile1.gif")
jimmy_immobile2 = PhotoImage(file="textures/personnage/jimmy/jimmy_immobile2.gif")
jimmy_immobile3 = PhotoImage(file="textures/personnage/jimmy/jimmy_immobile3.gif")
jimmy_immobile4 = PhotoImage(file="textures/personnage/jimmy/jimmy_immobile4.gif")
jimmy_dort = PhotoImage(file="textures/personnage/jimmy/jimmy_dort.gif")

mamadou_b1 = PhotoImage(file="textures/personnage/mamadou/mamadou_b1.gif")
mamadou_b2 = PhotoImage(file="textures/personnage/mamadou/mamadou_b2.gif")
mamadou_d1 = PhotoImage(file="textures/personnage/mamadou/mamadou_d1.gif")
mamadou_d2 = PhotoImage(file="textures/personnage/mamadou/mamadou_d2.gif")
mamadou_d3 = PhotoImage(file="textures/personnage/mamadou/mamadou_d3.gif")
mamadou_g1 = PhotoImage(file="textures/personnage/mamadou/mamadou_g1.gif")
mamadou_g2 = PhotoImage(file="textures/personnage/mamadou/mamadou_g2.gif")
mamadou_g3 = PhotoImage(file="textures/personnage/mamadou/mamadou_g3.gif")
mamadou_h1 = PhotoImage(file="textures/personnage/mamadou/mamadou_h1.gif")
mamadou_h2 = PhotoImage(file="textures/personnage/mamadou/mamadou_h2.gif")
mamadou_immobile1 = PhotoImage(file="textures/personnage/mamadou/mamadou_immobile1.gif")
mamadou_immobile2 = PhotoImage(file="textures/personnage/mamadou/mamadou_immobile2.gif")
mamadou_immobile3 = PhotoImage(file="textures/personnage/mamadou/mamadou_immobile3.gif")
mamadou_immobile4 = PhotoImage(file="textures/personnage/mamadou/mamadou_immobile4.gif")

#SOL
solPrison = PhotoImage(file="textures/cellules/sol.png")
solPrisonBillets = PhotoImage(file="textures/billets.png")
liasse = PhotoImage(file="textures/liasse.gif")

herbe = PhotoImage(file="textures/herbe.gif")

#OBJETS
lit = PhotoImage(file="textures/cellules/lit.gif")
wc = PhotoImage(file="textures/cellules/toilettes.gif")



#CASES ACTIONS
interactionMamadou = PhotoImage(file="textures/cellules/sol.png")
interactionPorte = PhotoImage(file="textures/cellules/sol.png")
interactionFrancois = PhotoImage(file="textures/cellules/sol.png")
interactionPolicier = PhotoImage(file="textures/herbe.gif")
enterPrison = PhotoImage(file="textures/herbe.gif")


#ROUTES
route1 = PhotoImage(file="textures/texturesroute/route1.gif")
route2 = PhotoImage(file="textures/texturesroute/route2.gif")
barriere = PhotoImage(file="textures/texturesroute/barriere.gif")
bordure1 = PhotoImage(file="textures/texturesroute/bordure1.gif")
bordure2 = PhotoImage(file="textures/texturesroute/bordure2.gif")
buisson = PhotoImage(file="textures/texturesroute/buisson.gif")
rocher = PhotoImage(file="textures/texturesroute/rocher.gif")
herbe2 = PhotoImage(file="textures/emprisonnement/herbe.gif")


#VEHICULES
carTexture = PhotoImage(file="textures/vehicules/car.gif")
police1texture = PhotoImage(file="textures/vehicules/police1.gif")
police2texture = PhotoImage(file="textures/vehicules/police2.gif")

frontPoliceCar = PhotoImage(file="textures/vehicules/frontPoliceCar.gif")
backPoliceCar = PhotoImage(file="textures/vehicules/backPoliceCar.gif")

#PNJ
pnj1 = PhotoImage(file="textures/personnage/PNJ/pnj1.gif")

#PRISON EXTERIEUR
lumiere1 = PhotoImage(file="textures/emprisonnement/lumiere1.gif")
lumiere2 = PhotoImage(file="textures/emprisonnement/lumiere2.gif")
prison_centre = PhotoImage(file="textures/emprisonnement/prison_centre.gif")
prison_coin1 = PhotoImage(file="textures/emprisonnement/prison_coin1.gif")
prison_coin2 = PhotoImage(file="textures/emprisonnement/prison_coin2.gif")
prison_coin3 = PhotoImage(file="textures/emprisonnement/prison_coin3.gif")
prison_coin4 = PhotoImage(file="textures/emprisonnement/prison_coin4.gif")
prison1 = PhotoImage(file="textures/emprisonnement/prison1.gif")
prison2 = PhotoImage(file="textures/emprisonnement/prison2.gif")
prison3 = PhotoImage(file="textures/emprisonnement/prison3.gif")
prison4 = PhotoImage(file="textures/emprisonnement/prison4.gif")
rebord1 = PhotoImage(file="textures/emprisonnement/rebord1.gif")
rebord2 = PhotoImage(file="textures/emprisonnement/rebord2.gif")


#CANTINE
cantine1 = PhotoImage(file="textures/cantine/cantine1.gif")
cantine2 = PhotoImage(file="textures/cantine/cantine2.gif")
cantine3 = PhotoImage(file="textures/cantine/cantine3.gif")
cantine4 = PhotoImage(file="textures/cantine/cantine4.gif")
cantine5 = PhotoImage(file="textures/cantine/cantine5.gif")
cantine6 = PhotoImage(file="textures/cantine/cantine6.gif")
cantine7 = PhotoImage(file="textures/cantine/cantine7.gif")
cantine8 = PhotoImage(file="textures/cantine/cantine8.gif")
cantine9 = PhotoImage(file="textures/cantine/cantine9.gif")
chaise1 = PhotoImage(file="textures/cantine/chaise1.gif")
chaise2 = PhotoImage(file="textures/cantine/chaise2.gif")
lumiereUnlock = PhotoImage(file="textures/cantine/lumiere.gif")
lumiereLock = PhotoImage(file="textures/cantine/lumiererouge.gif")
paillasson_cantine = PhotoImage(file="textures/cantine/paillasson_cantine.gif")
solcantine = PhotoImage(file="textures/cantine/solcantine.gif")
table1 = PhotoImage(file="textures/cantine/table1.gif")
table2 = PhotoImage(file="textures/cantine/table2.gif")

#BUREAU DE POLICE
bureau1 = PhotoImage(file="textures/bureaudepolice/bureau1.gif")
bureau2 = PhotoImage(file="textures/bureaudepolice/bureau2.gif")
bureau3 = PhotoImage(file="textures/bureaudepolice/bureau3.gif")
bureaudepolice1 = PhotoImage(file="textures/bureaudepolice/bureaudepolice1.gif")
bureaudepolice2 = PhotoImage(file="textures/bureaudepolice/bureaudepolice2.gif")
bureaudepolice3 = PhotoImage(file="textures/bureaudepolice/bureaudepolice3.gif")
bureaudepolice4 = PhotoImage(file="textures/bureaudepolice/bureaudepolice4.gif")
bureaudepolice5 = PhotoImage(file="textures/bureaudepolice/bureaudepolice5.gif")
bureaudepolice6 = PhotoImage(file="textures/bureaudepolice/bureaudepolice6.gif")
chaisebureau = PhotoImage(file="textures/bureaudepolice/chaisebureau.gif")
paillasson_bureau = PhotoImage(file="textures/bureaudepolice/paillasson_bureau.gif")
solbureau = PhotoImage(file="textures/bureaudepolice/solbureau.gif")
tenuepolicier = PhotoImage(file="textures/bureaudepolice/tenuepolicier.gif")

#PORTAIL
portail1 = PhotoImage(file="textures/PORTAIL/portail1.gif")
portail2 = PhotoImage(file="textures/PORTAIL/portail2.gif")
portail3 = PhotoImage(file="textures/PORTAIL/portail3.gif")
portail4 = PhotoImage(file="textures/PORTAIL/portail4.gif")
portail5 = PhotoImage(file="textures/PORTAIL/portail5.gif")
portail6 = PhotoImage(file="textures/PORTAIL/portail6.gif")
portail7 = PhotoImage(file="textures/PORTAIL/portail7.gif")
portail8 = PhotoImage(file="textures/PORTAIL/portail8.gif")


txnoir = PhotoImage(file="textures/noir.gif")

#RECUPERATION DE LA SAUVERGARDE
with open("saves.txt", "r") as f:
    for i in f.read().splitlines():
        data[i.split(":")[0]] = i.split(":")[1]

    data["money"] = int(data["money"])
    data["posX"] = int(data["posX"])
    data["posY"] = int(data["posY"])
    posX = data["posX"]
    posY = data["posY"]
    can1x = int(data["can1x"])
    can1y = int(data["can1y"])
    can1.place(x=can1x, y=can1y)
    data["missionMamadou"] = int(data["missionMamadou"])
    data["missionFrancois"] = int(data["missionFrancois"])
    data["key"] = int(data["key"])
    data["tenue"] = int(data["tenue"])
    data['ecranNum'] = int(data['ecranNum'])
    lastMouv = data["lastMouv"]
    # position du personnage
    perso = can1.create_image(posX, posY, image=prisonnier_immobile1, anchor="nw")
    # Interface
    affichageArgent = canArgent.create_text(53, 105 / 4, font=("Times", "20", "bold italic"), text=f"{data['money']}$")
    affichageMission = canMission.create_text(10, 27, font=("Times", "14", "bold italic"), anchor="w",text=f"{data['mission']}")
    affichageTouche = canTouche.create_text(10, 27, font=("Times", "14", "bold italic"), anchor="w",text=f"K")



#création de la map
dico={
    "MCI1__":mur_coin1,
    "MCI2__":mur_coin2,
    "MCI3__":mur_coin3,
    "MCI4__":mur_coin4,
    "MI1___":mur1,
    "MI2___":mur2,
    "INTER1":mur_intersection1,
    "INTER2":mur_intersection2,
    "PORTE1": porte1,
    "PORT1V": porte1verticale,
    "PORTE2": porte2,

    "ME1A__":murExterieur1A,
    "ME1B__":murExterieur1B,
    "ME2___":murExterieur2,
    "ME3___":murExterieur3,
    "ME4___":murExterieur4,
    "MEC1A_":murExterieur_coin1A,
    "MEC1B_":murExterieur_coin1B,
    "MEC2A_":murExterieur_coin2A,
    "MEC2B_":murExterieur_coin2B,
    "MEC3__":murExterieur_coin3,
    "MEC4__":murExterieur_coin4,
    "SORTI1":sortie1,
    "SORTI2":sortie2,
    "SORTI3":sortie3,
    "SORTI4":sortie4,


    "SOLPSN": solPrison,
    "SACB__": solPrisonBillets,
    "LIASSE": liasse,
    "HERBES": herbe,

    "BED___": lit,
    "WC____": wc,


    "I_MAMA": interactionMamadou,
    "IPORTE": interactionPorte,
    "I_FRAN": interactionFrancois,
    "I_POLI": interactionPolicier,
    "ENTERP": enterPrison,
    "DONE__": solPrison,


    "ROUTE1":route1,
    "ROUTE2":route2,
    "BARRER":barriere,
    "HERBE2":herbe2,

    "FRONTC":frontPoliceCar,
    "BACKC_":backPoliceCar,
    "PNJ1__":pnj1,
    "LUMEX1":lumiere1,
    "LUMEX2":lumiere2,
    "PSNCEN":prison_centre,
    "PSNCN1":prison_coin1,
    "PSNCN2": prison_coin2,
    "PSNCN3": prison_coin3,
    "PSNCN4": prison_coin4,
    "PRISO1": prison1,
    "PRISO2": prison2,
    "PRISO3": prison3,
    "PRISO4": prison4,
    "REBOR1": rebord1,
    "REBOR2": rebord2,

    "CANTI1": cantine1,
    "CANTI2": cantine2,
    "CANTI3": cantine3,
    "CANTI4": cantine4,
    "CANTI5": cantine5,
    "CANTI6": cantine6,
    "CANTI7": cantine7,
    "CANTI8": cantine8,
    "CANTI9": cantine9,
    "CHAIS1": chaise1,
    "CHAIS2": chaise2,
    "LUMPO1": lumiereUnlock,
    "LUMPO2": lumiereUnlock,
    "LULOCK": lumiereLock,
    "TAPISC": paillasson_cantine,
    "SOLCTN": solcantine,
    "TABLE1": table1,
    "TABLE2": table2,

    "DESK1_": bureau1,
    "DESK2_": bureau2,
    "DESK3_": bureau3,

    "PORTA1": portail1,
    "PORTA2": portail2,
    "PORTA3": portail3,
    "PORTA4": portail4,
    "PORTA5": portail5,
    "PORTA6": portail6,
    "PORTA7": portail7,
    "PORTA8": portail8,


    "EXTPO1": bureaudepolice1,
    "EXTPO2": bureaudepolice2,
    "EXTPO3": bureaudepolice3,
    "EXTPO4": bureaudepolice4,
    "EXTPO5": bureaudepolice5,
    "EXTPO6": bureaudepolice6,
    "DESKCH": chaisebureau,
    "TAPISB": paillasson_bureau,
    "SOLDSK": solbureau,
    "CLOTHS": tenuepolicier,
    "BORD1_": bordure1,
    "BORD2_": bordure2,
    "BUISON": buisson,
    "ROCHER": rocher,
    "TXNOIR": txnoir,




}


L0 = []
L1 = []
L2 = []
L3 = []
L4 = []
L5 = []
L6 = []
L7 = []
L8 = []
L9 = []
L10 = []
L11 = []
L12 = []
L13 = []
L14 = []
L15 = []
L16 = []
L17 = []
L18 = []
L19 = []
L20 = []
L21 = []
L22 = []
L23 = []
L24 = []
L25 = []
L26 = []
L27 = []
L28 = []
L29 = []
L30 = []
L31 = []
L32 = []
L33 = []
L34 = []
L35 = []
L36 = []
L37 = []
L38 = []
L39 = []
L40 = []


ma_matrice_fixe = [L0, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, L13, L14,L15,L16,L17,L18,L19,L20, L21, L22, L23, L24,L25,L26,L27,L28,L29,L30,L31,L32,L33, L34, L35, L36, L37, L38, L39, L40]

ma_matrice = []


def lastMouvFonction():
    global perso
    """Cette fonction remet le personnage au premier plan lors de la création d'un image sur lui."""
    can1.delete(perso)
    if lastMouv == "up":
        perso = can1.create_image(posX, posY, image=prisonnier_immobile3, anchor="nw")
    elif lastMouv == "down":
        perso = can1.create_image(posX, posY, image=prisonnier_immobile1, anchor="nw")
    elif lastMouv == "left":
        perso = can1.create_image(posX, posY, image=prisonnier_immobile4, anchor="nw")
    elif lastMouv == "right":
        perso = can1.create_image(posX, posY, image=prisonnier_immobile2, anchor="nw")



interdites = ["MCI1__","MCI2__","MCI3__","MCI4__","MI1___","MI2___","ME1A__","ME1B__","I_MAMA","I_FRAN",
              "ME2___","ME3___","ME4___","MEC1A_","MEC1B_","MEC2A_","MEC2B_","MEC3__","MEC4__", "PORTE1", "INTER1", "INTER2",
              "FRONTC", "BACKC_", "PORT1V","BARRER","PNJ1__","PSNCEN","PSNCN1", "PSNCN2", "PSNCN3", "PSNCN4", "PRISO1"
              , "PRISO2", "PRISO3", "PRISO4", "REBOR1", "REBOR2", "CANTI1", "CANTI2", "CANTI3", "CANTI4", "CANTI5", "CANTI6"
              , "CANTI7", "CANTI8", "CANTI9", "TABLE1", "TABLE2", "DESK1_", "DESK2_", "DESK3_", "EXTPO1", "EXTPO2", "EXTPO3"
              , "EXTPO4", "EXTPO5", "EXTPO6", "TXNOIR", "DONE__", "I_POLI", "PORTA1", "PORTA2", "PORTA3", "PORTA4", "PORTA5"
              , "PORTA6", "PORTA7", "PORTA8", "BORD1_", "BORD2_"]


def createMatrice(name):
    global ma_matrice, can1, canArgent, canMission, canTouche,affichageArgent, affichageMission, affichageTouche, bot_mamadou, bot_jimmy, bot_francois, bot_policier
    ma_matrice = ma_matrice_fixe
    compteur = 0

    with open(f"map/{name}.txt", "r") as f:
        for i in f.read().splitlines():
            ma_matrice[compteur] = i.split(',')
            compteur += 1

    can1.destroy()
    canArgent.delete(affichageArgent)
    canArgent.destroy()
    canMission.delete(affichageMission)
    canMission.destroy()
    canTouche.delete(affichageTouche)
    canTouche.destroy()
    can1 = Canvas(window, bg="#000", width=64*int(f"{len(ma_matrice[0])}") , height=64*int(f"{len(ma_matrice)}"), highlightthickness=0)
    can1.place(x=can1x, y=can1y)
    lastMouvFonction()



    for i in ma_matrice:
        if i == []:

            ma_matrice.remove(i)

    for i in range(len(ma_matrice)):  # on se place sur chacune des lignes
        for j in range(len(ma_matrice[i])):  # une fois sur la ligne, on la parcours -> colonne par colonne
            lettre = ma_matrice[i][j]
            can1.create_image(64 * j, 64 * i, image=dico[lettre], anchor="nw")  # on recuperere la lettre

    canArgent = Canvas(window, bg="#00F3FF", borderwidth="3", highlightthickness="0", relief="ridge", width=100,height=50)
    canArgent.place(x=width - 100 - 5, y=0)

    canMission = Canvas(window, bg="#DBDBDB", borderwidth="3", highlightthickness="0", relief="ridge", width=300,height=50)
    canMission.place(x=0, y=0)

    canTouche = Canvas(window, bg="#FFA118", borderwidth="3", highlightthickness="0", relief="ridge", width=50,height=50)
    canTouche.place(x=width / 2 -25, y=0)

    affichageArgent = canArgent.create_text(53, 105 / 4, font=("Times", "20", "bold italic"), text=f"{data['money']}$")
    affichageMission = canMission.create_text(10, 27, font=("Times", "14", "bold italic"), anchor="w",text=f"{data['mission']}")
    affichageTouche = canTouche.create_text(20, 28, font=("Times", "14", "bold italic"),fill="white", anchor="w",text="")

    if name=="spawn":
        bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_immobile1, anchor="nw")
        bot_jimmy = can1.create_image(640, 256, image=jimmy_dort, anchor="nw")
        bot_francois = can1.create_image(256, 704, image=francois_immobile1, anchor="nw")
        bot_policier = can1.create_image(768, 1216, image=policier_immobile3, anchor="nw")
        if data['key']==1:
            ma_matrice[960 // 64][896 // 64] = "LUMPO2"
            can1.create_image(896, 960, image=lumiereUnlock, anchor="nw")









#createMatrice('background')










#############################################CINEMATIQUE#############################################
def ecranCinematique():
    global car, ecranAffichage, can1x, can1y, perso, posX, posY, frame
    if data['ecranNum'] == 0:
        fond.delete(ecranAffichage)
        ecranAffichage = fond.create_image(0, 0, image=ecrannoir, anchor=NW)

        data['ecranNum'] += 1
        ecranAffichage = fond.after(3000, ecranCinematique)

    elif data['ecranNum'] == 1:
        fond.delete(ecranAffichage)
        ecranAffichage = fond.create_image(0, 0, image=ecran1, anchor=NW)
        data['ecranNum'] += 1
        fond.after(4000, ecranCinematique)

    elif data['ecranNum'] == 2:
        fond.delete(ecranAffichage)
        ecranAffichage = fond.create_image(0, 0, image=ecran2, anchor=NW)
        data['ecranNum'] += 1
        fond.after(4000, ecranCinematique)

    elif data['ecranNum'] == 3:
        fond.delete(ecranAffichage)
        ecranAffichage = fond.create_image(0, 0, image=ecran3, anchor=NW)
        data['ecranNum'] += 1
        fond.after(4000, ecranCinematique)

    elif data['ecranNum'] == 4:
        fond.delete(ecranAffichage)
        ecranAffichage = fond.create_image(0, 0, image=ecran4, anchor=NW)
        data['ecranNum'] += 1
        createMatrice("route")
        car = can1.create_image(posX, posY, image=carTexture, anchor="nw")
        can1.focus_set()
        can1.bind('<Key>', ClavierVehicule)
        forwardCar()
        gyrophare()
        sirene_police.set_volume(0.2)
        sirene_police.play()

    elif data['ecranNum'] == 5:
        fond.delete(ecranAffichage)
        can1x = 0
        can1y = -1024
        createMatrice("arrestation")
        posXcar = 512
        posYcar = 1216
        can1.delete(car)
        car = can1.create_image(posXcar, posYcar, image=carTexture, anchor="nw")
        can1.create_oval(512 - 206, 1088 - 32, 512, 1088 + 64, fill="#FFE6C3")
        can1.create_text(512 - 106, 1088 + 16, justify="center", font=('Times', '12', 'italic'),text="Vous êtes en état d'arrestation\npour braquage de banque !")
        data['ecranNum'] += 1
        fond.after(5000, ecranCinematique)
    elif data['ecranNum'] == 6:
        can1.destroy()
        canArgent.place_forget()
        canMission.place_forget()
        canTouche.place_forget()
        fond.delete(ecranAffichage)
        ecranAffichage = fond.create_image(0, 0, image=ecran5, anchor=NW)
        data['ecranNum'] += 1
        fond.after(3500, ecranCinematique)
    elif data['ecranNum'] == 7:
        posX = 192
        posY = 256
        can1x = 320
        can1y = -64
        fond.delete(ecranAffichage)
        data['mission']="Rentrez dans la prison."

        data['money']=0
        createMatrice("cheminprison")
        can1.delete(perso)
        perso = can1.create_image(posX, posY, image=prisonnier_immobile2, anchor="nw")
        can1.focus_set()
        can1.bind('<Key>' , Clavier)
    elif data['ecranNum'] == 8:
        can1.unbind('<Key>')
        can1.destroy()
        fond.delete(ecranAffichage)
        canArgent.place_forget()
        canMission.place_forget()
        canTouche.place_forget()
        ecranAffichage = fond.create_image(0, 0, image=debut, anchor=NW)
        fond.after(1000, video1)
    elif data['ecranNum'] == 9:
        fond.delete(ecranAffichage)
        ecranAffichage = fond.create_image(0, 0, image=fin, anchor=NW)
        data['ecranNum'] += 1
        fond.after(2000, ecranCinematique)
    elif data['ecranNum'] == 10:
        son_ingame.play(-1, 0, 0)
        fond.delete(ecranAffichage)
        posX = 384
        posY = 256

        can1x = 128
        can1y = -64
        data['money']=10
        data['mission'] = "Trouvez un moyen de vous échapper."
        createMatrice("spawn")

        can1.focus_set()
        can1.bind('<Key>' , Clavier)

        if data['tenue']==0:
            perso = can1.create_image(posX, posY, image=prisonnier_immobile1, anchor="nw")
        elif data['tenue']==1:
            dressingUp()
    elif data['ecranNum'] == 11:
        can1.unbind('<Key>')
        can1.destroy()
        fond.delete(ecranAffichage)
        canArgent.place_forget()
        canMission.place_forget()
        canTouche.place_forget()
        frame = 10

        ecranAffichage = fond.create_image(0, 0, image=ecran6, anchor=NW)
        data['ecranNum'] += 1
        fond.after(5000, ecranCinematique)
    elif data['ecranNum'] == 12:
        fond.delete(ecranAffichage)
        ecranAffichage = fond.create_image(0, 0, image=ecran7, anchor=NW)
        data['ecranNum'] += 1
        fond.after(5000, ecranCinematique)
    elif data['ecranNum'] == 13:
        fond.delete(ecranAffichage)
        ecranAffichage = fond.create_image(0, 0, image=ecran8, anchor=NW)
        fond.after(3000, video2)
    elif data['ecranNum'] == 14:
        fond.delete(ecranAffichage)
        ecranAffichage = fond.create_image(0, 0, image=ecrannoir, anchor=NW)
        data['ecranNum'] += 1
        fond.after(4000, ecranCinematique)
    elif data['ecranNum'] == 15:
        window.quit()



def video1():
    global frame, ecranAffichage, image

    image = PhotoImage(file=f"textures/ecranCinematique/video1/00{frame}.png")
    fond.delete(ecranAffichage)
    ecranAffichage = fond.create_image(0, 0, image=image, anchor=NW)

    frame+=1
    if frame < 90:
        fond.after(10, video1)
    else:
        data['ecranNum'] += 1
        ecranCinematique()


def video2():
    global frame, ecranAffichage, image

    if frame < 100:
        image = PhotoImage(file=f"textures/ecranCinematique/video2/00{frame}.png")
    else:
        image = PhotoImage(file=f"textures/ecranCinematique/video2/0{frame}.png")
    fond.delete(ecranAffichage)
    ecranAffichage = fond.create_image(0, 0, image=image, anchor=NW)

    frame+=1
    if frame < 120:
        fond.after(10, video2)
    else:
        data['ecranNum'] += 1
        ecranCinematique()



frame = 10
image = PhotoImage(file=f"textures/ecranCinematique/video1/00{frame}.png")

ecranAffichage = 0
ecrannoir = PhotoImage(file="textures/ecranCinematique/ecrannoir.png")
ecran1 = PhotoImage(file="textures/ecranCinematique/cinematique1.png")
ecran2 = PhotoImage(file="textures/ecranCinematique/cinematique2.png")
ecran3 = PhotoImage(file="textures/ecranCinematique/cinematique3.png")
ecran4 = PhotoImage(file="textures/ecranCinematique/cinematique4.png")
ecran5 = PhotoImage(file="textures/ecranCinematique/cinematique5.png")
ecran6 = PhotoImage(file="textures/ecranCinematique/cinematique6.png")
ecran7 = PhotoImage(file="textures/ecranCinematique/cinematique7.png")
ecran8 = PhotoImage(file="textures/ecranCinematique/cinematique8.png")

debut = PhotoImage(file="textures/ecranCinematique/video1/debut.png")
fin = PhotoImage(file="textures/ecranCinematique/video1/fin.png")







































animationY1 = 0
animationY2 = 0
animationX1 = 0
animationX2 = 0
fpsUp, fpsDown, fpsLeft, fpsRight = 0, 0, 0, 0

vitesseAnimation = 8

def up():
    global posX, posY, perso, animationY1, animationY2, can1x, can1y, fpsUp

    if posY % 64 == 0:
        animationY1 = posY
        animationY2 = posY-16

    posY -= vitesseAnimation
    can1y += vitesseAnimation
    can1.place(x=can1x, y=can1y)


    if posY%64 != 0:
        fpsUp = 1

        if animationY2 <= posY <= animationY1:  # -16 < x < 0
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_h1, anchor="nw")
            can1.after(1, up)

        elif animationY1 - 32 <= posY <= animationY2:  # -32 < x < -16
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_h2, anchor="nw")
            can1.after(1, up)

        elif animationY2 - 32 <= posY <= animationY1 - 32:  # -48 < x < -32
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_h1, anchor="nw")
            can1.after(1, up)

        elif animationY2 - 48 <= posY <= animationY1 - 48:  # -64 < x < -48
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_h2, anchor="nw")
            can1.after(1, up)


    else:
        can1.delete(perso)
        perso = can1.create_image(posX, posY, image=prisonnier_immobile3, anchor="nw")
        fpsUp = 0
        touche_action("Up")



def down():
    global posX, posY, perso, animationY1, animationY2, can1x, can1y, fpsDown

    if posY % 64 == 0:
        animationY1 = posY
        animationY2 = posY+16

    posY += vitesseAnimation
    can1y -= vitesseAnimation
    can1.place(x=can1x, y=can1y)


    if posY%64 != 0:
        fpsDown = 1

        if animationY1 <= posY <= animationY2:  # 0 < x < 16
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_b1, anchor="nw")
            can1.after(1, down)

        elif animationY2 <= posY <= animationY1+32:  # 16 < x < 32
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_b2, anchor="nw")
            can1.after(1, down)

        elif animationY1 <= posY <= animationY2 + 32:  # 32 < x < 48
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_b1, anchor="nw")
            can1.after(1, down)

        elif animationY2 + 32 <= posY <= animationY1 + 64:  # 48 < x < 64
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_b2, anchor="nw")
            can1.after(1, down)

    else:
        can1.delete(perso)
        perso = can1.create_image(posX, posY, image=prisonnier_immobile1, anchor="nw")
        fpsDown = 0
        touche_action("Down")



def left():
    global posX, posY, perso, animationX1, animationX2, can1x, can1y, fpsLeft

    if posX % 64 == 0:
        animationX1 = posX
        animationX2 = posX-22


    posX -= vitesseAnimation
    can1x += vitesseAnimation
    can1.place(x=can1x, y=can1y)


    if posX%64 != 0:
        fpsLeft = 1

        if animationX2 <= posX <= animationX1: #-22 < x < 0
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_g1, anchor="nw")
            can1.after(1, left)

        elif animationX1 - 44 <= posX <= animationX2:  #-44 < x < -22
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_g2, anchor="nw")
            can1.after(1, left)

        elif animationX2 - 42 <= posX <= animationX1 - 44:  #-64 < x < -44
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_g3, anchor="nw")
            can1.after(1, left)


    else:
        can1.delete(perso)
        perso = can1.create_image(posX, posY, image=prisonnier_immobile4, anchor="nw")
        fpsLeft = 0
        touche_action("Left")




def right():
    global posX, posY, perso, animationX1, animationX2, can1x, can1y, fpsRight

    if posX % 64 == 0:
        animationX1 = posX
        animationX2 = posX + 22

    posX += vitesseAnimation
    can1x -= vitesseAnimation
    can1.place(x=can1x, y=can1y)


    if posX%64 != 0:
        fpsRight = 1

        if animationX1 <= posX <= animationX2:  # 0 < x < 22
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_d1, anchor="nw")
            can1.after(1, right)

        elif animationX2 <= posX <= animationX1 + 44:  # 22 < x < 44
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_d2, anchor="nw")
            can1.after(1, right)

        elif animationX1 + 44 <= posX <= animationX2 + 42:  # 44 < x < 64
            can1.delete(perso)
            perso = can1.create_image(posX, posY, image=prisonnier_d3, anchor="nw")
            can1.after(1, right)


    else:
        can1.delete(perso)
        perso = can1.create_image(posX, posY, image=prisonnier_immobile2, anchor="nw")
        fpsRight = 0
        touche_action("Right")


def touche_action(touche):
    global affichageTouche
    ligne = posY // 64
    colonne = posX // 64
    if ma_matrice[ligne][colonne] == "SACB__" or ma_matrice[ligne][colonne] == "LIASSE" or ma_matrice[ligne][colonne] == "CLOTHS":
        canTouche.delete(affichageTouche)
        affichageTouche = canTouche.create_text(20, 28, font=("Times", "14", "bold italic"), fill="white", anchor="w",text=f"{toucheDico['ramasser']}")

    elif ma_matrice[ligne-1][colonne] == "I_MAMA" or ma_matrice[ligne][colonne+1] == "I_MAMA" or \
            ma_matrice[ligne+1][colonne] == "I_FRAN" or ma_matrice[ligne][colonne-1] == "I_FRAN" or \
            ma_matrice[ligne+1][colonne] == "I_POLI" or ma_matrice[ligne][colonne+1] == "I_POLI":
        canTouche.delete(affichageTouche)
        affichageTouche = canTouche.create_text(20, 28, font=("Times", "14", "bold italic"), fill="white", anchor="w",text=f"{toucheDico['interaction']}")

    elif ma_matrice[ligne][colonne] == "LUMEX1" or ma_matrice[ligne][colonne] == "LUMEX2" or ma_matrice[ligne][colonne] == "LUMPO1"\
            or ma_matrice[ligne][colonne] == "LUMPO2" or ma_matrice[ligne][colonne] == "TAPISC"\
            or ma_matrice[ligne][colonne] == "TAPISB" or ma_matrice[ligne][colonne] == "IPORTE":
        canTouche.delete(affichageTouche)
        affichageTouche = canTouche.create_text(6, 28, font=("Times", "10", "bold italic"), fill="white", anchor="w",text="ENTER")


    else:
        canTouche.delete(affichageTouche)


def cases_argent():
    global posY, posX, perso, can1, affichageArgent, affichageMission
    ligne = posY // 64
    colonne = posX // 64
    if ma_matrice[ligne][colonne] == "SACB__":
        data['money'] += 50
        data['mission'] = "Récolter 120$ puis retourner voir Mamadou."
        canMission.delete(affichageMission)
        affichageMission = canMission.create_text(10, 27, font=("Times", "11", "bold italic"), anchor="w",text=f"{data['mission']}")
        collect_coin.play()
    elif ma_matrice[ligne][colonne] == "LIASSE":
        data['money'] += 10
        collect_coin.play()

    if ma_matrice[ligne][colonne] == "SACB__" or ma_matrice[ligne][colonne] == "LIASSE":
        ma_matrice[ligne][colonne] = "SOLPSN"

        canArgent.delete(affichageArgent)
        affichageArgent = canArgent.create_text(53, 105 / 4, font=("Times", "20", "bold italic"),text=f"{data['money']}$")
        can1.create_image(64 * colonne, 64 * ligne, image=solPrison, anchor="nw")

        lastMouvFonction()


def dressingUp():
    global prisonnier_b1, prisonnier_b2, prisonnier_d1, prisonnier_d2, prisonnier_d3, \
        prisonnier_g1, prisonnier_g2, prisonnier_g3, prisonnier_h1, prisonnier_h2, prisonnier_immobile1, prisonnier_immobile2\
        , prisonnier_immobile3, prisonnier_immobile4
    prisonnier_b1 = prisonnierpolice_b1
    prisonnier_b2 = prisonnierpolice_b2
    prisonnier_d1 = prisonnierpolice_d1
    prisonnier_d2 = prisonnierpolice_d2
    prisonnier_d3 = prisonnierpolice_d3
    prisonnier_g1 = prisonnierpolice_g1
    prisonnier_g2 = prisonnierpolice_g2
    prisonnier_g3 = prisonnierpolice_g3
    prisonnier_h1 = prisonnierpolice_h1
    prisonnier_h2 = prisonnierpolice_h2
    prisonnier_immobile1 = prisonnierpolice_immobile1
    prisonnier_immobile2 = prisonnierpolice_immobile2
    prisonnier_immobile3 = prisonnierpolice_immobile3
    prisonnier_immobile4 = prisonnierpolice_immobile4
    data['tenue']=1
    lastMouvFonction()



def Clavier(event):
    """fonction qui se met en route à l'appui d'une touche"""
    global lastMouv, isCinematic, bot_mamadou, ma_matrice, perso, posX, posY, can1x, can1y, vitesseAnimation, bot_francois, bot_policier, affichageMission
    touche = event.keysym
    ligne = posY // 64
    colonne = posX // 64

    if isCinematic == False:
        if touche == toucheDico['monter'] and fpsUp == 0 and fpsDown == 0:
            lastMouv = "up"
            if ma_matrice[ligne-1][colonne] not in interdites:
                up()
            else:
                lastMouvFonction()


        elif touche == toucheDico['descendre'] and fpsDown == 0 and fpsUp == 0:
            lastMouv = "down"
            if ma_matrice[ligne+1][colonne] not in interdites:
                down()
            else:
                lastMouvFonction()

        elif touche == toucheDico['gauche'] and fpsLeft == 0 and fpsRight == 0:
            lastMouv = "left"
            if ma_matrice[ligne][colonne-1] not in interdites:
                left()
            else:
                lastMouvFonction()

        elif touche == toucheDico['droite'] and fpsRight == 0 and fpsLeft == 0:
            lastMouv = "right"
            if ma_matrice[ligne][colonne+1] not in interdites:
                right()
            else:
                lastMouvFonction()

        if touche == toucheDico['ramasser']:
             cases_argent()


        if touche == toucheDico['ramasser'] and ma_matrice[ligne][colonne] == "CLOTHS":
            ma_matrice[ligne][colonne] = "SOLDSK"
            can1.create_image(64 * colonne, 64 * ligne, image=solbureau, anchor="nw")
            data['mission'] = "Allez parler au garde de la sortie."
            canMission.delete(affichageMission)
            affichageMission = canMission.create_text(10, 27, font=("Times", "13", "bold italic"), anchor="w",text=f"{data['mission']}")

            dressingUp()

        if touche == toucheDico['interaction'] and ma_matrice[ligne+1][colonne] == "I_FRAN"  and data['missionFrancois']==0:
            isCinematic = True
            lastMouv = "down"
            lastMouvFonction()
            can1.delete(bot_francois)
            bot_francois = can1.create_image(256, 704, image=francois_immobile3, anchor="nw")

            cinematicFrancois()



        if touche == toucheDico['interaction'] and ma_matrice[ligne][colonne-1] == "I_FRAN" and data['missionFrancois']==0:
            isCinematic = True
            lastMouv = "left"
            lastMouvFonction()
            can1.delete(bot_francois)
            bot_francois = can1.create_image(256, 704, image=francois_immobile2, anchor="nw")

            cinematicFrancois()




        if touche == toucheDico['interaction'] and ma_matrice[ligne-1][colonne] == "I_MAMA":
            isCinematic = True
            ma_matrice[512 // 64][576 // 64] = "IPORTE"
            lastMouv = "up"
            lastMouvFonction()
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_immobile1, anchor="nw")

            if data['money'] < 120 and data['missionMamadou'] == 0:
                cinematicMamadou()
            elif data['money'] >= 120 and data['missionMamadou'] == 0:
                data['missionMamadou'] = 1
                cinematicMamadou2()
            elif data['missionMamadou'] == 1:
                cinematicMamadou3()

        #Le perso à gauche
        if touche == toucheDico['interaction'] and ma_matrice[ligne][colonne+1] == "I_MAMA":
            isCinematic = True
            ma_matrice[512 // 64][576 // 64] = "IPORTE"
            lastMouv = "right"
            lastMouvFonction()
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_immobile4, anchor="nw")
            if data['money'] < 120 and data['missionMamadou']==0:
                cinematicMamadou()
            elif data['money'] >= 120 and data['missionMamadou']==0:
                data['missionMamadou'] = 1
                cinematicMamadou2()
            elif data['missionMamadou']==1:
                cinematicMamadou3()



        if touche == toucheDico['interaction'] and ma_matrice[ligne+1][colonne] == "I_POLI":
            isCinematic = True
            lastMouv = "down"
            lastMouvFonction()
            can1.delete(bot_policier)
            bot_policier = can1.create_image(posXpolicier, posYpolicier, image=policier_immobile3, anchor="nw")
            if data['tenue']==0:
                cinematicPolicier1()
            elif data['tenue']==1:
                cinematicPolicier2()

        if touche == toucheDico['interaction'] and ma_matrice[ligne][colonne+1] == "I_POLI":
            isCinematic = True
            lastMouv = "right"
            lastMouvFonction()
            can1.delete(bot_policier)
            bot_policier = can1.create_image(posXpolicier, posYpolicier, image=policier_immobile4, anchor="nw")
            if data['tenue']==0:
                cinematicPolicier1()
            elif data['tenue']==1:
                cinematicPolicier2()





        if touche == "F3":
            print(f"PosX : {posX}\nPosY : {posY} \n\nCan1x : {can1x} \nCan1y : {can1y}\n")

        if touche == "Return" and data['ecranNum'] == 7:
            data['ecranNum']+=1
            ecranCinematique()

        if touche == "Return" and data['ecranNum'] == 10:
            if ma_matrice[ligne][colonne] == "LUMPO1":
                posX = 128
                posY = 64
                can1x = 384
                can1y = 128
                createMatrice("cantine")
                vitesseAnimation = 4
                can1.delete(perso)
                perso = can1.create_image(posX, posY, image=prisonnier_immobile1, anchor="nw")
                can1.create_image(128, 192, image=francois_immobile2, anchor="nw")
                can1.create_image(128, 512, image=jimmy_d2, anchor="nw")
                can1.create_image(256, 448, image=policier_immobile4, anchor="nw")
                can1.create_image(384, 256, image=policier_d2, anchor="nw")
                can1.focus_set()
                can1.bind('<Key>', Clavier)

            elif ma_matrice[ligne][colonne] == "TAPISC":
                posX = 320
                posY = 960
                can1x = 192
                can1y = -768
                createMatrice("spawn")
                vitesseAnimation = 8
                can1.delete(perso)
                perso = can1.create_image(posX, posY, image=prisonnier_immobile3, anchor="nw")
                can1.focus_set()
                can1.bind('<Key>', Clavier)



            elif ma_matrice[ligne][colonne] == "LUMPO2":
                posX = 128
                posY = 64
                can1x = 384
                can1y = 128
                data['mission'] = "Prenez l'uniforme de policier."
                canMission.delete(affichageMission)
                affichageMission = canMission.create_text(10, 27, font=("Times", "12", "bold italic"), anchor="w",text=f"{data['mission']}")
                createMatrice("bureau")
                vitesseAnimation = 8
                can1.delete(perso)
                perso = can1.create_image(posX, posY, image=prisonnier_immobile1, anchor="nw")
                can1.focus_set()
                can1.bind('<Key>', Clavier)

            elif ma_matrice[ligne][colonne] == "TAPISB":
                posX = 896
                posY = 960
                can1x = -384
                can1y = -768
                createMatrice("spawn")
                vitesseAnimation = 8
                can1.delete(perso)
                perso = can1.create_image(posX, posY, image=prisonnier_immobile3, anchor="nw")
                can1.focus_set()
                can1.bind('<Key>', Clavier)

            elif ma_matrice[ligne][colonne] == "IPORTE":
                lastMouv = "up"
                lastMouvFonction()
                ma_matrice[ligne-1][colonne] = "PORTE2"
                can1.create_image(64 * colonne, 64 * ligne - 64, image=porte2, anchor="nw")
                data['mission'] = "Récupérer l'argent de Mamadou."
                canMission.delete(affichageMission)
                affichageMission = canMission.create_text(10, 27, font=("Times", "14", "bold italic"), anchor="w",text=f"{data['mission']}")


    if touche == toucheDico['pompe'] and isCinematicFrancois == True and animationPompe == False:
        pompe()




def ClavierVehicule(event):
    touche = event.keysym
    ligne = posYcar // 64
    colonne = posXcar // 64
    if touche == toucheDico['gauche'] and ma_matrice[ligne][colonne - 1] not in interdites:
        leftCar()

    elif touche == toucheDico['droite'] and ma_matrice[ligne][colonne + 1] not in interdites:
        rightCar()

    if touche == "F3":
        print(f"PosXcar : {posXcar}\nPosYcar : {posYcar} \n\nCan1x : {can1x} \nCan1y : {can1y}\n")



isCinematic = False

#can1.focus_set()
#can1.bind('<Key>' , Clavier)


perso = 0






#################################
vitesseCar = 8


def gyrophare():
    global policeGyro, gyroNum
    if gyroNum == 0:
        policeGyro = police1texture
        gyroNum += 1
    else:
        policeGyro = police2texture
        gyroNum -= 1

    can1.after(300, gyrophare)

policeGyro = police2texture
gyroNum = 0


def forwardCar():
    global posYcar, can1y, car, vitesseCar, policeCar, posYpolice, ecranNum




    if can1y > 64:
        vitesseCar = 32
        pygame.mixer.stop()

        #can1.unbind('<Key>')
    if can1y < 450:
        posYcar -= vitesseCar
        posYpolice -= vitesseCar
        can1y += 8
        can1.place(x=can1x, y=can1y)
        can1.delete(car)
        car = can1.create_image(posXcar, posYcar, image=carTexture, anchor="nw")
        can1.delete(policeCar)
        policeCar = can1.create_image(posXpolice, posYpolice, image=policeGyro, anchor="nw")
        can1.after(10, forwardCar)
        if ma_matrice[posYcar // 64][posXcar // 64] == "BARRER":
            destruction_sound.play()


    else:

        bruitage_derapage.play()
        fond.after(5000, ecranCinematique)




def leftPolice():
    global posXpolice, policeCar
    posXpolice -= 32
    if posXpolice % 64 != 0:
        can1.delete(policeCar)
        policeCar = can1.create_image(posXpolice, posYpolice, image=policeGyro, anchor="nw")
        can1.after(1, leftPolice)


def rightPolice():
    global posXpolice, policeCar
    posXpolice += 32
    if posXpolice % 64 != 0:
        can1.delete(policeCar)
        policeCar = can1.create_image(posXpolice, posYpolice, image=policeGyro, anchor="nw")
        can1.after(1, rightPolice)


def leftCar():
    global posXcar, car
    posXcar -= 32
    if posXcar % 64 != 0:

        can1.delete(car)
        car = can1.create_image(posXcar, posYcar, image=carTexture, anchor="nw")
        can1.after(1, leftCar)

    else:
        can1.after(500, leftPolice)


def rightCar():
    global posXcar, car
    posXcar += 32

    if posXcar % 64 != 0:
        can1.delete(car)
        car = can1.create_image(posXcar, posYcar, image=carTexture, anchor="nw")
        can1.after(1, rightCar)

    else:
        can1.after(500, rightPolice)





posXcar = 512
posYcar = 1788

posXpolice = 512
posYpolice = 2044

car = can1.create_image(posXcar, posYcar, image=carTexture, anchor="nw")
policeCar = can1.create_image(posXpolice, posYpolice-256, image=police1texture, anchor="nw")




#############################################################
########################BOTS#################################
#############################################################
bot_jimmy = 0
bot_francois = 0
bot_policier = 0









def upMamadou():
    global posXmamadou, posYmamadou, bot_mamadou, animationY1mamadou, animationY2mamadou, can1x, can1y, fpsUp

    if posYmamadou % 64 == 0:
        animationY1mamadou = posYmamadou
        animationY2mamadou = posYmamadou-16

    posYmamadou -= 8

    if posYmamadou%64 != 0:


        if animationY2mamadou <= posYmamadou <= animationY1mamadou:  # -16 < x < 0
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_h1, anchor="nw")  
            can1.after(10, upMamadou)

        elif animationY1mamadou - 32 <= posYmamadou <= animationY2mamadou:  # -32 < x < -16
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_h2, anchor="nw")
            can1.after(10, upMamadou)

        elif animationY2mamadou - 32 <= posYmamadou <= animationY1mamadou - 32:  # -48 < x < -32
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_h1, anchor="nw")
            can1.after(10, upMamadou)

        elif animationY2mamadou - 48 <= posYmamadou <= animationY1mamadou - 48:  # -64 < x < -48
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_h2, anchor="nw")
            can1.after(10, upMamadou)


    else:
        can1.delete(bot_mamadou)
        bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_immobile3, anchor="nw")




def downMamadou():
    global posXmamadou, posYmamadou, bot_mamadou, animationY1mamadou, animationY2mamadou, can1x, can1y, fpsDown
    if posYmamadou % 64 == 0:
        animationY1mamadou = posYmamadou
        animationY2mamadou = posYmamadou+16

    posYmamadou += 8

    if posYmamadou%64 != 0:

        if animationY1mamadou <= posYmamadou <= animationY2mamadou:  # 0 < x < 16
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_b1, anchor="nw")
            can1.after(10, downMamadou)

        elif animationY2mamadou <= posYmamadou <= animationY1mamadou+32:  # 16 < x < 32
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_b2, anchor="nw")
            can1.after(10, downMamadou)

        elif animationY1mamadou <= posYmamadou <= animationY2mamadou + 32:  # 32 < x < 48
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_b1, anchor="nw")
            can1.after(10, downMamadou)

        elif animationY2mamadou + 32 <= posYmamadou <= animationY1mamadou + 64:  # 48 < x < 64
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_b2, anchor="nw")
            can1.after(10, downMamadou)

    else:
        can1.delete(bot_mamadou)
        bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_immobile1, anchor="nw")



def leftMamadou():
    global posXmamadou, posYmamadou, bot_mamadou, animationX1mamadou, animationX2mamadou, can1x, can1y, fpsLeft

    if posXmamadou % 64 == 0:
        animationX1mamadou = posXmamadou
        animationX2mamadou = posXmamadou-22

    posXmamadou -= 8

    if posXmamadou%64 != 0:

        if animationX2mamadou <= posXmamadou <= animationX1mamadou: #-22 < x < 0
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_g1, anchor="nw")
            can1.after(10, leftMamadou)

        elif animationX1mamadou - 44 <= posXmamadou <= animationX2mamadou:  #-44 < x < -22
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_g2, anchor="nw")
            can1.after(10, leftMamadou)

        elif animationX2mamadou - 42 <= posXmamadou <= animationX1mamadou - 44:  #-64 < x < -44
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_g3, anchor="nw")
            can1.after(10, leftMamadou)


    else:
        can1.delete(bot_mamadou)
        bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_immobile4, anchor="nw")





def rightMamadou():
    global posXmamadou, posYmamadou, bot_mamadou, animationX1mamadou, animationX2mamadou, can1x, can1y, fpsRight

    if posXmamadou % 64 == 0:
        animationX1mamadou = posXmamadou
        animationX2mamadou = posXmamadou + 22

    posXmamadou += 8

    if posXmamadou%64 != 0:

        if animationX1mamadou <= posXmamadou <= animationX2mamadou:  # 0 < x < 22
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_d1, anchor="nw")
            can1.after(10, rightMamadou)

        elif animationX2mamadou <= posXmamadou <= animationX1mamadou + 44:  # 22 < x < 44
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_d2, anchor="nw")
            can1.after(10, rightMamadou)

        elif animationX1mamadou + 44 <= posXmamadou <= animationX2mamadou + 42:  # 44 < x < 64
            can1.delete(bot_mamadou)
            bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_d3, anchor="nw")
            can1.after(10, rightMamadou)


    else:
        can1.delete(bot_mamadou)
        bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_immobile2, anchor="nw")



animationY1mamadou = 0
animationY2mamadou = 0
animationX1mamadou = 0
animationX2mamadou = 0
posXmamadou = 1344
posYmamadou = 256
bot_mamadou = 0
















dialogueNum = 0
dialogueCercleMamadou = 0
dialogueTextMamadou = 0
dialogueCercleMain = 0
dialogueTextMain = 0
def cinematicMamadou():
    global dialogueNum, dialogueTextMain, dialogueTextMamadou, dialogueCercleMamadou, dialogueCercleMain, variableCinematic
    canTouche.delete(affichageTouche)
    canMission.delete(affichageMission)


########################################################################################################################MAMADOU
    if dialogueNum == 0:


        dialogueCercleMamadou = can1.create_oval(posXmamadou+50, posYmamadou-64, posXmamadou+256, posYmamadou+32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou+150,posYmamadou-16, justify="center",font=('Times', '12', 'italic') ,text="Yo, tu cherches un \nbon plan pour t'échapper ?")

        dialogueNum+=1
        can1.after(2500, cinematicMamadou)
########################################################################################################################MAIN
    elif dialogueNum == 1:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueCercleMain = can1.create_oval(posX, posY + 64, posX - 206, posY - 32,fill="#FFE6C3")
        dialogueTextMain = can1.create_text(posX - 106, posY + 16, justify="center", font=('Times', '12', 'italic'), text="Ouais, tu me proposes quoi ?")

        dialogueNum += 1
        can1.after(2500, cinematicMamadou)
########################################################################################################################MAMADOU
    elif dialogueNum == 2:
        can1.delete(dialogueTextMain)
        can1.delete(dialogueCercleMain)

        dialogueCercleMamadou = can1.create_oval(posXmamadou + 20, posYmamadou - 64, posXmamadou + 256, posYmamadou + 32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou + 138, posYmamadou - 16, justify="center",font=('Times', '12', 'italic'), text="Si tu me ramènes 120$,\nje te dis où comment\n tu peux sortir d'ici.")

        dialogueNum += 1
        can1.after(3500, cinematicMamadou)
########################################################################################################################MAIN
    elif dialogueNum == 3:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueCercleMain = can1.create_oval(posX, posY + 64, posX - 206, posY - 32, fill="#FFE6C3")
        dialogueTextMain = can1.create_text(posX - 106, posY + 16, justify="center", font=('Times', '12', 'italic'),text=f"Et je trouve où 120$ j'ai\nque {data['money']}$ là.")

        dialogueNum += 1
        can1.after(2500, cinematicMamadou)
########################################################################################################################MAMADOU
    elif dialogueNum == 4:
        can1.delete(dialogueTextMain)
        can1.delete(dialogueCercleMain)

        dialogueCercleMamadou = can1.create_oval(posXmamadou + 20, posYmamadou - 64, posXmamadou + 256, posYmamadou + 32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou + 138, posYmamadou - 16, justify="center",font=('Times', '12', 'italic'), text="C'est simple, y'a un prisonnier \nqui s'appelle Jimmy\n qui me dois des sous.")

        dialogueNum += 1
        can1.after(3500, cinematicMamadou)
########################################################################################################################MAMADOU
    elif dialogueNum == 5:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueCercleMamadou = can1.create_oval(posXmamadou + 20, posYmamadou - 64, posXmamadou + 256, posYmamadou + 32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou + 138, posYmamadou - 16, justify="center",font=('Times', '12', 'italic'), text="Et j'ai l'impression qui veut\n pas me les rendre donc on va\n aller les récupérer.")

        dialogueNum += 1
        can1.after(3500, cinematicMamadou)

########################################################################################################################MAIN
    elif dialogueNum == 6:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueCercleMain = can1.create_oval(posX, posY + 64, posX - 206, posY - 32, fill="#FFE6C3")
        dialogueTextMain = can1.create_text(posX - 106, posY + 16, justify="center", font=('Times', '14', 'italic'),text="Azy je suis chaud\nil est où là ?")

        dialogueNum += 1
        can1.after(2500, cinematicMamadou)

########################################################################################################################MAMADOU
    elif dialogueNum == 7:
        can1.delete(dialogueTextMain)
        can1.delete(dialogueCercleMain)

        dialogueCercleMamadou = can1.create_oval(posXmamadou + 20, posYmamadou - 64, posXmamadou + 256, posYmamadou + 32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou + 138, posYmamadou - 16, justify="center",font=('Times', '12', 'italic'), text="Je crois qu'il est \ndans sa cellule entrain de dormir.\n Suis-moi on y va.")

        dialogueNum += 1
        can1.after(3000, cinematicMamadou)

########################################################################################################################MOUVEMENT
    elif dialogueNum == 8:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        mouvementCinematic()

########################################################################################################################MAMADOU
    elif dialogueNum == 9:
        dialogueCercleMamadou = can1.create_oval(posXmamadou - 20, posYmamadou + 64, posXmamadou - 256, posYmamadou - 32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou - 138, posYmamadou + 16, justify="center",font=('Times', '12', 'italic'),text="C'est ici. Essaye de détruire la\nporte et vole le sac de billet à\nson chevet.")

        dialogueNum += 1
        can1.after(3500, cinematicMamadou)

    elif dialogueNum == 10:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueCercleMamadou = can1.create_oval(posXmamadou - 10, posYmamadou + 64, posXmamadou - 300, posYmamadou - 64, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou - 155, posYmamadou, justify="center",font=('Times', '13', 'italic'),text="Je vais retourner à mon emplacement\nessaye de trouver des moyens de te faire\nde l'argent et reviens me voir.")

        dialogueNum += 1
        can1.after(4000, cinematicMamadou)

########################################################################################################################MAIN
    elif dialogueNum == 11:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueCercleMain = can1.create_oval(posX + 16, posY - 32, posX + 196, posY + 32, fill="#FFE6C3")
        dialogueTextMain = can1.create_text(posX + 106, posY, justify="center", font=('Times', '14', 'italic'),text="Vas-y vas-y !")

        dialogueNum += 1
        can1.after(2500, cinematicMamadou)

    elif dialogueNum == 12:
        can1.delete(dialogueCercleMain)
        can1.delete(dialogueTextMain)

        variableCinematic+=1
        can1.after(500, mouvementCinematic)
        dialogueNum = 0




variableCinematic = 0

def orienterMamadou():
    global bot_mamadou
    can1.delete(bot_mamadou)
    bot_mamadou = can1.create_image(posXmamadou, posYmamadou, image=mamadou_immobile2, anchor="nw")

def mouvementCinematic():
    global variableCinematic, bot_mamadou, lastMouv, dialogueNum, isCinematic, can1, affichageTouche, affichageMission
    if lastMouv == "up":
        if variableCinematic == 1:
            can1.after(400, leftMamadou)
            can1.after(400, up)

        elif 2 <= variableCinematic <= 5:
            if variableCinematic == 2:
                can1.after(400, left)
                can1.after(400, downMamadou)

            else:
                can1.after(400, downMamadou)
                can1.after(400, down)

        elif 6<= variableCinematic <= 17:
            if variableCinematic == 6:
                can1.after(400, leftMamadou)
                can1.after(400, down)
            else:
                can1.after(400, leftMamadou)
                can1.after(400, left)

        elif variableCinematic == 19:

            can1.after(200, orienterMamadou)
            dialogueNum += 1
            can1.after(200, cinematicMamadou)




    elif lastMouv == "right":
        if variableCinematic == 1:
            can1.after(400, right)
            can1.after(400, downMamadou)

        elif variableCinematic == 2:
            can1.after(400, down)
            can1.after(400, leftMamadou)

        elif variableCinematic == 3:
            can1.after(400, downMamadou)
            can1.after(400, left)
            lastMouv = "up"

    if variableCinematic < 19:
        variableCinematic += 1
        can1.after(400, mouvementCinematic)


    elif variableCinematic == 20:
        can1.after(400, downMamadou)
        variableCinematic += 1
        can1.after(400, mouvementCinematic)

    elif 21 <= variableCinematic <= 31:
        can1.after(400, rightMamadou)
        variableCinematic += 1
        can1.after(400, mouvementCinematic)

    elif variableCinematic == 32:
        rightMamadou()
        rightMamadou()
        upMamadou()
        upMamadou()
        upMamadou()
        upMamadou()
        upMamadou()
        downMamadou()
        downMamadou()
        variableCinematic = 1
        dialogueNum = 0
        canTouche.delete(affichageTouche)
        affichageTouche = canTouche.create_text(6, 28, font=("Times", "10", "bold italic"), fill="white", anchor="w",text="ENTER")
        data['mission'] = "Entrer dans la cellule de Jimmy."
        canMission.delete(affichageMission)
        affichageMission = canMission.create_text(10, 27, font=("Times", "14", "bold italic"), anchor="w",text=f"{data['mission']}")
        isCinematic = False









posXfrancois = 256
posYfrancois = 704

dialogueCercleFrancois = 0
dialogueTextFrancois = 0

isCinematicFrancois = False
def cinematicFrancois():
    global dialogueNum, dialogueTextMain, dialogueTextFrancois, dialogueCercleFrancois, dialogueCercleMain, variableCinematic, affichageTouche, affichageMission, isCinematicFrancois, affichageArgent, isCinematic
    canTouche.delete(affichageTouche)
    canMission.delete(affichageMission)


########################################################################################################################FRANCOIS
    if dialogueNum == 0:


        dialogueCercleFrancois = can1.create_oval(posXfrancois-206, posYfrancois+64, posXfrancois, posYfrancois-32, fill="#FFC030")
        dialogueTextFrancois = can1.create_text(posXfrancois-106,posYfrancois+16, justify="center",font=('Times', '12', 'italic') ,text="Salut le nouveau, tu veux te\n faire de l'argent facilement ?")

        dialogueNum+=1
        can1.after(3000, cinematicFrancois)
########################################################################################################################MAIN
    elif dialogueNum == 1:
        can1.delete(dialogueTextFrancois)
        can1.delete(dialogueCercleFrancois)

        dialogueCercleMain = can1.create_oval(posX+32, posY - 64, posX + 238, posY + 32,fill="#FFC030")
        dialogueTextMain = can1.create_text(posX + 138, posY - 16, justify="center", font=('Times', '18', 'italic'), text="Ouais vas-y !")

        dialogueNum += 1
        can1.after(2000, cinematicFrancois)
########################################################################################################################MAIN
    elif dialogueNum == 2:
        can1.delete(dialogueCercleMain)
        can1.delete(dialogueTextMain)

        dialogueCercleFrancois = can1.create_oval(posXfrancois - 206, posYfrancois + 64, posXfrancois, posYfrancois - 32, fill="#FFC030")
        dialogueTextFrancois = can1.create_text(posXfrancois - 106, posYfrancois + 16, justify="center",font=('Times', '12', 'italic'),text="On va voir si t'es un dur,\nsi tu fais 10 pompes,\n je te donne 20$.")

        dialogueNum += 1
        can1.after(3000, cinematicFrancois)
########################################################################################################################MAIN
    elif dialogueNum == 3:
        can1.delete(dialogueTextFrancois)
        can1.delete(dialogueCercleFrancois)

        dialogueCercleMain = can1.create_oval(posX+32, posY - 64, posX + 238, posY + 32,fill="#FFC030")
        dialogueTextMain = can1.create_text(posX + 138, posY - 16, justify="center", font=('Times', '12', 'italic'), text="Raweee t'es généreux mec !\n Et bah dis moi\n quand je commence.")

        dialogueNum += 1
        can1.after(3000, cinematicFrancois)
########################################################################################################################MAIN
    elif dialogueNum == 4:
        can1.delete(dialogueCercleMain)
        can1.delete(dialogueTextMain)
        isCinematicFrancois = True

        dialogueCercleFrancois = can1.create_oval(posXfrancois - 216, posYfrancois + 64, posXfrancois+16, posYfrancois - 32, fill="#FFC030")
        dialogueTextFrancois = can1.create_text(posXfrancois - 106, posYfrancois + 16, justify="center",font=('Times', '12', 'italic'),text=f"Quand tu veux, il suffit d'appuyer\nsur '{toucheDico['pompe']}' pour faire une pompe.")


        data['mission'] = "Faites 10 pompes."
        affichageMission = canMission.create_text(10, 27, font=("Times", "14", "bold italic"), anchor="w",text=f"{data['mission']}")
        affichageTouche = canTouche.create_text(20, 28, font=("Times", "10", "bold italic"), fill="white", anchor="w",text=f"{toucheDico['pompe']}")
########################################################################################################################MAIN
    elif dialogueNum == 5:
        can1.delete(dialogueTextFrancois)
        can1.delete(dialogueCercleFrancois)
        isCinematicFrancois = False

        dialogueCercleMain = can1.create_oval(posX+32, posY - 64, posX + 238, posY + 32,fill="#FFC030")
        dialogueTextMain = can1.create_text(posX + 138, posY - 16, justify="center", font=('Times', '12', 'italic'), text="Voilà mec, c'est fait.")

        dialogueNum += 1
        can1.after(2000, cinematicFrancois)
########################################################################################################################MAIN
    elif dialogueNum == 6:
        can1.delete(dialogueCercleMain)
        can1.delete(dialogueTextMain)

        dialogueCercleFrancois = can1.create_oval(posXfrancois - 206, posYfrancois + 64, posXfrancois, posYfrancois - 32, fill="#FFC030")
        dialogueTextFrancois = can1.create_text(posXfrancois - 106, posYfrancois + 16, justify="center",font=('Times', '12', 'italic'),text="Bien joué bien joué !\nVoilà tes 20$.")
        canArgent.delete(affichageArgent)
        data['money'] += 20
        collect_coin.play()
        canArgent.delete(affichageArgent)
        affichageArgent = canArgent.create_text(53, 105 / 4, font=("Times", "20", "bold italic"),text=f"{data['money']}$")


        dialogueNum += 1
        can1.after(2000, cinematicFrancois)
########################################################################################################################MAIN
    elif dialogueNum == 7:
        can1.delete(dialogueTextFrancois)

        dialogueTextFrancois = can1.create_text(posXfrancois - 106, posYfrancois + 16, justify="center",font=('Times', '14', 'italic'),text="Bref vas-y à plus mec.")

        dialogueNum += 1
        can1.after(2000, cinematicFrancois)
########################################################################################################################MAIN
    elif dialogueNum == 8:
        can1.delete(dialogueTextFrancois)
        can1.delete(dialogueCercleFrancois)

        dialogueCercleMain = can1.create_oval(posX+32, posY - 64, posX + 238, posY + 32,fill="#FFC030")
        dialogueTextMain = can1.create_text(posX + 138, posY - 16, justify="center", font=('Times', '12', 'italic'), text="Merci pour l'argent, ciao !")

        dialogueNum += 1
        can1.after(2000, cinematicFrancois)
########################################################################################################################MAIN
    elif dialogueNum == 9:
        can1.delete(dialogueTextMain)
        can1.delete(dialogueCercleMain)
        dialogueNum = 0
        isCinematic = False
        ma_matrice[posYfrancois//64][posXfrancois//64] = "DONE__"

        data['mission'] = "Trouvez un moyen de vous échapper."
        canMission.delete(affichageMission)
        affichageMission = canMission.create_text(10, 27, font=("Times", "14", "bold italic"), anchor="w",text=f"{data['mission']}")


        data['missionFrancois']=1





pompeRep = 0
animationPompe = False
def pompe():
    global perso, can1, animationPompe, pompeRep, affichageMission, dialogueNum


    if animationPompe == False:
        can1.delete(perso)
        perso = can1.create_image(posX, posY, image=prisonnier_pompe2, anchor="nw")
        animationPompe = True
        can1.after(300, pompe)
    elif animationPompe == True:
        can1.delete(perso)
        perso = can1.create_image(posX, posY, image=prisonnier_pompe1, anchor="nw")
        animationPompe = False
        pompeRep += 1
        data['mission'] = f"Faites {10-pompeRep} pompes."
        if pompeRep < 10:
            canMission.delete(affichageMission)
            affichageMission = canMission.create_text(10, 27, font=("Times", "14", "bold italic"), anchor="w",text=f"{data['mission']}")
        else:
            lastMouvFonction()
            dialogueNum+=1

            cinematicFrancois()








def cinematicMamadou2():
    global dialogueNum, dialogueTextMain, dialogueTextMamadou, dialogueCercleMamadou, dialogueCercleMain, variableCinematic, affichageArgent, isCinematic, affichageMission
    canTouche.delete(affichageTouche)
    canMission.delete(affichageMission)


########################################################################################################################MAMADOU
    if dialogueNum == 0:


        dialogueCercleMamadou = can1.create_oval(posXmamadou+50, posYmamadou-64, posXmamadou+256, posYmamadou+32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou+150,posYmamadou-16, justify="center",font=('Times', '16', 'italic') ,text="Alors t'as l'argent ?")

        dialogueNum+=1
        can1.after(2000, cinematicMamadou2)
########################################################################################################################MAIN
    elif dialogueNum == 1:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueCercleMain = can1.create_oval(posX, posY + 64, posX - 206, posY - 32,fill="#FFE6C3")
        dialogueTextMain = can1.create_text(posX - 106, posY + 16, justify="center", font=('Times', '16', 'italic'), text=f"Ouais, j'ai {data['money']}$ là.")

        dialogueNum += 1
        can1.after(2000, cinematicMamadou2)
########################################################################################################################MAMADOU
    elif dialogueNum == 2:
        can1.delete(dialogueTextMain)
        can1.delete(dialogueCercleMain)

        dialogueCercleMamadou = can1.create_oval(posXmamadou + 20, posYmamadou - 64, posXmamadou + 256, posYmamadou + 32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou + 138, posYmamadou - 16, justify="center",font=('Times', '16', 'italic'), text="Ok donne-moi 120$.")

        dialogueNum += 1
        can1.after(2000, cinematicMamadou2)
########################################################################################################################MAIN
    elif dialogueNum == 3:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueCercleMain = can1.create_oval(posX, posY + 64, posX - 206, posY - 32,fill="#FFE6C3")
        dialogueTextMain = can1.create_text(posX - 106, posY + 16, justify="center", font=('Times', '20', 'italic'), text="Tiens.")

        dialogueNum += 1
        can1.after(2000, cinematicMamadou2)
########################################################################################################################MAMADOU
    elif dialogueNum == 4:
        can1.delete(dialogueTextMain)
        can1.delete(dialogueCercleMain)

        data['money']-=120
        canArgent.delete(affichageArgent)
        affichageArgent = canArgent.create_text(53, 105 / 4, font=("Times", "20", "bold italic"),text=f"{data['money']}$")

        dialogueNum += 1
        can1.after(2000, cinematicMamadou2)
########################################################################################################################MAMADOU
    elif dialogueNum == 5:


        dialogueCercleMamadou = can1.create_oval(posXmamadou+50, posYmamadou-64, posXmamadou+256, posYmamadou+32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou+150,posYmamadou-16, justify="center",font=('Times', '11', 'italic') ,text="Prends cette clé.\nAvec, va dans le bureau de\npolice à coté de la cantine.")
        ma_matrice[960 // 64][896 // 64] = "LUMPO2"
        can1.create_image(896, 960, image=lumiereUnlock, anchor="nw")

        dialogueNum+=1
        can1.after(4000, cinematicMamadou2)
########################################################################################################################MAIN
    elif dialogueNum == 6:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueCercleMamadou = can1.create_oval(posXmamadou + 50, posYmamadou - 64, posXmamadou + 256,posYmamadou + 64, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou + 150, posYmamadou, justify="center",font=('Times', '11', 'italic'),text="Une fois dedans,\nmet un uniforme, va à la sortie\n de la prison et demande de sortir.")

        dialogueNum += 1
        can1.after(4000, cinematicMamadou2)
########################################################################################################################MAIN
    elif dialogueNum == 7:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueCercleMain = can1.create_oval(posX, posY + 64, posX - 206, posY - 32,fill="#FFE6C3")
        dialogueTextMain = can1.create_text(posX - 106, posY + 16, justify="center", font=('Times', '14', 'italic'), text="Ok merci beaucoup mec !")

        dialogueNum += 1
        can1.after(2500, cinematicMamadou2)

########################################################################################################################MAMADOU
    elif dialogueNum == 8:
        can1.delete(dialogueTextMain)
        can1.delete(dialogueCercleMain)

        dialogueCercleMamadou = can1.create_oval(posXmamadou + 20, posYmamadou - 64, posXmamadou + 256, posYmamadou + 32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou + 138, posYmamadou - 16, justify="center",font=('Times', '14', 'italic'), text="T'inquiète mon reuf.\nBonne chance !")

        dialogueNum += 1
        can1.after(2500, cinematicMamadou2)
########################################################################################################################MAIN
    elif dialogueNum == 9:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        dialogueNum = 0
        data['key']=1
        data['mission'] = "Allez dans le bureau de Police."
        canMission.delete(affichageMission)
        affichageMission = canMission.create_text(10, 27, font=("Times", "12", "bold italic"), anchor="w",text=f"{data['mission']}")
        isCinematic = False




def cinematicMamadou3():
    global dialogueNum, dialogueTextMain, dialogueTextMamadou, dialogueCercleMamadou, dialogueCercleMain, variableCinematic, affichageArgent, isCinematic, affichageMission
    canTouche.delete(affichageTouche)
    canMission.delete(affichageMission)


########################################################################################################################MAMADOU
    if dialogueNum == 0:


        dialogueCercleMamadou = can1.create_oval(posXmamadou+50, posYmamadou-64, posXmamadou+256, posYmamadou+32, fill="#FFE6C3")
        dialogueTextMamadou = can1.create_text(posXmamadou+150,posYmamadou-16, justify="center",font=('Times', '12', 'italic') ,text="T'as juste à aller dans\nle bureau,voler un uniforme et\ndemander de sortir.")

        dialogueNum+=1
        can1.after(5000, cinematicMamadou3)
########################################################################################################################MAIN
    elif dialogueNum == 1:
        can1.delete(dialogueTextMamadou)
        can1.delete(dialogueCercleMamadou)

        data['mission'] = "Allez dans le bureau de Police."
        canMission.delete(affichageMission)
        affichageMission = canMission.create_text(10, 27, font=("Times", "12", "bold italic"), anchor="w",text=f"{data['mission']}")
        dialogueNum = 0
        isCinematic = False










posXpolicier = 768
posYpolicier = 1216

dialogueCerclePolicier = 0
dialogueTextPolicier = 0

def cinematicPolicier1():
    global dialogueNum, dialogueTextMain, dialogueTextPolicier, dialogueCerclePolicier, dialogueCercleMain, variableCinematic, affichageTouche, affichageMission, isCinematicFrancois, affichageArgent, isCinematic
    canTouche.delete(affichageTouche)
    canMission.delete(affichageMission)


########################################################################################################################FRANCOIS
    if dialogueNum == 0:
        isCinematic = True

        dialogueCerclePolicier = can1.create_oval(posXpolicier+64, posYpolicier+64, posXpolicier+320, posYpolicier-32, fill="#FFC030")
        dialogueTextPolicier = can1.create_text(posXpolicier+192,posYpolicier+16, justify="center",font=('Times', '12', 'italic') ,text="Qu'est-ce que tu fais là toi ?\nFous le camp d'ici !")

        dialogueNum+=1
        can1.after(2500, cinematicPolicier1)
########################################################################################################################MAIN
    elif dialogueNum == 1:
        can1.delete(dialogueTextPolicier)
        can1.delete(dialogueCerclePolicier)

        up()

        dialogueNum = 0
        isCinematic = False


def cinematicPolicier2():
    global dialogueNum, dialogueTextMain, dialogueTextPolicier, dialogueCerclePolicier, dialogueCercleMain, variableCinematic, affichageTouche, affichageMission, isCinematicFrancois, affichageArgent, isCinematic
    canTouche.delete(affichageTouche)
    canMission.delete(affichageMission)


########################################################################################################################FRANCOIS
    if dialogueNum == 0:
        isCinematic = True

        dialogueCerclePolicier = can1.create_oval(posXpolicier+64, posYpolicier+64, posXpolicier+320, posYpolicier-32, fill="#FFC030")
        dialogueTextPolicier = can1.create_text(posXpolicier+192,posYpolicier+16, justify="center",font=('Times', '16', 'italic') ,text="Yo, il est frais ton uniforme !")

        dialogueNum+=1
        can1.after(2000, cinematicPolicier2)
########################################################################################################################MAIN
    elif dialogueNum == 1:
        can1.delete(dialogueTextPolicier)
        can1.delete(dialogueCerclePolicier)

        dialogueCercleMain = can1.create_oval(posX, posY + 64, posX - 206, posY - 32, fill="#FFC030")
        dialogueTextMain = can1.create_text(posX - 106, posY + 16, justify="center", font=('Times', '14', 'italic'),text="T'as vu ça ! Je vais\n sortir un peu tu peux\n ouvrir la grille ?")

        dialogueNum += 1
        can1.after(4000, cinematicPolicier2)
########################################################################################################################MAIN
    elif dialogueNum == 2:
        can1.delete(dialogueTextMain)
        can1.delete(dialogueCercleMain)

        dialogueCerclePolicier = can1.create_oval(posXpolicier+64, posYpolicier+64, posXpolicier+320, posYpolicier-32, fill="#FFC030")
        dialogueTextPolicier = can1.create_text(posXpolicier+192,posYpolicier+16, justify="center",font=('Times', '16', 'italic') ,text="Vas-y pas de problème !")

        dialogueNum+=1
        can1.after(2000, cinematicPolicier2)
########################################################################################################################MAIN
    elif dialogueNum == 3:
        can1.delete(dialogueTextPolicier)
        can1.delete(dialogueCerclePolicier)


        dialogueNum += 1
        can1.after(1000, cinematicPolicier2)
        pygame.mixer.stop()
        end_song.play(0, 0, 500)
    elif dialogueNum == 4:
        data['ecranNum'] += 1

        ecranCinematique()





window.resizable(width=False, height=False) #empecher la fênetre d'être en plein ecran ou modifier ses dimensions
window.mainloop()




#SYSTEME DE SAUVEGARDE TEST...
def saves():
    data['can1x']=can1x
    data['can1y']=can1y
    data['posX']=posX
    data['posY'] =posY
    with open("saves.txt", "w") as f:
        for k in data.keys():
            f.write(f"{k}:{data[k]}\n")
