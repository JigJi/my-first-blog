from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:

        model = Post

        fields = ('industry', 'function', 'location', 'career_level', 'qualification', 'experience',
                  'urgent', 'salary_negotiable', 'full_time', 'part_time', 'permanent', 'temporary', 'contract',
                  'internship', 'freelance', 'dental', 'education', 'five_day', 'flexible', 'shuttle', 'gratuity',
                  'housing', 'life', 'medical', 'overtime', 'bonus', 'transport', 'travel', 'home')

        widgets = {
            'experience': forms.TextInput(attrs={'style': 'width: 40px; height: 20px;'}),
        }

