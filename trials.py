import subprocess
import logging 
logging.basicConfig(filename='example.log',level=logging.DEBUG)
try:
    print subprocess.check_call(["ls","-ltr"])
except subprocess.CalledProcessError as e:
    print "Command failed"
    print e.returncode

try:
    output = subprocess.check_output(["s","-h"],stderr=subprocess.STDOUT,shell=True)
    print output
except subprocess.CalledProcessError as e:
    logging.warning("Command failed")
    print e.output


print '\nread:'
proc = subprocess.Popen(['echo', '"to stdout"'], 
                        stdout=subprocess.PIPE,
                        )
stdout_value = proc.communicate()[0]
print '\tstdout:', repr(stdout_value)


print '\nwrite:'
proc = subprocess.Popen(['cat', '-'],
                        stdin=subprocess.PIPE,
                        )
proc.communicate('\tstdin: to stdin\n')

print __name__
