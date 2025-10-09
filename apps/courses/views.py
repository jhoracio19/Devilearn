from django.shortcuts import render

# Create your views here.

def course_list(request):
    courses = [
        {
            'id': 1,
            'level' : 'Principiante',
            'rating' : 4.8,
            'course_title' : 'Python: fundamento hasta los detalles',
            'instructor' : 'Alison Walsh',
            'course_image' : 'images/curso_1.jpg',
            'instructor_image' : 'https://randomuser.me/api/portraits/women/68.jpg'
        },
        {
            'id': 2,
            'level' : 'Intermedio',
            'rating' : 5,
            'course_title' : 'Django: crea aplicaciones robustas',
            'instructor' : 'Patty Kutch',
            'course_image' : 'images/curso_2.jpg',
            'instructor_image' : 'https://randomuser.me/api/portraits/women/20.jpg'
        },
        {
            'id': 3,
            'level' : 'Principiante',
            'rating' : 4.9,
            'course_title' : 'Django: avanzado',
            'instructor' : 'Alonzo Murray',
            'course_image' : 'images/curso_3.jpg',
            'instructor_image' : 'https://randomuser.me/api/portraits/men/32.jpg'
        },
        {
            'id': 4,
            'level' : 'Avanzado',
            'rating' : 4.9,
            'course_title' : 'FastAPI: avanzado',
            'instructor' : 'Gregory Harris',
            'course_image' : 'images/curso_4.jpg',
            'instructor_image' : 'https://randomuser.me/api/portraits/men/45.jpg'
        },
    ]
    return render(request, "courses/courses.html", {
        'courses' : courses
    })

def course_detail(request):
    course = {
        "course_title" : "Django: Crea aplicaciones robustas",
        "course_link" : "",
        "info_course" : {
            "lessons" : 79,
            "duration" : 8,
            "instructor" : "Ricardo Cuellar",
        },
        "course_content" : [
            {
                'id': 1,
                'name': "Introducción al curso",
                'lessons' : [
                    {
                        'name': "Que aprenderas en este curso?",
                        'type' : "video",
                    },
                    {
                        'name': "Como usar la plataforma",
                        'type' : "article"
                    }
                ]
            }
        ]
    }
    return render(request, "courses/course_detail.html", {
        'course': course
    })

def course_lessons (request):
    pass