export FLASK_APP=ditti_web.server

flask db init
flask db migrate -m "create user table"
flask db upgrade
