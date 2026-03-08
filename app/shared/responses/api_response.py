from rest_framework.response import Response


class ApiResponse:

    @staticmethod
    def success(data=None, message="success", status=200, meta=None):

        body = {"success": True, "message": message, "data": data, "meta": meta}

        return Response(body, status=status)

    @staticmethod
    def error(message="error", status=400, errors=None):

        body = {"success": False, "message": message, "errors": errors}

        return Response(body, status=status)
