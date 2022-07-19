# Fastapi MLOps

This project is a rest api for a machine learning model that uses a dynamoDB database.

## Installation

Use the manager [make](https://www.gnu.org/software/make/) to install and run project.

```bash
make help 
  clean                       clean files
  install-dev-deps            install dev dependencies
  build-docker                build docker image for production
  test                        run the testsuite
  format                      format the python code
  check-code                  check vulnerabilities in the code
  check-deps                  check vulnerabilities in the packages
  run-dev                     run dev server (development mode)
  run                         run docker server (production mode)
  stop                        stop docker server (production mode)
```

## Usage

You a need a **doubleit_model.pt** file in app/ml/trained_models/ and shared-local-instance.db in my-dynamodb-data/

You can a create a shared-local-instance.db with the script create_db.py that is located in the folder database.

```bash
make install-dev-deps
source venv/bin/active
chmod o+w my-dynamodb-data/
chmod +x ./app/database/create_db.py
./app/database/create_db.py
```

For production mode:
```bash
make run
```
For development mode:
```bash
make run 
docker stop fastapi-mlops
make run-dev
```

Remember that for both modes you need a working database


## License
[MIT](https://choosealicense.com/licenses/mit/)
