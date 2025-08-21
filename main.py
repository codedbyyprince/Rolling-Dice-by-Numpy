from flask import Flask, render_template, request
import numpy as np
from modules.dice import dice_roll, reverse_dice, points   

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
