# -*- coding: iso-8859-1 -*-
"""
run_reloading_server
====================

:Author: Martin Wendt, moogle(at)wwwendt.de 
:Copyright: Lesser GNU Public License, see LICENSE file attached with package

Wrapper for run_server, that restarts the server when source code is modified.
"""
import subprocess
import sys
from subprocess import call, Popen 

def run():
    args = sys.argv[1:]
    if not "--reload" in args:
        args.append("--reload")

    print "run_reloading_server", args 

    try:
        while True:
            p = Popen(["python", "run_server.py", "-v"] + args, 
#                      stdin=sys.stdin, 
#                      stdout=subprocess.PIPE, 
#                      stderr=subprocess.PIPE, 
    #                  preexec_fn, close_fds, shell, cwd, env, universal_newlines, startupinfo, creationflags
                      )
            sys.stdout = p.stdout
            sys.stderr = p.stderr
            p.wait()
            sys.stdout = sys.__stdout__
            sys.stderr = sys.__stderr__
            
            if p.returncode == 3:
                print "run_server returned 3: restarting..."
            else:
                print "run_server returned %s: terminating." % p.returncode
                break
            
    except Exception, e:
        raise e
#    while 3 == call(["python", "run_server.py"] + args):
#        print "run_server returned 3: restarting..."
    
    
    
    
if __name__ == "__main__":
    run()
