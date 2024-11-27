# Explication de la méthodologie suivie pour appliquer la Particle Swarm Optimization au problème de Lennard-Jones

## Orienté Objet

    Pour appliquer le Particle Swarm Optimization (PSO) au problème de Lennard Jones, nous avons tout d'abord traduit le pseudo-code trouvé dans la littérature en python. Nous l'avons intégré au sein d'un structure orientée objet :

    - Une classe "Swarm" qui représente l'essaim et qui gère les différentes particules et leur coordination

    - Une classe "Particle" qui elle régit les trajectoires et comportements individuels propres aux particules.

    Cependant cette méthode était  trop couteuse en temps et mettait donc trop de temps à converger.

Nous avons donc cherché des manières de l'améliorer. Les codes associés à cette partie de la démarche sont dans le dossier "PSO_orienté_objet"

## PSO OO avec le Simulated Annealing en cas limite

    Pour remédier à ce problème de convergence, nous avons ensuite essayé d'intégré certaines phases de simulated annealing (SA) pour accélérer la recherche de solutio optimale par les particules. Cependant cela ajoutait trop de temps de calcul et donc le programme continuait à converger trop lentement.

Les codes associés à cette partie de la démarche sont dans le dossier "PSO_OO_SA"

## PSO OO avec du multithreading

    Nous avons envisagé pour accéler le programme de diviser les taches aux différents processeurs, cependant la deadline approchant nous n'avions pas le temps de l'implémenter complètement.

Les codes associés à cette partie de la démarche sont dans le dossier "PSO_OO_multithreading"

## PSO sans orienté objet

    Finalement il nous a semblé logique d'essayer une méthode minimaliste pour gagner le plus de temps de clacul possible, et ce en stockant toutes les informations sur les différentes particules dans un seul tableau sur lequel toutes les opérations sont faites.

Les codes associés à cette partie de la démarche sont dans le dossier "PSO_minimaliste"