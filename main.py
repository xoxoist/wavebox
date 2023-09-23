from app.routers import routers
from structure.application import ApplicationService


def main():
    application_service = ApplicationService()
    application_service = routers.Routers(application_service).apply()
    app = application_service.create_app()
    app.run(debug=True, port=5002)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
