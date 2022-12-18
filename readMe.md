# LA DATA DREAM TEAM

### Brief de groupe: Laurence, Rémi, Mehdi, Brice, Louis, Elida

&nbsp;
## CONTEXTE DU PROJET

PARTIE 1 : SEGMENTATION CLIENTS

Olist souhaite que vous fournissiez à ses équipes d'e-commerce une segmentation des clients qu’elles pourront utiliser au quotidien pour leurs campagnes de communication. Votre objectif est de comprendre les différents types d’utilisateurs grâce à leur comportement et à leurs données personnelles. Vous devrez fournir à l’équipe marketing une description actionnable de votre segmentation et de sa logique sous-jacente pour une utilisation optimale, ainsi qu’une proposition de contrat de maintenance basée sur une analyse de la stabilité des segments au cours du temps.

L'équipe marketing vous partage les détails de la mission via un pdf donné dans le drive du projet, où elle indique notamment les milestones à mettre en place pour réaliser cette mission : https://drive.google.com/file/d/1RyeqbBJPxmlY0Ke_aD4nGpgreW0CcxDs/view?usp=sharing

&nbsp;

PARTIE 2 : APPLICATION WEB DE PREDICTION ET DE REPRESENTATION DE CLUSTER

L’intention de cette partie de projet est de préparer et mettre en œuvre des transformations de features numériques et catégorielles (features engineering), de mettre en œuvre des modèles d’apprentissage supervisés, de les comparer, puis d’optimiser les hyperparamètres du modèle sélectionné. Le but final est de réaliser en local une interface ( front) sur la base de paramètres rentrés dans un formulaire : vous pourrez vous inspirer du fichier GIF Streamlit_voiture et du lien dans le fichier du projet où l’interface a été réalise en utilisant STREAMLIT et/ou FLASK, HTML, CSS.
Les variables à prédire sont les frais de transport et le délais de livraison d’un article.
L'expert technique de l'entreprise vous fournit en supplément un cahier des charge avec les milestones à réaliser pour cette partie dans le drive du projet. N'hésitez pas à vous y référer pour mieux comprendre ce qui est demandé : https://drive.google.com/file/d/1fGrryhJpf7hcTmJ869zxScyijnUUvK9K/view?usp=sharing

&nbsp;

Vous trouverez dans ce dépôt git :
- un fichier script.py, à exécuter en premier lieu afin de visualiser les données dans le fichier « data » ;

- un dossier MCD qui contient :
	- le script des requêtes SQL permettant de créer notre base de donnée relationnelle : Orders_mysql.sql ;
	- une représentation graphique (MCD = Modèle Conceptuel des Données) permettant de comprendre comment les différents éléments sont liés entre eux : mcd.png ;

- un dossier data qui contient un fichier de base de données générique des « marketplaces » : marketplaces.db

- un dossier « interface » comprenant les scripts ayant permis la réalisation de l’nterface ; pour plus d’information, se référer à « App Lauchement » en bas de page de ce readMe ;

- un dossier prediction comprenant un notebook de l’analyse exploratoire mis au propre et le préprocessing.

- un dossier segmentation_client comprenant :
	- un notebook de l’analyse exploratoire (non cleané, pour comprendre notre démarche) ;
	- un notebook d’essais des différentes approches de modélisation (non cleané, pour comprendre notre démarche) ;

&nbsp;

En cliquant sur ce lien https://drive.google.com/drive/folders/1hMkVQ18NSbdVXvu9VDhqWjynWNnSqmtW vous aurez accès au fichier.csv suivant :

- olist_customers_dataset.csv : ensemble de données contenant des informations sur le client et son emplacement ;

- olist_geolocation_dataset.csv : ensemble de données contenant des informations sur les codes postaux brésiliens et ses coordonnées latitude/longitude. 

- olist_order_items_dataset.csv : ensemble de données comprenant les information sur les articles achetés dans chaque commande. 
      
- olist_order_payments_dataset.csv : ensemble de données comprenant les informations sur les options de paiement des commandes. 

- olist_order_reviews_dataset.csv : ensemble de données comprenant les informations sur les avis rédigés par les clients. 
      
- olist_orders_dataset.csv : il s’agit de l’ensemble de données de base. Vous pouvez trouver toutes les informations pour chaque commande.
      
- olist_products_dataset.csv : ensemble de données contenant les informations sur les produits vendus par Olist. 

- olist_sellers_dataset.csv : ensemble de données contenant les informations sur les vendeurs qui ont exécuté les commandes passées chez Olist. 

- product_category_name_translation.csv : table contenant la traduction des noms de la « catégorie » de produits en anglais.

&nbsp;

## App Lauchment
```
git clone https://github.com/Data-dream-team-Laurence/Brief-data-dream-team.git

cd Brief-data-dream-team

pip install -r requirements.txt

python script.py

python interface/run.py
```

Follow [this link](https://drive.google.com/drive/folders/1SyuSldDuVqoMRQkvh3OTtonnoj8J_r2m) to collect images.

Then, put images in interface/app/static/img folder

Open a web browser and enter the following url: 
localhost:5000

Enjoy !

