# Nature-inspired optimization for predicting molecular structure

#### 28 Février : Clonage et prise en main du Git

    Lecture de la documentation sur le projet artishow

    Implémentation en python de la méthode par recherche aléatoire en groupe 

#### 1er Mars :  

    Planning rendu 
  
#### 13 Mars : 

    Première implémentation en python de la méthode par recuit simulé chacun de son côté. Relecture de la documentation pour codrrer en parallèle.

    Cependant nous avons tous rencontré des problèmes similaires :
    
        - Trouver une *cooling  schedule* adaptée qui permet à l'algorithme de changer de puits sur les premières itérations, mais qui se concentre sur le puits le plus profond en fin d'algorithme.
  
        - Structurer la boucle principale de l'algo de SA de manière la plus judicieuse pour trouver une solution la plus optimale en le moins d'itérations possibles.
  
        - En général, les algorithmes étaient extrêmement coûteux en temps en ayant une correction aléatoire.
  
    Toutes ces complications ont fait que nos algorithmes n'étaient pas optimaux en fin de séance, c'est pourquoi nous avons continué chacun de notre côté à chercher des solutions à ces problèmes.
  
  
        

#### 20 Mars :

    En *Simulated Annealing* :
    
        - Pour obtenir la meilleure  solution en le moins de temps nous avons observé qu'un algorithme de descente de gradient à chaque itération de la boucle principale permettait d'être extrêmement efficace. 
  
        - La *cooling schedule* de la forme 
            "self.temp = self.temp_initial*np.exp(-0.001*self.iter) " nous paru être la plus adaptée

    En Optimisation par essaim de particules, la stratégie étant assez simple à mettre en oeuvre, nous avons pu commencer directement à l'implémenter. Nous avons opté pour une structure avec une class "Swarm" qui gère l'essaim et une class "Particle" qui régit le comportement de chaque particule.
    
    Recherche d'amélioration de la présentation : évolution "en direct" du point de recherche.

#### 26 Mars :  

        Nous avons terminé l'implémentation en python de la méthode par essaim de particules. 

        Nous avons commencé à adaptér les méthodes SA et OPS aux problèmes de Lennard-Jones, donnant des résultats probants pour la méthode SA.
    
        Recherche d'amélioration des méthodes. 

#### 2 avril : 

        'Albane' 
        Recherhe pour implémenter/améliorer la méthode à essain de particules 


#### 9 avril :

        'Groupe'
        Point d'étape Artishow : 
        Objectif 2e partie : 
               - Chercher des paramètres optimaux pour les différentes fonctions 
               - Améliorer les programmes ( approcher par des fonctions différentes : exponentielle ? )
               - Comprendre les avantages et limitations de chaque méthode, l’influence des paramètres.
               - Faire les programmes pour une dimension > 2
            Possibilité de travailler sur les algorithmes génétiques si le temps (plus compliqué). 
    
        Réfléchir à comment se répartir les différentes tâches. 

#### 24 avril :
    Répartition des tâches 
        Pierre : Optimisation par essaim de particules : Influence paramètres
        Thomas : Optimisation par essaim de particules : Amélioration 
        Albane :  Méthode recuit simulé : influence loi décroissance Température 

#### 2 mai :
        Réunion pour connaître les avancées de chacun. 
        Pierre : 
        Thomas : 
        Albane : Méthode recuit simulé : Modification de la loi de décroissance de la Température.
         
         1-  Décroissance logarithmique : T(t) = T0/log(t+1)
         
                    Avantages : Permet une décroissance plus lente de la température => exploration plus    approfondie de l'espace des solutions.
                    Inconvénients : Convergence peut être très lente 

                2 - Décroissance linéaire : T(t) = T0 - kt
        
                    Avantages : Efficace pour des problèmes où une convergence rapide est nécessaire.
                    Inconvénients : Si la température atteint zéro avant que l'optimum global ne soit trouvé, l'algorithme s'arrête prématurément.
                
                

#### 15 mai :

        Réunion pour connaître les avancées de chacun. 
        Conclusion : 
            Pierre : - l'algorithme de recuit simulé fonctionne bien sur des fonctions simples mais la décroissance de la température est trop rapide.
                     - l'algorithme Particle Swarm Optimization ne fonctionne pas (structure du code OK mais choix des paramètres arbitraire)
            Thomas : 
            Albane : Recuit Simulé : 
            
                    3 - Décroissance exponentielle : T(t) = T0*exp(-λt)

                    Avantages : Contrôle précis sur le taux de décroissance de la température.
                    Inconvénients : Difficile de choisir le bon paramètre λ :
                        -  Si λ est trop grand, la température diminue trop rapidement.
                        -  Si λ est trop petit, la convergence peut être trop lente.
                
                4 - Décroissance Géométrique : T=k*T

                    Avantages :  Bon compromis entre une décroissance rapide au début et une exploration plus lente vers la fin =  équilibre entre exploration et exploitation.
                    Inconvénients : Choisir le paramètre k.
                 
                
                 Ccl : Le choix le plus simple et le plus effiace est de prendre T= kT. Pour quelles valeurs de k ?  


        

#### 22 mai :
    Réunion pour connaître les avancées de chacun. 
    Conclusion : 
        Pierre : le Particle Swarm Optimization ne fonctionne pas très bien. difficulté à choisir la valeur des paramètres
        Thomas : 
        Albane : Le paramètre k dans T= kT à beaucoup d'importance : 
                     -  Si k trop grand, la temperature diminue très rapidement et l'algorithme se bloque dans un minima local ;
                     - Si k trop petit, la temperature diminue très lentement donc le temps de calcul devient très long.
                    CCL : Bon fonctionnement avec k proche de 1 i.e 0.9<k<0.99.
     

#### 29 mai :
    Présentation de l'avancée du projet aux autres groupes.  
    Nous avons audité deux autres projets et pu obtenir les avis venant de deux trios différents sur notre projet.


#### 5 juin :
    Réunion pour connaître les avancées de chacun. 
    Conclusion : 
        Pierre : 
        Thomas : 
        Albane : Discussion des paramètres optimaux pour les différentes fonctions et différents algorithmes. 

     

#### 12 juin :
    Réunion avant le rush dernière semaine. 
    Nous avons beaucoup échangé à propos de la méthode par essain de particules pour en améliorer la complexité. En particulier, nous avons discuté de la possibilité de faire du multi-threading ou de modifier le nombre d'itérations de l'algorithme pour trouver le meilleur rapport qualité/complexité.

### 24 juin : 
    Mise à jour du fichier suivi
    amélioration de l'interface de travail pour comparer les résultats des différentes méthodes.
    finalisation du programme par recuit simulé

