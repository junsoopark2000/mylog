import mylog
import asyncio

logger = mylog.get_logger(__name__)


async def f1():
    for _ in range(1200):
        logger.debug("I am f1 in module1")
        logger.info("I am f1 in module1")
        logger.warning("I am f1 in module1")
        logger.error("I am f1 in module1")
        logger.critical("I am f1 in module1")
        await asyncio.sleep(3)
    logger.info("sub module 1 DONE")
