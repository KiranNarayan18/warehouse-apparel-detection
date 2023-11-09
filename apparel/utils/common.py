import os
import sys
import yaml
import json
import base64

from pathlib import Path
from box import ConfigBox
from ensure import ensure_annotations


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            # logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            print(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)

    except Exception as error:
        print("Error ", error)
        # logger.error(CustomException(e,sys))
        # raise CustomException(e,sys)
    



def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open("apparel/inference/images/" + fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())