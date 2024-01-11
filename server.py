from rich import print

from fastapi import FastAPI

from routes.route import router

app = FastAPI()

app.include_router(router=router)

# Run the application with uvicorn
if __name__ == "__main__":
    import uvicorn
    print("[green]STARTING UP...![/green]")
    uvicorn.run("server:app", host="0.0.0.0", port=8181, reload=True)
