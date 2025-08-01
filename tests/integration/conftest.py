from collections.abc import AsyncIterator
from typing import Any, Callable

import pytest

from platform_apps_client import AppsApiClient, AppsClientConfig


@pytest.fixture
def srv_port(unused_tcp_port_factory: Callable[[], int]) -> int:
    return unused_tcp_port_factory()


@pytest.fixture
async def client(srv_port: int) -> AsyncIterator[AppsApiClient]:
    async with AppsApiClient(
        config=AppsClientConfig(url=f"http://localhost:{srv_port}"),
    ) as cl:
        yield cl


@pytest.fixture
def app_instance_json() -> dict[str, str]:
    return {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "name": "app-instance-name",
        "created_at": "2019-08-24T14:15:22Z",
        "updated_at": "2019-08-24T14:15:22Z",
        "creator": "creator",
        "display_name": "display_name",
        "template_name": "template_name",
        "template_version": "version",
        "project_name": "project_name",
        "org_name": "org_name",
        "cluster_name": "cluster_name",
        "namespace": "default",
        "state": "queued",
        "app_type": "helm",
    }


@pytest.fixture
def app_instances_json(app_instance_json: dict[str, str]) -> dict[str, Any]:
    return {
        "items": [app_instance_json],
        "total": 0,
        "page": 1,
        "size": 1,
        "pages": 0,
    }
