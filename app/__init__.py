from flask import Flask
from flask_socketio import SocketIO
import datos
import secrets

def startapp(restartbot):
  app = Flask(__name__)
  io = SocketIO(app)
  from .views import view
  from .api import api, ogag
  
  datos.socket = io
  datos.log_session = secrets.token_hex(5)
  ogag(restartbot)
  
  app.register_blueprint(view)
  app.register_blueprint(api, url_prefix='/api')
  
  datos.logs.append({
    "message": "Website running",
    "label": {
      "text": "FLASK",
      "color": "#FF9D3D"
    }
  })
  return io, app