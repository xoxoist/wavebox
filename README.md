# Wavebox: Clean, Compact, and Easy Flask Backend Wrapper

[![PyPI Version](https://img.shields.io/pypi/v/wavebox.svg)](https://pypi.org/project/wavebox/)
[![Python Versions](https://img.shields.io/pypi/pyversions/wavebox.svg)](https://pypi.org/project/wavebox/)
[![License](https://img.shields.io/pypi/l/wavebox.svg)](https://pypi.org/project/wavebox/)

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-Donate-orange.svg)](https://www.buymeacoffee.com/wavebox)

Welcome to **Wavebox** – your ultimate solution for creating clean, compact, and blazing-fast Flask backend applications with ease! Whether you're a seasoned developer or just starting with Flask, Wavebox empowers you to build web applications quickly and efficiently.

## Features

- **Simplicity**: Wavebox is designed to make Flask backend development a breeze. Its clean and intuitive API lets you focus on your application's logic rather than boilerplate code.

- **Compact**: We believe in minimalism. With Wavebox, you get a lightweight package that doesn't bloat your project. It keeps your codebase neat and tidy.

- **Ease of Use**: Whether you're a beginner or a pro, Wavebox is easy to pick up. Our documentation is comprehensive and user-friendly, helping you get started in no time.

## Installation

Install Wavebox using pip:

```bash
pip install wavebox
```

## Quick Start

Getting started with Wavebox is as easy as 1-2-3! Here's a quick example of setting up a basic Flask app:

### Main
```python
from flask import Flask, Blueprint, Response, jsonify
from werkzeug.exceptions import NotFound, BadRequest
from wavebox.definitions import Applications
from wavebox.components.exceptions import FundamentalException

class ApplicationName(Applications):

    def __init__(self, flask_app: Flask):
        super().__init__(flask_app, Blueprint('root', flask_app.name, url_prefix="/"))

    def global_handle_http_exception(self, ex: FundamentalException) -> Response:
        pass

def main():
    app = Flask(__name__)
    application_name = ApplicationName(app)
    application_name.start()

if __name__ == '__main__':
    main()
```

Save this as `app.py`, and you're ready to go! Run your app with `python app.py`, and visit `http://localhost:5000` in your browser to see it in action.

## Documentation

For detailed information on using Wavebox, check out our [documentation](https://github.com/xoxoist/dicksy/wiki).

## Contributing

We welcome contributions from the community! If you have ideas, bug reports, or want to contribute to Wavebox, please see our [Contribution Guidelines](CONTRIBUTING.md).

## License

Wavebox is distributed under the [GNU General Public License](LICENSE).

## Get Started Now

Wavebox is here to simplify your Flask backend development. Start building web applications the clean, compact, fast, and easy way with Wavebox!

if you have ideas, bug reports, or want to contribute to Wavebox, please see our [Contribution Guidelines](CONTRIBUTING.md).

Happy coding with Wavebox! 🚀🌊