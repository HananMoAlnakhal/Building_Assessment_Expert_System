from flask import Flask, request, jsonify,render_template
from ES import construct_rules,create_fuzzy_system,define_variables,label,r_label,h_label
# Define the Flask app
app = Flask(__name__)


@app.before_first_request
def setup_fuzzy_system():
    global intact_col, tilt, ruble_percentage, building_area, building_hight, damage_per, building_age, damage, habitability, reparability
    global rules, damage_sim, results_sim
    intact_col,tilt, ruble_percentage, building_area, building_hight,damage_per,building_age,damage,habitability,reparability=define_variables()
    # Construct rules
    rules = construct_rules(intact_col,tilt, ruble_percentage, building_area, building_hight,damage_per,building_age,damage,habitability,reparability)
    # Create the fuzzy system
    damage_sim = create_fuzzy_system(rules[:34])
    results_sim = create_fuzzy_system(rules[35:])
    print("made the fuzzy ES!",'\n','-'*50)

@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json  # Parse JSON input
    if not data:
        return jsonify({'error': 'Invalid input data'}), 400
    for key,val in data.items() :
        data[key]=float(val)

    damage_sim.input['building_hight'] = data['building_hight']
    damage_sim.input['ruble_percentage'] = data['ruble_percentage']
    damage_sim.input['building_area'] = data['building_area']
    damage_sim.input['intact_col'] = data['intact_col']
    damage_sim.input['tilt'] = data['tilt']
    damage_sim.compute()
    results_sim.input['damage_out'] = damage_sim.output.get('damage')
    results_sim.input['building_age'] = data['building_age']
    results_sim.compute()
    print(data) 
    return {
        'damage': damage_sim.output.get('damage'),
        'habitability': results_sim.output.get('habitability'),
        'reparability': results_sim.output.get('reparability'),
        'damage_labels':label(damage_per,damage_sim.output.get('damage')),
        'r_labels':r_label(reparability,results_sim.output.get('reparability')),
        'h_labels':h_label(habitability,results_sim.output.get('habitability'))
    }

if __name__ == '__main__':
    app.run()
