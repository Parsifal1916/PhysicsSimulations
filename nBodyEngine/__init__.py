from . import Body
from . import GraphEngine
import json
import os

print('Modulo importato con successo')

def simulateFromJson(jsonFile: str) -> None:
	cwd: str = os.getcwd()
	with open(cwd+'\\'+jsonFile, 'r') as file:
		content = json.load(file) # estrae il contenuto del file

		#crea i corpi
		bodies: list = []
		_bodies: list = content['Bodies']
		for i in _bodies:
			bodies.append(Body.Body(i, bodies))


		#comincia la simulazione
		print(content['Simulation']['size'])
		simulation = GraphEngine.Graph(bodies, content['Simulation']['size'])
		simulation.start(content['Simulation']['speed'])
		print(cwd)
