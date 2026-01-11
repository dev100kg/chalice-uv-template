from chalice.app import Chalice

app = Chalice(app_name='chalice-uv-template')

@app.route('/')
def index():
    return {'hello': 'world'}
