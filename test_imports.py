import sys
import os

print("Python path:", sys.path)
print("Current directory:", os.getcwd())
print("Directory contents:", os.listdir("."))
print("App directory contents:", os.listdir("app"))

try:
    from app.main import app
    print("Successfully imported app")
except Exception as e:
    print("Failed to import app:", str(e)) 