from rest_framework import serializers as s
from .models import Students, Subjects

Class StudentSerializer(s.ModelSerializer):
    class Meta:
        model = Students
        fields = ('id','name','subject','marks')

class SubjectSerializer(s.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ('id','subject','faculty')
