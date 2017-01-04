import os
from app import create_app
from app import db
from app.models import User
# from app.models import Role
from flask_script import Shell
from flask_script import Manager
# from flask.ext.migrate import Migrate,MigrateCommand
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
# migrate = Migrate(app,db)

def make_shell_context():
    return dict(app=app,db=db,User=User)
#     return dict(app=app,db=db,User=User,Role=Role)

manager.add_command("shell",Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
