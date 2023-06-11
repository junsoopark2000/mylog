import sub_module1
import sub_module2
import asyncio
import mylog

logger = mylog.get_logger(__name__)


async def main():
    t1 = asyncio.create_task(sub_module1.f1())
    # t2 = asyncio.create_task(sub_module2.f2())

    await t1
    # await t2


if __name__ == "__main__":
    logger.info("program started")
    asyncio.run(main())
    logger.info("program finished")
