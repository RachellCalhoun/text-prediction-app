from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .clean_text import clean_text_input
from .forms import TextInputForm
# import gensim
import joblib
import os

def index(request):
    template = loader.get_template('predict/supervised.html')
    form = TextInputForm()
    return HttpResponse(template.render({'form': form}, request))


# custom method for generating predictions
def getPredictions(text):
    import pickle
    # small compressed model with n=10 not as accurate but useable
    # score on train: 0.9826730139230139
    # score on test: 0.7156211609336609

    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    # my_file = os.path.join(THIS_FOLDER, 'forest_model_small1.sav')
    # updated model
    my_file = os.path.join(THIS_FOLDER, 'forestmodel1.pk')
    model = joblib.load(open(my_file, "rb"))
    prediction = model.predict(text)
    print(prediction)
    if prediction == 0:
        return "Does not need to be simplified"
    elif prediction == 1:
        return "Needs to be simplified"
    else:
        return "error"


# our result page view
def result(request):
    form = TextInputForm()
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data.get('text')
            cleaned_text = clean_text_input(text)
            result = getPredictions(cleaned_text)
            # topic = get_topic(text)
            template = loader.get_template('predict/result.html')
            return HttpResponse(template.render({'result': result, 'text': text}, request))
        else:
            error_message = "Form is not valid please try again"
    else:
        error_message = "There was an error, please go back and try again"
    return HttpResponse(error_message)
