from fastapi import FastAPI, Query, Body, APIRouter
from schemas.hotels import Hotel, HotelPatch

router = APIRouter(prefix="/hotels", tags=["Отели"])

hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Дубай", "name": "dubai"},
    {"id": 4, "title": "Дубай", "name": "dubai"},
    {"id": 5, "title": "Дубай", "name": "dubai"},
    {"id": 6, "title": "Дубай", "name": "dubai"},
    {"id": 7, "title": "Дубай", "name": "dubai"},
    {"id": 8, "title": "Дубай", "name": "dubai"}
]

@router.get("/", summary="Получить все отели")
def get_hotels(
        id: int | None = Query(None, description="Айдишник"),
        title: str | None = Query(None, description="Название отеля"),
        page: int = Query(1, description="Страница", ge=1),
        per_page: int = Query(3, description="Кол-во элементов на странице", ge=1)
):
    filtered_hotels = []
    
    for hotel in hotels:
        if id and hotel["id"] != id:
            continue
        if title and hotel["title"] != title:
            continue
        filtered_hotels.append(hotel)
    
    start = (page - 1) * per_page
    end = start + per_page
    
    paginated_hotels = filtered_hotels[start:end]
    
    return {
        "total": len(filtered_hotels),
        "page": page,
        "per_page": per_page,
        "data": paginated_hotels
    }


@router.post("/", summary="Добавить данные об отеле")
def create_hotel(
        hotel_data: Hotel
):
    global hotels
    hotels.append({
        "id": hotels[-1]["id"] + 1,
        "title": hotel_data.title,
        "name": hotel_data.name
    })
    return {"status": "OK"}


@router.put("/{hotel_id}", summary="Полное обновление данных об отеле")
def edit_hotel(hotel_id: int, hotel_data: Hotel):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == hotel_id][0]
    hotel["title"] = hotel_data.title
    hotel["name"] = hotel_data.name
    return {"status": "OK"}


@router.patch(
    "/{hotel_id}",
    summary="Частичное обновление данных об отеле",
    description="<h1>Тут мы частично обновляем данные об отеле: можно отправить name, а можно title</h1>",
)
def partially_edit_hotel(
        hotel_id: int,
        hotel_data: HotelPatch
):
    global hotels
    hotel = [hotel for hotel in hotels if hotel["id"] == hotel_id][0]
    if hotel_data.title:
        hotel["title"] = hotel_data.title
    if hotel_data.name:
        hotel["name"] = hotel_data.name
    return {"status": "OK"}


@router.delete("/{hotel_id}", summary="Удаленгие данных об отеле")
def delete_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel["id"] != hotel_id]
    return {"status": "OK"}