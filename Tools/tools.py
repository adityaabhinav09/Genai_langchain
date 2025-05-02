print("Everything is Okay")
from dotenv import dotenv_values

secrets = dotenv_values(".env")
print(secrets)  # Shows all key-value pairs
