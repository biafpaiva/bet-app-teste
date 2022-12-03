from flask import *
from flask_cors import CORS, cross_origin

dbFilePath: str = 'flask_backend/database/database.db'

def create_app():

    """Construct the core application."""
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)


    #app.config.from_object('config.Config')

    # Set globals

    with app.app_context():


        '''
        # Initialize globals
        db.init_app(app)

        user = User(
            username="ilana",
            password="boloehtudo",
            email="ilana@example.com",
        )
        db.session.add(user)

        # Commit session.
        db.session.commit()

        db.create_all()

        '''
        ##CORS(app, resources={r"/*": {"origins": "*"}})
        # Add some routes
        from flask_backend.routes.home import home
        from flask_backend.routes.user_data import user_data
        from flask_backend.routes.list_matches import list_matches
        from flask_backend.routes.list_bets import list_bets
        from flask_backend.routes.make_bet import make_bet
        from flask_backend.routes.login_user import login_user
        from flask_backend.routes.logout import logout
        from flask_backend.routes.register_user import register_user
        from flask_backend.routes.list_ranking import list_ranking
        from flask_backend.routes.delete_account import delete_account
        from flask_backend.routes.delete_bet import delete_bet
        from flask_backend.routes.change_username import change_username
        from flask_backend.routes.register_result import register_result

        app.register_blueprint(home)
        app.register_blueprint(user_data)
        app.register_blueprint(list_matches)
        app.register_blueprint(list_bets)
        app.register_blueprint(make_bet)
        app.register_blueprint(login_user)
        app.register_blueprint(logout)
        app.register_blueprint(register_user)
        app.register_blueprint(delete_account)
        app.register_blueprint(delete_bet)
        app.register_blueprint(list_ranking)
        app.register_blueprint(change_username)
        app.register_blueprint(register_result)

    return app