from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

def handle_form_view(request, form_class, template_name, instance=None, redirect_url_name=None, detail_redirect=None):
    if instance:
        form = form_class(request.POST or None, instance=instance)
    else:
        form = form_class(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        obj = form.save()

        # ✅ Handle correct redirect pattern
        if detail_redirect:
            return redirect(detail_redirect, pk=obj.pk)
        elif redirect_url_name:
            return redirect(redirect_url_name)  # ← Don't pass pk

    return render(request, template_name, {'form': form})


def handle_delete_view(request, model, pk, redirect_url_name, template_name=None):
    obj = get_object_or_404(model, pk=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect(reverse(redirect_url_name))
    
    # Fallback to a template like delete_modelname.html if not provided
    template = template_name or f'delete_{model.__name__.lower()}.html'
    
    return render(request, template, {'object': obj})

