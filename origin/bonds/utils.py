import requests
from django.conf import settings

from .errors import LegalNameLookupError


def perform_get_request(lei: str):
    url = f"{settings.GLEIF_URL_BASE}/?lei={lei}"
    response = requests.get(url)
    return response.status_code, response.json()


def get_lei_legal_name(lei: str) -> str:
    status_code, identity_details = perform_get_request(lei)
    if status_code != 200:
        raise LegalNameLookupError(identity_details['message'])

    details_dict = next(iter(identity_details), None)
    if not details_dict:
        raise LegalNameLookupError(f"No legal name found for lei {lei}")

    return details_dict['Entity']['LegalName']['$']
