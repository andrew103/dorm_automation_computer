from server_backend_pi.main import app

if __name__ == "__main__":
    app.secret_key = "dorm_comp_password"
    app.debug = True
    app.run(port=8000)
