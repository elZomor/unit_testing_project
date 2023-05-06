from django.test import TestCase, override_settings, tag, Client, RequestFactory
from rest_framework.test import APIClient, APIRequestFactory
from django.conf import settings
from django.urls import reverse

from app.models import Student
from app.views import StudentViewSet


@tag("settings_test")
class TestMyApp(TestCase):
    def setUp(self):
        print("Setting up")

    def tearDown(self):
        print("Tearing down")

    def test_debug(self):
        print(settings.DEBUG) # Prints False

    """
        Let's say in the settings now debug=True
    """
    @override_settings(**{"DEBUG": True})
    def test_debug_overriden(self):
        print(settings.DEBUG) # Prints True

    @tag("group_a")
    def test_tag(self):
        print("group_a")


@tag("django-test")
class TestStudent(TestCase):

    def setUp(self):
        self.client = Client()
        self.request = RequestFactory()

    def test_student_with_client(self):
        Student.objects.create(name="student")
        response = self.client.get("/api/students/")
        print(response.__class__)

    def test_student_with_client_reversed_name(self):
        Student.objects.create(name="student1")
        response = self.client.get(reverse("student-viewset-list"))
        print(response.__class__)

    def test_student_with_request_factory(self):
        Student.objects.create(name="student2")
        response = self.request.get("/api/students/")
        print(response.__class__)


@tag("drf-test")
class TestStudentWithDRF(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.request = APIRequestFactory()

    def test_student_with_client(self):
        Student.objects.create(name="student")
        response = self.client.get("/api/students/")
        print(response.__class__)

    def test_student_with_client_reversed_name(self):
        Student.objects.create(name="student1")
        response = self.client.get(reverse("student-viewset-list"))
        print(response.__class__)

    def test_student_with_request_factory(self):
        Student.objects.create(name="student2")
        req = self.request.get("/api/students/")
        view = StudentViewSet.as_view({"get": "list"})
        response = view(req)
        print(response.__class__)


@tag("assertions")
class TestAssertionsStudent(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.test_list = [1, 2, 3]

    def test_student_creation(self):
        student_name = "s"
        student = Student.objects.create(name=student_name)
        self.assertEqual(student_name, student.name)
        self.assertIsNotNone(student)
        student_two, created = Student.objects.get_or_create(name=student_name)
        self.assertFalse(created)

    def test_number_in_list(self):
        self.assertIn(1, self.test_list)

