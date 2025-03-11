from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Flask extensions placeholder

    # Blueprint register placeholder
    from course.main import bp as main_bp
    app.register_blueprint(main_bp)

    @app.route('/university-admin/')
    def uni_admin_page():
        return '<h1>Testing Flask app</h1>'
    
    return app
