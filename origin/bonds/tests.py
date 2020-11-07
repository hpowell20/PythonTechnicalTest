import string
import random

from django.contrib.auth import get_user_model
from django.db import IntegrityError
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from .models import Bond
from .serializers import BondReadSerializer


def get_random_string(length=8):
    chars = string.ascii_uppercase + string.digits + string.digits
    return ''.join(random.choices(chars, k=length))


def get_random_int():
    return random.randint(1000, 100000000)


class BondModelTest(TestCase):
    def test_uniqueness(self):
        lei_name = get_random_string(20)
        Bond.objects.create(lei=lei_name,
                            isin=get_random_string(12),
                            size=get_random_int(),
                            currency=get_random_string(3),
                            maturity='2025-02-28')

        with self.assertRaises(IntegrityError):
            Bond.objects.create(lei=lei_name,
                                isin=get_random_string(12),
                                size=get_random_int(),
                                currency=get_random_string(3),
                                maturity='2025-02-28')

    def test_model_create(self):
        lei_name = get_random_string(20)

        # Create the model
        Bond.objects.create(lei=lei_name,
                            isin=get_random_string(12),
                            size=get_random_int(),
                            currency=get_random_string(3),
                            maturity='2025-02-28')

        # Retrieve the created model
        bond = Bond.objects.get(lei=lei_name)
        self.assertEqual(bond.lei, lei_name)
        self.assertEqual(bond.legal_name, None)


class BondsViewTest(APITestCase):
    """ Test module for GET all bonds API """

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'testuser',
            'password'
        )
        self.client.force_authenticate(self.user)

    def test_get_all_bonds_unauthenticated(self):
        # Generate the response
        self.client.force_authenticate(user=None, token=None)
        response = self.client.get("/bonds", follow=True)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_bonds(self):
        Bond.objects.create(lei=get_random_string(20),
                            isin=get_random_string(12),
                            size=get_random_int(),
                            currency=get_random_string(3),
                            maturity='2025-02-28')

        Bond.objects.create(lei=get_random_string(20),
                            isin=get_random_string(12),
                            size=get_random_int(),
                            currency=get_random_string(3),
                            maturity='2025-02-28')

        # Generate the response
        response = self.client.get("/bonds", follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Retrieve the information from the database
        bonds = Bond.objects.all()
        serializer = BondReadSerializer(bonds, many=True)
        self.assertEqual(response.data, serializer.data)

    # TODO: Mock the requests object for testing; move these create tests into integration level tests
    def test_create_bond_with_valid_lei_value(self):
        payload = {
            'isin': get_random_string(12),
            'size': get_random_int(),
            'currency': get_random_string(3),
            'maturity': '2025-02-28',
            'lei': 'R0MUWSFPU8MPRO8K5P83'
        }

        response = self.client.post("/bonds/", payload, follow=True)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        exists = Bond.objects.filter(
            lei=payload['lei'],
        ).exists()
        self.assertTrue(exists)

    def test_create_bond_when_no_legal_name_found(self):
        payload = {
            'isin': get_random_string(12),
            'size': get_random_int(),
            'currency': get_random_string(3),
            'maturity': '2025-02-28',
            'lei': 'R0MUWSFPU8MPRO8K5P82'
        }

        response = self.client.post("/bonds/", payload, follow=True)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_bond_when_lei_value_too_short(self):
        payload = {
            'isin': get_random_string(12),
            'size': get_random_int(),
            'currency': get_random_string(3),
            'maturity': '2025-02-28',
            'lei': 'R0MUWSFPU8MPRO8K5P'
        }

        response = self.client.post("/bonds/", payload, follow=True)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
