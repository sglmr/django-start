import pytest
from django.test import Client
from django.urls import resolve, reverse
from pytest_django.asserts import assertContains, assertNotContains, assertTemplateUsed

rel_url = "/about/"
url_name = "about"
templates = ["core/about.html"]
contains = ["about"]
excludes = ["should not  be here"]


@pytest.fixture()
def get_response():
    yield Client().get(rel_url)


def test_get_response_200(get_response):
    assert get_response.status_code == 200


def test_url_name_reverse():
    assert reverse(url_name) == rel_url


def test_url_loc_resolves():
    assert resolve(rel_url).view_name == url_name


@pytest.mark.parametrize("template", templates)
def test_template_used(get_response, template):
    assertTemplateUsed(get_response, template)


@pytest.mark.parametrize("content", contains)
def test_contains(get_response, content):
    assertContains(get_response, content)


@pytest.mark.parametrize("content", excludes)
def test_not_contains(get_response, content):
    assertNotContains(get_response, content)
