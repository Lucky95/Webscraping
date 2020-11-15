#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.common.Keys import Keys 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
PATH2 = "C:\\Users\ibrahim\\Desktop\\chromedriver.exe"
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


# In[2]:


#creer colonne
colonne =["Nom","Photo","Description","Contenu","Récompenses","Auteur","Auteur2","Auteur3","Auteur4","Illustrateurs","Illustrateurs2","Illustrateurs3","Illustrateurs4","Mecanisme","Mecanisme2","Mecanisme3","Mecanisme4","Theme","theme2","theme3","theme4","Age","Nombre joueurs","Temps","Note","Prix","Description2","Durée"]
#ligne=[]
print(colonne)
df2 = pd.DataFrame(columns = colonne)
print(df2)


# In[3]:


"""ETAPE 1 SE CONNECTER SUR LA PAGE OU Y A TOUS LES PROFIL"""

driver.get("https://www.philibertnet.com/fr/50-jeux-de-societe?orderby=sales&orderway=desc#content_sortPagiBar_top")
time.sleep(2)
#accepter les cookies
driver.find_element_by_xpath('//*[@id="allow_all"]').click() 
time.sleep(5)


# In[4]:


liste_site= []
compteur=0
i=0
for j in range(133,206):
    print("page egale a",j)
    site78=liste_site.append("https://www.philibertnet.com/fr/50-jeux-de-societe?orderby=sales&orderway=desc&p="+str(j))
    driver.get(liste_site[i])
    i+=1
    for nb in range(1,20):
        
        print("compteur egale a",compteur)
        ligne=[]
        #je clique sur le jeu de société 
        time.sleep(2)
        clique=driver.find_element_by_xpath(str("""//*[@id="center_column"]/ul/li["""+str(nb)+"""]/div/div[2]/p[1]/a""")).click()
        #ON PREND LES NOMS 1
        time.sleep(4)
        Nom=driver.find_element_by_xpath('//*[@id="product_name"]')
        print(Nom.text)
        ligne.append(Nom.text)
        time.sleep(1)
        #ON PREND LA PHOTO 2
        photo = driver.find_element_by_css_selector("#bigpic").get_attribute("src")
        print(photo)
        ligne.append(photo)
        print(len(ligne))
        print(ligne)
        #CLIQUE SUR LA DESCRIPTION 3
        try :
            descript=driver.find_element_by_xpath('//*[@id="short_description_content"]')
            descript.text
            ligne.append(descript.text)
            print(ligne)
        #cliquer sur contenu
            time.sleep(1)
        except:
                descript2=driver.find_element_by_xpath('//*[@id="tab-description"]/div/p/em[1]')
                descript2.text
                ligne.append(descript2.text)
                time.sleep(1)
        try :#4
            driver.find_element_by_link_text("Contenu").click()
            cont=driver.find_element_by_xpath('//*[@id="tab-content"]')
            ligne.append(cont.text)
            print("ça marche")
        except :
            ligne.append(".")
            print("pas de contenu")
            print(len(ligne))
            print(ligne)
            time.sleep(1)
        #cliquer sur les recompenses
        time.sleep(1)
        try :#5
            driver.find_element_by_link_text("Récompenses").click()
            time.sleep(1)
            rep=driver.find_element_by_xpath('//*[@id="ukooawards_award_5"]/a/p' )
            print(rep.text)
            print("hello")
            recompense=rep.text
            ligne.append(rep.text)
        except :
            print("pas de RECOMPENSE")
            ligne.append(".")
        caractéristique=driver.find_element_by_link_text("Fiche technique").click()
        time.sleep(3)

        bloc=driver.find_element_by_xpath('//*[@id="tab-features"]')
        a=bloc.text
        les_carac=a.split("\n")


        comptA=1
        for j in range (len(les_carac)):
            if les_carac[j].startswith("Auteur(s)") == True :
                print("vrai")
                auteur=les_carac[j][10:]
                #je veux pas tout
                auteurplit=auteur.split(',')
                if len(auteurplit) == 1: 
                    ligne.append(auteurplit[0])
                    ligne.append(".")
                    ligne.append(".")
                    ligne.append(".")
                if len(auteurplit) == 2: 
                    ligne.append(auteurplit[0])
                    ligne.append(auteurplit[1])
                    ligne.append(".")
                    ligne.append(".")
                if len(auteurplit) == 3: 
                    ligne.append(auteurplit[0])
                    ligne.append(auteurplit[1])
                    ligne.append(auteurplit[2])
                    ligne.append(".")
                if len(auteurplit) == 4: 
                    ligne.append(auteurplit[0])
                    ligne.append(auteurplit[1])
                    ligne.append(auteurplit[2])
                    ligne.append(auteurplit[3])
                trouve=1
                print(comptA,"nombre auteur")
                break
            else :
                print("pas d'auteur")
                ligne.append(".")
                ligne.append(".")
                ligne.append(".")
                ligne.append(".")
                break
            if comptA==7:
                print("valeur abente")
            comptA+=1
        comptI=1
        for j in range (len(les_carac)):
                if les_carac[j].startswith("Illustrateur") == True :
                    print("y a des illustrateurs")
                    Illustrateur=les_carac[j][13:]
                    #je veux pas tout
                    Illustrateursplit=Illustrateur.split(',')
                    if len(Illustrateursplit) == 1: 
                        ligne.append(Illustrateursplit[0])
                        ligne.append(".")
                        ligne.append(".")
                        ligne.append(".")
                    if len(Illustrateursplit) == 2: 
                        ligne.append(Illustrateursplit[0])
                        ligne.append(Illustrateursplit[1])
                        ligne.append(".")
                        ligne.append(".")
                    if len(Illustrateursplit) == 3: 
                        ligne.append(Illustrateursplit[0])
                        ligne.append(Illustrateursplit[1])
                        ligne.append(Illustrateursplit[2])
                        ligne.append(".")
                    if len(Illustrateursplit) == 4: 
                        ligne.append(Illustrateursplit[0])
                        ligne.append(Illustrateursplit[1])
                        ligne.append(Illustrateursplit[2])
                        ligne.append(Illustrateursplit[3])
                    trouve=1
                    print(comptI)
                    break
                else :
                    print("pas d'illustrateu")
                    ligne.append(".")
                    ligne.append(".")
                    ligne.append(".")
                    ligne.append(".")
                    break
              
                comptI+=1
         
                
        comptM=1
        for j in range (len(les_carac)):
            if les_carac[j].startswith("Mécanisme(s)") == True :
                print("Y a le Mécanisme")
                mecanisme=les_carac[j][12:]
                #je veux pas tout
                mecasplit=mecanisme.split(',')
                if len(mecasplit) == 1: 
                    ligne.append(mecasplit[0])
                    ligne.append(".")
                    ligne.append(".")
                    ligne.append(".")
                if len(mecasplit) == 2: 
                    ligne.append(mecasplit[0])
                    ligne.append(mecasplit[1])
                    ligne.append(".")
                    ligne.append(".")
                if len(mecasplit) == 3: 
                    ligne.append(mecasplit[0])
                    ligne.append(mecasplit[1])
                    ligne.append(mecasplit[2])
                    ligne.append(".")
                if len(mecasplit) == 4: 
                    ligne.append(mecasplit[0])
                    ligne.append(mecasplit[1])
                    ligne.append(mecasplit[2])
                    ligne.append(mecasplit[3])
            
                trouve=1
                print(comptM)
                break
            else :
                print("pas de meca")
                ligne.append(".")
                ligne.append(".")
                ligne.append(".")
                ligne.append(".")
                break
            if comptM==7:
                print("valeur abente")
            comptM+=1
        comptT=1
        for j in range (len(les_carac)):
            if les_carac[j].startswith("Thème(s)") == True :
                print("Y a le thème")
                theme=les_carac[j][9:]
                #je veux pas tout
                themesplit=theme.split(',')
                if len(themesplit) == 1: 
                    ligne.append(themesplit[0])
                    ligne.append(".")
                    ligne.append(".")
                    ligne.append(".")
                if len(themesplit) == 2: 
                    ligne.append(themesplit[0])
                    ligne.append(themesplit[1])
                    ligne.append(".")
                    ligne.append(".")
                if len(themesplit) == 3: 
                    ligne.append(themesplit[0])
                    ligne.append(themesplit[1])
                    ligne.append(themesplit[2])
                    ligne.append(".")
                if len(themesplit) == 4: 
                    ligne.append(themesplit[0])
                    ligne.append(themesplit[1])
                    ligne.append(themesplit[2])
                    ligne.append(themesplit[3])
                trouve=1
                print(comptT)
                break
            else :
                print("pas de theme")
                ligne.append(".")
                ligne.append(".")
                ligne.append(".")
                ligne.append(".")
                break
            if comptT==7:
                print("valeur abente")
            comptT+=1

        #10
        try:
            age=driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/div[2]/ul[1]/li[2]')
            age.text
            ligne.append(age.text)
        except:
            ligne.append(".")
        #11
        try:
            nombre_joueurs=driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/div[2]/ul[1]/li[4]')
            nombre_joueurs.text
            ligne.append(nombre_joueurs.text)
        except: 
            ligne.append(".")
        #12
        try:
            temps = driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/div[2]/ul[1]/li[3]')
            temps.text
            ligne.append(temps.text)
        except:
            ligne.append(".")

        try:
            #13
            note=driver.find_element_by_xpath('//*[@id="blockukooreviews-product-extra-left"]/ul/li[1]/div/span[2]')
            note.text
            ligne.append(note.text)
        except :
            ligne.append(".")
        #14
        try:
            prix=driver.find_element_by_xpath('//*[@id="our_price_display"]')
            prix.text
            ligne.append(prix.text)
        except:
            ligne.append(".")

        print(len(ligne))
        #15
        try:
            descript2 = driver.find_element_by_xpath('//*[@id="short_description_block"]')
            descript2.text
            ligne.append(descript2.text)
        except:
            ligne.append(".")
        #16
        try:
            durée = driver.find_element_by_xpath('//*[@id="center_column"]/div/div[1]/div[2]/ul[1]/li[3]/span')
            durée.text
            ligne.append(durée.text)
        except:
            ligne.append(".")
        try:
            df2.loc[compteur]=ligne
            compteur+=1
            driver.back()
        except:
            driver.back()
        print(df2)


# In[10]:


df2.to_excel('6cents.xlsx', index=True,header=True )


# In[ ]:




