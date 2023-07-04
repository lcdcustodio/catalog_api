
BASE_ROUTE = "recommendation"


def register_routes(api, app, root="api/v1"):
    from .controller import api as catalog_api

    api.add_namespace(catalog_api, path=f"/{root}/{BASE_ROUTE}")
