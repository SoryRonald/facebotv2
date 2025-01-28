import json
import importlib
import datos
from flask import (
  Blueprint,
  render_template,
  redirect,
  url_for,
  request,
  jsonify
)

api = Blueprint('api',__name__)
restarter = None
def ogag(v):
  global restarter
  restarter = v

@api.route('/bobot', methods=['POST'])
def bobot():
  fbstate = request.form.get('fbstate')
  if fbstate:
    json_fbstate = json.loads(fbstate)
    with open('fbstate.json', 'w') as file:
      json.dump(json_fbstate, file, indent=2)
    if restarter:
      restarter()
  return redirect(url_for('view.root'))

@api.route('/logs/<session>')
def logs(session):
  log_session = datos.log_session
  if session != log_session:
    return jsonify({"error": 'Invalid log session'}),3003
  data = datos.logs
  return jsonify(data),200