# Pirate Shooter Lab

Configurateur en ligne pour préparer un buggy **T2M Pirate Shooter II** (1/10 XL) pièce par pièce, avec les pièces d'option T2M et BSD Racing.

Ouvrir `index.html` dans un navigateur suffit : le site tient en un seul fichier, photos comprises.

## Parcours

1. Carrosserie : la teinte choisie colore tout le site.
2. Rubrique repliable « Le Pirate Shooter, en détail » : vidéos, châssis, transmission, suspension, électronique.
3. Prépa en étapes : moteur, batterie, châssis, platine batterie, amortisseurs, supports, triangles, fusées, direction, hexagones, jantes, pneus (avec jeux de rechange).
4. Compte-rendu : visualiseur multi-vues, performances estimées, fiche de montage avec références et prix total.

## Contenu du dépôt

- `index.html` : le site prêt à publier (GitHub Pages compatible).
- `source/configurateur.template.html` : la source du site, avant intégration des images.
- `source/outils/build.py` : intègre les photos et rendus dans le site.
- `source/outils/rendu-3d.html` et `rendu-3d.py` : moteur de rendu 3D des pièces d'option.
- `source/photos` et `source/rendus-3d` : photos du châssis, découpes et rendus des pièces.

## À savoir

- Prix « vérifié » : relevés chez des revendeurs en octobre 2026. « estimé » et « atelier » : à confirmer.
- Le bouton Commander est une maquette, aucun paiement n'est branché.
