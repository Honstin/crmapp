from app import app, db
from app.models import User, Client


@app.shell_context_processor
def make_shell_context():
    print("shell context should start here")
    return dict(db=db, User=User, Client=Client)