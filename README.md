#with poetry
export FLASK_APP=ditti_api.server

#for new
flask db init

flask db migrate -m "create api keys table"
flask db upgrade

poetry env use 3.10
