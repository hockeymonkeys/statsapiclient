from requests import HTTPError, get

from .constants import API_URL, HEADERS


def fetch_json(endpoint, params=None):
    """
    Helper method for json fetching.
    Args:
        endpoint (str): resource endpoint
        params (dict): query parameters
    Raises:
        HTTPError: if requests does not return 200
    Returns:
        json: json object for selected API call
    """
    try:
        headers = dict(HEADERS)
        response = get(
            API_URL.format(endpoint=endpoint),
            params=params, headers=headers
        )
        response.raise_for_status()

        return response.json()
    except HTTPError as error:
        raise HTTPError
