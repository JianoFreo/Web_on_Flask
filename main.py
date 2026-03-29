from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) 
    #debug=True
    #everytime we change anything to the python code
    #it will automatically rerun the web server
    #in production you want this to be off
    