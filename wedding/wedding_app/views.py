from django.shortcuts import render, get_object_or_404
from .models import Guest, Family
from django.http import Http404
from .models import Guest


INVITE_TO_ATTEND = {"invited_haldi": "attending_haldi",
                    "invited_mehendi": "attending_mehendi",
                    "invited_pre_wedding_party": "attending_pre_wedding_party",
                    "invited_wedding": "attending_wedding"}

BOOLEAN_CONVERT = {"true": True,
                   "false": False}


def index(request):
    return render(request, "index.html")


def validate_code(request, context):
    try:
        family = Family.objects.get(code = request.POST["code"])
        context["valid_code"] = True
        request.session["family_id"] = family.pk
        return context, family
    except Family.DoesNotExist:
        raise Http404("Code does not exist")


def get_family_invitations(family):
    event_dict = {"invited_haldi": family.invited_haldi,
                  "invited_mehendi": family.invited_mehendi,
                  "invited_pre_wedding_party": family.invited_pre_wedding_party,
                  "invited_wedding": family.invited_wedding}
    return event_dict


def get_family_guest_list(guests):
    family_guest_list = [{"name":guest.name,
                    "id": guest.pk,
                    "attending_haldi":guest.attending_haldi,
                    "attending_mehendi":guest.attending_mehendi,
                    "attending_pre_wedding_party":guest.attending_pre_wedding_party,
                    "attending_wedding":guest.attending_wedding} for guest in guests]
    return family_guest_list
        

def get_events(request):
    context = {}
    context, family = validate_code(request, context)
    guests =  Guest.objects.filter(family=family)

    context["family_list"] = get_family_guest_list(guests)
    context["event_dict"] = get_family_invitations(family)

    if family.comments != "":
        context["family_comment"] = family.comments
  
    return render(request, "index.html", context)


def write_rsvp_data(request):
    # Write comment
    if "comment" in request.POST.keys():
        family = Family.objects.get(pk=request.session["family_id"])
        family.comments = request.POST["comment"]
        family.save()

    # Write attendance
    for key in request.POST.keys():
        if key.startswith("invited"):
            event, guest_id = key.split(":")
            guest = Guest.objects.get(pk=guest_id)
            setattr(guest, INVITE_TO_ATTEND[event], BOOLEAN_CONVERT[request.POST[key]])
            guest.save()

    return render(request, "index.html")
