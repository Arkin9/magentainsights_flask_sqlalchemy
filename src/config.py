class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@127.0.0.1:3306/flask_aplication'
    SQLALCHEMY_TRACK_MODIFICATIONS = False