This is a script to create a zip bundle to deploy Python code to AWS Lambda.

Run it from the directory of your project and it will (recursively) copy all `.py` files into a zip bundle along with installing the modules from `requirements.txt`.

The output filename defaults to the directory name in lower case.

## Install

```
pip3.6 install git+https://github.com/aconz2/clam
```
