import pygame
from random import choice





#pygame alustus
pygame.init()
naytto = pygame.display.set_mode((640, 480))
kello = pygame.time.Clock()
naytto_r = 30
naytto_g = 30
naytto_b = 30
#kuvat
robo = pygame.image.load("robo.png")
hirviokuva = pygame.image.load("hirvio.png")
tele_kuva = pygame.image.load("ovi.png")
kolikko_kuva = pygame.image.load("kolikko.png")

#koordinaatit
robo_x = 320-robo.get_width()
robo_y = 240-robo.get_height()

hiiri_x = 0
hiiri_y = 0

tele_x1 = -100
tele_y1 = -100
tele_x2 = -100
tele_y2 = -100

kolikko_x = 0
kolikko_y = 0

#satunnaiskoordinaatit
randomkipina = [-5,-1,1,2,-2,0,5,]

class Perks:
    perk_list = []
    laser_bounce = ["Laser Bounce",50,1,"Laser Bounces Once"]
    laser_explosion = ["Explosive Laser",50,2,"Targets Explode"]
    vampire_laser = ["Bravery Laser",50,3,"Laser Lowers Spook"]
    teleport_vacuum = ["Vacuum Teleport",50,4,"Teleport Destroys Ghosts"]
    combo_boost = ["Combo Boost",50,5,"Combo Increases Attributes"]
    saldo = ["Coins available",None,None]
    perk_list.append(laser_bounce)
    perk_list.append(laser_explosion)
    perk_list.append(vampire_laser)
    perk_list.append(teleport_vacuum)
    perk_list.append(combo_boost)
    perk_list.append(saldo)

#päivityksiä
class Upgrades:
    upgrade_list = []
    laser_damage = ["Laser Damage",1,1]
    nopeus_upgrade = ["Robo-Speed",1,2]
    energia_kulutus_upgrade = ["Battery Efficiency",1,3]
    patteri_overcharge = ["Battery Over-charge",1,4]
    patteri_recharge = ["Battery recharge speed",1,5]
    combo_upgrade = ["Maximum Combo Upgrade",1,6]
    saldo = ["Coins available",None,None]
    upgrade_list.append(laser_damage)
    upgrade_list.append(nopeus_upgrade)
    upgrade_list.append(energia_kulutus_upgrade)
    upgrade_list.append(patteri_overcharge)
    upgrade_list.append(patteri_recharge)
    upgrade_list.append(combo_upgrade)

    upgrade_list.append(saldo)

#attribuutteja
class Attributes:
    suurin_combo = 0
    maximi_combo = 4
    maximi_patteri = 100
    patteri = 100 
    laser_teho = 1 
    energia_kulutus = 0.7
    robo_spook = 0
    robo_nopeus = 1.5
    pisteet = 0
    manaukset = 0
    kolikot = 0
    kolikkoja_keratty = 0
    robo_lataus_nopeus = 1
    reboot_nopeus = 1
    tele_energia = 25
    tele_kesto = 4
    kolikko_haavi = 1

#taso
taso = 1

#hirvioita
hirvio_hp = 100
hirvio_suunta = 1
hirvio_nopeus = 1
hirvio_nopeus_variaatio = [1,1.1,1.2,1.3,1.4,1.5]
hirviolista = []
hirviomaara = 10
suunnat = [1,2,3,4]
    

#totuusarvot
virta_paalla = True
oikealle = False
vasemmalle = False
alas = False
ylos = False
laser = False
palojalki = False
palojaljet = []
paloajastin = 1
kipinat = False
teleport = False
kolikko = False
kolikko_pelissa = False
isommaksi = True
pienemmaksi = False
isommaksi_g = True
pienemmaksi_g = False
isommaksi_b = True
pienemmaksi_b = False
intro = False
#perks
bounce = False
vampire = False
vacuum = False
boost = False
explosion = False
#ajastimet
tele_ajastin = 2
kolikko_ajastin = 0
combo = 0

def start_game():
    r = 254
    g = 254
    b = 254
    for i in range(640):
            
            pygame.draw.line(naytto, (r, g, b), (i,0), (i, 480), 1)
            if r> 1:
                r-=1
            if r<= 1 and g>1:
                g-=1
            if g<2:
                b-=1
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                quit()
            if tapahtuma.type == pygame.KEYDOWN:
                
                return
        fontti = pygame.font.SysFont("Futura", 100)
        fontti2 = pygame.font.SysFont("Futura", 90)
        fontti3 = pygame.font.SysFont("Futura", 20)
        teksti = "ROBO-EXORCIST"
        teksti2 = "ROBO-EXORCIST"
        teksti3 = "Manaa kummituksia ja kerää kolikoita"
        teksti4 = "Kerrytät comboa kunnes kummitus osuu robottiin tai kolikko valuu ohi"
        teksti5 = "Combo vaikuttaa pisteisiin ja rahaan"
        teksti6 = "Käytä rahaa robotin päivittämiseksi"
        teksti7 = "Paina näppäintä aloittaaksesi"
        teksti = fontti.render(teksti, True, (0, 0, 0))
        teksti2 = fontti2.render(teksti2, True, (255, 255, 255))
        teksti3 = fontti3.render(teksti3, True, (0, 0, 0))
        teksti4 = fontti3.render(teksti4, True, (0, 0, 0))
        teksti5 = fontti3.render(teksti5, True, (0, 0, 0))
        teksti6 = fontti3.render(teksti6, True, (0, 0, 0))
        teksti7 = fontti3.render(teksti7, True, (0, 0, 0))
        pygame.draw.rect(naytto, (255, 255, 255), ((320-teksti4.get_width()/2, 180, 445,100)))
        naytto.blit(teksti, (320-teksti.get_width()/2, 100))
        naytto.blit(teksti2, (320-teksti2.get_width()/2, 100))
        naytto.blit(teksti3, (320-teksti3.get_width()/2, 180))
        naytto.blit(teksti4, (320-teksti4.get_width()/2, 200))
        naytto.blit(teksti5, (320-teksti5.get_width()/2, 220))
        naytto.blit(teksti6, (320-teksti6.get_width()/2, 240))
        naytto.blit(teksti7, (320-teksti7.get_width()/2, 260))
        pygame.display.flip()
        kello.tick(60)



def game_over():
    r = 1
    g = 1
    b = 1
    for i in range(640):
            
            pygame.draw.line(naytto, (r, g, b), (i,0), (i, 480), 1)
            if r< 255:
                r+=1
            if r>= 254 and g<254:
                g+=1
            if g>=254:
                b+=1
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                quit()
            if tapahtuma.type == pygame.KEYDOWN:
                quit()
        fontti = pygame.font.SysFont("Futura", 100)
        fontti2 = pygame.font.SysFont("Futura", 90)
        fontti3 = pygame.font.SysFont("Futura", 30)
        teksti = "GAME OVER"
        teksti2 = "GAME OVER"
        teksti3 = f"You scored {int(Attributes.pisteet)} points!"
        teksti4 = f"You exorsized {Attributes.manaukset} ghosts!"
        teksti5 = f"You collected {Attributes.kolikkoja_keratty} coins!"
        teksti6 = f"Your best combo was {Attributes.suurin_combo}!"
        teksti = fontti.render(teksti, True, (0, 0, 0))
        teksti2 = fontti2.render(teksti2, True, (255, 255, 255))
        teksti3 = fontti3.render(teksti3, True, (0, 0, 0))
        teksti4 = fontti3.render(teksti4, True, (0, 0, 0))
        teksti5 = fontti3.render(teksti5, True, (0, 0, 0))
        teksti6 = fontti3.render(teksti6, True, (0, 0, 0))
        naytto.blit(teksti, (320-teksti.get_width()/2, 240))
        naytto.blit(teksti2, (320-teksti2.get_width()/2, 240))
        naytto.blit(teksti3, (320-teksti3.get_width()/2, 300))
        naytto.blit(teksti4, (320-teksti3.get_width()/2, 330))
        naytto.blit(teksti5, (320-teksti3.get_width()/2, 360))
        naytto.blit(teksti6, (320-teksti3.get_width()/2, 390))
        pygame.display.flip()
        kello.tick(60)
def perks():
    
        fontti = pygame.font.SysFont("Futura", 48)
        teksti = f"ROBO-PERKS"
        kauppa_teksti = fontti.render(teksti, True, (255, 15, 15))
        naytto.fill((0, 0, 0))
        naytto.blit(kauppa_teksti, (320-kauppa_teksti.get_width()/2, 0))
        upgrade_ohjeet = []
        for i in (Perks.perk_list):
            upgrade_nimi = i[0]
            upgrade_taso = i[1]
            upgrade_nappula = i[2]
            upgrade_ohje_alku = "OPTION ["
            upgrade_ohje_keski = "COST ["
            upgrade_ohje_loppu ="€] PRESS TO UNLOCK-->"
            upgrade_ohje_koko = upgrade_ohje_alku+upgrade_nimi+"]"+" "*(25-len(upgrade_nimi))+upgrade_ohje_keski+str(upgrade_taso)+upgrade_ohje_loppu +str(upgrade_nappula)
            if upgrade_taso == None:
                upgrade_ohje_koko = f"WORK IN PROGRESS, SORRY! PRESS (U) for Upgrades"
            upgrade_ohjeet.append(upgrade_ohje_koko)
        for i in range(len(upgrade_ohjeet)):
            fontti = pygame.font.SysFont("Futura", 24)
            upgrade_ohje_teksti = fontti.render(upgrade_ohjeet[i], True, (248,248,255))
            if i+1 == len(upgrade_ohjeet):
                fontti = pygame.font.SysFont("Futura", 36)
                upgrade_ohje_teksti = fontti.render(upgrade_ohjeet[i], True, (248,50,255))
            naytto.blit(upgrade_ohje_teksti, (0,30*(i+1)))
        

def upgrades(): 
        fontti = pygame.font.SysFont("Futura", 48)
        teksti = f"ROBO-UPGRADES"
        kauppa_teksti = fontti.render(teksti, True, (255, 15, 15))
        naytto.fill((0, 0, 0))
        naytto.blit(kauppa_teksti, (320-kauppa_teksti.get_width()/2, 0))
        upgrade_ohjeet = []
        for i in (Upgrades.upgrade_list):
            upgrade_nimi = i[0]
            upgrade_taso = i[1]
            upgrade_nappula = i[2]
            upgrade_ohje_alku = "OPTION ["
            upgrade_ohje_keski = "COST ["
            upgrade_ohje_loppu ="€] PRESS TO UPGRADE-->"
            upgrade_ohje_koko = upgrade_ohje_alku+upgrade_nimi+"]"+" "*(25-len(upgrade_nimi))+upgrade_ohje_keski+str(upgrade_taso)+upgrade_ohje_loppu +str(upgrade_nappula)
            if upgrade_taso == None:
                upgrade_ohje_koko = f"Money available: [{Attributes.kolikot}€] PRESS (P) for perks"
            upgrade_ohjeet.append(upgrade_ohje_koko)
        for i in range(len(upgrade_ohjeet)):
            fontti = pygame.font.SysFont("Futura", 24)
            upgrade_ohje_teksti = fontti.render(upgrade_ohjeet[i], True, (248,248,255))
            if i+1 == len(upgrade_ohjeet):
                fontti = pygame.font.SysFont("Futura", 36)
                upgrade_ohje_teksti = fontti.render(upgrade_ohjeet[i], True, (248,50,255))
            naytto.blit(upgrade_ohje_teksti, (0,30*(i+1)))
        
        
def kauppa():
    fontti = pygame.font.SysFont("Futura", 48)
    teksti = f"ROBO-SHOP"
    kauppa_teksti = fontti.render(teksti, True, (255, 15, 15))
    naytto.fill((0, 0, 0))
    naytto.blit(kauppa_teksti, (320-kauppa_teksti.get_width()/2, 0))
    upgrades()
    while True:
        for tapahtuma in pygame.event.get():
            if tapahtuma.type == pygame.QUIT:
                return
            if tapahtuma.type == pygame.KEYDOWN:
                if tapahtuma.key == pygame.K_ESCAPE or tapahtuma.key == pygame.K_TAB:
                    return
            if tapahtuma.type == pygame.KEYDOWN:
                pygame.display.flip()
                kello.tick(60)
                if tapahtuma.key == pygame.K_1 and Attributes.kolikot>=Upgrades.laser_damage[1]:
                    Attributes.kolikot -= Upgrades.laser_damage[1]
                    Upgrades.laser_damage[1]+=1
                    Attributes.laser_teho += 0.2
                    upgrades()
                if tapahtuma.key == pygame.K_2 and Attributes.kolikot>=Upgrades.nopeus_upgrade[1]:
                    Attributes.kolikot -= Upgrades.nopeus_upgrade[1]
                    Upgrades.nopeus_upgrade[1]+=1
                    Attributes.robo_nopeus += 0.2
                    upgrades()
                if tapahtuma.key == pygame.K_3 and Attributes.kolikot>=Upgrades.energia_kulutus_upgrade[1]:
                    Attributes.kolikot -= Upgrades.energia_kulutus_upgrade[1]
                    Upgrades.energia_kulutus_upgrade[1]+=1
                    Attributes.energia_kulutus *= 0.95
                    upgrades()
                if tapahtuma.key == pygame.K_4 and Attributes.kolikot>=Upgrades.patteri_overcharge[1]:
                    Attributes.kolikot -= Upgrades.patteri_overcharge[1]
                    Upgrades.patteri_overcharge[1]+=1
                    Attributes.maximi_patteri += 2
                    upgrades()
                if tapahtuma.key == pygame.K_5 and Attributes.kolikot>=Upgrades.patteri_recharge[1]:
                    Attributes.kolikot -= Upgrades.patteri_recharge[1]
                    Upgrades.patteri_recharge[1]+=1
                    Attributes.robo_lataus_nopeus += 0.2
                    upgrades()
                if tapahtuma.key == pygame.K_6 and Attributes.kolikot>=Upgrades.combo_upgrade[1]:
                    Attributes.kolikot -= Upgrades.combo_upgrade[1]
                    Upgrades.combo_upgrade[1]+=1
                    Attributes.maximi_combo += 2
                    upgrades()
                if tapahtuma.key == pygame.K_p:
                    naytto.fill((0, 0, 0))
                    perks()
                if tapahtuma.key == pygame.K_u:
                    naytto.fill((0, 0, 0))
                    upgrades()
        
        
            

        pygame.display.flip()
        kello.tick(60)
#tapahtumia
while True:
    if intro == False:
        start_game()
        intro = True
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEMOTION:
            hiiri_x = tapahtuma.pos[0]
            hiiri_y = tapahtuma.pos[1]
            if palojalki == True:
                if (hiiri_x,hiiri_y,paloajastin) not in palojaljet:
                    palojaljet.append([hiiri_x,hiiri_y,paloajastin])

        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            if Attributes.patteri > 0:
                palojalki = True
                kipinat = True
                laser = True
                
        if tapahtuma.type == pygame.MOUSEBUTTONUP:  
            laser = False
            palojalki = False
            kipinat = False
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_a:
                vasemmalle = True
            if tapahtuma.key == pygame.K_d:
                oikealle = True
            if tapahtuma.key == pygame.K_w:
                ylos = True
            if tapahtuma.key == pygame.K_s:
                alas = True
            
            if tapahtuma.key == pygame.K_SPACE:
                if Attributes.patteri > Attributes.tele_energia:
                    teleport = True
                    Attributes.patteri -= 50
                    tele_x1 = hiiri_x-(tele_kuva.get_width()/2)
                    tele_y1 = hiiri_y-(tele_kuva.get_height()/2)
                    tele_x2 = robo_x
                    tele_y2 = robo_y
            
            if tapahtuma.key == pygame.K_ESCAPE or tapahtuma.key == pygame.K_TAB:
                kauppa()
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_a:
                vasemmalle = False
            if tapahtuma.key == pygame.K_d:
                oikealle = False
            if tapahtuma.key == pygame.K_w:
                ylos = False
            if tapahtuma.key == pygame.K_s:
                alas = False
        
        if tapahtuma.type == pygame.QUIT:
            exit()

    if oikealle and virta_paalla:
        if robo_x < 640-robo.get_width():
            robo_x += 0.8*Attributes.robo_nopeus
    if vasemmalle and virta_paalla:
        if robo_x > 0:
            robo_x -= 0.8*Attributes.robo_nopeus
    if alas and virta_paalla:
        if robo_y < 480-robo.get_height():
            robo_y += 0.8*Attributes.robo_nopeus
    if ylos and virta_paalla:
        if robo_y > 0:
            robo_y -= 0.8*Attributes.robo_nopeus
    

    #näytön piirto
    naytto.fill((naytto_r, naytto_g, naytto_b))#tausta
    
    fontti = pygame.font.SysFont("Futura", 24)#tekstit
    fontti2 = pygame.font.SysFont("Futura", 48)
    score = f"Battery depleted, rebooting..."
    Attributes.patteri_teksti = fontti.render(score, True, (255, 15, 15))
    if Attributes.patteri > 50:
        score = f"Battery: {int(Attributes.patteri)}%"
        Attributes.patteri_teksti = fontti.render(score, True, (34, 139, 13))
    elif Attributes.patteri > 0:
        score = f"Battery: {int(Attributes.patteri)}%"
        Attributes.patteri_teksti = fontti.render(score, True, (255, 215, 0))
    
    
    if Attributes.robo_spook < 50:
        spookmeter = f"Spook-O-meter: {int(Attributes.robo_spook)}%"
        spook_teksti = fontti.render(spookmeter, True, (128, 3, 3))
    elif Attributes.robo_spook >= 50 and Attributes.robo_spook<90:
        spookmeter = f"Spook-O-meter: {int(Attributes.robo_spook)}% WARNING: SCARY!"
        spook_teksti = fontti.render(spookmeter, True, (128, 3, 3))
    else:
        spookmeter = f"Spook-O-meter: {int(Attributes.robo_spook)}% WARNING: EXTREME SPOOK LEVELS DETECTED!"
        spook_teksti = fontti.render(spookmeter, True, (128, 3, 3))
    
    pistestring = f"{int(Attributes.pisteet)}"
    piste_teksti1 = fontti.render(pistestring, True, (245,255,250))
    pistestring2 = f"Points:"
    piste_teksti2 = fontti.render(pistestring2, True, (245,255,250))

    
    kolikkostring = f"{str(Attributes.kolikot)} €"
    kolikko_teksti = fontti2.render(kolikkostring, True, (245,255,250))

    combostring = f"Combo {combo}x!"
    combo_teksti = fontti.render(combostring, True, (245,255,250))
    
    ohje1 = "MOVE: WASD or Arrowkeys"
    ohje_teksti1 = fontti.render(ohje1, True, (0,245,255))
    ohje2 = "LASER: MOUSE"
    ohje_teksti2 = fontti.render(ohje2, True, (0,245,255))
    ohje3 = "TELEPORT: SPACEBAR"
    ohje_teksti3 = fontti.render(ohje3, True, (0,245,255))
    ohje4 = "SHOP: TAB or ESC"
    ohje_teksti4 = fontti.render(ohje4, True, (0,245,255))
    
    
    
    #info & ohjeet
    pygame.draw.rect(naytto, (0, 0, 100), (0, 0, 640,0+kolikko_kuva.get_height()))
    
    pygame.draw.rect(naytto, (0, 0, 100), (420, 410, 640,480))
    pygame.draw.rect(naytto, (0, 255, 0), (0, 480-kolikko_kuva.get_height(), 150,480-kolikko_kuva.get_height()))
    naytto.blit(kolikko_kuva, (0, 480-kolikko_kuva.get_height()))
    naytto.blit(kolikko_teksti, (kolikko_kuva.get_width()+8,480-kolikko_teksti.get_height()))
    naytto.blit(spook_teksti, (0, 20))
    naytto.blit(Attributes.patteri_teksti, (0, 0))
    if combo>1:
        naytto.blit(combo_teksti,(640-combo_teksti.get_width(),20))
    naytto.blit(ohje_teksti1, (640-ohje_teksti1.get_width(),480-ohje_teksti1.get_height()))
    naytto.blit(ohje_teksti2, (640-ohje_teksti2.get_width(),480-(ohje_teksti2.get_height()*2)))
    naytto.blit(ohje_teksti3, (640-ohje_teksti3.get_width(),480-(ohje_teksti2.get_height()*3)))
    naytto.blit(ohje_teksti4, (640-ohje_teksti4.get_width(),480-(ohje_teksti2.get_height()*4)))
    naytto.blit(piste_teksti1, (640-piste_teksti1.get_width(),0))
    naytto.blit(piste_teksti2, (520,0))
    
    
    suunta = choice(suunnat)

    if teleport:
        naytto.blit(tele_kuva,(tele_x1,tele_y1))
        naytto.blit(tele_kuva,(tele_x2,tele_y2))
        tele_ajastin -= 0.01*Attributes.tele_kesto
        if tele_ajastin < 0:
            teleport = False
            tele_ajastin = 1
    if abs(tele_x1-robo_x) < 5 and abs(tele_y1-robo_y) < 5 and teleport:
        if vasemmalle:
            robo_x = tele_x2-10
            robo_y = tele_y2
        if oikealle:
            robo_x = tele_x2+10
            robo_y = tele_y2
        if alas:
            robo_x = tele_x2
            robo_y = tele_y2+10
        if ylos:
            robo_x = tele_x2
            robo_y = tele_y2-10
    if abs(tele_x2-robo_x) < 5 and abs(tele_y2-robo_y) < 5 and teleport:
        if vasemmalle:
            robo_x = tele_x1-10
            robo_y = tele_y1
        if oikealle:
            robo_x = tele_x1+10
            robo_y = tele_y1
        if alas:
            robo_x = tele_x1
            robo_y = tele_y1+10
        if ylos:
            robo_x = tele_x1
            robo_y = tele_y1-10
    
    
    
    
    if len(hirviolista)< hirviomaara and suunta==1 or taso == 1 and len(hirviolista)<hirviomaara:
        hirvio_x = [number-hirviokuva.get_width() for number in range(641)]
        hirvio_y = [-number for number in range(50,400)]
        hirvio_suunta_x = 0
        hirvio_suunta_y = 1
        ylahirvio = [choice(hirvio_x),choice(hirvio_y),hirviokuva,hirvio_hp,hirvio_suunta_x,hirvio_suunta_y,hirvio_nopeus*choice(hirvio_nopeus_variaatio)]
        hirviolista.append(ylahirvio)
    if len(hirviolista)<hirviomaara and taso >= 2 and suunta==2:
        hirvio_x = [number-hirviokuva.get_width() for number in range(641)]
        hirvio_y = [number+530 for number in range(100)]
        hirvio_suunta_x = 0
        hirvio_suunta_y = -1
        alahirvio = [choice(hirvio_x),choice(hirvio_y),hirviokuva,hirvio_hp,hirvio_suunta_x,hirvio_suunta_y,hirvio_nopeus*choice(hirvio_nopeus_variaatio)]
        hirviolista.append(alahirvio)
    if len(hirviolista)<hirviomaara and taso >= 3 and suunta==3:
        hirvio_x = [number+690 for number in range(100)]
        hirvio_y = [number-hirviokuva.get_height() for number in range(481)]
        hirvio_suunta_x = -1
        hirvio_suunta_y = 0
        vasenhirvio = [choice(hirvio_x),choice(hirvio_y),hirviokuva,hirvio_hp,hirvio_suunta_x,hirvio_suunta_y,hirvio_nopeus*choice(hirvio_nopeus_variaatio)]
        hirviolista.append(vasenhirvio)
    if len(hirviolista)<hirviomaara and taso >= 4 and suunta==4:
        hirvio_x = [-number for number in range(50,300)]
        hirvio_y = [number-hirviokuva.get_height() for number in range(50,590)]
        hirvio_suunta_x = 1
        hirvio_suunta_y = 0
        oikeahirvio = [choice(hirvio_x),choice(hirvio_y),hirviokuva,hirvio_hp,hirvio_suunta_x,hirvio_suunta_y,hirvio_nopeus*choice(hirvio_nopeus_variaatio)]
        hirviolista.append(oikeahirvio)
    
    naytto.blit(robo, (robo_x, robo_y)) #pelaaja
    
    for hirvio in hirviolista:
        naytto.blit(hirvio[2], (hirvio[0], hirvio[1]))
        if hirvio[5]==-1 and hirvio[1] < -30:
            hirviolista.remove(hirvio)
        if hirvio[5]==1 and hirvio[1] > 510:
            hirviolista.remove(hirvio)
        if hirvio[4]==-1 and hirvio[0] < -30:
            hirviolista.remove(hirvio)
        if hirvio[4]==1 and hirvio[0] > 670:
            hirviolista.remove(hirvio)
        
        hirvio[1]+=hirvio[5]*hirvio[6]
        hirvio[0]+=hirvio[4]*hirvio[6]
        
        if abs((hirvio[0]+(hirviokuva.get_width()/2))-(hiiri_x)) < 20 and abs((hirvio[1]+(hirviokuva.get_height()/2))-(hiiri_y)) < 20 and laser:
            hirvio[3]-= 5*Attributes.laser_teho
        if hirvio[3]<0: #hirvion tuhoaminen
            Attributes.pisteet += 1+1*combo
            Attributes.manaukset += 1
            if combo < Attributes.maximi_combo:
                combo += 1
            hirviolista.remove(hirvio)
        
        if abs((hirvio[0]+(hirviokuva.get_width()/2))-(robo_x+(robo.get_width()/2))) < 30 and abs((hirvio[1]+(hirviokuva.get_height()/2))-(robo_y+(robo.get_height()/2))) < 30:
            if combo > Attributes.suurin_combo:
                Attributes.suurin_combo = combo
            combo = 0
            hirvio[0] = robo_x
            hirvio[1] = robo_y
            Attributes.robo_spook += 0.5
        if Attributes.robo_spook > 100:
            game_over()

    
    

    if laser:
        pygame.draw.line(naytto, (238, 0, 0), (robo_x+15, robo_y+15), (hiiri_x, hiiri_y), 2)
        pygame.draw.line(naytto, (238, 0, 0), (robo_x+30, robo_y+15), (hiiri_x+15, hiiri_y), 2)
        Attributes.patteri -= 1.5*Attributes.energia_kulutus
        if Attributes.patteri <= 0:
            virta_paalla = False
            laser = False
            kipinat = False
            palojalki = False
            Attributes.patteri = -20
    if kipinat:
        for i in range(3):
            pygame.draw.line(naytto, (248,248,255), (hiiri_x, hiiri_y), (hiiri_x+choice(randomkipina), hiiri_y+choice(randomkipina)), 1)
            pygame.draw.line(naytto, (248,248,255), (hiiri_x+15, hiiri_y), (hiiri_x+15+choice(randomkipina), hiiri_y+choice(randomkipina)), 1)
    for jalki in palojaljet:
        if jalki[2]<=0:
            palojaljet.remove(jalki)
        pygame.draw.circle(naytto, (40, 40, 40), (jalki[0], jalki[1]), 5)
        pygame.draw.circle(naytto, (40, 40, 40), (jalki[0]+15, jalki[1]), 5)
        jalki[2] -= 0.05
    
    if kolikko:
        if kolikko_pelissa == False:
            kolikko_x = choice([number-kolikko_kuva.get_width() for number in range(30,610)])
            kolikko_y = -100
            kolikko_pelissa = True
        naytto.blit(kolikko_kuva,(kolikko_x,kolikko_y))
        kolikko_y += 1
    if abs(kolikko_x-robo_x) < 30*Attributes.kolikko_haavi and abs(kolikko_y-robo_y) < 30*Attributes.kolikko_haavi and kolikko:
        Attributes.kolikkoja_keratty += 1
        if combo >= 1:
            Attributes.kolikot += 1*combo
        elif combo == 0:
            Attributes.kolikot += 1
        Attributes.pisteet += 50
        kolikko = False
        kolikko_pelissa = False
        if combo < Attributes.maximi_combo:
            combo += 1
    if kolikko_y >500:
        kolikko = False
        kolikko_pelissa = False
        combo = 0
    #attribuuttimuutokset
    if Attributes.patteri < Attributes.maximi_patteri and laser == False and virta_paalla== True:
        Attributes.patteri += 0.2*Attributes.robo_lataus_nopeus
    if virta_paalla == False:
        Attributes.patteri += 0.2*Attributes.reboot_nopeus
    if Attributes.patteri > 0:
        virta_paalla = True
    
    if Attributes.robo_spook>0:
        Attributes.robo_spook -=0.01
    if kolikko_ajastin > 0 and kolikko == False:
        kolikko_ajastin -= 0.01
    if kolikko_ajastin <= 0:
        kolikko = True
        kolikko_ajastin = 1
    Attributes.pisteet += 0.01*combo
    
    if Attributes.pisteet < 100:
        hirviomaara = 5
        taso = 1
    elif Attributes.pisteet > 200 and Attributes.pisteet < 500:
        hirviomaara = 8
        taso = 2
    elif Attributes.pisteet > 500 and Attributes.pisteet < 1000:
        hirviomaara = 11
        taso = 3
    elif Attributes.pisteet > 1000:
        hirviomaara = 12
        taso = 4
    if Attributes.pisteet > 10000:
        hirvio_nopeus += Attributes.pisteet/100000
    if Attributes.pisteet > 10000:
        hirviomaara += Attributes.pisteet/10000
    
    
    
    pygame.display.update()
    if naytto_r < 255 and isommaksi:
        naytto_r +=0.01*combo
    if naytto_r == 255:
        pienemmaksi = True
        isommaksi = False
    if naytto_r > 0 and pienemmaksi:
        naytto_r -=0.01*combo
    if naytto_r == 0:
        pienemmaksi = False
        isommaksi = True
    
    if naytto_g < 255 and isommaksi_g:
        naytto_g +=0.005*combo
    if naytto_g > 254:
        pienemmaksi_g = True
        isommaksi_g = False
    if naytto_g > 0 and pienemmaksi_g:
        naytto_g -=0.005*combo
    if naytto_g < 1:
        pienemmaksi_g = False
        isommaksi_g = True
    
    if naytto_b< 255 and isommaksi_b:
        naytto_b+=0.0125*combo
    if naytto_b> 254:
        pienemmaksi_b= True
        isommaksi_b= False
    if naytto_b> 1 and pienemmaksi_b:
        naytto_b-=0.0125*combo 
    if naytto_b< 0 and pienemmaksi_b:
        pienemmaksi_b= False
        isommaksi_b= True
    
    
    
    kello.tick(60)