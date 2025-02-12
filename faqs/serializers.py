from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer']  # ✅ Only include necessary fields

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        lang = request.GET.get('lang', 'en')  # Default to English

        # ✅ Dynamically set translated content
        if lang == 'hi':
            data['question'] = instance.question_hi or instance.question  # Fallback to default if null
            data['answer'] = instance.answer_hi or instance.answer
        elif lang == 'bn':
            data['question'] = instance.question_bn or instance.question
            data['answer'] = instance.answer_bn or instance.answer

        return data
