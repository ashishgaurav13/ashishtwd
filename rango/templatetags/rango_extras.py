from django import template
register = template.Library()

@register.filter(name='auto_code')
def auto_code(value):
	if ' ' in value.strip():
		return value.replace(' ','_')
	return value.replace('_',' ')
