from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
import pickle
import numpy as np
import pandas as pd
import os
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestRegressor
from sklearn import model_selection
import warnings
from math import sqrt


def predict(train, test, targets):

    # Feature selection
    clf = ExtraTreesRegressor(n_estimators=200)
    clf = clf.fit(train, targets)

    model = SelectFromModel(clf, prefit=True)
    train_new = model.transform(train)
    test_new = model.transform(test)

    # Train model
    forest = RandomForestRegressor(max_features='sqrt')
    forest.fit(train_new, targets)
    #module_dir = os.path.dirname(__file__)
    #full_filename = os.path.join(module_dir, 'avg_model.sav')
    #pickle.dump(forest, open(full_filename, 'wb'))

    # Predict
    salary = forest.predict(test_new)

    return "{:,}".format(int(salary[0]))


def prediction(post, request):

    test = pd.DataFrame()
    module_dir = os.path.dirname(__file__)  # get current directory
    template_path = os.path.join(module_dir, 'model/Test_Template.csv')
    template = pd.read_csv(template_path)

    # Set Zero to all values
    for column in template:
        test[column] = [0]

    # Get industry
    test['Indus_Accounting / Audit / Tax Services'] = 1 if post.industry == '1' else 0
    test['Indus_Advertising / Public Relations / Marketing Services'] = 1 if post.industry == '2' else 0
    test['Indus_Architecture / Building / Construction'] = 1 if post.industry == '3' else 0
    test['Indus_Athletics / Sports'] = 1 if post.industry == '4' else 0
    test['Indus_Charity / Social Services / Non-Profit Organisation'] = 1 if post.industry == '5' else 0
    test['Indus_Chemical / Plastic / Paper / Petrochemical'] = 1 if post.industry == '6' else 0
    test['Indus_Civil Services (Government, Armed Forces)'] = 1 if post.industry == '7' else 0
    test['Indus_Clothing / Garment / Textile'] = 1 if post.industry == '8' else 0
    test['Indus_Education'] = 1 if post.industry == '9' else 0
    test['Indus_Electronics / Electrical Equipment'] = 1 if post.industry == '10' else 0
    test['Indus_Energy / Power / Water / Oil & Gas / Waste Management'] = 1 if post.industry == '11' else 0
    test['Indus_Engineering - Building, Civil, Construction / Quantity Survey'] = 1 if post.industry == '12' else 0
    test['Indus_Engineering - Electrical / Electronic / Mechanical'] = 1 if post.industry == '13' else 0
    test['Indus_Engineering - Others'] = 1 if post.industry == '14' else 0
    test['Indus_Entertainment / Recreation'] = 1 if post.industry == '15' else 0
    test['Indus_Financial Services'] = 1 if post.industry == '16' else 0
    test['Indus_Food and Beverage / Catering'] = 1 if post.industry == '17' else 0
    test['Indus_Freight Forwarding / Delivery / Shipping'] = 1 if post.industry == '18' else 0
    test['Indus_General Business Services'] = 1 if post.industry == '19' else 0
    test['Indus_Health & Beauty Care'] = 1 if post.industry == '20' else 0
    test['Indus_Hospitality / Catering'] = 1 if post.industry == '21' else 0
    test['Indus_Human Resources Management / Consultancy'] = 1 if post.industry == '22' else 0
    test['Indus_Industrial Machinery / Automation Equipment'] = 1 if post.industry == '23' else 0
    test['Indus_Information Technology'] = 1 if post.industry == '24' else 0
    test['Indus_Insurance / Pension Funding'] = 1 if post.industry == '25' else 0
    test['Indus_Interior Design / Graphic Design'] = 1 if post.industry == '26' else 0
    test['Indus_Jewellery / Gems / Watches'] = 1 if post.industry == '27' else 0
    test['Indus_Laboratory'] = 1 if post.industry == '28' else 0
    test['Indus_Legal Services'] = 1 if post.industry == '29' else 0
    test['Indus_Management Consultancy / Service'] = 1 if post.industry == '30' else 0
    test['Indus_Manufacturing'] = 1 if post.industry == '31' else 0
    test['Indus_Mass Transportation'] = 1 if post.industry == '32' else 0
    test['Indus_Media / Publishing / Printing'] = 1 if post.industry == '33' else 0
    test['Indus_Medical / Pharmaceutical'] = 1 if post.industry == '34' else 0
    test['Indus_Mixed Industry Group'] = 1 if post.industry == '35' else 0
    test['Indus_Motor Vehicles'] = 1 if post.industry == '36' else 0
    test['Indus_N/A'] = 1 if post.industry == '0' else 0
    test['Indus_Others'] = 1 if post.industry == '51' else 0
    test['Indus_Packaging'] = 1 if post.industry == '37' else 0
    test['Indus_Performance / Musical / Artistic'] = 1 if post.industry == '38' else 0
    test['Indus_Petroleum'] = 1 if post.industry == '39' else 0
    test['Indus_Property Development'] = 1 if post.industry == '40' else 0
    test['Indus_Property Management / Consultancy'] = 1 if post.industry == '41' else 0
    test['Indus_Public Utilities'] = 1 if post.industry == '42' else 0
    test['Indus_Research / Survey'] = 1 if post.industry == '43' else 0
    test['Indus_Security / Fire / Electronic Access Controls'] = 1 if post.industry == '44' else 0
    test['Indus_Security Escort'] = 1 if post.industry == '45' else 0
    test['Indus_Telecommunication'] = 1 if post.industry == '46' else 0
    test['Indus_Tourism / Travel Agency'] = 1 if post.industry == '47' else 0
    test['Indus_Toys'] = 1 if post.industry == '48' else 0
    test['Indus_Trading and Distribution'] = 1 if post.industry == '49' else 0
    test['Indus_Wholesale / Retail'] = 1 if post.industry == '50' else 0

    # Get Job Function
    test['Function_accounting'] = 1 if post.function == '1' else 0
    test['Function_admin-hr'] = 1 if post.function == '2' else 0
    test['Function_banking-finance'] = 1 if post.function == '3' else 0
    test['Function_beauty-care-health'] = 1 if post.function == '4' else 0
    test['Function_building-construction'] = 1 if post.function == '5' else 0
    test['Function_design'] = 1 if post.function == '6' else 0
    test['Function_education'] = 1 if post.function == '7' else 0
    test['Function_engineering'] = 1 if post.function == '8' else 0
    test['Function_hospitality-foodbeverage'] = 1 if post.function == '9' else 0
    test['Function_information-technology'] = 1 if post.function == '10' else 0
    test['Function_insurance'] = 1 if post.function == '11' else 0
    test['Function_management'] = 1 if post.function == '12' else 0
    test['Function_manufacturing'] = 1 if post.function == '13' else 0
    test['Function_marketing-public-relations'] = 1 if post.function == '14' else 0
    test['Function_media-advertising'] = 1 if post.function == '15' else 0
    test['Function_medical-services'] = 1 if post.function == '16' else 0
    test['Function_merchandising-purchasing'] = 1 if post.function == '17' else 0
    test['Function_others'] = 1 if post.function == '25' else 0
    test['Function_professional-services'] = 1 if post.function == '18' else 0
    test['Function_property'] = 1 if post.function == '19' else 0
    test['Function_public-civil'] = 1 if post.function == '20' else 0
    test['Function_sales-cs-business-devpt'] = 1 if post.function == '21' else 0
    test['Function_sciences-lab-researchdevelopment'] = 1 if post.function == '22' else 0
    test['Function_telecomm'] = 1 if post.function == '23' else 0
    test['Function_transportation-logistics'] = 1 if post.function == '24' else 0

    # Get Location
    test['Location_Bangkok'] = 1 if post.location == '1' else 0
    test['Location_Central'] = 1 if post.location == '2' else 0
    test['Location_Eastern'] = 1 if post.location == '3' else 0
    test['Location_Metro'] = 1 if post.location == '4' else 0
    test['Location_Northeastern'] = 1 if post.location == '5' else 0
    test['Location_Northern'] = 1 if post.location == '6' else 0
    test['Location_Others'] = 1 if post.location == '9' else 0
    test['Location_Overseas'] = 1 if post.location == '7' else 0
    test['Location_Southern'] = 1 if post.location == '8' else 0

    # Get Career Level
    test['Career_Entry'] = 1 if post.career_level == '2' else 0
    test['Career_Middle'] = 1 if post.career_level == '3' else 0
    test['Career_N/A'] = 1 if post.career_level == '1' else 0
    test['Career_Senior'] = 1 if post.career_level == '4' else 0
    test['Career_Top'] = 1 if post.career_level == '5' else 0

    # Get Qualification
    test['Quali_(N/A)'] = 1 if post.qualification == '1' else 0
    test['Quali_Degree'] = 1 if post.qualification == '4' else 0
    test['Quali_Diploma of High Vocational Education'] = 1 if post.qualification == '3' else 0
    test['Quali_Doctorate'] = 1 if post.qualification == '6' else 0
    test['Quali_High School Certificate'] = 1 if post.qualification == '2' else 0
    test['Quali_Master'] = 1 if post.qualification == '5' else 0
    test['Quali_N/A'] = 1 if post.qualification == '1' else 0

    # Get Experience
    test['experience'] = post.experience

    # Get Urgent
    test['urgent'] = 1 if post.urgent == '1' else 0

    # Get Salary Negotiable
    test['salaryNegotiable'] = 1 if post.salary_negotiable == '1' else 0

    # Get Employment Type
    test['fullTime'] = 1 if post.full_time is True else 0
    test['partTime'] = 1 if post.part_time is True else 0
    test['permanent'] = 1 if post.permanent is True else 0
    test['temporary'] = 1 if post.temporary is True else 0
    test['contract'] = 1 if post.contract is True else 0
    test['internship'] = 1 if post.internship is True else 0
    test['freelance'] = 1 if post.freelance is True else 0

    # Get Benefit
    test['dentalInsurance'] = 1 if post.dental is True else 0
    test['educationAllowance'] = 1 if post.education is True else 0
    test['five-dayWorkWeek'] = 1 if post.five_day is True else 0
    test['flexibleWorkingHours'] = 1 if post.flexible is True else 0
    test['freeShuttleBus'] = 1 if post.shuttle is True else 0
    test['gratuity'] = 1 if post.gratuity is True else 0
    test['housingAllowance'] = 1 if post.housing is True else 0
    test['lifeInsurance'] = 1 if post.life is True else 0
    test['medicalInsurance'] = 1 if post.medical is True else 0
    test['overtimePay'] = 1 if post.overtime is True else 0
    test['performanceBonus'] = 1 if post.bonus is True else 0
    test['transportationAllowance'] = 1 if post.transport is True else 0
    test['travelAllowance'] = 1 if post.travel is True else 0
    test['workFromHome'] = 1 if post.home is True else 0

    # Read model files
    train_file = os.path.join(module_dir, 'model/Train.csv')
    train = pd.read_csv(train_file)
    min_targets = train.minSalary
    max_targets = train.maxSalary
    avg_targets = train.avgSalary
    train.drop('minSalary', inplace=True, axis=1)
    train.drop('maxSalary', inplace=True, axis=1)
    train.drop('avgSalary', inplace=True, axis=1)

    # Prediction
    feature_selection = ['Career_Entry', 'Career_Middle', 'experience', 'fullTime', 'salaryNegotiable', 'Career_Top',
                      'Indus_Management Consultancy / Service', 'Indus_Human Resources Management / Consultancy',
                      'Indus_Entertainment / Recreation', 'Location_Others', 'Career_N/A', 'permanent',
                      'Indus_Food and Beverage / Catering', 'Location_Metro', 'five-dayWorkWeek', 'overtimePay',
                      'medicalInsurance', 'Function_management', 'Indus_Information Technology',
                      'Function_admin-hr', 'Indus_Motor Vehicles']

    min_model_file = os.path.join(module_dir, 'model/min_model.sav')
    max_model_file = os.path.join(module_dir, 'model/max_model.sav')
    avg_model_file = os.path.join(module_dir, 'model/avg_model.sav')
    min_model = pickle.load(open(min_model_file, 'rb'))
    max_model = pickle.load(open(max_model_file, 'rb'))
    avg_model = pickle.load(open(avg_model_file, 'rb'))
    min_salary = min_model.predict(test[feature_selection])
    max_salary = max_model.predict(test[feature_selection])
    avg_salary = avg_model.predict(test[feature_selection])

    return "{:,}".format(int(min_salary[0])), "{:,}".format(int(max_salary[0])), "{:,}".format(int(avg_salary[0]))


# Create your views here.
def post_list(request):
    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            # Predict salary
            min_salary, max_salary, avg_salary = prediction(post, request.POST)

            return render(request, 'blog/post_list.html', {'form': form,
                                                           'min_salary': min_salary,
                                                           'max_salary': max_salary,
                                                           'avg_salary': avg_salary})

    else:
        form = PostForm()
        return render(request, 'blog/post_list.html', {'form': form})

