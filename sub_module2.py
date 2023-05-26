import mylog
import asyncio

logger = mylog.get_logger(__name__)


async def f2():
    for _ in range(2000):
        logger.debug("I am f2 in module2")
        logger.info("I am f2 in module2")
        logger.warning("I am f2 in module2")
        logger.error("I am f2 in module2")
        logger.critical("I am f2 in module2")
        await asyncio.sleep(2)
    logger.info("sub module 2 DONE")
