# app.py

from flask import Flask, session
from keystone import bp as keystone_bp  # Import blueprint from __init__.py
from keystone.utils import is_keystone_online

app = Flask(__name__)
app.secret_key = 'supersecretkey'

app.register_blueprint(keystone_bp, url_prefix='')


@app.before_request
def check_keystone_status():
    session['keystone_online'] = is_keystone_online()

if __name__ == '__main__':
    app.run(debug=True , port=8000  )
