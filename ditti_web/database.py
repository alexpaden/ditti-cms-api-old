from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def init_app(app):
    db.init_app(app)
    migrate.init_app(app, db)

    @app.cli.command()
    def db_init():
        migrate.init()

    @app.cli.command()
    def db_migrate():
        migrate.migrate()

    @app.cli.command()
    def db_upgrade():
        migrate.upgrade()
