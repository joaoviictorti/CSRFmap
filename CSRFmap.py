import argparse
from payloads.csrf_payloads import CSRF

def banner():
    return """
  ____________  ____              
 / ___/ __/ _ \/ __/_ _  ___ ____ 
/ /___\ \/ , _/ _//  ' \/ _ `/ _ \\
\___/___/_/|_/_/ /_/_/_/\_,_/ .__/
                           /_/ 
                           Autor: joaovictorti
                           version: 1.1  

    """

parser = argparse.ArgumentParser(prog=banner(),usage="python3 CSRFmap.py -a \"http://exemplo.com\" -m post -pl form_interaction -n username password token")

parser.add_argument("-a","-A",dest="action",action="store",type=str,required=True,help="Insert action")
parser.add_argument("-m","-M",dest="method",action="store",type=str,required=True,help="Insert method")
parser.add_argument("-p",dest="payload",action="store",type=str,help=False,choices=["form1","form2","json1","json2"])
parser.add_argument("-n","-name",nargs="+",dest="name",action="store",required=True,help="Insert name")
parser.add_argument("-v","-value",nargs="+",dest="value",action="store",required=False,default="__valor__",help="Insert values")
args = parser.parse_args()

if __name__ == "__main__":
    
    match args.payload:
        case "form1":
            match args.value:
                case "__valor__":
                    CSRF(action=args.action,method=args.method,name=args.name,values=args.value).CsrfUserInteraction()
                case _:
                    if len(args.name) == len(args.value):
                        CSRF(action=args.action,method=args.method,name=args.name,values=args.value).CsrfUserInteraction()
                    else:
                        print(CSRF().Error)
        case "form2":
            match args.value:
                case "__valor__":
                    CSRF(action=args.action,method=args.method,name=args.name,values=args.value).CsrfNoUserInteraction()
                case _:
                    if len(args.name) == len(args.value):
                        CSRF(action=args.action,method=args.method,name=args.name,values=args.value).CsrfNoUserInteraction()
                    else:
                        print(CSRF().Error)
        case "json1":
            match args.value:
                case "__valor__":
                    CSRF(action=args.action,method=args.method,name=args.name,values=args.value).CsrfJson()
                case _:
                    if len(args.name) == len(args.value):
                        CSRF(action=args.action,method=args.method,name=args.name,values=args.value).CsrfJson()
                    else:
                        print(CSRF().Error)
        case "json2":
            match args.value:
                case "__valor__":
                    CSRF(action=args.action,method=args.method,name=args.name,values=args.value).CsrfJsonCredentials()
                case _:
                    if len(args.name) == len(args.value):
                        CSRF(action=args.action,method=args.method,name=args.name,values=args.value).CsrfJsonCredentials()
                    else:
                        print(CSRF().Error)
        case _:
            pass