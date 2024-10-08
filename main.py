from fastapi import FastAPI, Query, Body
import uvicorn

app = FastAPI()


@app.get("/")
def func():
    return "Hello, World!!"


hotels = [
    {"id": 1, "title": "One"},
    {"id": 2, "title": "Second"},
    {"id": 3, "title": "Third"}
]


@app.get("/hotels")
def get_hotels(
        id: int | None = Query(None, description="Id"),
        title: str | None = Query(None, description="Название отеля")
):
    hotels_ = []
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue
        if title and hotel["title"] != title:
            continue
        hotels_.append(hotel)
    return hotels_


@app.put("/hotels/{hotel_id}")
def full_change_hotel(hotel_id: int, title: str = Body(..., embed=True)):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            hotel["title"] = hotel.title
            return {
                "message": "Данные об отеле успешно обновлены",
                "hotel": hotel
            }
    return {"message": "Отель не найден"}, 404


@app.patch("/hotels/{hotel_id}")
def part_change_hotel(hotel_id: int, title: str = Body(..., embed=True)):
    global hotels
    for hotel in hotels:
        if hotel["id"] == hotel_id:
            if hotel.title is not None:
                hotel["title"] = hotel.title
            if hotel.id is not None:
                hotel["id"] = hotel.id
            return {
                    "message": "Данные об отеле успешно обновлены",
                    "hotel": hotel
                }
    return {"message": "Отель не найден"}, 404


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
