from flask import Flask, render_template, request
import numpy as np
from modules.dice import dice_roll, reverse_dice, points   

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == "POST":
        # only roll when button is clicked
        result = dice_roll()  
    
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)