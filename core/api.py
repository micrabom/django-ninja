from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/add")
def add(request, a: int, b: int):
    return {"result": a + b}

@api.get("/minus")
def minus(request, a: int, b: int):
    return {"result": a - b}

@api.get("/multiply")
def multiply(request, a: int, b: int):
    return {"result": a * b}
