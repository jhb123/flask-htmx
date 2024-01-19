from app import create_app

if __name__ == "__main__":
    # use this to start it in debug mode
    app =  create_app()

    app.run(host="0.0.0.0", port="5000", debug=True)