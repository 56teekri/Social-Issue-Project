from main import models
from django.http import JsonResponse


def likeapi(request):
    if request.method == "POST":
        issue_id = request.POST["issue_id"]
        user = request.user
        issue = models.SocialIssue.objects.get(id=issue_id)
        # checking pehle se hi to like nahi hai
        check = models.SocialIssueLikes.objects.filter(user=user, social_issue=issue)
        if check.exists():
            return JsonResponse(
                status=400, data={"status": "true", "message": "Already Liked"}
            )

        # if pehle se hi like nahi hai to like kro
        obj = models.SocialIssueLikes.objects.create(
            user=request.user, social_issue=issue
        )
        obj.save()
        return JsonResponse(status=201, data={"status": "true", "message": "Liked"})
    else:
        return JsonResponse(
            status=400, data={"status": "true", "message": "GET not allowed"}
        )
