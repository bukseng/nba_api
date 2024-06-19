from extract import extract
from transform import transform
from load import load, mongo_load

if __name__ == "__main__":
    try:
        #extract()
        #transform()
        load()
    except Exception as e:
        print(str(e))
