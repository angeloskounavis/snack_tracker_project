from django.views.generic import DetailView, ListView, TemplateView
from .models import snacks

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://www.fritolay.com/sites/fritolay.com/files/chesters-fries-flamin-hot.png",
                "title": "Hot Fries",
                "description": "One of the best hot fries in the world",
                "reference_url": "https://www.fritolay.com/brands/chesters-snacks"
            }, {
                "image_url": "https://s7d2.scene7.com/is/image/hersheysassets/0_34000_00243_6_701_24305_010_Item_Front?fmt=webp-alpha&hei=908&qlt=75",
                "title": "Mr. Goodbar",
                "description": "Best chocolate bar around!",
                "reference_url": "https://www.hersheyland.com/mrgoodbar"
            }, {
                "image_url": "https://www.nerdscandy.com/sites/default/files/2022-06/rainbow-rope-product-22.png",
                "title": "Nerds rope",
                "description": "Best candy on a rope that will have you wanting more",
                "reference_url": "https://www.nerdscandy.com/nerds-rope"
            },
        ]

        return context

class AboutView(TemplateView):
    template_name = 'about.html'

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = snacks

class SnacksDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = snacks
