import pytest
from pytest_bdd import given, scenarios, then, when

pytestmark = pytest.mark.django_db

scenarios('features/feature_name_here.feature')
