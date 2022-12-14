import argparse
from payloads.csrf_payloads import Generator

def banner():
    return """
  ____________  ____              
 / ___/ __/ _ \/ __/_ _  ___ ____ 
/ /___\ \/ , _/ _//  ' \/ _ `/ _ \\
\___/___/_/|_/_/ /_/_/_/\_,_/ .__/
                           /_/ 
                           Autor: joaovictorti
                           version: 1.0  

    """

parser = argparse.ArgumentParser(prog=banner(),usage="python3 CSRFmap.py -a \"http://exemplo.com\" -m post -pl form_interaction -n username password token")

parser.add_argument("-a","-A",dest="action",action="store",type=str,required=True,help="")
parser.add_argument("-m","-M",dest="method",action="store",type=str,required=True,help="")
parser.add_argument("-pl",dest="payload",action="store",type=str,help=False,choices=["form_interaction","form_no_interaction","json_request","json_credentials"])
parser.add_argument("-n","-name",nargs="+",dest="name",action="store",required=True,help="")
args = parser.parse_args()

if __name__ == "__main__":
    
    match args.payload:
        case "form_interaction":
            Generator(action=args.action,method=args.method,name=args.name).CsrfUserInteraction()
        case "form_no_interaction":
            Generator(action=args.action,method=args.method,name=args.name).CsrfNoUserInteraction()
        case "json_request":
            Generator(action=args.action,method=args.method,name=args.name).CsrfJson()
        case "json_credentials":
            Generator(action=args.action,method=args.method,name=args.name).CsrfJsonCredentials()
        case _:
            pass