import json

from flask import Request
from werkzeug.security import generate_password_hash

from app.dto.user.update_password_dto import UpdatePasswordDTO
from app.exception.user.empty_password_exception import EmptyPasswordException


class UserResolver:
    @staticmethod
    def resolve(request: Request) -> UpdatePasswordDTO:
        dto = json.loads(
            json.dumps(request.get_json()),
            object_hook=lambda d: UpdatePasswordDTO(**d)
        )

        if not dto.get_password():
            raise EmptyPasswordException('Password is empty')

        dto.set_password(
            generate_password_hash(dto.get_password(), method='sha256')
        )

        return dto
