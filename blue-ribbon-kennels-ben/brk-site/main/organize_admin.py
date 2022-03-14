
APPS_TO_REORDER = ['Gallery', 'Home', 'Main', 'Reservations', 'Services', 'Pages', 'Faqs', 'Facility', 'Contact']

APP_ORDER = {
    'Home': {'order': 1, 'models':[{'app':'Main', 'model':'Logo', 'order': 1}, {'app':'Home', 'model':'Slide', 'order': 2}, {'app':'Services', 'model':'Service', 'order': 3}, {'app':'Home', 'model':'TestimonialSection', 'order': 4}]},
    'Reservations': {'order': 3, 'models':[{'app':'Reservations', 'model':'Kennel', 'order': 1}, {'app':'Reservations', 'model':'Reservation', 'order': 2}]},
    'Pages': {'order': 2, 'models':[{'app':'Pages', 'model':'AboutPage', 'order': 1}, {'app':'Gallery', 'model':'GalleryPage', 'order': 4}, {'app':'Faqs', 'model':'FaqPage', 'order': 2}, {'app':'Facility', 'model':'FacilityPage', 'order': 3},]},
    'Contact': {'order': 4, 'models':[{'app':'Contact', 'model':'Contact', 'order': 1}, ]},
}


from operator import mod
from django import template
from django.db import models
from main import organize_admin

register = template.Library()


def pop_and_get_app(apps, key, app_label):
    for index, app in enumerate(apps):
        if app[key] == app_label:
            obj = apps.pop(index)
            return obj
    return None


def get_admin_url(model, ordered_apps):
    for app in ordered_apps:
        for model_attrs in app['models']:
            if model_attrs['name'] == model:
                return model_attrs['admin_url']
    return None


def get_app_url(model, ordered_apps):
    for app in ordered_apps:
        if app['name'] == model and 'app_url' in app.keys():
            app_url = app['app_url']
            return app_url
    return None


def get_model(apps, model_name):
    for app in apps:
        for model in app['models']:
            if model_name == model['object_name']:
                return model
    return None

def sort_list(model_list):
    new_ele = 0
    new_lis_len = len(model_list)  
    for k in range(0, new_lis_len):  
        for l in range(0, new_lis_len-k-1):  
            if (model_list[l][new_ele] > model_list[l + 1][new_ele]):  
                new_tem = model_list[l]  
                model_list[l]= model_list[l + 1]  
                model_list[l + 1]= new_tem  
    return model_list

def order_models(models, app_order, apps):
    current_models = [model['name'] for model in models]
            
    for k, v in app_order.items():
        for item in v['models']:
            model = item['model']
            if not model in current_models:
                new_model = get_model(apps, model)
                if new_model:
                    models.append(new_model)

    return models


def remove_models(app_order, models, app_name):
    new_models = list()
    model_list = list()
    app_order_nums = list()
    for k, v in app_order.items():
        for item in v['models']:
            app_order_nums.append((item['model'], item['order']))

    for k, v in app_order.items():
        if k == app_name:
            keep_models = [item['model'] for item in v['models']]
            for model in models:
                if model['object_name'] in keep_models and model not in [tup[1] for tup in model_list]:
                    model_list.append(([tup[1] for tup in app_order_nums if tup[0] == model['object_name']][0], model))

    sorted_list = sorted(model_list, key=lambda i: i[0])

    return [tup[1] for tup in sorted_list]


# @register.filter
def sort_apps(apps):
    new_apps = apps.copy()
    app_order = organize_admin.APP_ORDER
    ordered_apps = [pop_and_get_app(new_apps, 'name', i)
                    for i in organize_admin.APPS_TO_REORDER]

    for app in ordered_apps:
        if not app == None and app['name'] in app_order.keys():
            new_models = order_models(app['models'], app_order, apps)
            new_models = remove_models(app_order, new_models, app['name'])
            if new_models:
                app['models'] = new_models
            new_apps.insert(app_order[app['name']]['order'], app)

    return new_apps

# @register.filter
def get_admin_url_label(model):
    app_label = None
    app_order = organize_admin.APP_ORDER
    for k,v in app_order.items():
        for item in v['models']:
            if not item['app'] == k:
                app_label = k 
    return app_label
