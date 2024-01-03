# hello_world.py
from prefect import flow, serve


@flow(name="Hello world")
def hello_world(name: str = "world"):
    print(f"Hello {name}!")


if __name__ == "__main__":
    hello_world_deployment = hello_world.to_deployment(
        name='Hello world Deployment',
        version='0.1.0',
        tags=['hello world'],
        interval=600,
        parameters={
            'name': 'John Doe'
        }
    )
    # Above: can be tested in notebook. Below: must be called from python script
    serve(hello_world_deployment)