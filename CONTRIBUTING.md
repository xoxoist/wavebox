# Contributing to Wavebox

Thank you for your interest in contributing to Wavebox! We welcome contributions from the community, whether it's in the form of code, bug reports, feature requests, documentation improvements, or any other valuable input.

Please take a moment to review this document to understand how you can contribute effectively.

## Code of Conduct

Before getting started, please review our [Code of Conduct](CODE_OF_CONDUCT.md). We expect all contributors to adhere to these guidelines.

## Reporting Issues

If you find a bug or have a feature request, please create an issue on the [GitHub Issues](https://github.com/xoxoist/dicksy/issues) page. Make sure to provide a clear and detailed description of the issue or request. If possible, include relevant code snippets, error messages, or screenshots to help us understand the problem.

## Contributing Code

### Setting Up Your Development Environment

1. Fork the Wavebox repository to your GitHub account.
2. Clone your forked repository to your local machine:

```bash
git clone https://github.com/xoxoist/dicksy.git
```

3. Create a virtual environment and install the project dependencies:

```bash
cd wavebox
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

### Making Changes

1. Create a new branch for your changes:

```bash
git checkout -b feature-or-bugfix-branch
```

2. Make your changes and write tests if applicable.

3. Ensure all tests pass:

```bash
pytest
```

4. Commit your changes with a descriptive commit message:

```bash
git commit -m "Description of your changes"
```

5. Push your changes to your forked repository:

```bash
git push origin feature-or-bugfix-branch
```

### Creating a Pull Request

Once your changes are ready, you can create a pull request:

1. Go to the [Wavebox GitHub repository](https://github.com/xoxoist/dicksy).

2. Click on the "New Pull Request" button.

3. Select your branch and provide a clear title and description for your pull request.

4. Ensure your pull request adheres to the project's coding style and conventions.

5. Submit your pull request.

## Documentation

Improvements to documentation are always welcome. If you find any inaccuracies or areas that need clarification, please feel free to submit a documentation pull request.

## Community

Join the Wavebox community and connect with other contributors and users:

- [GitHub Discussions](https://github.com/xoxoist/dicksy/discussions)
- [Wavebox Gitter Chat](https://gitter.im/wavebox/community)

## Thank You!

We appreciate your contributions to Wavebox. Your involvement helps make Wavebox a better Flask backend wrapper for everyone. If you have any questions or need assistance, please don't hesitate to reach out to us.

Happy coding!