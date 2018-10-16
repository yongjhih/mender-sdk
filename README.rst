Usage
-----

.. code:: python

    mender: Mender = Mender()
    token: OauthToken = mender.login(Email("username@example.com"), "PASSWORD")

    res: List[Device] = mender.devices()

Installation
------------

.. code:: sh

    pip install git+git://github.com/yongjhih/mender-sdk.git

Development
-----------

.. code:: sh

    pipenv install
    pipenv install -d
    pipenv run "pytest -s"
    pipenv run "mypy --ignore-missing-imports mender"

Coverage
-----------

.. code:: sh

    pipenv run 'pytest tests --cov=mender'

Stack
-----

- Data Classes - PEP 557 (Python 3.7)
- Type hints - PEP 3107 (Python 3.0), PEP 484 (Python 3.5), PEP 526 (Python 3.6), PEP 563 (Python 3.7)
- Type checking - mypy (Python 3.6)
- Literal String Interpolation - PEP 498 (Python 3.6)

TODO
----

- aysncio / aiohttp
- runtime type checking or write ton of test cases for type checking
