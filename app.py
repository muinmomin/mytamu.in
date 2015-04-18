__author__ = 'Muin'
from flask import Flask, render_template, request, jsonify
import extractdata

app = Flask(__name__)