
class User:
  nb_user=0
  def __init__(self,ide,fname,lname,classe,genre,numero,answ):
    self.id=ide
    self.fname=fname
    self.lname=lname
    self.classe=classe
    self.genre=genre
    self.numero=numero
    self.answ=answ

bob=User("1","Bob","Carter","Seconde", "homme", "0100", {"1":'Seconde',"2":'Les deux',
"3":'Au macdo',"4":'Drôle',"5":'Franche',"6":'Casanier',"7":'Jalousie excessive',
"8":'Oui',"9":'Essayes de communiquer pour arranger les choses',"10":'Qui se ressemble s’assemble',"11":'Asie',"12":"Ninho"})

chad=User("2","Chad","Lokter","Terminale", "homme", "0600", {"1":'Terminale',"2":'Fille',
"3": 'Se balader dans un parc',"4":'Sociable',"5":'Attentionnée',"6": 'Tu calcules plus tes potes que ta meuf',
"7": 'Trop proche de ses ami(e)s',"8":'Non',"9":'T’excuses pas car t’as toujours raison',
"10":'Les opposés s’attirent',"11":'Amérique du Nord',"12":'Booba'})

tomah=User("3","Tomah","Peuret","Première", "homme", "0200", {"1":'Premiere',"2":'Fille',
"3":'Rdv romantique',"4":'Franche',"5":'Attentionnée',"6":'Jalousie excessive',"7":'Jalousie excessive',
"8":'Oui',"9":'Essayes de communiquer pour arranger les choses',"10":'Qui se ressemble s’assemble',"11":'Europe',"12":"Stromae"})

stephanie=User("4","Stephanie","Berelt","Première", "femme", "0900", {"1":'Premiere',"2":'Les deux',
"3":'Rdv romantique',"4":'Sociable',"5":'Drôle',"6":'Jalousie excessive',"7":'Trop proche de ses ami(e)s',
"8": 'Non',"9":'Cries un peu puis ça passe',"10":'Les opposés s’attirent',"11":'Océanie' ,"12":"Damso"})

betty=User("5","Betty","Laspière","Première", "femme", "0300", {"1":'Seconde',"2":'Gars',
"3":'Rdv romantique',"4":'Franche',"5":'Sociable',"6":'Casanier',"7":'Casanier',
"8": 'Oui',"9":'Essayes de communiquer pour arranger les choses',"10":'Les opposés s’attirent',"11":'Amérique du Nord' ,"12":"BTS"})

salia=User("6","Salia","Letire","Terminale", "femme", "0700", {"1":'Terminale',"2":'Peu importe',
"3":'Se balader dans un parc',"4":'Sociable',"5":'Drôle',"6":'Tu calcules plus tes potes que ta meuf',"7":'Casanier',
"8": 'Non',"9":'T’excuses pas car t’as toujours raison',"10": 'Qui se ressemble s’assemble',"11":'Amérique du Nord' ,"12":"BoOba"})

gael=User("7","Gael","Koldine","Terminale", "autre", "0800", {"1":'Terminale',"2":'Peu importe',
"3":'Rdv romantique',"4": 'Attentionnée',"5":'Franche',"6":'Jalousie excessive',"7": 'Trop proche de ses ami(e)s',
"8": 'Non',"9":'Cries un peu puis ça passe',"10": 'Les opposés s’attirent',"11":'Amérique du Sud' ,"12":"Ninho"})

list_user=[bob,chad,tomah,stephanie,betty,salia,gael]

def compatibility(user):
  #création d'une liste de la taille du nombre d'utilisateur, chaque nombre correspondra à l'indice de compatiblité avec les utilisateurs par leurs index respectivement
  #on va incrémenter l'indice de compatibilité de chaque utilisateur de la liste en fonction des réponses pour pouvoir les comparer à la fin
  compatarray=[0]*len(list_user)
  
  #On parcoure la liste(base de données) des utilisateurs
  for i in range(len(list_user)):
    #Maintenant on décrit les critères de compatibilité pour chaque réponse(si on incrémente/décrémente l'indice de compatibilité et de combien)
    
    #1: 
    classes=['Seconde','Premiere','Terminale']
    if user.answ["1"]==list_user[i].answ["1"]:
      compatarray[i]+=1
    elif abs(classes.index(user.answ["1"])-classes.index(list_user[i].answ["1"]))==1:
      compatarray[i]+=0.5
    elif abs(classes.index(user.answ["1"])-classes.index(list_user[i].answ["1"]))==1:
      compatarray[i]+=0.25
    
    #3:
    if user.answ["3"]==list_user[i].answ["3"]:
      compatarray[i]+=1
    elif user.answ["3"]!=list_user[i].answ["3"]:
      if user.answ["3"]=='Rdv romantique' and list_user[i].answ["3"]=='Se balader dans un parc':
        compatarray[i]+=0.5
      elif user.answ["3"]=='Se balader dans un parc' and list_user[i].answ["3"]=='Rdv romantique':
        compatarray[i]+=0.5
      elif user.answ["3"]=='Rdv romantique' and list_user[i].answ["3"]=='Au macdo':
        compatarray[i]-=1.5
      elif user.answ["3"]=='Au macdo' and list_user[i].answ["3"]=='Rdv romantique':
        compatarray[i]-=1.5
    
    #4 et 5:
    if user.answ["5"]==list_user[i].answ["4"] and list_user[i].answ["5"]==user.answ["4"]:
      compatarray[i]+=2
    
    #6 et 7:
    if user.answ["7"]==list_user[i].answ["6"]:
      compatarray[i]-=1
    elif user.answ["7"]=='Trop proche de ses ami(e)s' and list_user[i].answ["6"]=='Tu calcules plus tes potes que ta meuf':
      compatarray[i]-=1

    #8:
    if user.answ["8"]=="Oui":
      if list_user[i].answ["8"]=="Oui":
        compatarray[i]+=1
    elif user.answ["8"]=="Non":
      if list_user[i].answ["8"]=="Non":
        compatarray[i]+=0.5

    #9:
    if user.answ["9"]=='Essayes de communiquer pour arranger les choses':
      if list_user[i].answ["9"]=='Essayes de communiquer pour arranger les choses':
        compatarray[i]+=1
      elif list_user[i].answ["9"]=='Cries un peu puis ça passe':
        compatarray[i]+=0.5
      else:
        compatarray[i]+=0.25
    elif user.answ["9"]=='Cries un peu puis ça passe':
      if list_user[i].answ["9"]=='Essayes de communiquer pour arranger les choses':
        compatarray[i]+=0.5
    elif user.answ["9"]=='T’excuses pas car t’as toujours raison':
      if list_user[i].answ["9"]=='Essayes de communiquer pour arranger les choses':
        compatarray[i]+=0.25
    
    #10:
    if user.answ["10"]==list_user[i].answ["10"]:
      compatarray[i]+=1

    #11:
    if user.answ["11"]==list_user[i].answ["11"]:
      compatarray[i]+=1
    
    #12:
    if user.answ["12"].lower()==list_user[i].answ["12"].lower():
      compatarray[i]+=2
    #2:
    #Si les utilisateurs ne sont pas intéréssés l'un de l'autre en fonction de leur orientation sexuelle et leur genre, la compatibilité est de 0
    if user.genre=="autre":
      if list_user[i].answ["2"]!="Peu importe" and list_user[i].answ["2"]!="Les deux":
        compatarray[i]=0
    elif user.answ["2"]=="Fille":
      if list_user[i].genre!="femme":
        compatarray[i]=0
    elif user.answ["2"]=="Gars":
      if list_user[i].genre!="homme":
        compatarray[i]=0
    if list_user[i].answ["2"]=="Gars":
      if user.genre!="homme":
        compatarray[i]=0
    elif list_user[i].answ["2"]=="Fille":
      if user.genre!="femme":
        compatarray[i]=0
    if list_user[i]==user:
      compatarray[i]=0

  #Si l'indice de compatibilité est de 0 partout
  if sum(compatarray)==0:
    return "Que c'est dommage, vous n'êtes compatibles avec personne :("

  #Si l'indice de compatibilité maximale est associé à plusieurs individus, on retournera la liste de ces individus
  lovers=[]
  if compatarray.count(max(compatarray))>1:
    for i in range(len(compatarray)):
      if compatarray[i]==max(compatarray):
        if list_user[i]!=user:
            lovers.append(list_user[i].fname + " " + list_user[i].lname)
    return f" vous êtes autant compatible avec {lovers}"
    
  #On choisit l'utilisateur qui a l'indice de compatibilité le plus élevé
  lover=list_user[compatarray.index(max(compatarray))].fname + " " + list_user[compatarray.index(max(compatarray))].lname
  print(compatarray)
  return f" la personne avec laquelle vous êtes le plus compatible est {lover}" 

print(compatibility(salia))