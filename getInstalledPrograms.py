from pypsexec.client import Client

server = "WORKGROUP"
username = "xavier johanis"
password = "Xrepyh20090790"
executable = "whoami.exe"
arguments = "/all"

c = Client(server, username=username, password=password,
           encrypt=True)

c.connect()
try:
    c.create_service()
    result = c.run_executable(executable, arguments=arguments)
finally:
    c.remove_service()
    c.disconnect()

print("STDOUT:\n%s" % result[0].decode('utf-8') if result[0] else "")
print("STDERR:\n%s" % result[1].decode('utf-8') if result[1] else "")
print("RC: %d" % result[2])