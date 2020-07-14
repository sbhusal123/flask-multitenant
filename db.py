from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from restaurant import app, db

# Init migrate and migrate command
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
