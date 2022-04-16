import os

from flask_psql_service import create_app
from dotenv import load_dotenv

load_dotenv('.env')

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run(debug=True)