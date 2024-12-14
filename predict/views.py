from django.shortcuts import render
from .predictor import PostQualityPredictor

new_predictor = PostQualityPredictor()
new_predictor.load_model('post_quality_model.joblib')

# Make some example predictions
def predict_price(request):
    prediction = None
    if request.method == 'POST':
        try:
            reputation = float(request.POST.get('reputation'))
            delta =float(request.POST.get('delta'))
            prediction = new_predictor.predict(reputation, delta)
            
        except (ValueError, TypeError):
            prediction = "Invalid input"
    return render(request, 'predict.html', {'prediction': prediction})