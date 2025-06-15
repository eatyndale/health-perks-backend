import uvicorn
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        port = int(os.getenv("PORT", "8000"))
        logger.info(f"Starting server on port {port}")
        logger.info("Environment variables:")
        logger.info(f"PORT: {port}")
        logger.info(f"PYTHONPATH: {os.getenv('PYTHONPATH', 'Not set')}")
        
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=port,
            log_level="debug",
            reload=False,
            access_log=True
        )
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise 