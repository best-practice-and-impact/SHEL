from app import app, db
from app.models import User, Post, Logstakeholder
from user_setup import setup_app

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Logstakeholder':Logstakeholder}

if __name__ =='__main__':
    setup_app()
    app.run(host="0.0.0.0")
