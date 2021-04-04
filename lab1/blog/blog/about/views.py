import json

from django.http import JsonResponse
from django.shortcuts import render


def index(request):
    data = {
        'app_name': 'JustBlog',
        'about': 'This is just blog created for study aims.'
    }

    return JsonResponse(data, safe=False)


def doc(request):
    return render(request, 'doc.html')


def openapi(request):
    """This function serve to return JSON data for ReDoc api loading, cause with static files some problems appeared."""
    data = {
        "swagger": "2.0",
        "title": "Sample Pet Store App",
        "info": {
            "title": "Simple Blog",
            "description": "Simple app developed for studying aims.",
            "contact": {
                "name": "Vladyslav Boiko",
                "github": "https://github.com/vlad81"
            }
        },
        "basePath": "/",
        "paths": {
            "/about": {
                "get": {
                    "tags": [
                        "about"
                    ],
                    "summary": "Get app description",
                    "description": "",
                    "produces": [
                        "application/json"
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "app_name": {
                                        "type": "string"
                                    },
                                    "about": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/account/register": {
                "get": {
                    "tags": [
                        "account/register"
                    ],
                    "summary": "Register new account",
                    "produces": [
                        "application/json"
                    ],
                    "parameters": [
                        {
                            "name": "username",
                            "in": "path",
                            "description": "",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "password",
                            "in": "path",
                            "description": "",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "email",
                            "in": "path",
                            "description": "",
                            "required": True,
                            "type": "string"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "successful_register": {
                                        "type": "boolean"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/account/login": {
                "get": {
                    "tags": [
                        "account/login"
                    ],
                    "summary": "Log in",
                    "produces": [
                        "application/json"
                    ],
                    "parameters": [
                        {
                            "name": "password",
                            "in": "path",
                            "description": "",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "email",
                            "in": "path",
                            "description": "",
                            "required": True,
                            "type": "string"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "successful_login": {
                                        "type": "boolean"
                                    },
                                    "username": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/account/home": {
                "get": {
                    "tags": [
                        "account/home"
                    ],
                    "summary": "Home page",
                    "produces": [
                        "application/json"
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "username": {
                                        "type": "string"
                                    },
                                    "email": {
                                        "type": "string"
                                    },
                                    "date_joined": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/account/del_usr": {
                "get": {
                    "tags": [
                        "account/del_usr"
                    ],
                    "summary": "Delete account",
                    "description": "Staff member required",
                    "produces": [
                        "application/json"
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "successful_delete": {
                                        "type": "boolean"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/articles": {
                "get": {
                    "tags": [
                        "articles/"
                    ],
                    "summary": "List of latest articles",
                    "produces": [
                        "application/json"
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "schema": {
                                "type": "array",
                                "properties": {
                                    "title": {
                                        "type": "string"
                                    },
                                    "author_name": {
                                        "type": "string"
                                    },
                                    "article_content": {
                                        "type": "string"
                                    },
                                    "pub_date": {
                                        "type": "string"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/articles/{articleId}": {
                "get": {
                    "tags": [
                        "/articles/{articleId}"
                    ],
                    "summary": "Concrete article",
                    "produces": [
                        "application/json"
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "article_title": {
                                        "type": "string"
                                    },
                                    "article_author": {
                                        "type": "string"
                                    },
                                    "article_content": {
                                        "type": "string"
                                    },
                                    "latest_comments_list": {
                                        "type": "object",
                                        "properties": {
                                            "content": {
                                                "type": "string"
                                            },
                                            "author_name": {
                                                "type": "string"
                                            },
                                            "pub_date": {
                                                "type": "string"
                                            },
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/articles/leave_comment": {
                "get": {
                    "tags": [
                        "articles/leave_comment"
                    ],
                    "summary": "Leave comment for article",
                    "produces": [
                        "application/json"
                    ],
                    "parameters": [
                        {
                            "name": "comment_text",
                            "in": "path",
                            "description": "",
                            "required": True,
                            "type": "string"
                        },
                        {
                            "name": "article_id",
                            "in": "path",
                            "description": "",
                            "required": True,
                            "type": "int"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "article_id": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "comment_created": {
                                        "type": "boolean"
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "/articles/add_article": {
                "get": {
                    "tags": [
                        "articles/add_article"
                    ],
                    "summary": "Add new article",
                    "produces": [
                        "application/json"
                    ],
                    "parameters": [
                        {
                            "name": "title",
                            "in": "path",
                            "description": "",
                            "required": False,
                            "type": "string"
                        },
                        {
                            "name": "content",
                            "in": "path",
                            "description": "",
                            "required": False,
                            "type": "int"
                        }
                    ],
                    "responses": {
                        "200": {
                            "description": "successful operation",
                            "schema": {
                                "type": "object",
                                "properties": {
                                    "article_id": {
                                        "type": "integer",
                                        "format": "int64"
                                    },
                                    "article_created": {
                                        "type": "boolean"
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "securityDefinitions": {
            "api_key": {
                "type": "apiKey",
                "name": "api_key",
                "in": "header"
            }
        }
    }
    return JsonResponse(data, safe=False)
