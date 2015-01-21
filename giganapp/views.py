from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from giganapp.models import Paper
from giganapp.models import Figure
from giganapp.models import Table

from django.shortcuts import render


def workflow(request, paper_short_name_url, workflow_name):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render_to_response('giganapp/workflow.html', context_dict, context)


def paper(request, paper_short_name_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    # Change underscores in the paper name to spaces.
    # URLs don't handle spaces well, so we encode them as underscores.
    # We can then simply replace the underscores with spaces again to get the name.
    paper_short_name = paper_short_name_url.replace('_', ' ')

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the paper passed by the user.
    context_dict = {'paper_short_name': paper_short_name}

    try:
        # Can we find a paper with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        paper = Paper.objects.get(short_name=paper_short_name)

        paper_type = ""
        if paper.article_type == "RA":
            paper_type = "Research Article"
        elif paper.article_type == "CO":
            paper_type = "Commentary"
        elif paper.article_type == "DA":
            paper_type = "Data Note"
        elif paper.article_type == "RE":
            paper_type = "Review"
        else:
            paper_type = "Technical Note"

        context_dict['paper_type'] = paper_type

        # Retrieve all of the associated figures and tables
        # Note that filter returns >= 1 model instance.
        figures = Figure.objects.filter(paper=paper)
        tables = Table.objects.filter(paper=paper)

        # Adds our results list to the template context under name figures.
        context_dict['figures'] = figures
        context_dict['tables'] = tables
        # We also add the paper object from the database to the context dictionary.
        # We'll use this in the template to verify that the paper exists.
        context_dict['paper'] = paper
    except Paper.DoesNotExist:
        # We get here if we didn't find the specified paper.
        # Don't do anything - the template displays the "no paper" message for us.
        pass

    # Go render the response and return it to the client.
    return render_to_response('giganapp/paper.html', context_dict, context)


def tables(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query for categories - add the list to our context dictionary.
    table_list = Table.objects.order_by('title')[:5]
    context_dict = {'tables': table_list}

    # The following two lines are new.
    # We loop through each category returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    # for figure in figure_list:
    #     paper.url = paper.short_name

    # Render the response and return to the client.
    return render_to_response('giganapp/tables.html', context_dict, context)


def figures(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query for categories - add the list to our context dictionary.
    figure_list = Figure.objects.order_by('title')[:5]
    context_dict = {'figures': figure_list}

    # The following two lines are new.
    # We loop through each category returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    # for figure in figure_list:
    #     paper.url = paper.short_name

    # Render the response and return to the client.
    return render_to_response('giganapp/figures.html', context_dict, context)


def papers(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query for categories - add the list to our context dictionary.
    paper_list = Paper.objects.order_by('year')[:5]
    context_dict = {'papers': paper_list}

    # The following two lines are new.
    # We loop through each category returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    for paper in paper_list:
        paper.url = paper.short_name

    # Render the response and return to the client.
    return render_to_response('giganapp/papers.html', context_dict, context)


def index(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Query for categories - add the list to our context dictionary.
    paper_list = Paper.objects.order_by('year')[:5]
    context_dict = {'papers': paper_list}

    # The following two lines are new.
    # We loop through each category returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    for paper in paper_list:
        paper.url = paper.short_name

    # Render the response and return to the client.
    return render_to_response('giganapp/index.html', context_dict, context)


def about(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'giganapp/about.html', context_dict)
