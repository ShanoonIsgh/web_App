from flask import Flask, render_template

def foo(name):
    return render_template('index.html', to=name)
