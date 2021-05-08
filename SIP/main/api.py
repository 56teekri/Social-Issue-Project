from main import models
from django.http import JsonResponse

def likeapi(request):
    if(request.method=='POST'):
        issue_id=request.POST["issue_id"]
        user=request.user
        issue=models.SocialIssue.objects.get(id=issue_id)
        obj=models.SocialIssueLikes.objects.create(
            user=request.user,
            social_issue=issue
        )
        obj.save()
        return JsonResponse(status=201,data={'status':'true','message':'like done'})
    else:
        return JsonResponse(status=400,data={'status':'true','message':'GET not allowed'})