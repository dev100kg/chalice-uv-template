from chalice.app import Chalice

app = Chalice(app_name='chalice-uv-template')

@app.route('/')
def index() -> dict[str, str]:
    return {'hello': 'world'}
