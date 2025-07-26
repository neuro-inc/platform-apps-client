from typing import Any

import pytest
from aiohttp import web
from aiohttp.pytest_plugin import AiohttpServer

from platform_apps_client import AppInstance, AppsApiClient, AppsApiException


async def test_get_app(
    client: AppsApiClient,
    srv_port: int,
    aiohttp_server: AiohttpServer,
    app_instance_json: dict[str, str],
) -> None:
    async def hello(request: web.Request) -> web.Response:
        return web.json_response(app_instance_json)

    app = web.Application()
    app.router.add_get("/apis/apps/v2/instances/test-app-id", hello)
    await aiohttp_server(app, port=srv_port)

    app_instance = await client.get_app(app_instance_id="test-app-id")
    assert app_instance == AppInstance(**app_instance_json)  # type: ignore

    # Test app not found
    with pytest.raises(AppsApiException):
        await client.get_app(app_instance_id="test-app-id2")


async def test_get_apps(
    client: AppsApiClient,
    srv_port: int,
    aiohttp_server: AiohttpServer,
    app_instances_json: dict[str, Any],
) -> None:
    async def get_apps(request: web.Request) -> web.Response:
        if request.query.get("name") == "test-app-name":
            return web.json_response(app_instances_json)
        raise web.HTTPNotFound()

    app = web.Application()
    app.router.add_get("/apis/apps/v2/instances", get_apps)
    await aiohttp_server(app, port=srv_port)

    app_instance = await client.get_app_by_name(app_instance_name="test-app-name")
    assert app_instance == AppInstance(**app_instances_json["items"][0])

    # Test app not found
    with pytest.raises(AppsApiException):
        await client.get_app_by_name(app_instance_name="test-app-name2")
