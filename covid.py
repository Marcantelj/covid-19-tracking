# Project: Covid19 python3 flask script
# By Jonathan Marcantel
# 06/18/2020

from flask import Flask, redirect, url_for, render_template
import requests 
import json 
import pygal


app = Flask(__name__)

@app.route('/')
def hello():
	return redirect(url_for('covid'))


@app.route('/COVID19')
def covid():
# Add the name of the function you want to call to the address
	host = "https://api.covid19api.com/summary"
# param and header for api
	parameters = {}
	headers = {}
# we use HTTP GET
	response = requests.get(f'{host}', headers=headers, params=parameters)
# Raise an exception if the call returns an error code
	response.raise_for_status()
# Display the JSON results returned
	results = response.json()
	print(json.dumps(results))

	Global = results['Global']

	totpos = Global["TotalConfirmed"]
	totrec = Global["TotalRecovered"]
	totdeath = Global["TotalDeaths"]
	print(totpos)

# Graph for covid
	graph = pygal.Bar()
	graph.title = 'Global Statistics For Covid19'
	graph.x_labels = ['Total Confirmed Positive','Total Confirmed Recovered', 'Total Deaths' ]
	graph.add('Total Confirmed Positive',  [totpos])
	graph.add('Total Confirmed Recovered',  [totrec])
	graph.add('Total Deaths',  [totdeath])
	graph_data = graph.render_data_uri()

	return render_template("covid.html", graph_data = graph_data)


if __name__ == "__main__":
	app.run()