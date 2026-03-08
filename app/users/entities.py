from abc import ABC, abstractmethod
from typing import List, Optional
import uuid
from datetime import datetime


class BaseEntity:

    def __init__(self, id: Optional[uuid.UUID] = None):
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()


class UserEntity(BaseEntity):

    def __init__(
        self,
        email: str,
        first_name: str,
        password: str,
        last_name: str,
        phone_number: str = "",
        is_active: bool = True,
        is_staff: bool = False,
        is_superuser: bool = False,
        roles: List[str] = None,
        id: Optional[uuid.UUID] = None,
    ):
        super().__init__(id)

        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.is_active = is_active
        self.is_staff = is_staff
        self.is_superuser = is_superuser
        self.roles = roles or []


class RoleEntity(BaseEntity):
    def __int__(
        self,
        name: str,
        description: str = "",
        is_active: bool = True,
        id: Optional[uuid.UUID] = None,
    ):
        super().__init__(id)
        self.name = (name,)
        self.description = (description,)
        self.is_active = is_active


class UserRoleEntity(BaseEntity):
    def __init__(self, user_id = uuid.UUID, role_id: uuid.UUID, assigned_by :  Optional[uuid.UUID] =None ,id:Optional[uuid.UUID]= None):
        super().__init__(id)
        self.user_id = user_id
        self.role_id = role_id
        self.assigned_by = assigned_by
        self.assigned_at = datetime.now()


class PermissionEntity(BaseEntity):
    def __init__(
        self,
        name: str,
        codename: str,
        description: str = "",
        id: Optional[uuid.UUID] = None,
    ):
        super().__init__(id)
        self.name = name
        self.codename = codename
        self.description = description
    
    class RolePermissionEntity(BaseEntity):
        def __init__(self, 
                    role_id: uuid.UUID, 
                    permission_id: uuid.UUID, 
                    granted_by: Optional[uuid.UUID] = None, 
                    id: Optional[uuid.UUID] = None):
            super().__init__(id)
            self.role_id = role_id
            self.permission_id = permission_id
            self.granted_by = granted_by
            self.granted_at = datetime.now()
