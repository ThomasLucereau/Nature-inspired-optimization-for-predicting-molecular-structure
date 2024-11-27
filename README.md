# Projet Artishow :

 ## Nature-inspired optimization for predicting molecular structure



![Problèmes de Lennard - Jones](IllustrationsReadme/image_projet_artishow.png)

Problèmes de Lennard - Jones
#
## Organisation du Git :

- Dossier *RandomSearch* qui regroupe le travail sur la recherche aléatoire

- Dossier *SimulatedAnnealing* qui regroupe les implémentations de chaque élève du recuit simulé. *Une version finale peut être trouvée dans le dossier SA_Thomas\Version_organisée*

- Dossier *IllustrationsReadme* qui permet d'illustrer ce Readme
    

## Présentation des résultats :

#### La recherche aléatoire

![Problèmes de Lennard - Jones](IllustrationsReadme/animationf2_Random.gif)

*Exemple de recherche aléatoire menée sur une fonction avec beaucoup de minima locaux*


###### Remarque
    Cette méthode donne des résultats de qualité fortement variable en plus d'être extrêmement complexe en temps si l'on veut un résultat cohérent (1 million de samples minimum doivent être pris)

#### Le recuit simulé ou "simulated annealing"

Cette méthode s'inspire de travaux thermodynamiques sur la cuisson des poteries. Elle en tire aussi son nom. 

Elle permet surtout de sortir de minima locaux et de garantir un résultat correspondant à un minimum global.

##### Illustration 1

![Problèmes de Lennard - Jones](IllustrationsReadme/animationf1.gif)

![Problèmes de Lennard - Jones](IllustrationsReadme/energy_f1.png)

##### Illustration 2

![Problèmes de Lennard - Jones](IllustrationsReadme/animationf2.gif)

![Problèmes de Lennard - Jones](IllustrationsReadme/energy_f2.png)

###### Remarque :

    On voit bien sur les diagrammes en énergie que cette méthode permet de sortir de puits pour en trouver des plus bas en énergie.  







