# Dofusarium

Dofusarium est un logiciel qui permet d'effectuer des calculs de 
rentabilité ainsi que de répertorier nos achats.
Pour la V1, j'ai programmé 3 options :
- Calculer la rentabilité d'un craft selon le coût des ressources en 
prenant en compte la taxe d'HDV (Hôtel de vente)
- Répertorier les achats (nom de l'item, la quantité, le prix ainsi que 
la date (par défaut initialisée à la date du jour mais modifiable via 
le .txt))
- Calculer le prix de revente des items par 1, 10 et 100 en fonction du 
prix unitaire payé d'un item toujours en prenant en compte la taxe en 
HDV.

## EXEMPLES
### Exemple de l'option n°1 :
Nous souhaitons crafter une potion de bonta. Pour cela, il nous faut 1 
pépite qui nous coûte 200 kamas et 6 riz qui nous coûtent 250 kamas unité.
Le logiciel nous demandera de rentrer le nom de l'item à crafter (donc ici 
la potion de bonta), le nombre de ressources à utiliser (donc ici 2 : la 
pépite et le riz).
Il demandera le nom de la ressource 1 (donc la pépité), le prix unitaire 
payé (donc 250 kamas si on ne l'a pas recyclée sois-même) ainsi que le 
nombre de cette ressource dans le craft (donc une seule).
Ensuite il nous demandera les mêmes choses pour les autres ressources 
(donc dans le cas du craft de la potion de bonta ce sera les informations 
concernant le riz)
Après tout ça, le logiciel va demander le prix auquel nous pouvons vendre 
l'item crafté (dans l'exemple, nous dirons que l'on peut vendre la potion 
à 2000 kamas). Le logiciel va s'occuper de calculer la marge que nous 
faisons en comptant la taxe en HDV. Dans le cas présent, le logiciel va 
donc nous dire que la rentabilité du craft de la potion de bonta est de 
260 kamas.
"Mais pourquoi se servir de ce logiciel au lieu de faire les calculs moimême ?" allez vous me dire.
Après la première utilisation de cette option, le logiciel créera un 
document "craft.txt" vous mettant une phrase vous disant "La rentabilité 
de l'item ... (nom de l'item) est de ... (nombre de kamas) kamas". Ce 
document est actualisé (et non écrasé) après chaque craft à répertorier, 
ce qui vous permettra de vous y retrouver facilement.
### Exemple de l'option n°2
Après nous être rendu dans l'HDV de notre choix, on achète 105 magnifiques 
"Peau de bouftou".
Nous nous empressons d'utiliser l'option n°2 du logiciel afin de 
répertorier nos objets.
Pour cela rien de + simple : il faut entrer le nom de l'objet, le nombre 
acheté ainsi que le prix du lot. Le logiciel permet de faire une liste des 
items entrés (il faut entrer les items 1 à 1), de garder en mémoire le 
prix du lot et en calculer le prix des items à l'unité (en divisant le 
prix du lot par la quantité). Il permet aussi de mettre automatiquement la 
date du jour comme date d'achat afin de savoir depuis quand vous avez vos 
items sur les bras.
### Exemple de l'option n°3
Quelques jours après avoir répertorié nos Peau de bouftou dans notre 
logiciel, nous avons envie de les revendre car nous n'en avons plus 
l'utilité. Pour calculer la rentabilité, rien de + simple !
Il faut choisir l'option n°3 dans le logiciel, entrer le nom de l'item, la 
quantité d'items achetés (donc ici nos 105 peau de bouftou), le prix 
d'achat à l'unité (que vous aurez calculé grâce au programme n°2, ici nous 
allons dire que nous les avons acheté 90 kamas unité), entrer le prix en 
HDV par 1, par 10 puis par 100 (pour l'exemple nous allons dire 100 
kamas/1, 1250 kamas/10 et 25000 kamas/100)
Résultat donné par le logiciel :
" Meilleures options de rentabilité pour Graine de sésame : *100
- *1 : bénéfice de 840.00 kamas
- *10 : bénéfice de 3412.50 kamas
- *100 : bénéfice de 16275.00 kamas
Un conseil : gardez le restant en banque jusqu'à ce que le prix remonte !"
Résultat dans le fichier texte :
"
Meilleures options de rentabilité pour Peau de bouftou : *100
- *1 : bénéfice de 840.00 kamas
- *10 : bénéfice de 3412.50 kamas
- *100 : bénéfice de 16275.00 kamas
Un conseil : gardez le restant en banque jusqu'à ce que le prix remonte
"
(ça vous met en mémoire ce que le logiciel a dit afin que vous puissiez le 
retrouver)


Si vous avez des bugs à faire remonter, contactez moi via discord :
Romain#0614.


Pour me soutenir dans le développement du logiciel :
https://paypal.me/Romainfer62?country.x=FR&locale.x=fr_FR


### UPDATE :

Nouvelle option disponible :
- Une option permettant d'avoir la liste de tous les types de dragodindes, leur génération (de 1 à 10) les parents qu'il faut pour les obtenir par fécondation ainsi que le type de parchemin qu'elles apportent lorsque l'on les échange au PNJ. A cette option s'ajoutent plusieurs systèmes de tri : par ID (ordre croissant ou décroissant), par génération (ordre croissant ou décroissant également), par ordre alphabétique (a à z ou z à a) selon son type, son parent numéro 1 ou parent numéro 2 ainsi que pour le type de parchemin obtenu. 
