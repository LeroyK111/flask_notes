#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, abort

# 为
index = Blueprint('index', __name__, template_folder='templates')
