import gdb 

start_sampling = gdb.Breakpoint("*0x0000555555555175")
stop_sampling = gdb.Breakpoint("*0x0000555555555183")

def start_event(event):
    print("\n### GDB RUN ###\nStart sampling\n###############")
    gdb.execute("continue")

def stop_event(event):
    print("\n### GDB RUN ###\nStop sampling\nFunction input: ",end="")
    mem = gdb.inferiors()[0].read_memory(0x7fffffffdd4c,1).tobytes()
    print(mem,end="\n###############\n\n")
    gdb.execute("continue")
def get_events():
    return {
        start_sampling : start_event,
        stop_sampling : stop_event
        }
    
gdb.execute("file ./hello")
