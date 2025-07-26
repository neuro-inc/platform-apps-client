from collections.abc import AsyncIterator

import pytest
from yarl import URL

from platform_apps_client import AppsApiClient


@pytest.fixture
async def client() -> AsyncIterator[AppsApiClient]:
    async with AppsApiClient(
        url=URL("http://platform-apps:8080"),
    ) as cl:
        yield cl


async def test_get_app_url(client: AppsApiClient) -> None:
    url = client._get_app_url(instance_id="test-app-id", version="v1")
    assert url == URL("http://platform-apps:8080/apis/apps/v1/instances/test-app-id")

    url = client._get_app_url(instance_id="test-app-id", version="v2")
    assert url == URL("http://platform-apps:8080/apis/apps/v2/instances/test-app-id")


async def test_get_apps_url(client: AppsApiClient) -> None:
    url = client._get_apps_url(version="v2")
    assert url == URL("http://platform-apps:8080/apis/apps/v2/instances")
