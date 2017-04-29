#CEVIPOF
##[iramuteq.org](http://iramuteq.org/)

-

Interface de R pour les Analyses Multidimensionnelles de Textes
et de Questionnaires

-

Développé par Pierre Ratinaud @ LERASS, Toulouse

-

Un logiciel libre construit avec des logiciels libres

- Python
- R
- Lexique 3 (www.lexique.org)

[Open source](http://www.iramuteq.org/git/iramuteq)

===

##Entrée

Nécessite pré-traitement avant import

-

####Exemple d'entrée :

~~~~
0001 *an_2000 *sexe_2 *age_6 *cspc_3 *nivet_5 *sympeco_1
JE CROIS QUE C'EST LE RECHAUFFEMENT DE L'ATMOSPHERE DUE A LA POLLUTION 

0003 *an_2000 *sexe_2 *age_3 *cspc_3 *nivet_3 *sympeco_2
COUCHE D OZONE POLLUTION 

0005 *an_2000 *sexe_1 *age_2 *cspc_3 *nivet_3 *sympeco_2
RECHAUFFEMENT DE LA PLANETE 

0006 *an_2000 *sexe_2 *age_4 *cspc_1 *nivet_4 *sympeco_2
ÇA NE ME DIT RIEN NON 

0007 *an_2000 *sexe_1 *age_5 *cspc_1 *nivet_5 *sympeco_1
C'EST LE RECHAUFFEMENT DE LA PLANETE DU AU DEVELOPPEMENT DES INDUSTRIES 

[...]
~~~~

<span style="font-size:0.5em;">(Exemple : résultat d'enquête ADEME réalisée par Daniel Boy)</span>

-

####Format des variables associées au segment de texte :

~~~~
0003 *an_2000 *sexe_2 *age_3 *cspc_3 *nivet_3 *sympeco_2
COUCHE D OZONE POLLUTION 

N° de segment *variable1_valeur1 *variable2_valeur2 [...]
segment de texte
~~~~

-

####Paramètres d'import de l'exemple

- Langue : français
- Marqueur de texte = 0000
- Segment de textes = paragraphes

===

##Fonction n°1 : <br> Statistiques

Statistiques textuelles descriptives basiques

-

####Résumé de l'import

- Nombre de textes
- Nombre d'occurrences
- Nombre de formes
- Nombre d'hapax
- Moyenne d'occurrences par texte
- Visualisation fréquence/rang : loi de Zipf

-

<div style="text-align: center">

![frequences](images/frequences.jpg)

</div>

<div style="text-align: center">Fréquences de termes lemmatisés et catégorisés grammaticalement</div>

===

##Fonction n°2 : <br> Nuage de mots

-

####Paramètres du nuage de mots

- Lemmatisation
- Formes actives ou supplémentaires
- Nombre de mots dans le nuage
- Taille maximum et minimum des mots
- Liste des mots à inclure dans le nuage

-

<div style="text-align: center; height: 600px">![nuage](images/nuage.png)</div>

===

##Fonction n°3 : <br> Analyse de similitudes

Réseau de cooccurrences ou de similarités de mots

-

####Paramètres de l'analyse de similitudes

- Indice de similitude : __cooccurrences__, Jaccard, Dice, Chi-2 etc...
- Spacialisation du graphe : random, cercle, __Fruchterman-Reingold__
- Totalité des liens, poid minimum des liens ou __arbre maximum__
- Clustering en communautés : 8 algos dispo (__betweenness__)
- Liste des mots à inclure dans le graphe

-

<div style="text-align: center; height: 600px">![simi](images/simi.png)</div>

<div style="text-align: center">Export en .graphml pour utilisation dans [gephi](https://gephi.org/)</div>

===

##Fonction n°4 : <br> Spécificités et AFC

Produit une [analyse factorielle des correspondances](https://fr.wikipedia.org/wiki/Analyse_factorielle_des_correspondances) sur un tableau de contingence qui croise formes actives et les variables choisies

-

####Paramètres des spécificités

- Formes actives et/ou supplémentaires
- Variables ou modalités choisies
- Indice : loi hypergéométrique ou chi-2
- Fréquence minimale des termes considérés

-

<div style="text-align: center; height: 600px">![afcf1](images/afcf_1.jpg)</div>

-

<div style="text-align: center; height: 600px">![afcf2](images/afcf_2.jpg)</div>

===

##Fonction n°5 : <br> Clustering

Cette analyse propose une classification hiérarchique descendante selon la méthode décrite par Reinert

-

####Paramètres de la classification
- Trois modalités : double sur RST (méthode héritée d'Alceste), simple sur segments ou sur texte
- Nombre de classes terminales
- Nombre de formes (mots) considérées dans le corpus
- __*MODE PATATE*__ (optimisation pour gros corpus)

-

<div style="text-align: center; height: 600px">![dendrogramme](images/dendrogramme.jpg)</div>

-

<div style="text-align: center; height: 600px">![philogramme](images/philogramme.jpg)</div>

-

<div style="text-align: center; height: 600px">![afcf3](images/afcf_3.jpg)</div>

===

##Sorties

Iramuteq met à disposition de nombreuses sorties en format .csv dans le dossier local correspondant au corpus courant

===

##Autres outils d'analyses textuelles

- [TXM](http://textometrie.ens-lyon.fr/) : agrège beaucoup des fonctions d'analyse et de statistiques textuelles disponibles ailleurs
- [CorText](https://managerv2.cortext.net/login) : représentation de réseaux de cooccurrences, extraction de concepts saillants
- [Gargantext](http://mines.gargantext.org/) : directement branché sur les API de sites tels que wikipédia ou europresse et factiva
- [Voyant Tools](http://www.voyant-tools.org/) : facile et rapide à prendre en main

===

##Merci

Un groupe MATE-SHS s'est formé lors de l'ANF de Fréjus autour des données textuelles - contact : diego.antolinosbasso@sciencespo.fr