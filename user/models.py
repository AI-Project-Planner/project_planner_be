from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    auth_token = models.CharField(max_length=255)

    def serialize_user(serializer, user_id):
        return {
                    "data":
                    {
                        "id": f"{user_id}",
                        "type": "user",
                        "attributes": serializer.data,
                    }
                }