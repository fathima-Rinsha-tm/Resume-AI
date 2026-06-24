from django.shortcuts import render
from .models import Resume
from .forms import ResumeForm


# HOME PAGE
def home(request):
    return render(request, 'home.html')


# TEMPLATE SELECT PAGE
def template_select(request):
    return render(request, 'template_select.html')


# RESUME FORM PAGE
def resume_form(request):

    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)

        if form.is_valid():
            resume = form.save()

            # Template Selection Logic
            if resume.template == "student":
                return render(
                    request,
                    "resume_output_student.html",
                    {"resume": resume}
                )

            elif resume.template == "professional":
                return render(
                    request,
                    "resume_output_professional.html",
                    {"resume": resume}
                )

            elif resume.template == "modern":
                return render(
                    request,
                    "resume_output_modern.html",
                    {"resume": resume}
                )

            elif resume.template == "creative":
                return render(
                    request,
                    "resume_output_creative.html",
                    {"resume": resume}
                )

            elif resume.template == "developer":
                return render(
                    request,
                    "resume_output_developer.html",
                    {"resume": resume}
                )

            elif resume.template == "executive":
                return render(
                    request,
                    "resume_output_executive.html",
                    {"resume": resume}
                )

    else:
        form = ResumeForm()

    return render(
        request,
        "resume_form.html",
        {"form": form}
    )


def resume_output(request, id):

    resume = Resume.objects.get(id=id)

    if resume.template == "student":
        template = "resume_output_student.html"

    elif resume.template == "professional":
        template = "resume_output_professional.html"

    elif resume.template == "modern":
        template = "resume_output_modern.html"

    elif resume.template == "creative":
        template = "resume_output_creative.html"

    elif resume.template == "developer":
        template = "resume_output_developer.html"

    elif resume.template == "executive":
        template = "resume_output_executive.html"

    else:
        template = "resume_output_student.html"

    return render(
        request,
        template,
        {"resume": resume}
    )
