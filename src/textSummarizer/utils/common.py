import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations #Decorator to be used on functions with annotations. Runs type checks to enforce annotations
from box import ConfigBox # allows us to access dictoinaries differently
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yamL: Path):
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
        with open(path_to_yamL) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yamL} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """creates list of directories

    Args:
        path_to_directories (list): list path of directories
        verbose (bool, optional): ignores if multiple dirs is to be created. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
@ensure_annotations
def get_size(path:Path):
    """get size in KB

    Args:
        path (Path): path of the file
        
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"