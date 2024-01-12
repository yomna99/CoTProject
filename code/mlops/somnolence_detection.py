from ultralytics import YOLO

# Load a model
model = YOLO('yolov8n.yaml')  # build a new model from YAML

# Train the model
results = model.train(data='app/data/data.yaml', epochs=100, imgsz=640,device=[0])