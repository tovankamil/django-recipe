from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from ..repositories.role_repository import RoleRepository
from ..services.role_service import RoleService
from ..models.role_model import Role

from .serializers import RoleCreateSerializer
from app.shared.responses.api_response import ApiResponse


class RoleView(APIView):

    permission_classes = [IsAuthenticated]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        repo = RoleRepository()
        self.service = RoleService(repo)

    def post(self, request):

        serializer = RoleCreateSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        role = self.service.create(serializer.validated_data["name"])

        return ApiResponse.success(
            data={"id": str(role.id), "name": role.name}, message="Role created"
        )

    def get(self, request):

        page = int(request.GET.get("page", 1))
        page_size = int(request.GET.get("page_size", 10))

        result = self.service.list(page, page_size)

        data = [{"id": str(r.id), "name": r.name} for r in result["data"]]

        return ApiResponse.success(
            data=data,
            meta={
                "page": result["page"],
                "page_size": result["page_size"],
                "total": result["total"],
            },
        )


class RoleDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def delete(self, request, role_id):

        repo = RoleRepository()
        service = RoleService(repo)

        service.delete(role_id)

        return ApiResponse.success(message="Role deleted")
