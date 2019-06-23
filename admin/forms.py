# from flask_wtf import Form
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import Required, Email, Length
# # 每一个form都可以用flask_wtf.Form里面的一些属性和方法
# # 但同时需要引入 wtforms 包来完善功能

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField,ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp
from common.models.User import User


class BaseForm(FlaskForm):
    LANGUAGES = ['zh']
#登陆表
class Login_Form(BaseForm):
    email = StringField('电子邮件', validators=[DataRequired(), Length(1, 64), Email('检查用户名')])
    password = PasswordField('密 码', validators=[DataRequired()])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')
#注册表
class RegistrationForm(FlaskForm):
    email = StringField('用户名', validators=[DataRequired(), Length(1, 64),
                                             Email('请输入用户名')])
    password = PasswordField('Password', validators=[
        DataRequired('密码不能为空'), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired('密码不一致')])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_nickname(self, field):
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('Username already in use.')