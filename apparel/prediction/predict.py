
import os
import sys
import shutil
import cv2
from pathlib import Path
from ultralytics import YOLO

from apparel.utils.common import *


class WarehouseApparel:
    def __init__(self,filename):

        
        self.filename =filename
        self.weights = os.path.join('apparel', 'model', 'best.pt')
        self.source = os.path.join('apparel', 'inference', 'images', self.filename)
        self.save_dir = os.path.join('apparel', 'inference', 'output', self.filename)
        
        self.label_names = read_yaml(Path(os.path.join('apparel', 'model', 'predefined_labels.yaml'))).names
        

    def detect(self):
        try:
            
            model = YOLO(self.weights)

            results = model.predict(self.source, save=True, conf=0.5)
            
            results = results[0]
          
            shutil.move(os.path.join(results.save_dir, self.filename), self.save_dir)
            shutil.rmtree(results.save_dir)
            
            bgr_image = cv2.imread(self.save_dir)
            im_rgb = cv2.cvtColor(bgr_image, cv2.COLOR_RGB2BGR)
            cv2.imwrite(self.save_dir, im_rgb)
            opencodedbase64 = encodeImageIntoBase64(self.save_dir)
            result = {"image": opencodedbase64.decode('utf-8')}
            return result
        

        except Exception as error:
            print('error', error)