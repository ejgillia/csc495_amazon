from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/cities')
def show_cities():
	return render_template("cities.html", cities = ["xd", "ezpz"])

@app.route('/weights', methods=['POST', 'GET'])
def weights():
	if request.method == "GET":
		return render_template("layout.html")


	if request.method == "POST":

		logistics = float(request.form["logistics"])
		# all the nested logistics stuff starts now
		travel_time = float(request.form["travel_time"]) if len(request.form["travel_time"]) > 0 else logistics
		hours_spent_in_congestion = float(request.form["hours_spent_in_congestion"]) if len(request.form["hours_spent_in_congestion"]) > 0 else logistics
		peak = float(request.form["peak"]) if len(request.form["peak"]) > 0 else logistics
		daytime = float(request.form["daytime"]) if len(request.form["daytime"]) > 0 else logistics
		transit_score = float(request.form["transit_score"]) if len(request.form["transit_score"]) > 0 else logistics
		road_length = float(request.form["road_length"]) if len(request.form["road_length"]) > 0 else logistics
		highway_length = float(request.form["highway_length"]) if len(request.form["highway_length"]) > 0 else logistics


		airway_connectivity = float(request.form["airway_connectivity"]) if len(request.form["airway_connectivity"]) > 0 else logistics
		seattle = float(request.form["seattle"]) if len(request.form["seattle"]) > 0 else airway_connectivity
		new_york = float(request.form["new_york"]) if len(request.form["new_york"]) > 0 else airway_connectivity
		san_francisco = float(request.form["san_francisco"]) if len(request.form["san_francisco"]) > 0 else airway_connectivity
		washington_dc = float(request.form["washington_dc"]) if len(request.form["washington_dc"]) > 0 else airway_connectivity
		
		


		site_building = float(request.form["site_building"])
		# site building info starts now
		
		human_capital = float(request.form["human_capital"]) if len(request.form["human_capital"]) > 0 else site_building
		Infrastructure = float(request.form["Infrastructure"]) if len(request.form["Infrastructure"]) > 0 else site_building
		growth_and_economy = float(request.form["growth_and_economy"]) if len(request.form["growth_and_economy"]) > 0 else site_building
		technology_and_innovation = float(request.form["technology_and_innovation"]) if len(request.form["technology_and_innovation"]) > 0 else site_building
		business_friendly = float(request.form["business_friendly"]) if len(request.form["business_friendly"]) > 0 else site_building
		prosperity = float(request.form["prosperity"]) if len(request.form["prosperity"]) > 0 else site_building


		taxes = float(request.form["taxes"]) if len(request.form["taxes"]) > 0 else site_building
		state_tax = float(request.form["state_tax"]) if len(request.form["state_tax"]) > 0 else taxes
		local_tax = float(request.form["local_tax"]) if len(request.form["local_tax"]) > 0 else taxes



		labor_force = float(request.form["labor_force"])
		#labor force starts now
		average_commute_time = float(request.form["average_commute_time"]) if len(request.form["average_commute_time"]) > 0 else labor_force
		number_of_graduates = float(request.form["number_of_graduates"]) if len(request.form["number_of_graduates"]) > 0 else labor_force
		



		cultural = float(request.form["cultural"])
		# nested cultural stuff starts now
		diversity = float(request.form["diversity"]) if len(request.form["diversity"]) > 0 else cultural
		colleges = float(request.form["colleges"]) if len(request.form["colleges"]) > 0 else cultural
		qol = float(request.form["qol"]) if len(request.form["qol"]) > 0 else cultural

		list_form = [Infrastructure, growth_and_economy, prosperity, human_capital, average_commute_time, diversity, colleges, qol, 
			    seattle, new_york, san_francisco, washington_dc, travel_time, hours_spent_in_congestion, peak, daytime, transit_score,
			    road_length, highway_length, technology_and_innovation, business_friendly, number_of_graduates, state_tax, local_tax]

		print(list_form)
		

		return "k"
