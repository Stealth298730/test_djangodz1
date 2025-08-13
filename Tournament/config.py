from pydantic_settings import BaseSettings,SettingsConfigDict


class Settings(BaseSettings):
    engine:str
    name:str
    password:str
    host:str
    port:str
    user:str
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()