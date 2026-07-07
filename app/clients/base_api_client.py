import httpx


class BaseAPIClient:

    DEFAULT_TIMEOUT = 30.0

    def __init__(
        self,
        base_url: str,
        timeout: float = DEFAULT_TIMEOUT,
        headers: dict | None = None,
    ):

        self.client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers=headers,
        )

    def get(self, endpoint: str, params=None):

        response = self.client.get(
            endpoint,
            params=params,
        )

        response.raise_for_status()

        return response.json()

    def post(self, endpoint: str, data=None, json=None):

        response = self.client.post(
            endpoint,
            data=data,
            json=json,
        )

        response.raise_for_status()

        return response.json()

    def close(self):

        self.client.close()