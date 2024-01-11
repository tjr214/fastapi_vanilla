# from rich import print
from fastapi import APIRouter

from models.todos import Todo
from config.db import collection_name
from bson import ObjectId
from typing import List

router = APIRouter()


@router.get("/")
async def get_todos() -> List[dict]:
    return_list = []
    for todo_data in collection_name.find():
        todo = {
            "id": str(todo_data["_id"]),
            "name": todo_data["name"],
            "description": todo_data["description"],
            "task_complete": todo_data["task_complete"],
        }
        return_list.append(todo)
    return return_list


@router.post("/")
def post_todos(todo: Todo):
    # Notice: NO ASYNC because writing to dB
    collection_name.insert_one(dict(todo))
    return {
        "status": 1,
        "data": "insert_good",
    }


@router.put("/{id}")
def put_todo(id: str, todo: Todo):
    # Notice: NO ASYNC because writing to dB
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(todo)})


@router.delete("/{id}")
def delete_todo(id: str):
    # Notice: NO ASYNC because writing to dB
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
