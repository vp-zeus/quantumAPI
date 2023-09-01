import json
from pprint import pprint
from django.urls import reverse
from rest_framework.test import force_authenticate, APITestCase


class UserTests(APITestCase):
    fixtures=["users/fixtures/users.json"] 

    def test_create_user(self):
        url = reverse("User")
        user_data = {
            "email": "test@test.com",
            "password": "testing$1234",
            "profile": {
                "first_name": "vignesh",
                "last_name": "pillutla",
                "phone": "8828459033",
                "portfolio_url": "myportfolio.com",
                "referral": "Employee 1",
                "mail_list": "true",
                "preferred_roles": [1, 2, 3],
                "educational_qualification": {
                    "aggregate_percentage": 98,
                    "year_of_passing": 2023,
                    "degree": 1,
                    "stream": 1,
                    "college": 1
                },
                "professional_qualification": {
                    "applicant_type": "FRESHER",
                    "familiar_skills": [1, 2],
                    "applied_recently": False,
                }
            }
        }

        raw_data = json.dumps(user_data)

        with open("users/test/resume.pdf", "rb") as resume, open("users/test/profile.jpg", "rb") as profile_pic:
            data = {
                "raw_data": raw_data,
                "resume": resume,
                "profile_pic": profile_pic
            }

            response = self.client.post(url, data, format="multipart")
            pprint(response.data,indent=4)
            assert response.status_code == 200
            self.assertEqual(response.data["user"]
                             ["email"], user_data["email"])
