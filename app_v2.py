from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

diseases_info = {
    "Late Blight": {
        "solution": "Remove infected plants and apply fungicides.",
        "medicine": "Chlorothalonil",
        "application": "Mix 2 ml of Chlorothalonil per liter of water and spray every 7-10 days during wet weather.",
        "explanation": "A serious disease causing dark blotches on leaves and rapid decay."
    },
    "Powdery Mildew": {
        "solution": "Improve air circulation and apply sulfur-based fungicides.",
        "medicine": "Sulfur fungicide",
        "application": "Apply 3 grams of sulfur fungicide per liter of water at the first sign of disease and repeat every 7-14 days."
    },
    "Leaf Spot": {
        "solution": "Remove affected leaves and use copper-based fungicides.",
        "medicine": "Copper oxychloride",
        "application": "Spray with a solution of 2.5 grams of copper oxychloride per liter of water every 10-14 days during the growing season."
    },
    "Rust": {
        "solution": "Use resistant varieties and apply fungicides.",
        "medicine": "Myclobutanil",
        "application": "Apply fungicide at early disease stages and repeat as needed."
    },
    "Anthracnose": {
        "solution": "Remove infected debris and apply fungicides.",
        "medicine": "Mancozeb",
        "application": "Spray every 7-14 days during disease outbreaks."
    },
    "Bacterial Blight": {
        "solution": "Use disease-free seeds and copper sprays.",
        "medicine": "Copper hydroxide",
        "application": "Apply before flowering and repeat after rain."
    },
    "Fusarium Wilt": {
        "solution": "Use resistant varieties and crop rotation.",
        "medicine": "No chemical control; use cultural practices.",
        "application": "Practice crop rotation and soil solarization."
    },
    "Verticillium Wilt": {
        "solution": "Use resistant varieties and avoid infected soil.",
        "medicine": "No chemical control; use cultural practices.",
        "application": "Rotate crops and improve soil drainage."
    },
    "Downy Mildew": {
        "solution": "Apply fungicides and improve air circulation.",
        "medicine": "Metalaxyl",
        "application": "Spray at early disease signs and repeat every 7-10 days."
    },
    "Scab": {
        "solution": "Use resistant varieties and apply fungicides.",
        "medicine": "Captan",
        "application": "Spray during early fruit development."
    },
    "Black Spot": {
        "solution": "Remove infected leaves and apply fungicides.",
        "medicine": "Chlorothalonil",
        "application": "Spray every 7-10 days during wet weather."
    },
    "Canker": {
        "solution": "Prune infected branches and apply fungicides.",
        "medicine": "Copper fungicide",
        "application": "Apply during dormant season and after pruning."
    },
    "Leaf Curl": {
        "solution": "Apply fungicides and remove infected leaves.",
        "medicine": "Fungicide containing dodine",
        "application": "Spray before bud swell and repeat as needed."
    },
    "Root Rot": {
        "solution": "Improve drainage and avoid overwatering.",
        "medicine": "No effective chemical control.",
        "application": "Use well-drained soil and avoid waterlogging."
    },
    "Smut": {
        "solution": "Use resistant varieties and seed treatment.",
        "medicine": "Carbendazim",
        "application": "Treat seeds before planting."
    },
    "Wilt": {
        "solution": "Use resistant varieties and crop rotation.",
        "medicine": "No chemical control; use cultural practices.",
        "application": "Practice crop rotation and soil management."
    },
    "Blight": {
        "solution": "Remove infected plants and apply fungicides.",
        "medicine": "Copper oxychloride",
        "application": "Spray every 7-14 days during outbreaks."
    },
    "Mosaic Virus": {
        "solution": "Use virus-free seeds and control insect vectors.",
        "medicine": "No chemical control.",
        "application": "Control aphids and whiteflies."
    },
    "Leaf Mold": {
        "solution": "Improve air circulation and apply fungicides.",
        "medicine": "Chlorothalonil",
        "application": "Spray every 7-10 days during humid conditions."
    },
    "Bacterial Spot": {
        "solution": "Use disease-free seeds and copper sprays.",
        "medicine": "Copper hydroxide",
        "application": "Apply before flowering and after rain."
    },
    "Gray Mold": {
        "solution": "Remove infected debris and apply fungicides.",
        "medicine": "Iprodione",
        "application": "Spray during flowering and fruiting stages."
    },
    "Leaf Blight": {
        "solution": "Remove infected leaves and apply fungicides.",
        "medicine": "Mancozeb",
        "application": "Spray every 7-14 days during outbreaks."
    },
    "Downy Spot": {
        "solution": "Apply fungicides and improve air circulation.",
        "medicine": "Metalaxyl",
        "application": "Spray at early disease signs and repeat as needed."
    },
    "Powdery Scab": {
        "solution": "Use resistant varieties and crop rotation.",
        "medicine": "No chemical control; use cultural practices.",
        "application": "Practice crop rotation and soil management."
    },
    "Cercospora Leaf Spot": {
        "solution": "Apply fungicides and remove infected leaves.",
        "medicine": "Chlorothalonil",
        "application": "Spray every 7-10 days during outbreaks."
    }
}

feedbacks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        disease = request.form.get('disease')
        other_disease = request.form.get('other_disease')
        if other_disease and other_disease.strip():
            disease = other_disease.strip()
            disease_info = {
                "solution": "The disease you entered is not in our database. Please consult a local agricultural expert for advice.",
                "medicine": "N/A",
                "application": "N/A"
            }
        else:
            disease_info = diseases_info.get(disease, {
                "solution": "The disease you entered is not in our database. Please consult a local agricultural expert for advice.",
                "medicine": "N/A",
                "application": "N/A"
            })
        return render_template('disease.html', disease=disease, disease_info=disease_info)
    filtered_diseases = [d for d, info in diseases_info.items() if info.get('medicine') and "no chemical control" not in info.get('medicine').lower()]
    return render_template('index.html', diseases=filtered_diseases)

@app.route('/feedback', methods=['POST'])
def feedback():
    feedback_text = request.form.get('feedback_text')
    if feedback_text:
        feedbacks.append(feedback_text)
        flash('Thank you for your feedback!', 'success')
    else:
        flash('Please enter feedback before submitting.', 'error')
    return redirect(request.referrer or url_for('index'))

if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(debug=True, port=5001)
