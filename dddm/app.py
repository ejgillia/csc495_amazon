from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/weights', methods=['POST', 'GET'])
def weights():
	if request.method == "GET":
		return render_template("layout.html")


	if request.method == "POST":

		logistics = float(request.form["logistics"])
		# all the nested logistics stuff starts now
		travel_time = float(request.form["travel_time"]) if len(request.form["travel_time"]) > 0 else logistics
		hours_spent_in_congestion = float(request.form["hours_spent_in_congestion"]) if len(request.form["hours_spent_in_congestion"]) > 0 else logistics
		ICI = float(request.form["ICI"]) if len(request.form["ICI"]) > 0 else logistics
		peak = float(request.form["peak"]) if len(request.form["peak"]) > 0 else logistics
		daytime = float(request.form["daytime"]) if len(request.form["daytime"]) > 0 else logistics
		overall = float(request.form["overall"]) if len(request.form["overall"]) > 0 else logistics
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
		workforce = float(request.form["workforce"]) if len(request.form["workforce"]) > 0 else site_building
		Infrastructure = float(request.form["Infrastructure"]) if len(request.form["Infrastructure"]) > 0 else site_building
		cost_of_doing_business = float(request.form["cost_of_doing_business"]) if len(request.form["cost_of_doing_business"]) > 0 else site_building
		economy = float(request.form["economy"]) if len(request.form["economy"]) > 0 else site_building
		technology_and_innovation = float(request.form["technology_and_innovation"]) if len(request.form["technology_and_innovation"]) > 0 else site_building
		education = float(request.form["education"]) if len(request.form["education"]) > 0 else site_building
		business_friendly = float(request.form["business_friendly"]) if len(request.form["business_friendly"]) > 0 else site_building
		access_to_capital = float(request.form["access_to_capital"]) if len(request.form["access_to_capital"]) > 0 else site_building


		taxes = float(request.form["taxes"]) if len(request.form["taxes"]) > 0 else site_building
		state_tax = float(request.form["state_tax"]) if len(request.form["state_tax"]) > 0 else taxes
		local_tax = float(request.form["local_tax"]) if len(request.form["local_tax"]) > 0 else taxes
		sales_tax = float(request.form["sales_tax"]) if len(request.form["sales_tax"]) > 0 else taxes



		labor_force = float(request.form["labor_force"])
		#labor force starts now
		average_commute_time = float(request.form["average_commute_time"]) if len(request.form["average_commute_time"]) > 0 else labor_force
		number_of_graduates = float(request.form["number_of_graduates"]) if len(request.form["number_of_graduates"]) > 0 else labor_force
		



		cultural = float(request.form["cultural"])
		# nested cultural stuff starts now
		diversity = float(request.form["diversity"]) if len(request.form["diversity"]) > 0 else cultural
		colleges = float(request.form["colleges"]) if len(request.form["colleges"]) > 0 else cultural
		quality_of_life = float(request.form["quality_of_life"]) if len(request.form["quality_of_life"]) > 0 else cultural
		all_city_rank = float(request.form["all_city_rank"]) if len(request.form["all_city_rank"]) > 0 else cultural
		qol = float(request.form["qol"]) if len(request.form["qol"]) > 0 else cultural

		x = locals()
		for item in x: print(item, x[item])


		return "k"
