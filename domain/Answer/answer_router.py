from fastapi import APIRouter

router = APIRouter(
    prefix = "/api"
)


@router.get("/answer")
async def get_question():
    pass

@router.post("/answer")
async def create_question():
    pass

@router.put("/answer/{answer_id}")
async def update_question():
    pass

@router.delete("/answer/{answer_id}")
async def delete_question():
    pass
