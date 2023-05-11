from fastapi import APIRouter

from .database import cursor, conn
from .models import SunnyWebData


router = APIRouter()


@router.get("/power/{year}")
async def retrieve_power_per_year(year: int):
    cursor.execute(
        """SELECT created_at, power FROM t_power WHERE power <> 0 AND EXTRACT(
        YEAR FROM CREATED_AT) = %s""",
        (year,))
    power = cursor.fetchall()
    if not power:
        return {"message": "No Data within the given Date"}
    return {"data": power}


@router.get("/power/{year}/{month}")
async def retrieve_power_per_month(year: int, month: int):
    cursor.execute(
        """SELECT created_at, power FROM t_power WHERE power <> 0 AND EXTRACT(
        YEAR FROM CREATED_AT) = %s AND EXTRACT( MONTH FROM CREATED_AT) = %s""",
        (year, month))
    power = cursor.fetchall()
    if not power:
        return {"message": "No Data within the given Date"}
    return {"data": power}


@router.get("/power/{year}/{month}/{day}")
async def retrieve_power_per_day(year: int, month: int, day: int):
    cursor.execute(
        """SELECT created_at, power FROM t_power WHERE power <> 0 AND EXTRACT(
        YEAR FROM CREATED_AT) = %s AND EXTRACT( MONTH FROM CREATED_AT) = %s
        AND EXTRACT( DAY FROM CREATED_AT) = %s
        """,
        (year, month, day))
    power = cursor.fetchall()
    if not power:
        return {"message": "No Data within the given Date"}
    return {"data": power}


@router.get("/d-yield/{year}")
async def retrieve_daily_yield_per_year(year: int):
    cursor.execute(
        """SELECT created_at::timestamp::date, daily_yield FROM t_power WHERE
        EXTRACT( YEAR FROM CREATED_AT) = %s AND EXTRACT(HOUR FROM CREATED_AT)
        >= 23 AND EXTRACT(MINUTE FROM CREATED_AT) >= 59 ORDER BY created_at
        ASC""",
        (year,))
    dyield = cursor.fetchall()
    if not dyield:
        return {"message": "No Data within the given Date"}
    return {"data": dyield}


@router.get("/d-yield/{year}/{month}")
async def retrieve_daily_yield_per_month(year: int, month: int):
    cursor.execute(
        """SELECT created_at::timestamp::date, daily_yield FROM t_power WHERE
        daily_yield <> 0 AND EXTRACT( YEAR FROM CREATED_AT) = %s AND EXTRACT(
            MONTH FROM CREATED_AT) = %s AND EXTRACT(HOUR FROM CREATED_AT) >= 23
        AND EXTRACT(MINUTE FROM CREATED_AT) >= 59 ORDER BY created_at ASC""",
        (year, month))
    dyield = cursor.fetchall()
    if not dyield:
        return {"message": "No Data within the given Date"}
    return {"data": dyield}


@router.get("/d-yield/{year}/{month}/{day}")
async def retrieve_daily_yield_per_day(year: int, month: int, day: int):
    cursor.execute(
        """SELECT created_at::timestamp::date, daily_yield FROM t_power WHERE
        daily_yield <> 0 AND EXTRACT( YEAR FROM CREATED_AT) = %s AND EXTRACT(
            MONTH FROM CREATED_AT) = %s AND EXTRACT( DAY FROM CREATED_AT) = %s
        AND EXTRACT(HOUR FROM CREATED_AT) >= 23 AND EXTRACT(MINUTE FROM
        CREATED_AT) >= 59 ORDER BY created_at ASC""",
        (year, month, day))
    dyield = cursor.fetchall()
    if not dyield:
        return {"message": "No Data within the given Date"}
    return {"data": dyield}


@router.get("/t-yield")
async def retrieve_total_yield():
    cursor.execute(
        """SELECT CREATED_AT::timestamp::date, TOTAL_YIELD FROM T_POWER WHERE
        EXTRACT(HOUR FROM CREATED_AT) >= 23 AND EXTRACT(MINUTE FROM CREATED_AT)
        >= 59 ORDER BY created_at ASC""")
    tyield = cursor.fetchall()
    return {"data": tyield}


@router.get("/t-yield/{year}")
async def retrieve_total_yield_per_year(year: int):
    cursor.execute(
        """SELECT CREATED_AT::timestamp::date, TOTAL_YIELD FROM T_POWER WHERE
        EXTRACT(HOUR FROM CREATED_AT) >= 23 AND EXTRACT(MINUTE FROM CREATED_AT)
        >= 59 AND EXTRACT( YEAR FROM CREATED_AT) = %s ORDER BY created_at
        ASC""", (year,))
    tyield = cursor.fetchall()
    if not tyield:
        return {"message": "No Data within the given Date"}
    return {"data": tyield}


@router.get("/t-yield/{year}/{month}")
async def retrieve_total_yield_per_month(year: int, month: int):
    cursor.execute(
        """SELECT CREATED_AT::timestamp::date, TOTAL_YIELD FROM T_POWER WHERE
        EXTRACT(HOUR FROM CREATED_AT) >= 23 AND EXTRACT(MINUTE FROM CREATED_AT)
        >= 59 AND EXTRACT( YEAR FROM CREATED_AT) = %s AND EXTRACT( MONTH FROM
        CREATED_AT) = %s ORDER BY created_at ASC""", (year, month))
    tyield = cursor.fetchall()
    if not tyield:
        return {"message": "No Data within the given Date"}
    return {"data": tyield}


@router.get("/t-yield/{year}/{month}/{day}")
async def retrieve_total_yield_per_day(year: int, month: int, day: int):
    cursor.execute(
        """SELECT CREATED_AT::timestamp::date, TOTAL_YIELD FROM T_POWER WHERE
        EXTRACT(HOUR FROM CREATED_AT) >= 23 AND EXTRACT(MINUTE FROM CREATED_AT)
        >= 59 AND EXTRACT( YEAR FROM CREATED_AT) = %s AND EXTRACT( MONTH FROM
        CREATED_AT) = %s AND EXTRACT( DAY FROM CREATED_AT) = %s ORDER BY
        created_at ASC""", (year, month, day))
    tyield = cursor.fetchall()
    if not tyield:
        return {"message": "No Data within the given Date"}
    return {"data": tyield}


@router.post("/data")
async def add_data(data: SunnyWebData):
    cursor.execute(
        """INSERT INTO t_power (power, daily_yield, total_yield) VALUES (%s, %s
        ,%s) RETURNING *""",
        (data.power, data.daily_yield, data.total_yield),)
    new_data = cursor.fetchone()
    conn.commit()
    return {"data": new_data}
