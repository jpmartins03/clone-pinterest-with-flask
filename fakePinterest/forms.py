# arquivo que define a estrutura dos formularios
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakePinterest.models import User

class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    confirm_button = SubmitField("Fazer Login")

class FormCriarConta(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(min=6, max=16)])
    password_confirm = PasswordField("Confirmar Senha", validators=[DataRequired(), EqualTo("password")])
    confirm_button = SubmitField("Criar Conta")

    ##validação de email
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return ValidationError("E-mail já cadastrado")
            