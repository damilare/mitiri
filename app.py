from setup import app
from public.views import pages
from admin.views import admin

app.register_blueprint(pages)
app.register_blueprint(admin)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


