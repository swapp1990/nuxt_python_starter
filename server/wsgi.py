from flask_socketio import SocketIO, emit
from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import Worker as workerCls
from easydict import EasyDict
import myapp
# import dynamo
import logging

application = Flask(__name__)
CORS(application, resources={r'/*': {'origins': '*'}})
application.config['CORS_HEADERS'] = 'Content-Type'
socketio = SocketIO(application, cors_allowed_origins="*",
					logger=False, async_mode='threading')
mainCls = myapp.main()

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

users = {}
clientThread = None

@socketio.on('connect')
def connect():
	print("connected: create new thread")
	global clientThread
	clientThread = myapp.ClientThread(mainCls=mainCls)
	clientThread.set_thread_id(request.sid)
	threadUser = workerCls.Worker(request.sid, clientThread, socketio=socketio)
	threadUser.start()
	
@socketio.on('clientAction')
def gotActionFromClient(actionData):
	print('clientAction ', actionData['actionToCls'])
	msg = EasyDict(actionData)
	if 'action' in msg.keys():
		msg.actionToCls = msg.action
	msg.id = request.sid
	workerCls.broadcast_event(msg)

@socketio.on('set-session')
def set_session(params):
	global users, clientThread
	if 'user' not in params.keys():
		print("no user, create new session", request.sid)
		clientThread.connect(locked=True)
		return
	users[params['user']] = {'sid': request.sid }
	print('User joined ', params['email'], request.sid)
	clientThread.connect()
	if params['email'] is not None:
		clientThread.set_email(params['email'])

@socketio.on('remove-user')
def remove_user(params):
	if 'user' not in params.keys():
		return
	global users
	if params['user'] in users.keys():
		user = users.pop(params['user'])
	print('Users left ', users.keys())

@application.route("/ping", methods=["GET"])
def ping():
	return "pong"

if __name__ == "__main__":
	# application.run()
	socketio.run(application, host='0.0.0.0', port='8081')