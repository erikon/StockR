from flask import Flask, render_template, Blueprint
from application.mod_api.controllers import *

import json

mod_game = Blueprint('game', __name__, url_prefix='/game')

def getSectors():
    data = get_sectors();
    print data;
    return render_template('index.html',
                            data = data);
getSectors();
