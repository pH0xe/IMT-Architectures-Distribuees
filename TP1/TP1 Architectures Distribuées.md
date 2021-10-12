# TP 1
## TP Vert
### Question 1
- Mise à jours de `/json` la structure exemple n'est pas correct:
	```json
	// Avant
	{
	  "id": {
	    "title": "The Martian",
	    "rating": "7",
	    "director": "Paul McGuigan"
	  }
	}

	// Après
	[
	  {
	    "id": "a8034f44-aee4-44cf-b32c-74cf452aaaa",
	    "title": "The Martian",
	    "rating": "7",
	    "director": "Paul McGuigan"
	  }
	]
	```
- Changement de `/title` à `/moviesbytitle` dans open api pour correspondre au code 
- changement de `[HTTP POST] /movies/{movieid}` en `[HTTP POST] /movies` pour eviter la redondance de l'id
- Ajout d'un point d'entré dans `/`  amenant a `/json`
- `[HTTP GET] /movies/{movieid}` ajout de 2 champs a la réponse pour supprimer ce film ou modifier la note du film:
	```json
	"deleteLink": 
	"updateLink": 
	```
- `[HTTP GET] /moviesbytitle?title=title` ajout de 2 champs a la réponse pour supprimer ce film ou modifier la note du film :
	```json
	"deleteLink": 
	"updateLink": 
	"updateRateLink": 
	```
- `[HTTP POST] /movies` ajout d'un champs dans le retours de la création d'un film pour pouvoir consulter le détail du films ajouté
	```json
	"filmDetail": 
	```
### Question 2
- ajout d'une methode generique pour modifier n'importe quel champs d'un film : 
`/movies/{moviesid}?title=***&rating=***&director=***`
Aucun champs n'est obligatoire

## TP Bleu