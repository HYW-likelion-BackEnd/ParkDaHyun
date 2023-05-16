from django.shortcuts import render, get_object_or_404, redirect
from .models import Photo
from .forms import PhotoForm

# Create your views here.
# 사진 목록
def photo_list(request):
    photos = Photo.objects.all()
    return render (request , 'photo/photo_list.html', {'photos':photos})

# 세부 화면
def photo_detail(request, pk):
    photo = get_object_or_404(Photo, pk = pk)
    return render (request, 'photo/photo_detail.html', {'photo': photo})

# 작성 화면
def photo_post(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm()
        return render(request,'photo/photo_post.html',{'form':form})

# 수정 화면
def photo_edit(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    if request.method == "POST":
        form = PhotoForm(request.POST, instance=photo)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.save()
            return redirect('photo_detail', pk=photo.pk)
    else:
        form = PhotoForm(instance=photo)
    return render(request, 'photo/photo_post.html', {'form':form})
