import os
from dotenv import load_dotenv

load_dotenv()

print("🔍 DB_USERNAME:", os.getenv("DB_USERNAME"))
print("🔍 DB_PASSWORD:", os.getenv("DB_PASSWORD"))
print("🔍 DB_HOST:", os.getenv("DB_HOST"))

class ConfigDebug:
    # Hämtar miljövariabler och använder standardvärden vid behov
    DB_USERNAME = os.getenv('DB_USERNAME', 'root')  # Standard: root
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')  # Standard: tomt
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '3306')  # MySQL standardport
    DB_NAME = os.getenv('DB_NAME', 'shop20220128')

    # Bygger upp databas-URI:n dynamiskt med infon från .env filen
    SQLALCHEMY_DATABASE_URI = f'mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
    
    # Flask hemlig nyckel
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')

    # Flask-Mail SMTP server settings
    MAIL_SERVER = os.getenv('MAIL_SERVER', '127.0.0.1')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 1025))  # Konvertera till int
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'False').lower() in ['true', '1']
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'False').lower() in ['true', '1']
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'email@example.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'password')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', '"MyApp" <noreply@example.com>')

    # Flask-User settings
    USER_APP_NAME = os.getenv('USER_APP_NAME', "Flask-User Basic App")
    USER_ENABLE_EMAIL = os.getenv('USER_ENABLE_EMAIL', 'True').lower() in ['true', '1']
    USER_ENABLE_USERNAME = os.getenv('USER_ENABLE_USERNAME', 'False').lower() in ['true', '1']
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = os.getenv('USER_EMAIL_SENDER_EMAIL', "noreply@example.com")

    # Flask-Security salt
    SECURITY_PASSWORD_SALT = os.getenv('SECURITY_PASSWORD_SALT', "341231232")