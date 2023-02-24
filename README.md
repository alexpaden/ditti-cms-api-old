#with poetry
export FLASK_APP=ditti_web.server

#for new
flask db init

flask db migrate -m "create user table"
flask db upgrade
