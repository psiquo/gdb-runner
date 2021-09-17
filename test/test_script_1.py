import gdb 

start_sampling = gdb.Breakpoint("*0x0000555555555175")
stop_sampling = gdb.Breakpoint("*0x0000555555555183")
start_event = lambda x: print("Start sampling")
stop_event = lambda x: print("Stop sampling")

def get_events():
    return {
        start_sampling : start_event,
        stop_sampling : stop_event
        }
    
gdb.execute("file ./hello")
