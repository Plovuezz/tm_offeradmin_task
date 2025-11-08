import granian
from granian.constants import Interfaces, Loops
from granian.log import LogLevels
import platform
from granian.constants import Loops

from config import get_settings

settings = get_settings()

system = platform.system()

if __name__ == "__main__":
    granian.Granian(
        target="application:build_app",
        factory=True,
        address=settings.APP_HOST,
        port=settings.APP_PORT,
        interface=Interfaces.ASGI,
        log_level=LogLevels.info,
        loop=Loops.asyncio,
    ).serve()
