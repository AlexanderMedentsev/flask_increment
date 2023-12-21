from os import environ


class Config(object):
    SQLALCHEMY_DATABASE_URI = '{dialect}://{user}:{pw}@{host}/{db}'.format(dialect=environ.get("DATABASE_DIALECT"),
                                                                           user=environ.get("POSTGRES_USER"),
                                                                           pw=environ.get("POSTGRES_PASSWORD"),
                                                                           host=environ.get("POSTGRES_HOST"),
                                                                           db=environ.get("POSTGRES_DB"))
