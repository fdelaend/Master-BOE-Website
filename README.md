# Master BOE — site de présentation

Site Quarto en français destiné aux futurs étudiants. Projet local indépendant ; aucun déploiement effectué.

## Modifier et prévisualiser

Avec Quarto installé, depuis ce dossier :

```sh
quarto preview
```

Pour produire le site statique :

```sh
quarto render
```

Les pages HTML sont créées dans `_site/` (non versionné).

## Contenu

- `index.qmd` : accueil
- `a-propos.qmd` : formation
- `equipe.qmd` : interlocuteurs identifiés
- `memoires.qmd` : expérience de recherche
- `stages.qmd` : immersion professionnelle
- `liens.qmd` : ressources et admission
- `debouches.qmd` : métiers et témoignages alumni
- `_quarto.yml` : navigation et configuration
- `styles.css` : identité visuelle et affichage mobile
- `assets/` : illustrations SVG originales, sans dépendance externe

## Sources éditoriales

Consultées le 2 novembre 2026 :

- Manuel fourni : https://fdl-courses.unamur.be/MasterBOE-Guidelines.html
- Catalogue officiel : https://uclouvain.be/prog-2026-boe2m
- Conditions d’accès : https://uclouvain.be/prog-2026-boe2m-cond_adm

Le manuel est utilisé comme source, sans lien public vers le site existant. Les informations administratives internes, dates de dépôt, Moodle et procédures des étudiants inscrits sont volontairement écartées. La page équipe présente les promoteurs et leurs spécialités, à partir des documents fournis et de sources publiques de recherche. Les témoignages et exemples de structures de stage proviennent du dossier input ; aucun débouché garanti ni offre de stage actuelle n’est affirmé.

## Avant publication

Faire relire le contenu et les fonctions des contacts par les responsables du programme ; relire les profils alumni avant publication. Actualiser les liens du catalogue lors du changement d’année académique.

Le dossier possède déjà un dépôt Git local. Pour une publication ultérieure, connecter un nouveau dépôt GitHub dédié à un nouveau contenu Posit Connect Cloud. Ne pas activer GitHub Pages. Les fichiers source et ressources suffisent ; ne pas versionner les jetons d’authentification ni les fichiers de session.


## Intégration du dossier input — 2 novembre 2026

- Trois PPTX examinés : modules, enjeux sociétaux, exemples de stages et métiers, noms des équipes de mémoire. Les calendriers et démarches internes, parfois anciens, ne sont pas repris.
- Témoignages : profils finaux de Sophie-Charlotte Depestel et Cassandra Liévin ; profil, expérience et PDF d’Anne-Sophie Voisin ; transcription du 19 mai 2026 dans N Laurent.
- Le fichier « 12 - Alumni - N Laurant - final.docx » contient en réalité un ancien profil d’Anne-Sophie Voisin. Il ne sert pas à attribuer le parcours de recherche en conservation. L’utilisateur a confirmé que cette transcription est celle de Nicolas Laurent ; ce nom est utilisé dans le site.
- La transcription fournie a été lue ; le MP4 n’a pas été retranscrit ni intégré au site.
- Les deux captures LinkedIn de SC Depestel et les deux PDF LinkedIn d’AS Voisin ont été examinés comme éléments de contexte, sans publier les captures, documents ni données de navigation.
- Les 20 photos de terrain ont été examinées. Quatre sont utilisées : P1000460 (accueil), P1000446 et P1000514 (à propos), P1000555 (stages). Copies JPEG optimisées, proportions conservées, originaux inchangés. Les légendes décrivent les scènes sans inventer de lieu ni de nom.
- Les logos UCLouvain.png et UNamur.png sont repris tels quels sur l’accueil ; ils ne sont ni recolorés ni déformés.
- L’affiche de 2022 a été examinée mais n’est pas intégrée : son ancienneté ne permet pas de la présenter comme le programme actuel.
- `input/` est exclu des ressources de publication Quarto. Seules les images sélectionnées dans `assets/` sont publiables avec le site ; les documents sources et la vidéo restent dans le dossier de travail.

## Portraits alumni

Les quatre portraits `input/depestel.png`, `lievin.png`, `voisin.png` et `laurent.png` sont copiés dans `assets/alumni-*.png`. La page Débouchés les affiche dans des cercles, avec un cadrage CSS propre à chaque fichier pour exclure la bannière et les marges des images fournies. Les originaux restent inchangés.

## Nouvelle intégration : mémoires, modules, employeurs et terrain

- Les 13 PDF du dossier input/memoires servent de base à une synthèse des grands thèmes de recherche sur memoires.qmd, sans reproduire les propositions annuelles. Les PDF bruts ne sont pas publiés (ils contiennent notamment des courriels).
- Les six illustrations des modules proviennent de la diapositive 5 de Master BOE 25-26_2026.pptx : image22, image24, image25, image13, image23 et image26.
- La page terrain.qmd présente le cours de terrain, distinct du stage professionnel. Sélection contrôlée : aucune photo ne montre une personne tenant un oiseau.
- Logos PlantC, Natagora, SPW extraits de la présentation fournie. Logos VIVUS, CRA-W et European Metals récupérés sur leurs sites officiels. Les sources des emplois sont liées depuis la page Débouchés, vérification du 2 novembre 2026. Le PDF du groupe LinkedIn a servi à identifier les personnes à rechercher ; aucune appartenance au groupe n’est présentée comme preuve d’emploi.
- Les adresses électroniques et liens mailto ont été supprimés de toutes les pages QMD. Les sources privées restent inchangées dans input, exclu du site généré.

## Révision éditoriale des mémoires et de l’équipe

Les sujets annuels sont remplacés par quatre grands horizons de recherche et leurs approches. Les informations de présence à la foire et les détails organisationnels associés ont été supprimés. Les profils de promoteurs s’appuient sur les documents fournis ; les compléments publics sont liés sur la page équipe (UNamur, UCLouvain, laboratoire Baeckens et FNRS). Les doctorants et collaborateurs cités dans les propositions ne sont pas automatiquement présentés comme promoteurs.

## Rafraîchissement visuel et précisions

Stage professionnel : durée de quatre mois confirmée par le responsable ; exemples de structures explicitement présentés comme illustratifs, photo du cours de terrain et références aux interviews retirées. Témoignages placés en tête de la page Débouchés. Accueil illustré par trois images fournies (paysage, coraux, insecte). Date de création 2007 confirmée par l’utilisateur, en accord avec l’image Picture 1.png-10. L’accueil présente cette date sous forme de bandeau typographique. Treize portraits du dossier PIs exportés en PNG circulaires transparents ; aucune photo fournie pour Thierry Hance. Originaux conservés.

## Versions française et anglaise — novembre 2026

Les huit pages existent en français (racine) et en anglais (`en/`). Les images et la feuille de style restent partagées. `quarto render` compile les seize pages et lance `scripts/localize_site.py` : ce script adapte la navigation anglaise, le pied de page et les liens FR/EN statiques vers la page correspondante (sans JavaScript). Python 3 est nécessaire au rendu. Modifier les deux versions lors des mises à jour éditoriales. Les traductions des citations sont signalées. La langue principale de l’enseignement reste le français.

Le ton a été revu pour privilégier des intitulés factuels. Enquête : `input/enquête alumnis 2026.pptx`, avril 2026. La diapositive 5 et son graphique BOE portent sur 115 répondants : 21 sans emploi, 7 en doctorat, 87 dans les autres activités (soit 94/115 en activité ou doctorat). La diapositive 10 indique spécifiquement pour BOE : 9 % à la fin du stage, 45 % en moins de six mois, 13 % après plus d’un an. Les captures de graphiques intégrées dans cette diapositive regroupent plusieurs masters et ne sont pas utilisées. Les textes publics donnent des ordres de grandeur, sans comparaison entre masters, et précisent la population et les limites. Aucun résultat global sur la localisation ou la stabilité des emplois n’est attribué au BOE.

Les résultats de l’enquête alumni ont été retirés des deux versions publiques à la demande du responsable le 19 novembre 2026. Le document source est conservé dans input, exclu du site.

## Précisions sur le programme et le stage

Durée du stage professionnel corrigée à quatre à six mois dans les deux langues, y compris sur l’accueil. La page À propos est renommée Programme dans le menu, son titre et son introduction pour préciser son rôle : cours, modules et organisation. Son chemin a-propos.html est conservé afin de préserver les liens existants.
