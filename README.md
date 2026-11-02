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

Le manuel est utilisé comme source, sans lien public vers le site existant. Les informations administratives internes, dates de dépôt, Moodle et procédures des étudiants inscrits sont volontairement écartées. La page équipe présente les trois interlocuteurs et les scientifiques nommés dans la foire aux mémoires 2026–2027. Les témoignages et exemples de structures de stage proviennent du dossier input ; aucun débouché garanti ni offre de stage actuelle n’est affirmé.

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
