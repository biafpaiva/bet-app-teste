from __init__ import create_app

if __name__ == "__main__":
    app = create_app()
    app.secret_key = 'super secret key'
    app.config["SESSION_PERMANENT"] = True
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)