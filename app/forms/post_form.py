from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class PostForm(FlaskForm):
    """Form for creating and editing posts."""
    title = StringField('标题', validators=[
        DataRequired(message='请输入标题'),
        Length(min=1, max=100, message='标题长度应在1-100个字符之间')
    ])
    content = TextAreaField('内容 (Markdown格式)', validators=[
        Optional()
    ])
    submit = SubmitField('保存')
