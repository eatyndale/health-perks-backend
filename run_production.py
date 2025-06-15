import uvicorn
from config import settings

if __name__ == "__main__":
    ssl_keyfile = settings.SSL_KEY if settings.SSL_KEY else None
    ssl_certfile = settings.SSL_CERTIFICATE if settings.SSL_CERTIFICATE else None
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        ssl_keyfile=ssl_keyfile,
        ssl_certfile=ssl_certfile,
        workers=4,  # Adjust based on your server's CPU cores
        proxy_headers=True,
        forwarded_allow_ips="*"
    ) 