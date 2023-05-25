import mylog
import asyncio

logger = mylog.get_logger(__name__)

print("I am sub_module1, myid is ", id(logger))


async def f1():
    for _ in range(10):
        logger.debug("I am f1 in module1")
        logger.info("I am f1 in module1")
        logger.warning("I am f1 in module1")
        logger.error("I am f1 in module1")
        logger.critical("I am f1 in module1")
        await asyncio.sleep(1)
    print("sub module 1 DONE")
