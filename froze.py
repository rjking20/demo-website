from flask_frozen import Freezer
from main import app
freeze = Freezer(app)

if __name__ == '__main__':
    freeze.run()