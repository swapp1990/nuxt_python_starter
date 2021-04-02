import threading
import queue
active_queues = []
active_threads = []


class Worker(threading.Thread):
    def __init__(self, id, modelCls=None, socketio=None):
        threading.Thread.__init__(self)
        self.mailbox = queue.Queue()
        self.id = id
        self.modelCls = modelCls
        self.socketio = socketio
        # print("init worker thread ", self.id)
        # self.modelCls.connect()
        active_queues.append(self.mailbox)
        active_threads.append(self)

    def run(self):
        while True:
            data = self.mailbox.get()
            # print("run ", data['id'])
            if data == 'shutdown':
                return
            if self.id == data['id']:
                # Action to be sent to the current thread class
                if 'actionToCls' in data.keys():
                    # print(data.keys(), data.actionToCls)
                    self.modelCls.doWork(data)
                # Action to be sent directly to client
                elif 'actionToClient' in data.keys():
                    # print('received a message',data['actionToClient'], str(data['id']))
                    self.emitGeneral(data)
            elif 'close' in data.keys():
                if self.id == data['id']:
                    self.stop()

    def sentClient(self, payload):
        # print("sentClient")
        if 'destination' in payload.keys():
            self.emitGeneralFromGlobal(payload)
            return

    # Emit 'General' payload to client with the given session id. Client handles based on the content of the payload
    def emitGeneral(self, payload):
        # print('emitGeneral ', payload.keys())
        # if 'broadcastToAll' in payload.keys():
        #     if payload.broadcastToAll:
        #         print("broadcastToAll")
        #         self.socketio.emit('General', payload)
        #         return
        payload.action = payload.actionToClient
        self.socketio.emit('General', payload, room=payload.id)

    def stop(self):
        print("stop ", self.id)
        self.mailbox.put("shutdown")
        # self.join()
        active_queues.remove(self.mailbox)
        active_threads.remove(self)
        print("active_queues ", len(active_queues),
              "active_threads", len(active_threads))


def clear():
    active_queues = []
    for t in active_threads:
        t.stop()
    print("cleared all threads", active_threads)


def broadcast_event(data):
    for q in active_queues:
        # print("put into q")
        q.put(data)
