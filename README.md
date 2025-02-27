# todo-challenge-api


## what is included

Auth via session (django admin console) and JWT.

Filter/search via created_at (lt, gt, exact, range) and description(Noncasesensitive)

order by created_at (using date YYYY%MM%DD)


Generate api schema doc

python manage.py spectacular --color --file schema.yml


docker compose exec todo_api python manage.py populate_db_static_data
docker compose exec todo_api python manage.py populate_db_random_data

