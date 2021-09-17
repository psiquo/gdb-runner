import gdb

class IsolateExecutionListener:
    def __init__(self, breakpoint_event_dictionary):
        self.call_event = breakpoint_event_dictionary
    def __call__(self,event):
        if(isinstance(event,gdb.BreakpointEvent)) and event.breakpoint in self.call_event.keys():
            self.call_event[event.breakpoint](event)
            