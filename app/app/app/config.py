from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    tron_network: str = "nile"
    trongrid_api_key: str = ""
    private_key: str
    destination_address: str = "TAm8gAri4sj6t2WdKLsSzEu8zqhGUenQgb"

    class Config:
        env_file = ".env"

settings = Settings()
