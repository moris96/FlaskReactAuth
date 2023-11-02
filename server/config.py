class ApplicationConfig:
    #stops logging useless messages
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    #whats happening with database
    SQLALCHEMY_ECHO = True
    #using sqlite database 
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./db.sqlite"