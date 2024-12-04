from flask import Flask
from extensions import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0000@localhost:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from routes.users_routes import users_bp
from routes.media_routes import media_bp
from routes.roles_routes import roles_bp

app.register_blueprint(users_bp, url_prefix='/api/users')
app.register_blueprint(media_bp, url_prefix='/api/media')
app.register_blueprint(roles_bp, url_prefix='/api/roles')

from error_handlers import register_error_handlers
register_error_handlers(app)

if __name__ == '__main__':
    app.run()
