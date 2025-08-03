from collections.abc import AsyncIterator

import pytest
from yarl import URL

from apolo_apps_client import AppsApiClient, AppsClientConfig


@pytest.fixture
def apps_client_config() -> AppsClientConfig:
    return AppsClientConfig(url="http://platform-apps:8080")


@pytest.fixture
async def client(apps_client_config: AppsClientConfig) -> AsyncIterator[AppsApiClient]:
    async with AppsApiClient(config=apps_client_config) as cl:
        yield cl


async def test_get_app_url(client: AppsApiClient) -> None:
    url = client._get_app_url(instance_id="test-app-id", version="v1")
    assert url == URL("http://platform-apps:8080/apis/apps/v1/instances/test-app-id")

    url = client._get_app_url(instance_id="test-app-id", version="v2")
    assert url == URL("http://platform-apps:8080/apis/apps/v2/instances/test-app-id")


async def test_get_apps_url(client: AppsApiClient) -> None:
    url = client._get_apps_url(version="v2")
    assert url == URL("http://platform-apps:8080/apis/apps/v2/instances")
