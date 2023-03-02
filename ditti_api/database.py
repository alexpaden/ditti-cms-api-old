from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from supabase import create_client, Client
from farcaster import Warpcast
from dotenv import load_dotenv

load_dotenv()
_url: str = os.environ.get("SUPABASE_URL")
_key: str = os.environ.get("SUPABASE_KEY")
_warp_secret: str = os.environ.get("WARP_SECRET")

try:
    warpcast = Warpcast(access_token=_warp_secret)
    supabase: Client = create_client(_url, _key)
    alchemy_db = SQLAlchemy()
    migrate = Migrate()
except:
    raise ValueError("Failed to initialize database")

def init_app(app):
    alchemy_db.init_app(app)
    migrate.init_app(app, alchemy_db)

    @app.cli.command()
    def db_init():
        migrate.init()

    @app.cli.command()
    def db_migrate():
        migrate.migrate()

    @app.cli.command()
    def db_upgrade():
        migrate.upgrade()
