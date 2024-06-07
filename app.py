from flask import Flask, request, render_template
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    make = request.form['make']
    model = request.form['model']
    year = request.form['year']
    color = request.form['color']
    features = request.form['features']
    
    # Write the form data to a CSV file
    with open('ideal_cars.csv', 'a', newline='') as csvfile:
        fieldnames = ['Make', 'Model', 'Year', 'Color', 'Features']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write the header only if the file is empty
        if csvfile.tell() == 0:
            writer.writeheader()
        
        writer.writerow({
            'Make': make,
            'Model': model,
            'Year': year,
            'Color': color,
            'Features': features
        })
    
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
