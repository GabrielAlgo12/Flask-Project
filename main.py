from flask import Flask
import random

app = Flask(__name__)

facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
            "Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
            "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna."]
url = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]

Moneda= ["Cara", "Cruz"]

@app.route("/")
def hello_world():
    return '<h1>Hola en está pagina hay datos curiosos</h1> <a href="/random_facts">¡Ver un dato aleatorio!</a> <p>Te podria interesar</p> <a href="/Youtube_video"> Este es rl link'
    

@app.route("/random_facts")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/Youtube_video")
def video():
    
    return f"<p>{random.choice(url)}</p>"

app.run(debug=True)
