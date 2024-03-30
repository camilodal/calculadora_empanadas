# app.py
from flask import Flask, render_template, request, session
import pandas as pd
import random

app = Flask(__name__)

# Cargar el archivo CSV
df = pd.read_csv('vocabulario_clases.csv')

app.secret_key = 'clave_secreta'  # Clave secreta para la sesión


def obtener_palabra_y_traduccion():
    random_row = df.sample()

    word_english = random_row['word_english'].iloc[0]
    word_spanish = random_row['word_spanish'].iloc[0]
    if random.choice([True, False]):
        return word_english, word_spanish
    else:
        return word_spanish, word_english

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/practice', methods=['GET', 'POST'])
def practice():
    session['word'], session['translation'] = obtener_palabra_y_traduccion()  # Siempre actualizar la palabra en la sesión
    if request.method == 'POST':
        return render_template('practice.html', word=session['word'], correct_translation=session['translation'])
    return render_template('practice.html', word=session['word'])

@app.route('/check', methods=['POST'])
def check():
    user_translation = request.form['translation']
    correct_translation = session['translation']
    is_correct = user_translation.lower() == correct_translation.lower()
    #word, translation = obtener_palabra_y_traduccion()
    return render_template('check.html', word=session['word'], is_correct=is_correct, correct_translation=correct_translation)

if __name__ == '__main__':
    app.run(debug=True)
