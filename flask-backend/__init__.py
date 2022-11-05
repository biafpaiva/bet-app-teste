from flask import *
from flask_cors import CORS, cross_origin

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
        from routes.home import home
        from routes.user_data import user_data
        from routes.list_matches import list_matches
        from routes.list_bets import list_bets
        from routes.make_bet import make_bet
        from routes.login_user import login_user
        from routes.logout import logout
        from routes.register_user import register_user
        from routes.list_ranking import list_ranking
        from routes.delete_account import delete_account
        from routes.delete_bet import delete_bet

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

    return app