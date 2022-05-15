from mapper.app_factory import create_app

import os
import configparser

config = configparser.ConfigParser()
config.read(os.path.abspath(os.path.join(".ini")))

if __name__ == "__main__":
    app = create_app()
    app.config['DEBUG'] = True
    app.config['MONGO_URI'] = config['PROD']['DB_URI']
    print(config['PROD']['DB_URI'])
    # app.config['MONGO_URL'] = 'mongodb+srv://web-mapper-admin:SJONnl3HPGhvJOHe@web-mapper-test.qskew.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'

    app.run()

