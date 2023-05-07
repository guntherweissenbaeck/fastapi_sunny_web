from fastapi import APIRouter
from .models import SunnyWebData
from .database import cursor, conn

router = APIRouter()


@router.get("/power/{year}/{month}")
async def retrieve_power_per_moth(year: int, month: int):
    cursor.execute(
        "SELECT created_at, power FROM t_power WHERE power <> 0 AND EXTRACT( YEAR FROM CREATED_AT) = %s AND EXTRACT( MONTH FROM CREATED_AT) = %s",
        (year, month))
    power = cursor.fetchall()
    return {"data": power}

@router.get("/d-yield/{year}")
async def retrieve_daily_yield_per_moth(year: int):
    cursor.execute(
        "SELECT created_at::timestamp::date, daily_yield FROM t_power WHERE EXTRACT( YEAR FROM CREATED_AT) = %s AND EXTRACT(HOUR FROM CREATED_AT) >= 23 AND EXTRACT(MINUTE FROM CREATED_AT) >= 59 ORDER BY created_at ASC",
        (year,))
    dyield = cursor.fetchall()
    return {"data": dyield}



@router.get("/d-yield/{year}/{month}")
async def retrieve_daily_yield_per_moth(year: int, month: int):
    cursor.execute(
        "SELECT created_at::timestamp::date, daily_yield FROM t_power WHERE daily_yield <> 0 AND EXTRACT( YEAR FROM CREATED_AT) = %s AND EXTRACT( MONTH FROM CREATED_AT) = %s AND EXTRACT(HOUR FROM CREATED_AT) >= 23 AND EXTRACT(MINUTE FROM CREATED_AT) >= 59 ORDER BY created_at ASC",
        (year, month))
    dyield = cursor.fetchall()
    return {"data": dyield}


@router.get("/t-yield")
async def retrieve_total_yield():
    cursor.execute(
        """SELECT CREATED_AT::timestamp::date, TOTAL_YIELD FROM T_POWER WHERE EXTRACT(HOUR FROM CREATED_AT) >= 23 AND EXTRACT(MINUTE FROM CREATED_AT) >= 59 ORDER BY created_at ASC""")
    tyield = cursor.fetchall()
    return {"data": tyield}


@router.post("/data")
async def add_data(data: SunnyWebData):
    cursor.execute(
        "INSERT INTO t_power (power, daily_yield, total_yield) VALUES (%s, %s ,%s) RETURNING *",
        (data.power, data.daily_yield, data.total_yield),)
    new_data = cursor.fetchone()
    conn.commit()
    # data_list.append(data)
    return {"data": new_data}
