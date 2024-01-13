from rest_framework import serializers
from .models import Question, Choice, Answer, Result, Test
 
#for putting in question view
class ChoiceGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['value', 'choice']


#for teacher to create a question
class QuestionCreateSerializer(serializers.ModelSerializer):
    choices = ChoiceGetSerializer(read_only = True, many = True)
    class Meta:
        model = Question
        fields = ['question', 'choices', 'course']


#for teacher to provide multiple choice for the question.
class MultipleChoiceMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [
            # 'question',
            'value',
            'choice',
            'is_correct'
        ]

    def create(self, validated_data):
        question_id = self.context['question_id']
        return Choice.objects.create(question_id = question_id, **validated_data)


#for student to answer a question
class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceGetSerializer(read_only = True, many = True)
    question = serializers.CharField(read_only = True)
    answer = serializers.StringRelatedField()
    class Meta:
        model = Question
        fields = ['question', 'choices', 'answer', 'id']


class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.CurrentUserDefault()
    class Meta:
        model = Answer
        fields = ['answer', 'user', 'question', 'course']

    def create(self, validated_data):
        answer = validated_data['answer']
        question_id = validated_data['question']

        choice = Choice.objects.get(value = answer, question_id= question_id.id)
        
        if choice.is_correct==False:
            marks = 0
        else:
            marks = 1
        return Answer.objects.create(question_id= question_id.id, marks = marks, **validated_data)
    


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ['course_id']



class ResultmakeSerializer(serializers.ModelSerializer):
    total = serializers.IntegerField(read_only = True)
    # user = serializers.HiddenField(default = serializers.CurrentUserDefault())

    # def get_total(self, result:Result):
    #     course = self.context['course_id']
    #     # request = self.context['request']
    #     # user = result.course
    #     # print(user)
    #     # correct_answers_count = Answer.objects.filter(user = user, course = course, marks=1).count()
    #     return result.course.course_id*3
    

    class Meta:
        model = Result
        fields = ['user', 'course', 'total']
    
    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['total'] = Answer.objects.filter(course=instance.course).count()
    #     return ret
    
    def create(self, validated_data):
        user = self.validated_data['user']
        course = self.context['course_id']
        total = Answer.objects.filter(user = user, course = course, marks=1).count()
        return Result.objects.create(total = total, **validated_data)

    # def update(self, instance, validated_data):
    #     total = self.get_total(validated_data)
    #     validated_data['total'] = total
    #     return super().update(instance, validated_data)
    
    #create signal for this feature hence only get method will be used.
    # for asnwering endpoint user has to send only once