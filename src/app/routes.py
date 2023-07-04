def register_routes(api, app, root="api"):
    from app.recommendation import register_routes as attach_color

    # Add routes
    attach_color(api, app)
