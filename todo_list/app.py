from distutils.log import debug
from ssl import CertificateError
from todo_list import create_app 

app = create_app()

if __name__ == "__main__": 
    app.run(debug =True)