from flask_script import Manager
from app.routers import routers
from structure import controllers
from structure.application import ApplicationService
from structure.routes_manager import RoutesManager


def main():
    application_service = ApplicationService()
    application_service = routers.Routers(application_service).apply()
    application_service.set_config(debug=1)
    application_service.create_app()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()