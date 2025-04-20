import torch
import torchvision.transforms as transforms
from torchvision.models import resnet18
from PIL import Image
import io

# Class labels
class_names = ['Apta', 'Indian Rubber Tree', 'Karanj', 'Kashid', 'Nilgiri',
               'Pimpal', 'Sita Ashok', 'Sonmohar', 'Vad', 'Vilayati Chinch']

# Define the same preprocessing used during training
transform = transforms.Compose([
    transforms.Resize((256, 256)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Load the model and weights
def load_model():
    model = resnet18(pretrained=False)
    model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
    model.load_state_dict(torch.load('./Models/best_leaf_cnn_model.pt', map_location=torch.device('cpu')))
    model.eval()
    return model

model = load_model()

# Predict function
def predict_image(img_bytes):
    img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
    img_tensor = transform(img).unsqueeze(0)
    with torch.no_grad():
        outputs = model(img_tensor)
        _, predicted = torch.max(outputs, 1)
    return class_names[predicted.item()]