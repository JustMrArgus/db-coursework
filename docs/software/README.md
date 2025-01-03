# Реалізація інформаційного та програмного забезпечення


## SQL-скрипт для створення початкового наповнення бази даних

```sql
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`Role`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Role` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Role` (
  `id` INT NOT NULL,
  `Rolecol` VARCHAR(45) NULL,
  `permission` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`User`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`User` ;

CREATE TABLE IF NOT EXISTS `mydb`.`User` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_Name` VARCHAR(45) NOT NULL,
  `last_Name` VARCHAR(45) NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE,
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE,
  UNIQUE INDEX `Usercol_UNIQUE` (`password` ASC) VISIBLE,
  UNIQUE INDEX `last_Name_UNIQUE` (`last_Name` ASC) VISIBLE,
  UNIQUE INDEX `first_Name_UNIQUE` (`first_Name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Media`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Media` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Media` (
  `id` INT NOT NULL,
  `title` VARCHAR(45) NULL,
  `keywords` VARCHAR(45) NULL,
  `createdAt` DATE NULL,
  `updatedAt` DATE NULL,
  `User_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_Media_User_idx` (`User_id` ASC) VISIBLE,
  CONSTRAINT `fk_Media_User`
    FOREIGN KEY (`User_id`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`Admin`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`Admin` ;

CREATE TABLE IF NOT EXISTS `mydb`.`Admin` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`CommentModeration`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`CommentModeration` ;

CREATE TABLE IF NOT EXISTS `mydb`.`CommentModeration` (
  `comment_Id` INT NOT NULL,
  `userId` INT NOT NULL,
  `moderatorId` INT NOT NULL,
  `moderationReason` VARCHAR(45) NULL,
  `moderationDate` DATE NULL,
  `moderationStatus` VARCHAR(45) NULL,
  PRIMARY KEY (`comment_Id`),
  INDEX `fk_CommentModeration_Admin1_idx` (`moderatorId` ASC) VISIBLE,
  INDEX `fk_CommentModeration_User1_idx` (`userId` ASC) VISIBLE,
  CONSTRAINT `fk_CommentModeration_Admin1`
    FOREIGN KEY (`moderatorId`)
    REFERENCES `mydb`.`Admin` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_CommentModeration_User1`
    FOREIGN KEY (`userId`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`DeleteAccount`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`DeleteAccount` ;

CREATE TABLE IF NOT EXISTS `mydb`.`DeleteAccount` (
  `id` INT NOT NULL,
  `userId` INT NULL,
  `reason` VARCHAR(45) NULL,
  `date` DATE NULL,
  `type` VARCHAR(45) NULL,
  `description` VARCHAR(45) NULL,
  `Admin_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_DeleteAccount_Admin1_idx` (`Admin_id` ASC) VISIBLE,
  CONSTRAINT `fk_DeleteAccount_Admin1`
    FOREIGN KEY (`Admin_id`)
    REFERENCES `mydb`.`Admin` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `mydb`.`UserRole`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`UserRole` ;

CREATE TABLE IF NOT EXISTS `mydb`.`UserRole` (
  `User_id` INT NOT NULL,
  `User_id1` INT NOT NULL,
  `Role_id` INT NOT NULL,
  PRIMARY KEY (`User_id`),
  INDEX `fk_UserRole_User1_idx` (`User_id1` ASC) VISIBLE,
  INDEX `fk_UserRole_Role1_idx` (`Role_id` ASC) VISIBLE,
  CONSTRAINT `fk_UserRole_User1`
    FOREIGN KEY (`User_id1`)
    REFERENCES `mydb`.`User` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_UserRole_Role1`
    FOREIGN KEY (`Role_id`)
    REFERENCES `mydb`.`Role` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- Fill database with data
USE mybd;

START TRANSACTION;
-- Role
INSERT INTO `mydb`.`Role` (`id`, `Rolecol`, `permission`) VALUES
(1, 'Admin', 'Full Access'),
(2, 'Editor', 'Edit Content'),
(3, 'Viewer', 'View Content'),
(4, 'Moderator', 'Manage Comments'),
(5, 'Contributor', 'Submit Content');

-- User
INSERT INTO `User` (`id`,`first_Name`, `last_Name`, `email`, `password`) 
VALUES 
(1,'John', 'Doe', 'john.doe@example.com', 'password123'),
(2,'Jane', 'Smith', 'jane.smith@example.com', 'securepassword'),
(3,'Alice', 'Johnson', 'alice.johnson@example.com', 'mypassword'),
(4,'George', 'Joestar', 'George.Joestar@example.com', 'bestpassword'),
(5,'Nicole', 'Tesla', 'Nicole.Nesla@example.com', 'cringepassword');

-- Media
INSERT INTO `Media` (`id`,`title`,`keywords`,`createdAT`,`updatedAT`,`User_id`) 
VALUES
(1,'test.png','image','07-12','2020-08-12',1),
(2,'Metalica.mp3','Rock,music,guitar','07-12','2020-08-12',2),
(3,'message.txt','text','07-12','2019-03-7',3),
(4,'recipe.mp4','video,cooking','07-12','2019-01-01',4),
(5,'test.png','image','2018-06-11','2020-08-12',5);

--  Admin
INSERT INTO `mydb`.`Admin` (`id`, `name`) VALUES
(1, 'Super Admin'),
(2, 'Moderator Andryi'),
(3, 'Moderator Boris'),
(4, 'Deleted Admin 1'),
(5, 'Deleted Admin 2');

-- CommentModeration
INSERT INTO `mydb`.`CommentModeration` (`comment_Id`, `userId`, `moderatorId`, `moderationReason`, `moderationDate`, `moderationStatus`) VALUES
(1, 1, 2, 'Inappropriate Language', '2020-08-12', 'Removed'),
(2, 2, 1, 'Spam', '2024-11-13', 'Flagged'),
(3, 3, 3, 'Off-topic', '2020-08-12', 'Removed'),
(4, 4, 4, 'Hate Speech', '2019-01-01', 'Banned'),
(5, 5, 5, 'Misleading Info', '2020-08-12', 'Under Review');

INSERT INTO `mydb`.`DeleteAccount` (`id`, `userId`, `reason`, `date`, `type`, `description`, `Admin_id`) VALUES
(1, 3, 'Privacy Concerns', '2024-11-14', 'Permanent', 'User requested account deletion', 1),
(2, 2, 'Inactive Account', '2024-11-13', 'Temporary', 'Account marked as inactive', 2),
(3, 1, 'Too Many Emails', '2024-11-10', 'Temporary', 'User opted for temporary deactivation', 3),
(4, 4, 'Security Issues', '2024-10-01', 'Permanent', 'Security concerns raised by user', 4),
(5, 5, 'Other', '2024-09-15', 'Permanent', 'No specific reason provided', 5);

INSERT INTO `mydb`.`UserRole` (`User_id`, `User_id1`, `Role_id`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 3, 3),
(4, 4, 4),
(5, 5, 5);

COMMIT;
```

## RESTfull сервіс для управління даними

### Налаштування Flask додатка (app.py)
```py
from flask import Flask
from extensions import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:0000@localhost:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from routes.users_routes import users_bp
from routes.media_routes import media_bp
from routes.roles_routes import roles_bp

app.register_blueprint(users_bp, url_prefix='/api/users')
app.register_blueprint(media_bp, url_prefix='/api/media')
app.register_blueprint(roles_bp, url_prefix='/api/roles')

from error_handlers import register_error_handlers
register_error_handlers(app)

if __name__ == '__main__':
    app.run()
```

### Ініціалізація SQLAlchemy (extensions.py)
```py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

### Створення SQLAlchemy моделей таблиць бази данних (models.py)
```py
from extensions import db

class Role(db.Model):
    __tablename__ = 'Role'
    id = db.Column(db.Integer, primary_key=True)
    roleName = db.Column(db.String(45), nullable=False)
    permission = db.Column(db.String(45), nullable=False)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(45), nullable=False)
    lastName = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)

class Media(db.Model):
    __tablename__ = 'Media'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(45), nullable=False)
    keywords = db.Column(db.String(45), nullable=False)
    createdAt = db.Column(db.Date, nullable=False)
    updatedAt = db.Column(db.Date, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
```

### Створення обробників базових помилок (error_handlers.py)
```py
from flask import jsonify

def register_error_handlers(app):
    @app.errorhandler(404)
    def resource_not_found(e):
        return jsonify({'error': 'Resource not found'}), 404

    @app.errorhandler(400)
    def bad_request(e):
        return jsonify({'error': 'Bad request'}), 400

    @app.errorhandler(Exception)
    def handle_generic_error(e):
        return jsonify({'error': f'An unexpected internal server error occurred: {str(e)}'}), 500
```

### Створення контролерів додатака
#### Media controller (media_controller.py)
```py
from models import Media
from extensions import db
from sqlalchemy.exc import IntegrityError
from flask import jsonify, request

def get_all_media():
    media_items = Media.query.all()
    return jsonify([{
        'id': media.id,
        'title': media.title,
        'keywords': media.keywords,
        'createdAt': media.createdAt.isoformat(),
        'updatedAt': media.updatedAt.isoformat(),
        'userId': media.userId
    } for media in media_items])

def create_media():
    data = request.json
    try:
        new_media = Media(
            title=data['title'],
            keywords=data['keywords'],
            createdAt=data['createdAt'],
            updatedAt=data['updatedAt'],
            userId=data['userId']
        )
        db.session.add(new_media)
        db.session.commit()
        return jsonify({'message': 'Media item created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Invalid data or user does not exist'}), 400

def get_media(media_id):
    media = Media.query.get(media_id)
    if not media:
        return jsonify({'error': 'Media item not found'}), 404
    return jsonify({
        'id': media.id,
        'title': media.title,
        'keywords': media.keywords,
        'createdAt': media.createdAt.isoformat(),
        'updatedAt': media.updatedAt.isoformat(),
        'userId': media.userId
    })

def update_media(media_id):
    media = Media.query.get(media_id)
    if not media:
        return jsonify({'error': 'Media item not found'}), 404
    data = request.json
    media.title = data.get('title', media.title)
    media.keywords = data.get('keywords', media.keywords)
    media.createdAt = data.get('createdAt', media.createdAt)
    media.updatedAt = data.get('updatedAt', media.updatedAt)
    media.userId = data.get('userId', media.userId)
    db.session.commit()
    return jsonify({'message': 'Media item updated successfully'})

def delete_media(media_id):
    media = Media.query.get(media_id)
    if not media:
        return jsonify({'error': 'Media item not found'}), 404
    db.session.delete(media)
    db.session.commit()
    return jsonify({'message': 'Media item deleted successfully'})
```
#### Users controller (users_controller.py)
```py
from models import User
from extensions import db
from sqlalchemy.exc import IntegrityError
from flask import jsonify, request

def get_all_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'firstName': user.firstName,
        'lastName': user.lastName,
        'email': user.email,
        'password': user.password
    } for user in users])

def create_new_user():
    data = request.json
    try:
        new_user = User(
            firstName=data['firstName'],
            lastName=data['lastName'],
            email=data['email'],
            password=data['password']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Email already exists'}), 400

def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({
        'id': user.id,
        'firstName': user.firstName,
        'lastName': user.lastName,
        'email': user.email,
        'password': user.password
    })

def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    data = request.json
    user.firstName = data.get('firstName', user.firstName)
    user.lastName = data.get('lastName', user.lastName)
    user.email = data.get('email', user.email)
    user.password = data.get('password', user.password)
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})
```
#### Roles controller (roles_controller.py)
```py
from extensions import db
from models import Role
from sqlalchemy.exc import IntegrityError
from flask import request, jsonify

def get_all_roles():
    roles = Role.query.all()
    return jsonify([{
        'id': role.id,
        'roleName': role.roleName,
        'permission': role.permission
    } for role in roles])

def create_role():
    data = request.json
    try:
        new_role = Role(
            roleName=data['roleName'],
            permission=data['permission']
        )
        db.session.add(new_role)
        db.session.commit()
        return jsonify({'message': 'Role created successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Role creation failed. Integrity error'}), 400

def get_role(role_id):
    role = Role.query.get(role_id)
    if not role:
        return jsonify({'error': 'Role not found'}), 404
    return jsonify({
        'id': role.id,
        'roleName': role.roleName,
        'permission': role.permission
    })

def update_role(role_id):
    role = Role.query.get(role_id)
    if not role:
        return jsonify({'error': 'Role not found'}), 404
    data = request.json
    role.roleName = data.get('roleName', role.roleName)
    role.permission = data.get('permission', role.permission)
    db.session.commit()
    return jsonify({'message': 'Role updated successfully'})

def delete_role(role_id):
    role = Role.query.get(role_id)
    if not role:
        return jsonify({'error': 'Role not found'}), 404
    db.session.delete(role)
    db.session.commit()
    return jsonify({'message': 'Role deleted successfully'})
```

### Налаштування маршрутизації
#### Media routes (media_routes.py)
```py
from flask import Blueprint, request
import controllers.media_controller as controller

media_bp = Blueprint('media', __name__)

@media_bp.route('/', methods=['GET', 'POST'])
def handle_media():
    if request.method == 'GET':
        return controller.get_all_media()

    if request.method == 'POST':
        return controller.create_media()

@media_bp.route('/<int:media_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_media_item(media_id):
    if request.method == 'GET':
        return controller.get_media(media_id)

    if request.method == 'PUT':
        return controller.update_media(media_id)

    if request.method == 'DELETE':
        return controller.delete_media(media_id)
```
#### Users routes (users_routes.py)
```py
from flask import Blueprint, request
import controllers.users_controller as controller

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'GET':
        return controller.get_all_users()

    if request.method == 'POST':
        return controller.create_new_user()

@users_bp.route('/<int:user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    if request.method == 'GET':
        return controller.get_user(user_id)

    if request.method == 'PUT':
        return controller.update_user(user_id)

    if request.method == 'DELETE':
        return controller.delete_user(user_id)

```
#### Roles routes (roles_routes.py)
```py
from flask import Blueprint, request
import controllers.roles_controller as controller

roles_bp = Blueprint('roles', __name__)

@roles_bp.route('/', methods=['GET', 'POST'])
def handle_roles():
    if request.method == 'GET':
        return controller.get_all_roles()

    if request.method == 'POST':
        return controller.create_role()

@roles_bp.route('/<int:role_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_role(role_id):
    if request.method == 'GET':
        return controller.get_role(role_id)

    if request.method == 'PUT':
        return controller.update_role(role_id)

    if request.method == 'DELETE':
        return controller.delete_role(role_id)
```
