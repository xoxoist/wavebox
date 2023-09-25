from structure.application import ApplicationService
from app.routers.routers import RoutesFoo, RoutesBar


def main():
    application_service = ApplicationService()
    application_service = RoutesFoo(application_service).apply()
    application_service = RoutesBar(application_service).apply()
    application_service.set_config(debug=1)
    application_service.create_app()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
