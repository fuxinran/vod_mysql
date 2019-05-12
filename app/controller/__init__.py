# 控制器的核心文件
from flask import Blueprint
web = Blueprint('web',__name__)
from app.controller import userController,roleController,ruleController
