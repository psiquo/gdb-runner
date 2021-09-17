import gdb 

if "get_events" in locals().keys():
    gdb.events.stop.connect(IsolateExecutionListener(get_events()))
    gdb.execute("run")
else:
    raise gdb.GdbError ("No function get events provided")

