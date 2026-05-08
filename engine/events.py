
class Event:
    def __init__(self, name: str, data: dict = None):
        self.name = name
        self.data = data or {}
class EventManager:
    def __init__(self):
        self.disparos= {}

    def subscribe(self, tipo_evento: str, callback):
        if tipo_evento not in self.disparos:
            self.disparos[tipo_evento] = []
        self.disparos[tipo_evento].append(callback)

    def emit(self, event: Event):
        if event.name in self.disparos:
            for callback in self.disparos[event.name]:
                callback(event.data)    
event_manager = EventManager()      

