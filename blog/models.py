from django.db import models
from django.utils import timezone


class Post(models.Model):

    data_industry = (
        ('0', 'N/A'),
        ('1', 'Accounting / Audit / Tax Services'),
        ('2', 'Advertising / Public Relations / Marketing Services'),
        ('3', 'Architecture / Building / Construction'),
        ('4', 'Athletics / Sports'),
        ('5', 'Charity / Social Services / Non-Profit Organisation'),
        ('6', 'Chemical / Plastic / Paper / Petrochemical'),
        ('7', 'Civil Services (Government, Armed Forces)'),
        ('8', 'Clothing / Garment / Textile'),
        ('9', 'Education'),
        ('10', 'Electronics / Electrical Equipment'),
        ('11', 'Energy / Power / Water / Oil & Gas / Waste Management'),
        ('12', 'Engineering - Building, Civil, Construction / Quantity Survey'),
        ('13', 'Engineering - Electrical / Electronic / Mechanical'),
        ('14', 'Engineering - Others'),
        ('15', 'Entertainment / Recreation'),
        ('16', 'Financial Services'),
        ('17', 'Food and Beverage / Catering'),
        ('18', 'Freight Forwarding / Delivery / Shipping'),
        ('19', 'General Business Services'),
        ('20', 'Health & Beauty Care'),
        ('21', 'Hospitality / Catering'),
        ('22', 'Human Resources Management / Consultancy'),
        ('23', 'Industrial Machinery / Automation Equipment'),
        ('24', 'Information Technology'),
        ('25', 'Insurance / Pension Funding'),
        ('26', 'Interior Design / Graphic Design'),
        ('27', 'Jewellery / Gems / Watches'),
        ('28', 'Laboratory'),
        ('29', 'Legal Services'),
        ('30', 'Management Consultancy / Service'),
        ('31', 'Manufacturing'),
        ('32', 'Mass Transportation'),
        ('33', 'Media / Publishing / Printing'),
        ('34', 'Medical / Pharmaceutical'),
        ('35', 'Mixed Industry Group'),
        ('36', 'Motor Vehicles'),
        ('37', 'Packaging'),
        ('38', 'Performance / Musical / Artistic'),
        ('39', 'Petroleum'),
        ('40', 'Property Development'),
        ('41', 'Property Management / Consultancy'),
        ('42', 'Public Utilities'),
        ('43', 'Research / Survey'),
        ('44', 'Security / Fire / Electronic Access Controls'),
        ('45', 'Security Escort'),
        ('46', 'Telecommunication'),
        ('47', 'Tourism / Travel Agency'),
        ('48', 'Toys'),
        ('49', 'Trading and Distribution'),
        ('50', 'Wholesale / Retail'),
        ('51', 'Others'),
    )

    data_function = (
        ('1', 'Accounting'),
        ('2', 'Admin / HR'),
        ('3', 'Banking / Finance'),
        ('4', 'Beauty / Care / Health'),
        ('5', 'Building / Construction'),
        ('6', 'Design'),
        ('7', 'Education'),
        ('8', 'Engineering'),
        ('9', 'Hospitality / Food Beverage'),
        ('10', 'Information Technology'),
        ('11', 'Insurance'),
        ('12', 'Management'),
        ('13', 'Manufacturing'),
        ('14', 'Marketing'),
        ('15', 'Media / Advertising'),
        ('16', 'Medical / Services'),
        ('17', 'Merchandising / Purchasing'),
        ('18', 'Professional / Services'),
        ('19', 'Property'),
        ('20', 'Public Civil'),
        ('21', 'Sales / Business'),
        ('22', 'Sciences / Lab / Research Development'),
        ('23', 'Telecommunication'),
        ('24', 'Transportation / Logistics'),
        ('25', 'Others'),
    )

    data_location = (
        ('1', 'Bangkok'),
        ('2', 'Central'),
        ('3', 'Eastern'),
        ('4', 'Metro'),
        ('5', 'Northeastern'),
        ('6', 'Northern'),
        ('7', 'Overseas'),
        ('8', 'Southern'),
        ('9', 'Others'),
    )

    data_career = (
        ('1', 'N/A'),
        ('2', 'Entry'),
        ('3', 'Middle'),
        ('4', 'Senior'),
        ('5', 'Top'),
    )

    data_qualification = (
        ('1', 'N/A'),
        ('2', 'High School Certificate'),
        ('3', 'Diploma of High Vocational Education'),
        ('4', 'Degree'),
        ('5', 'Master'),
        ('6', 'Doctorate'),
    )

    choices = (
        ('1', 'Yes'),
        ('0', 'No'),
    )

    industry = models.CharField(max_length=2, choices=data_industry, default=0)
    function = models.CharField(max_length=2, choices=data_function, default=1)
    location = models.CharField(max_length=2, choices=data_location, default=1)
    career_level = models.CharField(max_length=2, choices=data_career, default=1)
    qualification = models.CharField(max_length=2, choices=data_qualification, default=1)
    experience = models.CharField(max_length=2, default=0)
    urgent = models.CharField(max_length=2, choices=choices, default=0)
    salary_negotiable = models.CharField(max_length=2, choices=choices, default=0)

    # Employment Type
    full_time = models.BooleanField()
    part_time = models.BooleanField()
    permanent = models.BooleanField()
    temporary = models.BooleanField()
    contract = models.BooleanField()
    internship = models.BooleanField()
    freelance = models.BooleanField()

    # Benefit
    dental = models.BooleanField()
    education = models.BooleanField()
    five_day = models.BooleanField()
    flexible = models.BooleanField()
    shuttle = models.BooleanField()
    gratuity = models.BooleanField()
    housing = models.BooleanField()
    life = models.BooleanField()
    medical = models.BooleanField()
    overtime = models.BooleanField()
    bonus = models.BooleanField()
    transport = models.BooleanField()
    travel = models.BooleanField()
    home = models.BooleanField()

