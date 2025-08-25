from fastapi import FastAPI
from fastapi.routing import APIRoute

def ensure_unique_route_names(app: FastAPI) -> None:
    """
    检查路由名称的唯一

    :param app: FastAPI实例
    :return:
    """
    temp_routes = set()
    for route in app.routes:
        if isinstance(route, APIRoute):
            if route.name in temp_routes:
                raise ValueError(f'Non-unique route name: {route.name}')
            temp_routes.add(route.name)