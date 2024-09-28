class Config:
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    
class TestingConfig(Config):
    TESTING = True
    DEBUG = True 
    
class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'    