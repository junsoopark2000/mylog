import mylog
import asyncio

logger = mylog.get_logger(__name__)

print("I am sub_module2, myid is ", id(logger))


async def f2():
    for _ in range(3):
        logger.debug("I am f2 in module2")
        logger.info("I am f2 in module2")
        logger.warning("I am f2 in module2")
        logger.error("I am f2 in module2")
        logger.critical("I am f2 in module2")
        await asyncio.sleep(1)
    print("sub module 2 DONE")
