from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the form data
        name = request.form['name']
        date = request.form['date']
        patient_id = request.form['patient_id']
        image = request.files['image']

        # Save the uploaded image
        image.save('uploads/' + image.filename)

        # Process the data or perform any other required operations

        return "Data uploaded successfully!"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
