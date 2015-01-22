from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from giganapp.models import Paper
from giganapp.models import Figure
from giganapp.models import Table
from giganapp.models import Workflow

from django.shortcuts import render
from giganapp.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

import wf2cyto


def galaxy2cytoscape(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)
    galaxy_url = None
    if request.method == 'GET':
        galaxy_url = request.GET['galaxy_wf_json_url']
    if galaxy_url:
        content = wf2cyto.run(galaxy_url, False, True)
        print content
        # Render response and return to client
        return HttpResponse(content, content_type='text/json')
    else:
        return HttpResponse("", content_type='text/plain')


def files(request):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Render the response and return to the client.
    return render_to_response('giganapp/files.html', context)


def workflow(request, paper_short_name_url, workflow_name):
    # Obtain the context from the HTTP request.
    context = RequestContext(request)

    # Create a context dictionary which we can pass to the template rendering engine.
    # We start by containing the name of the paper passed by the user.
    context_dict = {'paper_short_name_url': paper_short_name_url}

    # We need information about the workflow
    try:
        # Can we find a paper with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        paper = Paper.objects.get(short_name=paper_short_name_url)

        # Retrieve all of the associated figures and tables
        # Note that filter returns >= 1 model instance.
        wf = Workflow.objects.get(paper=paper, name=workflow_name)
        # print "Workflow link: ", wf

        # Adds our results list to the template context under name figures.
        context_dict['wf'] = wf
        # We also add the paper object from the database to the context dictionary.
        # We'll use this in the template to verify that the paper exists.
        context_dict['paper'] = paper
    except Paper.DoesNotExist:
        # We get here if we didn't find the specified paper.
        # Don't do anything - the template displays the "no paper" message for us.
        pass

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


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # new_user = authenticate(username=request.POST['username'],
            #                        password=request.POST['password'])
            # login(request, new_user)

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render_to_response(
            'giganapp/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/giganapp/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your GigaFig account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('giganapp/login.html', {}, context)


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/giganapp/')